import os
import random
import collections
import numpy as np

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.problems.functional import FunctionalProblem

from loaddata import Loaddata
from generationdata import Generationdata
from csdata import Csdata

# Variáveis Globais
CONSTANT = 100
VMIN, VMAX = 0.95, 1.05
CS_TOTAL_COST = 7807 + 16781.35
CHARGER_COST = 832.5 + 324
BUDGET = 200000


class Gaoptimization:
    def __init__(self, npts, resolucao, sc):
        self.npts = npts
        self.resolucao = resolucao
        self.sc = sc

    def foo_1(self, dss, load_list, new_population, pv_orig, cs_dict):

        # Compilando arquivo do OpenDSS com a rede da UFJF
        dss_file = os.path.dirname(os.path.realpath(__file__)) + "\Modelagem_Circ_Dist_UFJF"
        dss.text("compile {}".format(dss_file))

        # Carregando cargas
        Loaddata().get_dss_load(dss, load_list)

        # Carregando geração PV
        Generationdata().get_dss_pv(dss, pv_orig, self.sc)

        # Criando Estação de recarga
        cs_list = Csdata().get_cs_curve(load_list, new_population, cs_dict)
        Csdata().get_cs_loadshape(dss, cs_list)
        Csdata().get_cs_load(dss, cs_list)

        # Definindo EnergyMeter
        dss.text("New EnergyMeter.Feeder1 Line.3F_MT_T1/1.C1 1")
        dss.text("New EnergyMeter.Feeder2 Line.3F_MT_T2/1.C2 1")

        # Solução
        v_list = []
        for m in range(1):  # -------self.npts
            m = 95
            dss.text("Set VoltageBases=[23.1, 6.6, 0.22]")
            dss.text("CalcVoltageBases")
            dss.text("Set mode=daily  number={}  stepsize={}m".format((m + 1), self.resolucao))
            dss.solution_solve()

            # Armazenando tensões nos minutos
            vmag_list = dss.circuit_all_bus_vmag_pu()  # pu
            v_list.extend(vmag_list)

        # Perdas
        dss.meters_write_name("Feeder1")
        losses_calc1 = dss.meters_register_values()[12]
        dss.meters_write_name("Feeder2")
        losses_calc2 = dss.meters_register_values()[12]
        total_losses = losses_calc1 + losses_calc2

        return total_losses, v_list

    def foo_2(self, load_list, new_population):

        # Densidade de carga
        density = {}
        consumption = []
        for load_dict in load_list:
            zipped_load_list = zip(load_dict['LOADSHAPE_P_A'], load_dict['LOADSHAPE_P_B'], load_dict['LOADSHAPE_P_C'])
            load_p_curve = [x + y + z for (x, y, z) in zipped_load_list]
            load_density = sum(load_p_curve)
            density[load_dict['NAME']] = load_density
            consumption.append(load_density)

        # Consumo total
        total_consumption = sum(consumption)
        weigth = [x / total_consumption for x in consumption]

        # Ponderando as escolhas da CS
        zipped_choice = zip(new_population, weigth)
        choice = [x * y for (x, y) in zipped_choice]
        total_aproximation = sum(choice)

        return total_aproximation

    def fitness_total(self, dss, w, load_list, x, cs_max, pv_orig, cs_dict):

        # Iluminação e UsinaEng não tem CS
        x[10] = 0
        x[17] = 0

        # FOB 1: minimizar perdas
        fob_1, v_list = self.foo_1(dss, load_list, x, pv_orig, cs_dict)
        opt_losses = fob_1 * 3.971

        # FOB 2: minimizar distância do centro de carga
        fob_2 = ((1 / self.foo_2(load_list, x)) * 1000)
        opt_density = fob_2

        # FOB
        opt = w * opt_losses + (1 - w) * opt_density

        # Restrição de capacidade do trafo
        for index in range(len(x)):
            if x[index] > cs_max[index]:
                opt += opt * 0.30

        # Restrição de custo de instalação de CS
        cs_alloc = []
        for cs in x:
            if cs > 0:
                cs_alloc.append(CS_TOTAL_COST)
            else:
                cs_alloc.append(0)
        if (sum(cs_alloc) + sum(x) * CHARGER_COST) > BUDGET:
            opt += opt * 2

        # Restrição de limite de tensão
        for v in v_list:
            if v < VMIN or v > VMAX:
                opt += opt_losses * 0.10

        # Restrição do limite de ampacidade
        # OpenDSS

        # Função de aptidão
        if opt == 0:
            return -99999, opt_losses, opt_density
        else:
            return opt, opt_losses, opt_density

    def fitness(self, dss, w, load_list, x, cs_max, pv_orig, cs_dict):

        # FOB 1: minimizar perdas
        x = [int(n) for n in x]
        fob_1, v_list = self.foo_1(dss, load_list, x, pv_orig, cs_dict)
        opt_losses = fob_1 * 3.971

        # FOB 2: minimizar distância do centro de carga
        fob_2 = ((1 / self.foo_2(load_list, x)) * 1000)
        opt_density = fob_2

        # FOB
        opt = w * opt_losses + (1 - w) * opt_density

        # Iluminação e UsinaEng não tem CS
        if x[9] != 0 or x[17] != 0:
            opt += opt * 0.20

        # Restrição de capacidade do trafo
        for index in range(len(x)):
            if x[index] > cs_max[index]:
                opt += opt * 0.30

        # Restrição de custo de instalação de CS
        cs_alloc = []
        for cs in x:
            if cs > 0:
                cs_alloc.append(CS_TOTAL_COST)
            else:
                cs_alloc.append(0)
        if (sum(cs_alloc) + sum(x) * CHARGER_COST) > BUDGET:
            opt += opt * 2

        # Restrição de limite de tensão
        for v in v_list:
            if v < VMIN or v > VMAX:
                opt += opt_losses * 0.10

        # Restrição do limite de ampacidade
        # OpenDSS

        # Função de aptidão
        if opt == 0:
            return -99999
        else:
            return opt

    def get_max_char(self, cs_dict):
        # Recebendo nomes das barras
        bus = []
        for key in list(cs_dict.keys()):
            if key[-2] == '_':
                bus.append(key[:-2])
            else:
                bus.append(key[:-3])
        bus = list(dict.fromkeys(bus))

        # Entendendo o limite de cada estação
        cs_max = np.zeros(len(bus) + 2)
        n_cs_bus = 0
        for name in range(len(bus) + 2):
            if name != 9 and name != 17:
                for key in cs_dict.keys():
                    bus_name = key.split('_')[0]
                    if bus[n_cs_bus] == bus_name:
                        cs_max[name] = int(key.split('_')[1])
                n_cs_bus += 1
            else:
                cs_max[name] = 1
        cs_max = list(cs_max)
        cs_max = [int(n) for n in cs_max]
        return cs_max

    def isfloat(self, num):
        try:
            len(num)
            return True
        except TypeError:
            return False

    def get_optimal_value(self, dss, max_iter, w, load_list, pv_orig, cs_dict):
        # Parâmetros Genéticos
        n_var = 23  # Número de cromossomos
        sol_per_pop = 200  # Tamanho da população

        # Inicialização da População
        cs_max_chargers = self.get_max_char(cs_dict)  # Csdata().get_max_chargers(load_list)

        # Algoritmo Genético
        problem = FunctionalProblem(n_var,
                                    lambda x: self.fitness(dss, w, load_list, x[:n_var], cs_max_chargers, pv_orig,
                                                           cs_dict),
                                    constr_ieq=[],
                                    xl=np.zeros(n_var),
                                    xu=np.array(cs_max_chargers),
                                    verbose=True
                                    )
        algorithm = NSGA2(
            pop_size=sol_per_pop,
            eliminate_duplicates=True)
        res = minimize(problem,
                       algorithm,
                       termination=('n_gen', max_iter),
                       seed=1,
                       verbose=False)
        if self.isfloat(res.X[0]):
            population = [int(round(n)) for n in res.X[0].tolist()]
        else:
            population = [int(round(n)) for n in res.X]
        opt, opt_loss, opt_density = self.fitness_total(dss, w, load_list, population, cs_max_chargers, pv_orig,
                                                        cs_dict)

        bestsolution = (opt, opt_loss, opt_density, population)

        return bestsolution

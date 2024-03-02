'''
PROJECT: OPTIMUM SIZING AND SITING ELECTRIC VEHICLE CHARGING STATIONS BASED ON GENETIC ALGORITHM
NAME: LETICIA FRITZ HENRIQUE
E-MAIL: FRITZ.LETICIA@GMAIL.COM
'''

# Importando as Bibliotecas
import py_dss_interface
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from loaddata import Loaddata
from csdata import Csdata
from scenarios import Scenarios, Scenarioreduction
from gaoptimization import Gaoptimization


def get_data_in_15m(data, npts):
    data15 = {}
    for key, value in data.items():
        curve15 = np.zeros((len(value), npts))
        for case in range(len(value)):
            count = 0
            count15 = 0
            for m in range(len(value[case])):
                if count == 0:
                    curve15[case, count15] = value[case][m]
                    count15 += 1
                if count == 14:
                    count = 0
                else:
                    count += 1

        data15[key] = curve15
    return data15


def get_data_in_list(data, n_cluster):
    bus = []
    for key in data.columns.values:
        if key[-2] == '_':
            bus.append(key[:-2])
        else:
            bus.append(key[:-3])
    bus = list(dict.fromkeys(bus))
    data_orig = {}
    for key in bus:
        data_array = np.zeros((n_cluster, len(data[key + '_' + str(0)])))
        for n in range(n_cluster):
            data_array[n, :] = data[key + '_' + str(n)].tolist()
        data_orig[key] = data_array
    return data_orig


if __name__ == '__main__':
    # Instanciando objeto OpenDSS
    dss = py_dss_interface.DSSDLL()

    # Dados de Entrada
    npts = 1440 * 1  # Número de Pontos da Simulação (1440 pts,  96 pts, ...)
    resolucao = 15  # Resolução da Simulação (1 min, 15 min, ...)
    n_cluster = 5
    n_scenarios = 1000
    max_iter = 20

    print("----- DADOS DE ENTRADA -----")
    print("[0] Gerar novos dados de entrada")
    print("[1] Carregar dados de entrada existentes")
    mode = int(input("O que deseja? "))
    # Carregando cargas
    data_demand = Loaddata().get_demand(npts)
    if mode == 0:
        sc_pv = []
        sc_load = []
        sc_cs = []

        # Curva PV medida
        df_pv = pd.read_excel('PV_UFJF.xlsx')
        pv_list = df_pv['Lab solar UFJF / Power / Mean Values  [kW]3'].tolist()
        pv_list = pv_list[96:96 * 2]
        pv_list = [n / 1000 for n in pv_list]

        # Monte Carlo: PV
        for sc in range(n_scenarios):
            sc_pv.append(Scenarios().get_pv_scenarios(pv_list))
            print(sc)
        # Redução de cenários
        pv_orig = Scenarioreduction(n_cluster).get_scenarioreduction_pv(sc_pv)
        # Organizando dicionário para transformar em DataFrame
        pv_dict = Scenarios().get_dict_results(pv_orig)
        # Armazenar dados de entrada
        pv_df = pd.DataFrame.from_dict(pv_dict)
        pv_df.to_excel('input_pv.xlsx', sheet_name='pv', index=False)

        # Monte Carlo: Load
        for sc in range(n_scenarios):
            sc_load.append(Scenarios().get_load_scenarios(data_demand, npts))
            print(sc)
        # Redução de cenários
        load_orig = Scenarioreduction(n_cluster).get_scenarioreduction_load(sc_load)
        # Organizando dicionário para transformar em DataFrame
        load_dict = Scenarios().get_dict_results(load_orig)
        # Armazenar dados de entrada
        load_df = pd.DataFrame.from_dict(load_dict)
        load_df.to_excel('input_load.xlsx', sheet_name='load', index=False)

        # Monte Carlo: CS
        for sc in range(n_scenarios):
            sc_cs.append(Scenarios().get_cs_scenarios(sc_load[0]))
            print(sc)
        # Redução de cenários
        cs_orig = Scenarioreduction(n_cluster).get_scenarioreduction_cs(sc_cs)
        # Organizando dicionário para transformar em DataFrame
        cs_dict = Scenarios().get_dict_results(cs_orig)
        # Armazenar dados de entrada
        cs_dict_1 = {}
        cs_dict_2 = {}
        cs_dict_3 = {}
        cs_dict_4 = {}
        cs_dict_5 = {}
        key_list = [*cs_dict.keys()]
        for key, value in cs_dict.items():
            if key in key_list[:int(round(len(key_list) / 5))]:
                cs_dict_1[key] = value
            elif key in key_list[int(round(len(key_list) / 5)):(2 * int(round(len(key_list) / 5)))]:
                cs_dict_2[key] = value
            elif key in key_list[(2 * int(round(len(key_list) / 5))):(3 * int(round(len(key_list) / 5)))]:
                cs_dict_3[key] = value
            elif key in key_list[(3 * int(round(len(key_list) / 5))):(4 * int(round(len(key_list) / 5)))]:
                cs_dict_4[key] = value
            else:
                cs_dict_5[key] = value
        cs1_df = pd.DataFrame.from_dict(cs_dict_1)
        cs2_df = pd.DataFrame.from_dict(cs_dict_2)
        cs3_df = pd.DataFrame.from_dict(cs_dict_3)
        cs4_df = pd.DataFrame.from_dict(cs_dict_4)
        cs5_df = pd.DataFrame.from_dict(cs_dict_5)
        with pd.ExcelWriter('input_cs.xlsx') as writer:
            cs1_df.to_excel(writer, sheet_name='cs1', index=False)
            cs2_df.to_excel(writer, sheet_name='cs2', index=False)
            cs3_df.to_excel(writer, sheet_name='cs3', index=False)
            cs4_df.to_excel(writer, sheet_name='cs4', index=False)
            cs5_df.to_excel(writer, sheet_name='cs5', index=False)
    elif mode == 1:
        # Carregando dados de entrada
        pv_df = pd.read_excel('input_pv.xlsx', sheet_name='pv')
        load_df = pd.read_excel('input_load.xlsx', sheet_name='load')
        cs_df = pd.read_excel('input_cs.xlsx', sheet_name='cs1')
        cs2_df = pd.read_excel('input_cs.xlsx', sheet_name='cs2')
        cs3_df = pd.read_excel('input_cs.xlsx', sheet_name='cs3')
        cs4_df = pd.read_excel('input_cs.xlsx', sheet_name='cs4')
        cs5_df = pd.read_excel('input_cs.xlsx', sheet_name='cs5')
        cs_df = cs_df.join(cs2_df)
        cs_df = cs_df.join(cs3_df)
        cs_df = cs_df.join(cs4_df)
        cs_df = cs_df.join(cs5_df)

        # Formatando dados de entrada
        pv_orig_total = get_data_in_list(pv_df, n_cluster)
        load_orig_total = get_data_in_list(load_df, n_cluster)
        cs_orig_total = get_data_in_list(cs_df, n_cluster)

    # Passar valores para granularidade de 15 min
    npts = int(npts / 15)
    pv_orig = get_data_in_15m(pv_orig_total, npts)
    load_orig = get_data_in_15m(load_orig_total, npts)
    cs_orig = get_data_in_15m(cs_orig_total, npts)

    # Otimização: Generic Algorithm
    sc = 1
    w = 0.0
    population = [15, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 15, 0, 0, 0]
    load_list = Loaddata().get_loadshape(load_orig, data_demand, npts, sc)
    cs_dict = Csdata().get_loadshape_charger(cs_orig, load_list, sc)
    opt_value = Gaoptimization(npts, resolucao, sc)
    cs_max_chargers = opt_value.get_max_char(cs_dict)
    opt, opt_loss, opt_density = opt_value.fitness_total(dss, w, load_list, population, cs_max_chargers, pv_orig,
                                                         cs_dict)
    print("Scenario: ", str(sc))
    print("Passo: ", str(w))
    print(opt)
    print(opt_loss)
    print(opt_density)
    print(population)

    # for sc in range(1):
    #     # Carregando Cenário N
    #     load_list = Loaddata().get_loadshape(load_orig, data_demand, npts, sc)
    #     cs_dict = Csdata().get_loadshape_charger(cs_orig, load_list, sc)
    #
    #     # Otimização
    #     opt_value = Gaoptimization(npts, resolucao, sc)
    #     fob_solution = []
    #     fob1_solution = []
    #     fob2_solution = []
    #     for step in range(11):
    #         w = 1 - ((step * 10) / 100)
    #         print('CENÁRIO ' + str(sc) + ' COM PESO DE ' + str(w))
    #         opt, opt_losses, opt_density, pop = opt_value.get_optimal_value(dss, max_iter, w, load_list, pv_orig,
    #                                                                         cs_dict)
    #         fob_solution.append(opt)
    #         fob1_solution.append(opt_losses)
    #         fob2_solution.append(opt_density)
    #         population['POP_sc' + str(sc) + '_w' + str(w)] = pop
    #         print("Scenario: ", str(sc))
    #         print("Passo: ", str(w))
    #         print(fob_solution)
    #         print(fob1_solution)
    #         print(fob2_solution)
    #         print(population)
    #     results['FOB_sc' + str(sc)] = fob_solution
    #     results['FOB1_sc' + str(sc)] = fob1_solution
    #     results['FOB2_sc' + str(sc)] = fob2_solution

    # # Output
    # results['w'] = [(1 - (x / 10)) for x in range(5)]
    # results_df = pd.DataFrame.from_dict(results)
    # results_df.set_index('w', inplace=True)
    # population_df = pd.DataFrame.from_dict(population)
    # with pd.ExcelWriter('output.xlsx') as writer:
    #     results_df.to_excel(writer, sheet_name='results')
    #     population_df.to_excel(writer, sheet_name='population', index=False)

import math
import numpy as np
import matplotlib.pyplot as plt

# Variáveis globais
CHARGER = 7.2  # kW


class Csdata:
    def __init__(self):
        self.trafo_list = {'ICB': 500, 'CGCO2': 225, 'CGCO1': 500, 'EComputacao': 300, 'ModelagemCom': 150,
                           'Engenharia': 500, 'RU': 300, 'Biblioteca': 225, 'CBR': 300, 'UsinaEng': 45, 'IAD': 300,
                           'CRITT': 300, 'FAEFID1': 300, 'FAEFID2': 300, 'ICH': 225, 'Servicos': 225, 'Planetario': 500,
                           'ILuminacao': 225, 'Economia': 225, 'Odontologia': 500, 'Comunicacao': 45, 'Bombeiros': 150,
                           'Reitoria': 300}

    def get_loadshape_charger(self, cs_orig, load_list, sc):
        # Máximo de carregadores
        max_chargers = self.get_max_chargers(load_list)
        max_chargers["ILuminacao"] = 0
        max_chargers["UsinaEng"] = 0

        # Dicionário com todas as curvas desse cenário
        cs_dict = {}
        for key, value in max_chargers.items():
            if key == 'ICB':
                value = 40
            if key == 'CGCO1':
                value = 40
            if key == 'Engenharia':
                value = 47
            if key == 'CGCO2':
                value = 17
            if key == 'EComputacao':
                value = 31
            if key == 'RU':
                value = 13
            if key == 'CRITT':
                value = 33
            if key == 'FAEFID1':
                value = 20
            if key == 'FAEFID2':
                value = 26
            if key == 'Odontologia':
                value = 36
            if key == 'IAD':
                value = 31
            if key == 'Reitoria':
                value = 19
            if key == 'ICH':
                value = 18
            if key == 'Servicos':
                value = 15
            if key == 'Economia':
                value = 23
            for ev in range(value):
                cs_dict[key + '_' + str(ev)] = cs_orig[key + '_' + str(ev)][sc].tolist()

        return cs_dict

    def get_max_chargers(self, load_list):
        max_chargers = {}
        for load_dict in load_list:
            kva = self.trafo_list[load_dict['NAME']]
            zipped_load_list = zip(load_dict['LOADSHAPE_P_A'], load_dict['LOADSHAPE_P_B'], load_dict['LOADSHAPE_P_C'])
            load_p_curve = [x + y + z for (x, y, z) in zipped_load_list]
            if load_dict['NAME'] != 'ILuminacao':
                zipped_load_list = zip(load_dict['LOADSHAPE_Q_A'], load_dict['LOADSHAPE_Q_B'],
                                       load_dict['LOADSHAPE_Q_C'])
                load_q_curve = [x + y + z for (x, y, z) in zipped_load_list]
                zipped_load_list = zip(load_p_curve, load_q_curve)
                load_s_curve = [np.sqrt((x ** 2) + (y ** 2)) for (x, y) in zipped_load_list]
            else:
                load_s_curve = load_p_curve
            max_chargers[load_dict['NAME']] = math.floor(0.9 * (kva - max(load_s_curve)) / CHARGER)

        return max_chargers

    def get_cs_curve(self, load_list, new_population, cs_dict, sc):

        # Criando dicionário com as curvas das estações
        cs_list = []
        n = 0
        for load_dict in load_list:
            if load_dict['NAME'] != 'UsinaEng' and load_dict['NAME'] != 'ILuminacao':
                if new_population[n] > 0:
                    for ev in range(new_population[n]):
                        name = str(load_dict['NAME']) + '_' + str(ev)
                        kw = cs_dict[load_dict['NAME'] + '_' + str(ev)][sc]
                        info = {'NAME': name,
                                'NPTS': 96,
                                'MINTERVAL': 15,
                                'USEACTUAL': "yes",
                                'LOADSHAPE_P': kw
                                }
                        cs_list.append(info)
            n += 1

        return cs_list

    def get_cs_loadshape(self, dss, cs_curve):
        for cs_dict in cs_curve:
            # Criando o LoadShape da Carga "Dicionario_Cargas["Nome"]"
            dss.text("New Loadshape.LS_CS_{}   npts={}   minterval={}   useactual={} ".format(cs_dict['NAME'],
                                                                                              cs_dict['NPTS'],
                                                                                              cs_dict['MINTERVAL'],
                                                                                              cs_dict['USEACTUAL']))
            curve = [round(n) for n in cs_dict['LOADSHAPE_P']]
            dss.loadshapes_write_name("LS_CS_{}".format(cs_dict['NAME']))
            dss.loadshapes_write_p_mult(curve)

    def get_cs_load(self, dss, cs_list):
        cod_old = '.3.1'
        cod = '.1.2'
        for cs_dict in cs_list:
            if cod_old == '.3.1':
                cod = '.1.2'
            elif cod_old == '.1.2':
                cod = '.2.3'
            elif cod_old == '.2.3':
                cod = '.3.1'
            if cs_dict['NAME'].split("_")[0] != 'ILuminacao' and cs_dict['NAME'].split("_")[0] != 'UsinaEng':
                # Criando o eletroposto
                script_text = "New Load.Carga_CS_{0}      bus1=busCarga_{1}{2}    KV=0.220       status=variable" \
                              "      daily=LS_CS_{0}       phases=3".format(cs_dict['NAME'],
                                                                            cs_dict['NAME'].split("_")[0], cod)
                dss.text(script_text)
                if cod == '.1.2':
                    cod_old = '.1.2'
                elif cod == '.2.3':
                    cod_old = '.2.3'
                elif cod == '.3.1':
                    cod_old = '.3.1'

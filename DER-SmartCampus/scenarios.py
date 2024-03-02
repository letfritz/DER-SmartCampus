import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from csdata import Csdata

SD_LOAD, SD_PV, SD_CHARGER = .05, .05, .05


class Scenarios:
    def __init__(self):
        pass

    def get_pv_scenarios(self, pv_list):

        # Gerando incerteza
        pv_orig = []
        for value in pv_list:
            for m in range(15):
                pv_orig.append(np.random.normal(value, value * SD_PV))

        return pv_orig

    def get_load_scenarios(self, data_demand, npts):
        load_total_dict = {}
        for key, value in data_demand.items():
            day_chose = np.random.randint(0, 6)
            load_total_dict[key + '_P_A'] = [np.random.normal(x, abs(x) * SD_LOAD)
                                             for x in value[npts * day_chose:npts * (1 + day_chose), 0].tolist()]
            load_total_dict[key + '_P_B'] = [np.random.normal(x, abs(x) * SD_LOAD)
                                             for x in value[npts * day_chose:npts * (1 + day_chose), 1].tolist()]
            load_total_dict[key + '_P_C'] = [np.random.normal(x, abs(x) * SD_LOAD)
                                             for x in value[npts * day_chose:npts * (1 + day_chose), 2].tolist()]
            if key != 'ILuminacao':
                load_total_dict[key + '_Q_A'] = [np.random.normal(x, abs(x) * SD_LOAD)
                                                 for x in value[npts * day_chose:npts * (1 + day_chose), 3].tolist()]
                load_total_dict[key + '_Q_B'] = [np.random.normal(x, abs(x) * SD_LOAD)
                                                 for x in value[npts * day_chose:npts * (1 + day_chose), 4].tolist()]
                load_total_dict[key + '_Q_C'] = [np.random.normal(x, abs(x) * SD_LOAD)
                                                 for x in value[npts * day_chose:npts * (1 + day_chose), 5].tolist()]
        return load_total_dict

    def get_cs_scenarios(self, sc_load):

        # Máximo de carregadores
        load = []
        for key, value in Csdata().trafo_list.items():
            if key != 'ILuminacao' and key != 'UsinaEng':
                info = {'NAME': key,
                        'LOADSHAPE_P_A': sc_load[key + '_P_A'],
                        'LOADSHAPE_P_B': sc_load[key + '_P_B'],
                        'LOADSHAPE_P_C': sc_load[key + '_P_C'],
                        'LOADSHAPE_Q_A': sc_load[key + '_Q_A'],
                        'LOADSHAPE_Q_B': sc_load[key + '_Q_B'],
                        'LOADSHAPE_Q_C': sc_load[key + '_Q_C']}
                load.append(info)
        max_chargers = Csdata().get_max_chargers(load)

        cs_total_dict = {}
        for key, value in sc_load.items():
            if key.split('_')[0] != 'UsinaEng' and key.split('_')[0] != 'ILuminacao':
                for ev in range(max_chargers[key.split('_')[0]] + 3):  # + 3 considera folga no resultado do cenário
                    cs_total_dict[key.split('_')[0] + '_' + str(ev)] = self.get_charge_curve(key.split('_')[0], ev)

        return cs_total_dict

    def get_charge_curve(self, bus, ev):

        # Quantidade de pessoas com carro elétrico no prédio
        # 5 pontos -> close to parking lots and building with high traffic of people;
        # 4 pontos -> building with high traffic of people  \\  \cline{1-3}
        #     1, 8, 20, 21 & 5.0\% & close to parking lots   \\ \cline{1-3}
        #     4, 5 & 5.0\% & building with medium traffic of people; high  traffic of vehicles    \\  \cline{1-3}
        #     12, 17 & 3.3\% & building with medium traffic of people   \\  \cline{1-3}
        #     2, 9, 10, 11 & 1.9\% & building with low traffic of people; high  traffic of vehicles   \\ \cline{1-3}
        #     13, 19 & 1.4\% & building with low traffic of people
        people_car = {'ICB': 3, 'CGCO2': 1, 'CGCO1': 5, 'EComputacao': 3, 'ModelagemCom': 3,
                      'Engenharia': 5, 'RU': 5, 'Biblioteca': 3, 'CBR': 1, 'UsinaEng': 0, 'IAD': 1,
                      'CRITT': 1, 'FAEFID1': 2, 'FAEFID2': 1, 'ICH': 4, 'Servicos': 4, 'Planetario': 5,
                      'ILuminacao': 0, 'Economia': 2, 'Odontologia': 4, 'Comunicacao': 1, 'Bombeiros': 3,
                      'Reitoria': 3}

        # Quantidade de pessoas com bicicleta elétrica no prédio
        people_bike = {'ICB': 30, 'CGCO2': 20, 'CGCO1': 50, 'EComputacao': 20, 'ModelagemCom': 10,
                       'Engenharia': 50, 'RU': 50, 'Biblioteca': 30, 'CBR': 20, 'UsinaEng': 0, 'IAD': 30,
                       'CRITT': 20, 'FAEFID1': 15, 'FAEFID2': 10, 'ICH': 30, 'Servicos': 30, 'Planetario': 20,
                       'ILuminacao': 0, 'Economia': 30, 'Odontologia': 50, 'Comunicacao': 10, 'Bombeiros': 30,
                       'Reitoria': 20}

        # Probabilidade de VE querendo carregar por hora em cada prédio
        prob = {'ICB': [0, 0, 0, 0, 0, 0, 0, 0.6, 0.6, 0.7, 0.5, 0.5, 0.2, 0.3, 0.5, 0.5, 0.4, 0.6, 0.7, 0.4, 0.2, 0,
                        0, 0],
                'CGCO2': [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.5, 0.7, 0.7, 0.5, 0.2, 0.4, 0.5, 0.6, 0.6, 0.3, 0.2, 0.1, 0,
                          0, 0, 0],
                'CGCO1': [0, 0, 0, 0, 0, 0, 0.3, 0.4, 0.3, 0.5, 0.4, 0.5, 0.2, 0.2, 0.3, 0.4, 0.4, 0.4, 0, 0, 0, 0,
                          0, 0],
                'EComputacao': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.4, 0.5, 0.4, 0.3, 0.1, 0, 0, 0, 0.2, 0.3, 0.4, 0.4, 0.3,
                                0, 0, 0],
                'ModelagemCom': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.6, 0.6, 0.3, 0.6, 0.6, 0.5, 0.3, 0.2, 0.3, 0.4, 0.2,
                                 0, 0, 0, 0],
                'Engenharia': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.6, 0.7, 0.7, 0.6, 0.4, 0.2, 0.3, 0.5, 0.6, 0.6, 0.7, 0.5,
                               0.2, 0.1, 0, 0],
                'RU': [0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0.3, 0.6, 0.7, 0.7, 0.6, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0],
                'Biblioteca': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.2, 0.1, 0, 0, 0, 0.3, 0.4, 0.3, 0.3, 0.3, 0.2, 0, 0,
                               0, 0],
                'CBR': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.4, 0.4, 0.2, 0.2, 0.2, 0.4, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2, 0,
                        0, 0],
                'UsinaEng': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'IAD': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.5, 0.5, 0.3, 0.5, 0.6, 0.4, 0.4, 0.3, 0.3, 0.2, 0.2, 0, 0,
                        0, 0],
                'CRITT': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.2, 0.1, 0, 0, 0,
                          0, 0],
                'FAEFID1': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0.3, 0.3, 0, 0, 0, 0, 0.2, 0.3, 0.3, 0.4, 0.3, 0.1, 0, 0, 0],
                'FAEFID2': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.4, 0.3, 0.1, 0, 0, 0, 0.2, 0.4, 0.4, 0.3, 0.2, 0.1, 0,
                            0, 0],
                'ICH': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.4, 0.5, 0.6, 0.3, 0.2, 0.2, 0.3, 0.4, 0.5, 0.3, 0.2, 0.2, 0.2, 0.1,
                        0, 0],
                'Servicos': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.5, 0.4, 0.2,
                             0, 0, 0],
                'Planetario': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0.7, 0.6, 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0, 0, 0., 0, 0,
                               0, 0],
                'ILuminacao': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Economia': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.5, 0.5, 0.3, 0.2, 0.3, 0.4, 0.5, 0.5, 0.3, 0.2, 0.2, 0.1,
                             0, 0, 0],
                'Odontologia': [0, 0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.4, 0.6, 0.3, 0.2, 0.1, 0.1, 0.3, 0.5, 0.5, 0.4, 0.2,
                                0.1, 0, 0, 0],
                'Comunicacao': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.5, 0.5, 0.3, 0.2, 0.1, 0.1, 0.3, 0.5, 0.5, 0.4, 0.3, 0.2,
                                0.1, 0, 0, 0],
                'Bombeiros': [0, 0, 0, 0, 0, 0, 0, 0.3, 0.4, 0.5, 0.5, 0.3, 0.2, 0.2, 0.4, 0.5, 0.4, 0.2, 0, 0, 0,
                              0, 0, 0],
                'Reitoria': [0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.4, 0.6, 0.7, 0.4, 0.5, 0.7, 0.6, 0.3, 0.3, 0.2, 0.1, 0, 0,
                             0, 0, 0]}

        # Probabilidade do carregador ser para carro ou para bicicleta
        charger_type = {'CAR': 1, 'BIKE': 0}

        # Fator de utilização do carregador
        factor = 1 - ev / 100

        # Probabilidade de utilização em cada hora
        charge_curve_h = [x * factor for x in prob[bus]]

        # Probabilidade de utilização em cada minuto
        charge_curve_m = []
        for value in charge_curve_h:
            for m in range(60):
                p = np.random.normal(value, abs(value) * SD_CHARGER)
                if p < 0:
                    p = 0
                charge_curve_m.append(p)
        # Curva do veículo elétrico
        cs_point = random.uniform(0, 1)  # Teste do tipo de carregador
        charge_curve = []
        for value in charge_curve_m:
            if cs_point <= charger_type['CAR']:
                # Quantidade de pessoas com carro elétrico no prédio
                n_ev = value * people_car[bus]
                # Potência consumida pelo carregador
                charge_curve.append(round(n_ev) * 7.2)  # 7.2 kW de potência para carregar o carro

            else:
                # Quantidade de pessoas com bicicleta elétrica no prédio
                n_ev = value * people_bike[bus]
                # Potência consumida pelo carregador
                charge_curve.append(round(n_ev) * 0.8)  # 0.8 kW de potência para carregar a bike

        return charge_curve

    def get_dict_results(self, data):
        data_dict = {}

        for key, value in data.items():
            n = 0
            for curve in value:
                data_dict[key + '_' + str(n)] = curve
                n += 1

        return data_dict


class Scenarioreduction:
    def __init__(self, n_cluster):
        self.n_cluster = n_cluster

    def get_scenarioreduction(self, data):

        # K-Maens para encontrar os cenários
        cluster = KMeans(n_clusters=self.n_cluster, random_state=10)
        cluster_labels = cluster.fit_predict(data)

        # Encontrando a média das curvas de cada cluster
        cluster_data = []
        for sc in range(len(cluster_labels)):
            cluster_data.append((cluster_labels[sc], data[sc]))

        # Criando média
        cluster_mean = np.zeros((self.n_cluster, len(data[0])))
        for k in range(self.n_cluster):
            count = 0
            for sc in range(len(cluster_labels)):
                if cluster_data[sc][0] == k:
                    cluster_mean[k, :] = [x + y for (x, y) in zip(list(cluster_mean[k, :]), list(cluster_data[sc][1]))]
                    count += 1
            cluster_mean[k, :] = [x / count for x in list(cluster_mean[k, :])]

        return cluster_mean

    def get_scenarioreduction_pv(self, sc_pv):
        # Redução de cenários
        cluster_mean = self.get_scenarioreduction(sc_pv)

        # Encontrando os valores das curvas a serem utilizadas
        sc_pv_dict = {'Engenharia': cluster_mean}
        return sc_pv_dict

    def get_scenarioreduction_load(self, sc_load):
        # Organizando dados
        sc_load_dict = {}
        for key, value in sc_load[0].items():
            load = []
            for sc in range(len(sc_load)):
                load.append(sc_load[sc][key])

            # Redução de cenários
            cluster_mean = self.get_scenarioreduction(load)

            # Encontrando os valores das curvas a serem utilizadas
            sc_load_dict[key] = cluster_mean

        return sc_load_dict

    def get_scenarioreduction_cs(self, sc_cs):
        # Organizando dados
        sc_cs_dict = {}
        for key, value in sc_cs[0].items():
            cs = []
            for sc in range(len(sc_cs)):
                cs.append(sc_cs[sc][key])
            # Redução de cenários
            if key.split('_')[0] != 'UsinaEng' and key.split('_')[0] != 'ILuminacao':
                cluster_mean = self.get_scenarioreduction(cs)
            else:
                cluster_mean = cs[0]

            # Encontrando os valores das curvas a serem utilizadas
            sc_cs_dict[key] = cluster_mean

        return sc_cs_dict

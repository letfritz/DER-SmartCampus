# Importando as bibliotecas
import numpy as np
import pandas as pd


class Loaddata:
    def __init__(self):
        pass

    def get_loadshape(self, data, data_demand, npts, sc):

        load_list = []
        for key, value in data_demand.items():
            if key != 'ILuminacao':
                info = {'NAME': key,
                        'NPTS': npts,
                        'MINTERVAL': 15,
                        'USEACTUAL': "yes",
                        'LOADSHAPE_P_A': data[key + '_P_A'][sc].tolist(),
                        'LOADSHAPE_Q_A': data[key + '_Q_A'][sc].tolist(),
                        'LOADSHAPE_P_B': data[key + '_P_B'][sc].tolist(),
                        'LOADSHAPE_Q_B': data[key + '_Q_B'][sc].tolist(),
                        'LOADSHAPE_P_C': data[key + '_P_C'][sc].tolist(),
                        'LOADSHAPE_Q_C': data[key + '_Q_C'][sc].tolist()
                        }
            else:
                info = {'NAME': key,
                        'NPTS': npts,
                        'MINTERVAL': 1,
                        'USEACTUAL': "yes",
                        'LOADSHAPE_P_A': data[key + '_P_A'][sc].tolist(),
                        'LOADSHAPE_P_B': data[key + '_P_B'][sc].tolist(),
                        'LOADSHAPE_P_C': data[key + '_P_C'][sc].tolist()
                        }
            load_list.append(info)

        return load_list

    def get_demand(self, npts):
        total_day_in_input = 6
        # Dados de entrada
        power = 6  # Quantidade de medidas de potência

        # Demandas Medidas
        df_demand = pd.read_excel('Demanda_Cargas.xlsx', sheet_name=None, header=None)

        data = {}
        for name, sheet in df_demand.items():
            sheet.drop(index=sheet.index[0], axis=0, inplace=True)
            sheet.drop(sheet.columns[4], axis=1, inplace=True)
            sheet.drop(sheet.columns[0], axis=1, inplace=True)
            matrix_value = np.zeros((npts * total_day_in_input, power))
            for hour in range(npts * total_day_in_input):
                if name != 'ILuminacao':
                    for p in range(power):
                        matrix_value[hour, p] = sheet.iloc[hour, p]
                else:
                    for p in range(power - 3):
                        matrix_value[hour, p] = sheet.iloc[hour, p]
            data[name] = matrix_value
        return data

    def get_dss_load(self, dss, load_list):

        for load_dict in load_list:
            # Criando o LoadShape da Carga "Dicionario_Cargas["Nome"]"
            dss.text("New Loadshape.LS_{}_A   npts={}   minterval={}   useactual={} ".format(load_dict['NAME'],
                                                                                             load_dict['NPTS'],
                                                                                             load_dict['MINTERVAL'],
                                                                                             load_dict['USEACTUAL']))
            dss.loadshapes_write_name("LS_{}_A".format(load_dict['NAME']))
            dss.loadshapes_write_p_mult(load_dict['LOADSHAPE_P_A'])
            if load_dict['NAME'] != 'ILuminacao':
                dss.loadshapes_write_name("LS_{}_A".format(load_dict['NAME']))
                dss.loadshapes_write_q_mult(load_dict['LOADSHAPE_Q_A'])

            dss.text("New Loadshape.LS_{}_B   npts={}   minterval={}   useactual={} ".format(load_dict['NAME'],
                                                                                             load_dict['NPTS'],
                                                                                             load_dict['MINTERVAL'],
                                                                                             load_dict['USEACTUAL']))
            dss.loadshapes_write_name("LS_{}_B".format(load_dict['NAME']))
            dss.loadshapes_write_p_mult(load_dict['LOADSHAPE_P_B'])
            if load_dict['NAME'] != 'ILuminacao':
                dss.loadshapes_write_name("LS_{}_B".format(load_dict['NAME']))
                dss.loadshapes_write_q_mult(load_dict['LOADSHAPE_Q_B'])

            dss.text("New Loadshape.LS_{}_C   npts={}   minterval={}   useactual={}".format(load_dict['NAME'],
                                                                                            load_dict['NPTS'],
                                                                                            load_dict['MINTERVAL'],
                                                                                            load_dict['USEACTUAL']))
            dss.loadshapes_write_name("LS_{}_C".format(load_dict['NAME']))
            dss.loadshapes_write_p_mult(load_dict['LOADSHAPE_P_C'])
            if load_dict['NAME'] != 'ILuminacao':
                dss.loadshapes_write_name("LS_{}_C".format(load_dict['NAME']))
                dss.loadshapes_write_q_mult(load_dict['LOADSHAPE_Q_C'])

            if load_dict['NAME'] != 'UsinaEng':
                # Criando o Carga
                script_text = "New Load.Carga_{0}_A      bus1=busCarga_{0}.1     KV=0.127       status=variable      " \
                              "daily=LS_{0}_A       phases=1".format(load_dict['NAME'])
                dss.text(script_text)
                script_text = "New Load.Carga_{0}_B      bus1=busCarga_{0}.2     KV=0.127       status=variable      " \
                              "daily=LS_{0}_B       phases=1".format(load_dict['NAME'])
                dss.text(script_text)
                script_text = "New Load.Carga_{0}_C      bus1=busCarga_{0}.3     KV=0.127       status=variable      " \
                              "daily=LS_{0}_C       phases=1".format(load_dict['NAME'])
                dss.text(script_text)
            else:
                # Criando a Usina da Engenharia
                script_text = "New Generator.Gerador_Engenharia_A      bus1=busGerador_Engenharia.1     phases=1     " \
                              "KV=0.127      daily=LS_UsinaEng_A        status=variable      Model=3"
                dss.text(script_text)
                script_text = "New Generator.Gerador_Engenharia_B      bus1=busGerador_Engenharia.2     phases=1     " \
                              "KV=0.127      daily=LS_UsinaEng_B        status=variable      Model=3"
                dss.text(script_text)
                script_text = "New Generator.Gerador_Engenharia_C      bus1=busGerador_Engenharia.3     phases=1     " \
                              "KV=0.127      daily=LS_UsinaEng_C        status=variable      Model=3"
                dss.text(script_text)

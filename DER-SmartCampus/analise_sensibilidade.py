import os
import py_dss_interface

import numpy as np
import pandas as pd
from os.path import exists
import matplotlib.pyplot as plt

from loaddata import Loaddata
from generationdata import Generationdata
from csdata import Csdata

# Instanciando objeto OpenDSS
dss = py_dss_interface.DSSDLL()

# Cenário 5
sc = 4
w = 0.4
resolucao = 15
npts = 1440 * 1  # Número de Pontos da Simulação (1440 pts,  96 pts, ...)
n_cluster = 5


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


def get_pv_generation(dss, pv_kw, pv_orig, sc):
    dss.text("New Loadshape.LS_PV_ICB   npts=96   minterval=15")
    dss.loadshapes_write_name("LS_PV_ICB")
    curve = [round(n) for n in pv_orig['Engenharia'][sc, :]]
    dss.loadshapes_write_p_mult(curve)
    dss.loadshapes_write_name("LS_PV_ICB")
    dss.loadshapes_normalize()

    dss.text("New Loadshape.LS_PV_FAEFID1   npts=96   minterval=15")
    dss.loadshapes_write_name("LS_PV_FAEFID1")
    curve = [round(n) for n in pv_orig['Engenharia'][sc, :]]
    dss.loadshapes_write_p_mult(curve)
    dss.loadshapes_write_name("LS_PV_FAEFID1")
    dss.loadshapes_normalize()

    dss.text("New Loadshape.LS_PV_ODONTOLOGIA   npts=96   minterval=15")
    dss.loadshapes_write_name("LS_PV_ODONTOLOGIA")
    curve = [round(n) for n in pv_orig['Engenharia'][sc, :]]
    dss.loadshapes_write_p_mult(curve)
    dss.loadshapes_write_name("LS_PV_ODONTOLOGIA")
    dss.loadshapes_normalize()

    script_text = "New Generator.PV_Gerador_ICB_A      bus1=busCarga_ICB.1     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_ICB        status=variable      " \
                  "Model=3".format(pv_kw[0])
    dss.text(script_text)
    script_text = "New Generator.PV_Gerador_ICB_B      bus1=busCarga_ICB.2     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_ICB        status=variable      " \
                  "Model=3".format(pv_kw[0])
    dss.text(script_text)
    script_text = "New Generator.PV_Gerador_ICB_C      bus1=busCarga_ICB.3     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_ICB        status=variable      " \
                  "Model=3".format(pv_kw[0])
    dss.text(script_text)

    script_text = "New Generator.PV_Gerador_FAEFID1_A      bus1=busCarga_FAEFID1.1     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_FAEFID1        status=variable      " \
                  "Model=3".format(pv_kw[1])
    dss.text(script_text)
    script_text = "New Generator.PV_Gerador_FAEFID1_B      bus1=busCarga_FAEFID1.2     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_FAEFID1        status=variable      " \
                  "Model=3".format(pv_kw[1])
    dss.text(script_text)
    script_text = "New Generator.PV_Gerador_FAEFID1_C      bus1=busCarga_FAEFID1.3     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_FAEFID1        status=variable      " \
                  "Model=3".format(pv_kw[1])
    dss.text(script_text)

    script_text = "New Generator.PV_Gerador_ODONTOLOGIA_A      bus1=busCarga_ODONTOLOGIA.1     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_ODONTOLOGIA        status=variable      " \
                  "Model=3".format(pv_kw[2])
    dss.text(script_text)
    script_text = "New Generator.PV_Gerador_ODONTOLOGIA_B      bus1=busCarga_ODONTOLOGIA.2     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_ODONTOLOGIA        status=variable      " \
                  "Model=3".format(pv_kw[2])
    dss.text(script_text)
    script_text = "New Generator.PV_Gerador_ODONTOLOGIA_C      bus1=busCarga_ODONTOLOGIA.3     phases=1     " \
                  "KV=0.127      KW={0}      daily=LS_PV_ODONTOLOGIA        status=variable      " \
                  "Model=3".format(pv_kw[2])
    dss.text(script_text)


def foo(dss, load_list, new_population, pv_orig, cs_dict, pv_kw, sc):
    # Compilando arquivo do OpenDSS com a rede da UFJF
    dss_file = os.path.dirname(os.path.realpath(__file__)) + "\Modelagem_Circ_Dist_UFJF"
    dss.text("compile {}".format(dss_file))

    # Carregando cargas
    Loaddata().get_dss_load(dss, load_list)

    # Carregando geração PV
    get_pv_generation(dss, pv_kw, pv_orig, sc)

    # Criando Estação de recarga
    cs_list = Csdata().get_cs_curve(load_list, new_population, cs_dict, sc)
    Csdata().get_cs_loadshape(dss, cs_list)
    Csdata().get_cs_load(dss, cs_list)

    # Definindo EnergyMeter
    dss.text("New EnergyMeter.Feeder1 Line.3F_MT_T1/1.C1 1")
    dss.text("New EnergyMeter.Feeder2 Line.3F_MT_T2/1.C2 1")

    # Solução
    dss.text("Set VoltageBases=[23.1, 6.6, 0.22]")
    dss.text("CalcVoltageBases")
    dss.text("Set mode=daily  number={}  stepsize={}m".format(1, resolucao))
    dss.text("Set hour=0")
    for _ in range(npts):
        dss.solution_solve()
        dss.text("Export meter")


# Arquivos
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
npts = int(npts / 15)

# Carga
data_demand = Loaddata().get_demand(npts)
load_orig_total = get_data_in_list(load_df, n_cluster)
load_orig = get_data_in_15m(load_orig_total, npts)
load_list = Loaddata().get_loadshape(load_orig, data_demand, npts, sc)

# PV
pv_orig_total = get_data_in_list(pv_df, n_cluster)
pv_orig = get_data_in_15m(pv_orig_total, npts)

# CS
cs_orig_total = get_data_in_list(cs_df, n_cluster)
cs_dict = get_data_in_15m(cs_orig_total, npts)

# FOB 1: minimizar perdas
pv_list = [[90, 50, 50], [40, 50, 50], [140, 50, 50], [190, 50, 50], [90, 100, 50], [90, 150, 50], [90, 200, 50],
           [90, 50, 100], [90, 50, 150], [90, 50, 200]]
ev_list = [[6, 6, 6, 5, 6, 12], [5, 6, 6, 5, 6, 12], [14, 6, 6, 5, 6, 12], [15, 6, 6, 5, 6, 12], [6, 8, 6, 5, 6, 12],
           [6, 11, 6, 5, 6, 12], [6, 12, 6, 5, 6, 12], [6, 6, 8, 5, 6, 12], [6, 6, 9, 5, 6, 12], [6, 6, 10, 5, 6, 12],
           [6, 6, 6, 4, 6, 12], [6, 6, 6, 5, 4, 12], [6, 6, 6, 5, 5, 12], [6, 6, 6, 5, 6, 8], [6, 6, 6, 5, 6, 10],
           [6, 6, 6, 5, 6, 13], [6, 6, 6, 5, 6, 15], [6, 6, 6, 5, 6, 16]]
for pv_kw_3 in pv_list:
    for ev in ev_list:
        x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        x[0], x[1], x[11], x[12], x[13], x[22] = ev
        pv_kw = [y / 3 for y in pv_kw_3]

        # Apagando o arquivo Meter
        if exists('subestacao_EXP_METERS.csv'):
            os.remove('subestacao_EXP_METERS.csv')

        foo(dss, load_list, x, pv_orig, cs_dict, pv_kw, sc)

        # Calculando o custo
        meter = pd.read_csv("subestacao_EXP_METERS.csv")
        meter = meter[[" Hour", " Meter", " \"kWh\"", " \"kvarh\""]]
        meter_feeder1 = meter[meter[' Meter'] == ' "FEEDER1"     ']
        meter_feeder2 = meter[meter[' Meter'] == ' "FEEDER2"     ']

        kvah_feeder1 = np.zeros(24)
        kvah_feeder2 = np.zeros(24)
        for hour in range(meter_feeder1.shape[0] - 1):
            kvah_feeder1[meter_feeder1[" Hour"][hour * 2]] += float(meter_feeder1[" \"kWh\""][hour * 2])
            kvah_feeder2[meter_feeder2[" Hour"][hour * 2 + 1]] += float(meter_feeder2[" \"kWh\""][hour * 2 + 1])
        kvah_feeder1[0] += float(meter_feeder1[" \"kWh\""][meter.shape[0] - 2])
        kvah_feeder2[0] += float(meter_feeder2[" \"kWh\""][meter.shape[0] - 1])
        kvah = kvah_feeder1 + kvah_feeder2

        te = np.concatenate(([0.3688 * np.ones(17), 1.6840 * np.ones(3), 0.3688 * np.ones(4)]), axis=0)
        contrato = 1400 * 15.32
        tributo_grid = (1 - (0.0076 + 0.0349 + 0.06))
        te_total = (te + contrato) / tributo_grid

        print("-----")
        print(ev)
        print(pv_kw_3)
        print("R$ ", str(sum(te * kvah) * 30))

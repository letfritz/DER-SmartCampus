import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from loaddata import Loaddata
import pandas as pd
from kneed import KneeLocator

# Colocar metodologia


sns.set_theme(style="whitegrid")
sns.set(font_scale=1.5)
sns.set_style(style="whitegrid")

# GRÁFICO DA POSSIBLIDADE DE PESSOAS COM CARRO ELÉTRICO
# people_car = {'ICB': 3, 'CGCO2': 1, 'CGCO1': 5, 'EComputacao': 3, 'ModelagemCom': 3,
#               'Engenharia': 5, 'RU': 5, 'Biblioteca': 3, 'CBR': 1, 'UsinaEng': 0, 'IAD': 1,
#               'CRITT': 1, 'FAEFID1': 2, 'FAEFID2': 1, 'ICH': 4, 'Servicos': 4, 'Planetario': 5,
#               'ILuminacao': 0, 'Economia': 2, 'Odontologia': 4, 'Comunicacao': 1, 'Bombeiros': 3,
#               'Reitoria': 3}
# people_bike = {'ICB': 30, 'CGCO2': 20, 'CGCO1': 50, 'EComputacao': 20, 'ModelagemCom': 10,
#                'Engenharia': 50, 'RU': 50, 'Biblioteca': 30, 'CBR': 20, 'UsinaEng': 0, 'IAD': 30,
#                'CRITT': 20, 'FAEFID1': 15, 'FAEFID2': 10, 'ICH': 30, 'Servicos': 30, 'Planetario': 20,
#                'ILuminacao': 0, 'Economia': 30, 'Odontologia': 50, 'Comunicacao': 10, 'Bombeiros': 30,
#                'Reitoria': 20}
# names = list(people_car.keys())
# values_car = list(people_car.values())
# values_bike = list(people_bike.values())
# data = [values_car, values_bike]
#
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
#
# plt.bar(range(len(people_car)), values_car, tick_label=names, label='Carro')
# plt.bar(range(len(people_car)), values_bike, tick_label=names, label='Bike')
# plt.xticks(rotation=90)
# plt.show()

# GRÁFICO DAS POTÊNCIAS
# data_demand = Loaddata().get_demand(1440)
# load = np.zeros((3, 1440))
# load_q = np.zeros((3, 1440))
# for key, value in data_demand.items():
#     load[0, :] += value[:, 0].tolist()
#     load[1, :] += value[:, 1].tolist()
#     load[2, :] += value[:, 2].tolist()
#     if key != 'ILuminacao':
#         load_q[0, :] += value[:, 3].tolist()
#         load_q[1, :] += value[:, 4].tolist()
#         load_q[2, :] += value[:, 5].tolist()
# df_pv = pd.read_excel('PV_UFJF.xlsx')
# pv_list = df_pv['Lab solar UFJF / Power / Mean Values  [kW]3'].tolist()
# pv_list = pv_list[96:96*2]
# pv_list = [n / 1000 for n in pv_list]
# pv_norm = [n / max(pv_list) for n in pv_list]
# pv_norm = [n * (500 / 3) for n in pv_norm]
# pv_orig = []
# for value in pv_norm:
#     for m in range(15):
#         pv_orig.append(value)
#
# load[0, :] -= pv_orig
# load[1, :] -= pv_orig
# load[2, :] -= pv_orig
#
# plt.plot(load[0], label='Fase A')
# plt.plot(load[1], label='Fase B')
# plt.plot(load[2], label='Fase C')
# plt.xlabel("Tempo [h]")
# plt.ylabel("Potência Ativa [kW]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()
#
# plt.plot(load_q[0], label='Fase A')
# plt.plot(load_q[1], label='Fase B')
# plt.plot(load_q[2], label='Fase C')
# plt.xlabel("Tempo [h]")
# plt.ylabel("Potência Reativa [kvar]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()

# GRÁFICO DOS CENÁRIOS
# # pv_df = pd.read_excel('input_pv.xlsx', sheet_name='pv')
# # load_df = pd.read_excel('input_load.xlsx', sheet_name='load')
# #
# # n_cluster = 5
# # bus = []
# # for key in pv_df.columns.values:
# #     if key[-2] == '_':
# #         bus.append(key[:-2])
# #     else:
# #         bus.append(key[:-3])
# #     bus = list(dict.fromkeys(bus))
# # pv_orig = {}
# # for key in bus:
# #     data_array = np.zeros((n_cluster, len(pv_df[key + '_' + str(0)])))
# #     for n in range(n_cluster):
# #         data_array[n, :] = [((500 / 3) * x) / max(pv_df[key + '_' + str(n)].tolist())
# #                             for x in pv_df[key + '_' + str(n)].tolist()]
# #     pv_orig[key] = data_array
# # bus = []
# # for key in load_df.columns.values:
# #     if key[-2] == '_':
# #         bus.append(key[:-2])
# #     else:
# #         bus.append(key[:-3])
# #     bus = list(dict.fromkeys(bus))
# # load_orig = {}
# # for key in bus:
# #     data_array = np.zeros((n_cluster, len(load_df[key + '_' + str(0)])))
# #     for n in range(n_cluster):
# #         data_array[n, :] = load_df[key + '_' + str(n)].tolist()
# #     load_orig[key] = data_array
# #
# # plt.plot(pv_orig['Engenharia'][0, :], label='Scenario 1')
# # plt.plot(pv_orig['Engenharia'][1, :], label='Scenario 2')
# # plt.plot(pv_orig['Engenharia'][2, :], label='Scenario 3')
# # plt.plot(pv_orig['Engenharia'][3, :], label='Scenario 4')
# # plt.plot(pv_orig['Engenharia'][4, :], label='Scenario 5')
# # plt.xlabel("Time [h]")
# # plt.ylabel("Photovoltaic Generation [kW]")
# # plt.xlim([0, 1439])
# # plt.grid()
# # plt.legend()
# # plt.show()
#
# load_p_a = np.zeros((n_cluster, 1440))
# load_p_b = np.zeros((n_cluster, 1440))
# load_p_c = np.zeros((n_cluster, 1440))
# load_q_a = np.zeros((n_cluster, 1440))
# load_q_b = np.zeros((n_cluster, 1440))
# load_q_c = np.zeros((n_cluster, 1440))
# for key, value in load_orig.items():
#     if key.split('_')[1] == 'P' and key.split('_')[2] == 'A':
#         load_p_a[0, :] += value[0, :].tolist()
#         load_p_a[1, :] += value[1, :].tolist()
#         load_p_a[2, :] += value[2, :].tolist()
#         load_p_a[3, :] += value[3, :].tolist()
#         load_p_a[4, :] += value[4, :].tolist()
#     if key.split('_')[1] == 'P' and key.split('_')[2] == 'B':
#         load_p_b[0, :] += value[0, :].tolist()
#         load_p_b[1, :] += value[1, :].tolist()
#         load_p_b[2, :] += value[2, :].tolist()
#         load_p_b[3, :] += value[3, :].tolist()
#         load_p_b[4, :] += value[4, :].tolist()
#     if key.split('_')[1] == 'P' and key.split('_')[2] == 'C':
#         load_p_c[0, :] += value[0, :].tolist()
#         load_p_c[1, :] += value[1, :].tolist()
#         load_p_c[2, :] += value[2, :].tolist()
#         load_p_c[3, :] += value[3, :].tolist()
#         load_p_c[4, :] += value[4, :].tolist()
#     if key.split('_')[1] == 'Q' and key.split('_')[2] == 'A':
#         load_q_a[0, :] += value[0, :].tolist()
#         load_q_a[1, :] += value[1, :].tolist()
#         load_q_a[2, :] += value[2, :].tolist()
#         load_q_a[3, :] += value[3, :].tolist()
#         load_q_a[4, :] += value[4, :].tolist()
#     if key.split('_')[1] == 'Q' and key.split('_')[2] == 'B':
#         load_q_b[0, :] += value[0, :].tolist()
#         load_q_b[1, :] += value[1, :].tolist()
#         load_q_b[2, :] += value[2, :].tolist()
#         load_q_b[3, :] += value[3, :].tolist()
#         load_q_b[4, :] += value[4, :].tolist()
#     if key.split('_')[1] == 'Q' and key.split('_')[2] == 'C':
#         load_q_c[0, :] += value[0, :].tolist()
#         load_q_c[1, :] += value[1, :].tolist()
#         load_q_c[2, :] += value[2, :].tolist()
#         load_q_c[3, :] += value[3, :].tolist()
#         load_q_c[4, :] += value[4, :].tolist()
#
# plt.plot(load_p_a[0, :], label='Scenario 1')
# plt.plot(load_p_a[1, :], label='Scenario 2')
# plt.plot(load_p_a[2, :], label='Scenario 3')
# plt.plot(load_p_a[3, :], label='Scenario 4')
# plt.plot(load_p_a[4, :], label='Scenario 5')
# plt.xlabel("Time [h]")
# plt.ylabel("Active Power Phase A [kW]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()
#
# plt.plot(load_p_b[0, :], label='Scenario 1')
# plt.plot(load_p_b[1, :], label='Scenario 2')
# plt.plot(load_p_b[2, :], label='Scenario 3')
# plt.plot(load_p_b[3, :], label='Scenario 4')
# plt.plot(load_p_b[4, :], label='Scenario 5')
# plt.xlabel("Time [h]")
# plt.ylabel("Active Power Phase B [kW]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()
#
# plt.plot(load_p_c[0, :], label='Scenario 1')
# plt.plot(load_p_c[1, :], label='Scenario 2')
# plt.plot(load_p_c[2, :], label='Scenario 3')
# plt.plot(load_p_c[3, :], label='Scenario 4')
# plt.plot(load_p_c[4, :], label='Scenario 5')
# plt.xlabel("Time [h]")
# plt.ylabel("Active Power Phase C [kW]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()
#
# plt.plot(load_q_a[0, :], label='Scenario 1')
# plt.plot(load_q_a[1, :], label='Scenario 2')
# plt.plot(load_q_a[2, :], label='Scenario 3')
# plt.plot(load_q_a[3, :], label='Scenario 4')
# plt.plot(load_q_a[4, :], label='Scenario 5')
# plt.xlabel("Time [h]")
# plt.ylabel("Reactive Power Phase A [kvar]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()
#
# plt.plot(load_q_b[0, :], label='Scenario 1')
# plt.plot(load_q_b[1, :], label='Scenario 2')
# plt.plot(load_q_b[2, :], label='Scenario 3')
# plt.plot(load_q_b[3, :], label='Scenario 4')
# plt.plot(load_q_b[4, :], label='Scenario 5')
# plt.xlabel("Time [h]")
# plt.ylabel("Reactive Power Phase B [kvar]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()
#
# plt.plot(load_q_c[0, :], label='Scenario 1')
# plt.plot(load_q_c[1, :], label='Scenario 2')
# plt.plot(load_q_c[2, :], label='Scenario 3')
# plt.plot(load_q_c[3, :], label='Scenario 4')
# plt.plot(load_q_c[4, :], label='Scenario 5')
# plt.xlabel("Time [h]")
# plt.ylabel("Reactive Power Phase C [kvar]")
# plt.xlim([0, 1439])
# plt.grid()
# plt.legend()
# plt.show()

# Carregadores por barra
# bus = ['ICB', 'CGCO2', 'Engenharia', 'CBR', 'CRITT', 'FAEFID1', 'FAEFID2', 'Servicos', 'Odontologia', 'Comunicacao',
#        'Bombeiros', 'Reitoria']
# pop = [[16, 0, 12, 0, 0, 15, 0, 7, 0, 0, 0, 16], [18, 0, 0, 0, 0, 16, 16, 0, 0, 0, 0, 15],
#        [8, 0, 4, 0, 0, 8, 0, 8, 0, 4, 0, 13], [5, 3, 0, 0, 0, 7, 7, 0, 0, 0, 0, 15],
#        [0, 12, 0, 14, 20, 0, 0, 0, 0, 5, 0, 15],
#        [6, 11, 0, 0, 0, 4, 4, 0, 4, 0, 0, 16],
#        [11, 8, 0, 0, 8, 5, 0, 2, 0, 0, 0, 11],
#        [4, 11, 0, 0, 6, 5, 6, 0, 0, 0, 0, 13]]
# plt.scatter(bus, pop[0], label='Scenario 1', marker=11, c="red")
# plt.scatter(bus, pop[1], label='Scenario 1', marker=11, c="red")
# plt.scatter(bus, pop[2], label='Scenario 1', marker=11, c="red")
# plt.scatter(bus, pop[3], label='Scenario 1', marker=11, c="red")
# plt.scatter(bus, pop[4], label='Scenario 2', marker='X', c="green")
# plt.scatter(bus, pop[5], label='Scenario 3', marker='D', c="blue")
# plt.scatter(bus, pop[6], label='Scenario 4', marker='*', c="orange")
# plt.scatter(bus, pop[7], label='Scenario 5', marker='o', c="purple")
# plt.ylabel("Quantidade de Carregadores")
# plt.xticks(rotation=90)
# plt.legend(loc="upper right", ncol=5)
# plt.show()

# # Fronteira de Pareto
fob11 = [1131.6894, 802.251081, 731.609346, 708.0590393, 699.5465244, 619.2454162, 612.8741498, 595.4402585,
         566.7083671, 557.4443947, 570.9954834]
fob21 = [243.1203759, 175.8489782, 199.7850683, 212.5542499, 253.9025378, 315.0919714, 329.3497925, 366.5599208,
         377.3807449, 486.3381362, 825.0518288]
fob11_nd = [802.251081, 731.609346, 708.0590393, 699.5465244, 619.2454162, 612.8741498, 595.4402585, 566.7083671,
            557.4443947]
fob21_nd = [175.8489782, 199.7850683, 212.5542499, 253.9025378, 315.0919714, 329.3497925, 366.5599208, 377.3807449,
            486.3381362]
fob12 = [430.9917138, 359.7099932, 343.2275027, 353.228738, 374.9053193, 365.0803256, 382.443608, 351.8136086,
         353.5536971, 397.6353918, 518.4520105]
fob22 = [590.682706, 476.0637419, 470.8871869, 468.2595414, 399.1106196, 357.8598172, 331.6574771, 295.8123563,
         266.2198967, 245.9557748, 247.4356043]
fob12_nd = [343.2275027, 351.8136086, 353.5536971, 397.6353918]
fob22_nd = [470.8871869, 295.8123563, 266.2198967, 245.9557748]
fob13 = [705.1430991, 654.005642, 628.9937852, 606.2931781, 620.9100419, 638.2150406, 634.8103909, 648.2723873,
         651.918635, 681.666936, 883.6692379]
fob23 = [561.5193739, 385.9836526, 398.9690196, 384.8776829, 366.0011526, 312.3763876, 319.6371893, 324.3656351,
         308.6485747, 278.9543337, 377.151186]
fob13_nd = [606.2931781, 620.9100419, 638.2150406, 634.8103909, 651.918635, 681.666936]
fob23_nd = [384.8776829, 366.0011526, 312.3763876, 319.6371893, 308.6485747, 278.9543337]
fob14 = [710.7564611, 638.5215703, 615.9994322, 626.0828427, 633.2581146, 642.7161955, 649.0059508, 666.6524627,
         698.5508803, 724.8781881, 959.9911123]
fob24 = [519.6615886, 552.8931783, 497.1604962, 418.1600081, 384.6312983, 383.1140547, 362.6823088, 335.674932,
         320.3726027, 274.0852544, 356.9372524]
fob14_nd = [615.9994322, 626.0828427, 633.2581146, 642.7161955, 649.0059508, 666.6524627, 698.5508803, 724.8781881]
fob24_nd = [497.1604962, 418.1600081, 384.6312983, 383.1140547, 362.6823088, 335.674932, 320.3726027, 274.0852544]
fob15 = [615.819455, 578.2305396, 575.8804854, 616.986183, 589.326653, 605.5349548, 679.1104088, 652.9232786,
         675.7254267, 683.394985, 931.1398586]
fob25 = [513.8808317, 430.4999441, 406.5757407, 422.8122549, 357.133929, 338.2756307, 337.5658184, 280.2705826,
         275.3172172, 273.1926157, 369.6483595]
fob15_nd = [575.8804854, 589.326653, 605.5349548, 652.9232786, 675.7254267, 683.394985]
fob25_nd = [406.5757407, 357.133929, 338.2756307, 280.2705826, 275.3172172, 273.1926157]
fob21 = [x / 1000 for x in fob21]
fob21 = [x * 100 for x in fob21]
fob21_nd = [x / 1000 for x in fob21_nd]
fob21_nd = [x * 100 for x in fob21_nd]
fob22 = [x / 1000 for x in fob22]
fob22 = [x * 100 for x in fob22]
fob22_nd = [x / 1000 for x in fob22_nd]
fob22_nd = [x * 100 for x in fob22_nd]
fob23 = [x / 1000 for x in fob23]
fob23 = [x * 100 for x in fob23]
fob23_nd = [x / 1000 for x in fob23_nd]
fob23_nd = [x * 100 for x in fob23_nd]
fob24 = [x / 1000 for x in fob24]
fob24 = [x * 100 for x in fob24]
fob24_nd = [x / 1000 for x in fob24_nd]
fob24_nd = [x * 100 for x in fob24_nd]
fob25 = [x / 1000 for x in fob25]
fob25 = [x * 100 for x in fob25]
fob25_nd = [x / 1000 for x in fob25_nd]
fob25_nd = [x * 100 for x in fob25_nd]
plt.scatter(fob11_nd, fob21_nd, marker='o', color='blue')
plt.plot(fob11_nd, fob21_nd, '--', color='blue')
plt.fill(fob11, fob21, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.1, label='Scenario 1')
plt.scatter(fob12_nd, fob22_nd, marker='o', color='orange')
plt.plot(fob12_nd, fob22_nd, '--', color='orange')
plt.fill(fob12, fob22, linewidth=2, edgecolor='orange', facecolor='orange', alpha=0.1, label='Scenario 2')
plt.scatter(fob13_nd, fob23_nd, marker='o', color='green')
plt.plot(fob13_nd, fob23_nd, '--', color='green')
plt.fill(fob13, fob23,  linewidth=2, edgecolor='green', facecolor='green', alpha=0.1, label='Scenario 3')
plt.scatter(fob14_nd, fob24_nd, marker='o', color='red')
plt.plot(fob14_nd, fob24_nd, '--', color='red')
plt.fill(fob14, fob24,  linewidth=2, edgecolor='red', facecolor='red', alpha=0.1, label='Scenario 4')
plt.scatter(fob15_nd, fob25_nd, marker='o', color='purple')
plt.plot(fob15_nd, fob25_nd, '--', color='purple')
plt.fill(fob15, fob25,  linewidth=2, edgecolor='purple', facecolor='purple', alpha=0.1,  label='Scenario 5')
kn = KneeLocator(fob11_nd, fob21_nd, curve='convex', direction='decreasing', interp_method='interp1d')
print(kn.knee)
kn = KneeLocator(fob12_nd, fob22_nd, curve='convex', direction='decreasing', interp_method='interp1d')
print(kn.knee)
kn = KneeLocator(fob13_nd, fob23_nd, curve='convex', direction='decreasing', interp_method='interp1d')
print(kn.knee)
kn = KneeLocator(fob14_nd, fob24_nd, curve='convex', direction='decreasing', interp_method='interp1d')
print(kn.knee)
kn = KneeLocator(fob15_nd, fob25_nd, curve='convex', direction='decreasing', interp_method='interp1d')
print(kn.knee)
fob1 = [566.7083671, 353.5536971, 638.2150406, 649.0059508, 589.326653]
fob2 = [37.73807449, 26.62198967, 31.23763876, 36.26823088, 35.7133929]
plt.plot(fob1, fob2, marker='*', linestyle='None', markersize=10, color='black', label='Pareto Knee')
plt.xlabel("Active Power [kW]")
plt.ylabel("Dist. to the highest load buses [%]")
plt.legend()
plt.show()

# Carregadores por barra
# sc1 = [[3, 0, 0, 0, 10, 5, 7, 0, 0, 0, 0, 13], [4, 0, 0, 0, 0, 10, 5, 9, 0, 4, 0, 13],
#        [0, 7, 0, 0, 0, 0, 7, 0, 0, 0, 5, 16], [6, 0, 0, 0, 0, 8, 0, 0, 0, 0, 3, 16],
#        [5, 3, 0, 0, 0, 7, 7, 0, 0, 0, 0, 15], [8, 0, 4, 0, 0, 8, 0, 8, 0, 4, 0, 13],
#        [18, 0, 0, 0, 0, 16, 16, 0, 0, 0, 0, 15], [16, 0, 12, 0, 0, 15, 0, 7, 0, 0, 0, 16],
#        [21, 0, 9, 0, 0, 15, 0, 6, 0, 0, 0, 15], [14, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 10],
#        [15, 0, 16, 0, 10, 0, 0, 0, 15, 0, 0, 0], [2, 0, 4, 10, 8, 0, 11, 0, 10, 0, 0, 0],
#        [0, 3, 4, 7, 0, 0, 15, 0, 0, 4, 0, 12], [0, 6, 0, 8, 0, 9, 0, 0, 0, 0, 4, 12],
#        [0, 10, 0, 8, 0, 0, 10, 0, 0, 0, 0, 8], [0, 8, 0, 8, 10, 0, 8, 0, 0, 0, 0, 8],
#        [0, 12, 0, 14, 20, 0, 0, 0, 0, 5, 0, 15], [0, 12, 0, 10, 16, 0, 14, 0, 0, 0, 0, 14],
#        [14, 0, 0, 12, 18, 0, 7, 0, 0, 0, 0, 15], [10, 6, 0, 8, 10, 4, 0, 0, 0, 0, 0, 7],
#        [8, 6, 0, 8, 10, 0, 5, 0, 0, 0, 0, 8], [15, 0, 16, 0, 10, 0, 0, 0, 15, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 11, 0, 7, 0, 0, 8], [0, 6, 0, 9, 0, 9, 5, 0, 0, 0, 0, 10],
#        [0, 11, 0, 0, 6, 0, 0, 0, 5, 0, 0, 14], [6, 7, 0, 0, 12, 5, 0, 0, 0, 0, 0, 13],
#        [6, 11, 0, 0, 0, 4, 4, 0, 4, 0, 0, 16], [5, 11, 0, 0, 6, 0, 4, 0, 0, 0, 0, 13],
#        [6, 9, 0, 0, 8, 6, 0, 0, 0, 0, 0, 10], [14, 6, 0, 0, 8, 0, 4, 0, 0, 0, 0, 10],
#        [14, 8, 0, 0, 6, 4, 4, 0, 0, 0, 0, 9], [13, 6, 0, 0, 6, 8, 0, 0, 0, 0, 0, 8],
#        [8, 0, 10, 0, 5, 0, 0, 0, 4, 0, 0, 0], [0, 6, 6, 0, 9, 0, 0, 0, 0, 0, 0, 10],
#        [0, 8, 0, 4, 11, 0, 0, 0, 0, 0, 4, 14], [0, 12, 0, 0, 8, 6, 0, 0, 0, 0, 0, 12],
#        [5, 12, 0, 0, 8, 5, 5, 0, 0, 0, 0, 10], [5, 14, 0, 0, 8, 0, 0, 0, 0, 0, 0, 12],
#        [7, 12, 0, 0, 9, 5, 0, 0, 0, 2, 0, 10], [10, 8, 0, 0, 8, 4, 4, 0, 0, 0, 0, 11],
#        [11, 8, 0, 0, 8, 5, 0, 2, 0, 0, 0, 11], [15, 8, 0, 0, 6, 0, 0, 0, 0, 0, 0, 9],
#        [14, 8, 0, 0, 4, 4, 0, 0, 0, 0, 0, 9], [6, 0, 10, 0, 4, 0, 0, 0, 4, 0, 0, 0],
#        [0, 0, 0, 5, 7, 8, 8, 0, 0, 0, 0, 12], [0, 0, 0, 0, 12, 0, 6, 0, 4, 4, 0, 15],
#        [7, 0, 0, 0, 0, 0, 6, 5, 0, 0, 6, 15], [0, 5, 0, 0, 9, 0, 6, 0, 0, 0, 0, 15],
#        [2, 13, 0, 0, 5, 0, 0, 0, 0, 0, 0, 16], [0, 11, 0, 4, 9, 0, 0, 0, 0, 3, 0, 14],
#        [4, 11, 0, 0, 6, 5, 6, 0, 0, 0, 0, 13], [12, 11, 0, 0, 4, 5, 0, 0, 2, 0, 0, 11],
#        [15, 10, 0, 0, 0, 3, 6, 0, 0, 0, 0, 8], [12, 8, 0, 0, 5, 0, 5, 0, 0, 0, 0, 9],
#        [6, 0, 9, 5, 0, 0, 0, 0, 5, 0, 0, 0]]
# # sns.set_theme(style="whitegrid")
# df = pd.DataFrame(sc1, columns=['1', '2', '6', '9', '11', '12', '13', '15', '18', '19', '20', '21'])
# sns.boxplot(data=df, palette="Set3")
# sns.swarmplot(data=df, color=".25")
# plt.xlabel("Bus")
# plt.ylabel("Number of chargers")
# plt.show()

# GRÁFICO BOXPLOT GD
# gd = [[100, 0, 40, 0, 0, 40, 0], [100, 0, 40, 0, 0, 30, 0], [120, 0, 20, 90, 0, 0, 0], [120, 0, 60, 0, 0, 30, 0],
#       [80, 0, 50, 0, 40, 0, 0], [90, 0, 40, 0, 130, 0, 0], [80, 0, 50, 0, 50, 0, 0], [90, 0, 20, 0, 180, 0, 0],
#       [80, 0, 40, 0, 0, 30, 0], [110, 0, 30, 0, 0, 50, 0], [100, 30, 0, 0, 130, 0, 0], [60, 40, 0, 0, 0, 30, 0],
#       [100, 0, 0, 0, 40, 0, 30], [80, 20, 0, 0, 0, 30, 0], [70, 40, 0, 0, 0, 30, 0], [60, 40, 0, 0, 0, 40, 0],
#       [60, 30, 0, 0, 80, 0, 0], [80, 20, 0, 0, 0, 40, 0], [110, 10, 0, 0, 0, 30, 0], [100, 0, 0, 0, 30, 0, 10],
#       [90, 0, 60, 0, 0, 50, 0], [90, 0, 50, 0, 0, 50, 0], [80, 0, 30, 0, 0, 100, 0], [180, 0, 80, 0, 0, 70, 0],
#       [80, 0, 30, 0, 0, 60, 0], [120, 0, 20, 0, 0, 70, 0], [80, 0, 50, 0, 0, 50, 0], [100, 0, 100, 0, 0, 40],
#       [90, 0, 20, 0, 0, 60, 0], [100, 0, 30, 0, 0, 80, 0], [90, 0, 40, 0, 0, 40, 0], [90, 0, 50, 0, 0, 50, 0],
#       [80, 0, 40, 0, 0, 50, 0], [110, 0, 130, 0, 0, 70, 0], [120, 0, 120, 0, 0, 70, 0], [130, 0, 140, 0, 0, 60, 0],
#       [100, 0, 50, 0, 130, 0, 0], [110, 0, 190, 0, 0, 70, 0], [110, 0, 50, 0, 0, 30, 0], [110, 0, 40, 0, 190, 0, 0],
#       [90, 0, 40, 0, 0, 80, 0], [100, 0, 50, 0, 0, 50, 0], [80, 0, 30, 0, 0, 40, 0], [100, 0, 30, 0, 0, 30, 0],
#       [90, 0, 30, 0, 0, 60, 0], [90, 0, 50, 0, 0, 60, 0], [100, 0, 110, 0, 0, 50, 0], [190, 0, 30, 0, 0, 70, 0],
#       [80, 0, 50, 0, 0, 60, 0], [100, 0, 110, 0, 0, 50, 0]
#       ]
# # sns.set_theme(style="whitegrid")
# df = pd.DataFrame(gd, columns=['1', '3', '12', '14', '15', '18', '20'])
# sns.boxplot(data=df, palette="Set3")
# sns.swarmplot(data=df, color=".25")
# plt.xlabel("Bus")
# plt.ylabel("Power generation [kW]")
# plt.show()

# HEATMAP
# data = pd.read_excel('results/results.xlsx', sheet_name='Análise')
# analise = data.pivot("pv", "chargers", "cost")
# ax = sns.heatmap(analise, xticklabels=True, yticklabels=True, center=analise.loc["Median", "Median"],
#                  cbar_kws={'label': 'Operational cost [R$]'}) #, cbar=False, linewidths=.5
# plt.xlabel("Number of chargers")
# plt.ylabel("Photovoltaic system capacity")
# plt.show()

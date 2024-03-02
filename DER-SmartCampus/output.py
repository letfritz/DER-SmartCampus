# ----------------------------------------------------------------------------------------------
# ------------------------ UNIVERSIDADE FEDERAL DE JUIZ DE FORA --------------------------------
# ----------------------------------------------------------------------------------------------
# -------------------------- FACULDADE DE ENGENHARIA ELÉTRICA ----------------------------------
# ----------------------------------------------------------------------------------------------
# --------------------------------- PLOT DOS MONITORES -----------------------------------------
# ----------------------------------------------------------------------------------------------

# Bolsistas: Caio Cesar Amorim Silva & Michael Santos Nepomuceno


# Objetivo: Este código tem por objetivo criar uma função para fazer a plotagem dos monitores através da biblioteca
# Matplotlib


def Plot_Monitor_Potencia_Cargas(Nome_do_Monitor, Nome_da_Carga, Npts, Resolucao, dss, np, plt):

    Monitor_FaseA = "Monitor_Carga_{}_A".format(Nome_do_Monitor)
    Monitor_FaseB = "Monitor_Carga_{}_B".format(Nome_do_Monitor)
    Monitor_FaseC = "Monitor_Carga_{}_C".format(Nome_do_Monitor)


    dss.monitors_write_name("{}".format(Monitor_FaseA)) # Ativando o elemento monitor
    P_FaseA = dss.monitors_channel(1)  # Potência Ativa na fase A da Carga em kW, ou seja o próprio LoadShape
    Q_FaseA = dss.monitors_channel(2)  # Potência Reativa na fase A da Carga em kVAr, ou seja o próprio LoadShape

    dss.monitors_write_name("{}".format(Monitor_FaseB))
    P_FaseB = dss.monitors_channel(1)
    Q_FaseB = dss.monitors_channel(2)

    dss.monitors_write_name("{}".format(Monitor_FaseC))
    P_FaseC = dss.monitors_channel(1)
    Q_FaseC = dss.monitors_channel(2)

    # Potência Total demandada pela carga Escolhida (Para somar as potências das 3 fases devemos transformar as tuplas em arrays(Matrizes))
    P_Total = np.array(P_FaseA) + np.array(P_FaseB) + np.array(P_FaseC)
    Q_Total = np.array(Q_FaseA) + np.array(Q_FaseB) + np.array(Q_FaseC)


    # Plotando a Demanda da Carga da Escolhida com os monitores através da Biblioteca Matplotlib

    Hora = np.linspace(0, 23+((60 - Resolucao)/60), Npts) # Eixo x do gráfico com "Npts" pts
    plt.plot(Hora, P_Total, "g", label='P') # Nesta linha de comando iremos plotar um gráfico com "len(P_Total_Engenharia)" valores no eixo x e Os valores de P_Total_Engenharia no eixo y. A cor do grágico será verde ("g")
    plt.plot(Hora, Q_Total, "b", label='Q') # Cor Azul ("b"), O Gráfico será nomeado com Q (label='Q')
    plt.title("Potência Ativa e Reativa da Carga {}".format(Nome_da_Carga)) # Título do gráfico
    plt.legend() # Colocaremos legendas nesse gráfico (Legenda nos eixos)
    plt.ylabel("kW, kvar") #Legenda do eixo y
    plt.xlabel("Hora")   #Legenda do eixo X
    plt.xlim(0,23+((60 - Resolucao)/60))
    plt.grid(True)
    plt.show()  # Este comando é responsável por apresentar o gráfico na tela

    # Podemos Salvar esse plot como um arquivo .png em um diretório
    # plt.savefig(r"C:\Users\CAIO\Desktop\Caio\UFJF\Iniciacao_Cientifica\Bolsa_IC_PIBIC_2020\Python\Alocacao_VE_UFJF_Cargas_Deseq\Graficos\Demanda_Engenharia.png")
    # Podemos salvar também no disquete que aparece no próprio subplot disponibilizado pela matplotlib.


def Plot_Monitor_Potencia_Gerador(Nome_do_Monitor_Gerador, Nome_do_Gerador, Npts, Resolucao, dss, np, plt):

    Monitor_FaseA = "Monitor_Gerador_{}_A".format(Nome_do_Monitor_Gerador)
    Monitor_FaseB = "Monitor_Gerador_{}_B".format(Nome_do_Monitor_Gerador)
    Monitor_FaseC = "Monitor_Gerador_{}_C".format(Nome_do_Monitor_Gerador)


    dss.monitors_write_name("{}".format(Monitor_FaseA)) # Ativando o elemento monitor
    P_FaseA = dss.monitors_channel(1)  # Potência Ativa na fase A da Carga em kW, ou seja o próprio LoadShape
    Q_FaseA = dss.monitors_channel(2)  # Potência Reativa na fase A da Carga em kVAr, ou seja o próprio LoadShape

    dss.monitors_write_name("{}".format(Monitor_FaseB))
    P_FaseB = dss.monitors_channel(1)
    Q_FaseB = dss.monitors_channel(2)

    dss.monitors_write_name("{}".format(Monitor_FaseC))
    P_FaseC = dss.monitors_channel(1)
    Q_FaseC = dss.monitors_channel(2)

    # Potência Total demandada pela carga Escolhida (Para somar as potências das 3 fases devemos transformar as tuplas em arrays(Matrizes))
    P_Total = np.array(P_FaseA) + np.array(P_FaseB) + np.array(P_FaseC)
    Q_Total = np.array(Q_FaseA) + np.array(Q_FaseB) + np.array(Q_FaseC)


    # Plotando a Demanda da Carga da Escolhida com os monitores através da Biblioteca Matplotlib

    Hora = np.linspace(0, 23 + ((60 - Resolucao) / 60), Npts)  # Eixo x do gráfico com "Npts" pts
    plt.plot(Hora, P_Total, "g", label='P') # Nesta linha de comando iremos plotar um gráfico com "len(P_Total_Engenharia)" valores no eixo x e Os valores de P_Total_Engenharia no eixo y. A cor do grágico será verde ("g")
    plt.plot(Hora, Q_Total, "b", label='Q') # Cor Azul ("b"), O Gráfico será nomeado com Q (label='Q')
    plt.title("Potência Ativa e Reativa do Gerador - {}".format(Nome_do_Gerador)) # Título do gráfico
    plt.legend() # Colocaremos legendas nesse gráfico (Legenda nos eixos)
    plt.ylabel("kW, kvar") #Legenda do eixo y
    plt.xlabel("Hora")   #Legenda do eixo X
    plt.xlim(0,23+((60 - Resolucao)/60))
    plt.grid(True)
    plt.show()  # Este comando é responsável por apresentar o gráfico na tela
import numpy as np


class Generationdata:
    def __init__(self):
        pass

    def get_pv_curve(self, pv):
        # Curva PV
        pv_curve_orig = []
        for kw in pv:
            for hour in range(60):
                pv_curve_orig.append(kw)
        pv_curve = []
        for kw in pv_curve_orig:
            if kw > 0:
                kw = np.random.normal(kw, kw * 0.3)
            if kw < 0:
                kw = 0
            pv_curve.append(kw)
        return pv_curve

    def get_dss_pv(self, dss, pv, sc):

        # Criando loadshape LS_PV
        for key, value in pv.items():
            dss.text("New Loadshape.LS_PV_{}   npts=96   minterval=15".format(key))
            dss.loadshapes_write_name("LS_PV_{}".format(key))
            curve = [round(n) for n in value[sc, :]]
            dss.loadshapes_write_p_mult(curve)
            dss.loadshapes_write_name("LS_PV_{}".format(key))
            dss.loadshapes_normalize()

        # Criando carga
        for key, value in pv.items():
            script_text = "New Generator.PV_Gerador_{0}_A      bus1=busCarga_{0}.1     phases=1     " \
                          "KV=0.127      KW=166.66      daily=LS_PV_{0}        status=variable      " \
                          "Model=3".format(key)
            dss.text(script_text)
            script_text = "New Generator.PV_Gerador_{0}_B      bus1=busCarga_{0}.2     phases=1     " \
                          "KV=0.127      KW=166.66      daily=LS_PV_{0}        status=variable      " \
                          "Model=3".format(key)
            dss.text(script_text)
            script_text = "New Generator.PV_Gerador_{0}_C      bus1=busCarga_{0}.3     phases=1     " \
                          "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
                          "Model=3".format(key)
            dss.text(script_text)

            # Alocação Cenário 0
            # script_text = "New Generator.PV_Gerador_ICB_A      bus1=busCarga_ICB.1     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # script_text = "New Generator.PV_Gerador_ICB_B      bus1=busCarga_ICB.2     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # script_text = "New Generator.PV_Gerador_ICB_C      bus1=busCarga_ICB.3     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # # --
            # script_text = "New Generator.PV_Gerador_FAEFID1_A      bus1=busCarga_FAEFID1.1     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # script_text = "New Generator.PV_Gerador_FAEFID1_B      bus1=busCarga_FAEFID1.2     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # script_text = "New Generator.PV_Gerador_FAEFID1_C      bus1=busCarga_FAEFID1.3     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # # --
            # script_text = "New Generator.PV_Gerador_SERVICOS_A      bus1=busCarga_SERVICOS.1     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # script_text = "New Generator.PV_Gerador_SERVICOS_B      bus1=busCarga_SERVICOS.2     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)
            # script_text = "New Generator.PV_Gerador_SERVICOS_C      bus1=busCarga_SERVICOS.3     phases=1     " \
            #               "KV=0.127      KW=66.66      daily=LS_PV_{0}        status=variable      " \
            #               "Model=3".format(key)
            # dss.text(script_text)

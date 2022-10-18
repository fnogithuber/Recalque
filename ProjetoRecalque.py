import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import pandas as pd
import xlrd
from xlrd import *


diam13 = pd.Series({'DIÂMETRO': '13mm', 'curva de 90°': 0.2, 'curva de 45°': 0.2, 'Registro gaveta': 0.1, 'Registro de globo': 4.9,
                    'Válvula de pé e crivo': 3.6, 'Válvula de retenção tipo leve': 1.1, 'Válvula de retenção tipo pesado': 1.6})

diam19 = pd.Series({'DIÂMETRO': '19mm', 'curva de 90°': 0.3, 'curva de 45°': 0.2, 'Registro gaveta': 0.1, 'Registro de globo': 6.7,
                    'Válvula de pé e crivo': 5.6, 'Válvula de retenção tipo leve': 1.6, 'Válvula de retenção tipo pesado': 2.4})

diam25 = pd.Series({'DIÂMETRO': '25mm', 'curva de 90°': 0.3, 'curva de 45°': 0.2, 'Registro gaveta': 0.2, 'Registro de globo': 8.2,
                    'Válvula de pé e crivo': 7.3, 'Válvula de retenção tipo leve': 2.1, 'Válvula de retenção tipo pesado': 3.2})

diam32 = pd.Series({'DIÂMETRO': '32mm', 'curva de 90°': 0.4, 'curva de 45°': 0.3, 'Registro gaveta': 0.2, 'Registro de globo': 11.3,
                    'Válvula de pé e crivo': 10, 'Válvula de retenção tipo leve': 2.7, 'Válvula de retenção tipo pesado': 4})

diam38 = pd.Series({'DIÂMETRO': '38mm', 'curva de 90°': 0.5, 'curva de 45°': 0.3, 'Registro gaveta': 0.3, 'Registro de globo': 13.4,
                    'Válvula de pé e crivo': 11.6, 'Válvula de retenção tipo leve': 3.2, 'Válvula de retenção tipo pesado': 4.8})

diam50 = pd.Series({'DIÂMETRO': '50mm', 'curva de 90°': 0.6, 'curva de 45°': 0.4, 'Registro gaveta': 0.4, 'Registro de globo': 17.4,
                    'Válvula de pé e crivo': 14, 'Válvula de retenção tipo leve': 4.2, 'Válvula de retenção tipo pesado': 6.4})

diam63 = pd.Series({'DIÂMETRO': '63mm', 'curva de 90°': 0.8, 'curva de 45°': 0.5, 'Registro gaveta': 0.4, 'Registro de globo': 21,
                    'Válvula de pé e crivo': 17, 'Válvula de retenção tipo leve': 5.2, 'Válvula de retenção tipo pesado': 8.1})

diam75 = pd.Series({'DIÂMETRO': '75mm', 'curva de 90°': 1, 'curva de 45°': 0.6, 'Registro gaveta': 0.5, 'Registro de globo': 26,
                    'Válvula de pé e crivo': 20, 'Válvula de retenção tipo leve': 6.3, 'Válvula de retenção tipo pesado': 9.7})

diam100 = pd.Series({'DIÂMETRO': '100mm', 'curva de 90°': 1.3, 'curva de 45°': 0.7, 'Registro gaveta': 0.7, 'Registro de globo': 34,
                    'Válvula de pé e crivo': 23, 'Válvula de retenção tipo leve': 8.4, 'Válvula de retenção tipo pesado': 12.9})

diam125 = pd.Series({'DIÂMETRO': '125mm', 'curva de 90°': 1.6, 'curva de 45°': 0.9, 'Registro gaveta': 0.9, 'Registro de globo': 43,
                    'Válvula de pé e crivo': 30, 'Válvula de retenção tipo leve': 10.4, 'Válvula de retenção tipo pesado': 16.1})

diam150 = pd.Series({'DIÂMETRO': '150mm', 'curva de 90°': 1.9, 'curva de 45°': 1.1, 'Registro gaveta': 1.1, 'Registro de globo': 51,
                    'Válvula de pé e crivo': 39, 'Válvula de retenção tipo leve': 12.5, 'Válvula de retenção tipo pesado': 19.3})

diam200 = pd.Series({'DIÂMETRO': '200mm', 'curva de 90°': 2.4, 'curva de 45°': 1.5, 'Registro gaveta': 1.4, 'Registro de globo': 67,
                    'Válvula de pé e crivo': 52, 'Válvula de retenção tipo leve': 16, 'Válvula de retenção tipo pesado': 25})

diam250 = pd.Series({'DIÂMETRO': '250mm', 'curva de 90°': 3, 'curva de 45°': 1.8, 'Registro gaveta': 1.7, 'Registro de globo': 85,
                    'Válvula de pé e crivo': 65, 'Válvula de retenção tipo leve': 20, 'Válvula de retenção tipo pesado': 32})

diam300 = pd.Series({'DIÂMETRO': '300mm', 'curva de 90°': 3.6, 'curva de 45°': 2.2, 'Registro gaveta': 2.1, 'Registro de globo': 102,
                    'Válvula de pé e crivo': 78, 'Válvula de retenção tipo leve': 24, 'Válvula de retenção tipo pesado': 38})

diam350 = pd.Series({'DIÂMETRO': '350mm', 'curva de 90°': 4.4, 'curva de 45°': 2.5, 'Registro gaveta': 2.4, 'Registro de globo': 120,
                    'Válvula de pé e crivo': 90, 'Válvula de retenção tipo leve': 28, 'Válvula de retenção tipo pesado': 45})


df = pd.DataFrame([diam13, diam19, diam25, diam32, diam38, diam50, diam63, diam75, diam100, diam125, diam150, diam200,
                   diam250, diam300, diam350])





janela = Tk()
janela.title("Projeto de Recalque")
janela.geometry("950x500")
janela.resizable(width=False, height=False)
janela.configure(bg='#0e89c7')


global curva_90_perda_s
global curva_45_perda_s
global registro_gaveta_perda_s
global registro_globo_perda_s
global valvula_crivo_perda_s
global altura_man_total
global vazao_ajustada_cubic_meters
global vazao_ajustada_cubic_hours

def calculo():
    global curva_90_perda_s
    global curva_45_perda_s
    global registro_gaveta_perda_s
    global registro_globo_perda_s
    global valvula_crivo_perda_s

    global curva_90_perda_r
    global curva_45_perda_r
    global registro_gaveta_perda_r
    global registro_globo_perda_r
    global retencao_leve_perda_r
    global retencao_pesada_perda_r
    global altura_man_total
    global vazao_ajustada_cubic_meters
    global vazao_ajustada_cubic_hours

    if campo_vazao.get() == '' or campo_horas.get() == '' or campo_comprimento_succao.get() == '' or campo_comprimento_recalque.get() == '' or campo_altura_succao.get() == '' or campo_altura_recalque.get() == '':
        tkinter.messagebox.showinfo("Aviso", "Campos não preenchidos!")
    else:
        vazao_ajustada = (float(campo_vazao.get()) * 24) / float(campo_horas.get())
        vazao_ajustada_cubic_meters = vazao_ajustada / 1000
        vazao_ajustada_cubic_hours = vazao_ajustada_cubic_meters * 3600


        tempo_funcionamento = float(campo_horas.get())

        diametro = ((1.3 * (tempo_funcionamento / 24) ** 0.25) * vazao_ajustada_cubic_meters ** (1 / 2)) * 1000


        if diametro <= 6.3:
            diametro_succao = 6.3
            diametro_recalque = 6.3
        elif diametro <= 9.5:
            diametro_succao = 9.5
            diametro_recalque = 6.3
        elif diametro <= 12.5:
            diametro_succao = 12.5
            diametro_recalque = 9.5
        elif diametro <= 16:
            diametro_succao = 16
            diametro_recalque = 12.5
        elif diametro <= 19:
            diametro_succao = 19
            diametro_recalque = 16
        elif diametro <= 25:
            diametro_succao = 25
            diametro_recalque = 19
        elif diametro <= 31:
            diametro_succao = 31
            diametro_recalque = 25
        elif diametro <= 38:
            diametro_succao = 38
            diametro_recalque = 31
        elif diametro <= 50:
            diametro_succao = 50
            diametro_recalque = 38
        elif diametro <= 62:
            diametro_succao = 62
            diametro_recalque = 50
        elif diametro <= 75:
            diametro_succao = 75
            diametro_recalque = 62
        elif diametro <= 100:
            diametro_succao = 100
            diametro_recalque = 75
        elif diametro <= 125:
            diametro_succao = 125
            diametro_recalque = 100
        elif diametro <= 150:
            diametro_succao = 150
            diametro_recalque = 125
        elif diametro <= 200:
            diametro_succao = 200
            diametro_recalque = 150
        elif diametro <= 250:
            diametro_succao = 250
            diametro_recalque = 200
        elif diametro <= 300:
            diametro_succao = 300
            diametro_recalque = 250
        elif diametro <= 350:
            diametro_succao = 350
            diametro_recalque = 300
        elif diametro <= 400:
            diametro_succao = 400
            diametro_recalque = 350
        elif diametro <= 450:
            diametro_succao = 450
            diametro_recalque = 400
        elif diametro <= 500:
            diametro_succao = 500
            diametro_recalque = 450
        elif diametro <= 550:
            diametro_succao = 550
            diametro_recalque = 500
        elif diametro <= 600:
            diametro_succao = 600
            diametro_recalque = 550
        elif diametro <= 650:
            diametro_succao = 650
            diametro_recalque = 600
        elif diametro <= 700:
            diametro_succao = 700
            diametro_recalque = 650
        elif diametro <= 750:
            diametro_succao = 750
            diametro_recalque = 700

        velocidade_econ_succao = (4 * vazao_ajustada_cubic_meters) / (3.1415 * (diametro_succao / 1000)**2)
        velocidade_econ_succao = round(velocidade_econ_succao, 3)

        velocidade_econ_recalque = (4 * vazao_ajustada_cubic_meters) / (3.1415 * (diametro_recalque / 1000)**2)
        velocidade_econ_recalque = round(velocidade_econ_recalque, 3)

        altura_succao = float(campo_altura_succao.get())
        altura_recalque = float(campo_altura_recalque.get())

        altura_geometrica = altura_succao + altura_recalque

        #Atribuir valor do diâmetro de sucção para relacionar com a tabela de perda de carga

        if diametro_succao == 13:
            curva_90_perda_s = df.loc[0, 'curva de 90°']
            curva_45_perda_s = df.loc[0, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[0, 'Registro gaveta']
            registro_globo_perda_s = df.loc[0, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[0, 'Válvula de pé e crivo']
        elif diametro_succao == 19:
            curva_90_perda_s = df.loc[1, 'curva de 90°']
            curva_45_perda_s = df.loc[1, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[1, 'Registro gaveta']
            registro_globo_perda_s = df.loc[1, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[1, 'Válvula de pé e crivo']
        elif diametro_succao == 25:
            curva_90_perda_s = df.loc[2, 'curva de 90°']
            curva_45_perda_s = df.loc[2, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[2, 'Registro gaveta']
            registro_globo_perda_s = df.loc[2, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[2, 'Válvula de pé e crivo']
        elif diametro_succao == 32:
            curva_90_perda_s = df.loc[3, 'curva de 90°']
            curva_45_perda_s = df.loc[3, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[3, 'Registro gaveta']
            registro_globo_perda_s = df.loc[3, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[3, 'Válvula de pé e crivo']
        elif diametro_succao == 38:
            curva_90_perda_s = df.loc[4, 'curva de 90°']
            curva_45_perda_s = df.loc[4, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[4, 'Registro gaveta']
            registro_globo_perda_s = df.loc[4, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[4, 'Válvula de pé e crivo']
        elif diametro_succao == 50:
            curva_90_perda_s = df.loc[5, 'curva de 90°']
            curva_45_perda_s = df.loc[5, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[5, 'Registro gaveta']
            registro_globo_perda_s = df.loc[5, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[5, 'Válvula de pé e crivo']
        elif diametro_succao == 63:
            curva_90_perda_s = df.loc[6, 'curva de 90°']
            curva_45_perda_s = df.loc[6, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[6, 'Registro gaveta']
            registro_globo_perda_s = df.loc[6, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[6, 'Válvula de pé e crivo']
        elif diametro_succao == 75:
            curva_90_perda_s = df.loc[7, 'curva de 90°']
            curva_45_perda_s = df.loc[7, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[7, 'Registro gaveta']
            registro_globo_perda_s = df.loc[7, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[7, 'Válvula de pé e crivo']
        elif diametro_succao == 100:
            curva_90_perda_s = df.loc[8, 'curva de 90°']
            curva_45_perda_s = df.loc[8, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[8, 'Registro gaveta']
            registro_globo_perda_s = df.loc[8, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[8, 'Válvula de pé e crivo']
        elif diametro_succao == 125:
            curva_90_perda_s = df.loc[9, 'curva de 90°']
            curva_45_perda_s = df.loc[9, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[9, 'Registro gaveta']
            registro_globo_perda_s = df.loc[9, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[9, 'Válvula de pé e crivo']
        elif diametro_succao == 150:
            curva_90_perda_s = df.loc[10, 'curva de 90°']
            curva_45_perda_s = df.loc[10, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[10, 'Registro gaveta']
            registro_globo_perda_s = df.loc[10, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[10, 'Válvula de pé e crivo']
        elif diametro_succao == 200:
            curva_90_perda_s = df.loc[11, 'curva de 90°']
            curva_45_perda_s = df.loc[11, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[11, 'Registro gaveta']
            registro_globo_perda_s = df.loc[11, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[11, 'Válvula de pé e crivo']
        elif diametro_succao == 250:
            curva_90_perda_s = df.loc[12, 'curva de 90°']
            curva_45_perda_s = df.loc[12, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[12, 'Registro gaveta']
            registro_globo_perda_s = df.loc[12, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[12, 'Válvula de pé e crivo']
        elif diametro_succao == 300:
            curva_90_perda_s = df.loc[13, 'curva de 90°']
            curva_45_perda_s = df.loc[13, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[13, 'Registro gaveta']
            registro_globo_perda_s = df.loc[13, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[13, 'Válvula de pé e crivo']
        elif diametro_succao == 350:
            curva_90_perda_s = df.loc[14, 'curva de 90°']
            curva_45_perda_s = df.loc[14, 'curva de 45°']
            registro_gaveta_perda_s = df.loc[14, 'Registro gaveta']
            registro_globo_perda_s = df.loc[14, 'Registro de globo']
            valvula_crivo_perda_s = df.loc[14, 'Válvula de pé e crivo']



        # Atribuir valor do diâmetro de recalque para relacionar com a tabela de perda de carga

        if diametro_recalque == 13:
            curva_90_perda_r = df.loc[0, 'curva de 90°']
            curva_45_perda_r = df.loc[0, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[0, 'Registro gaveta']
            registro_globo_perda_r = df.loc[0, 'Registro de globo']
            retencao_leve_perda_r = df.loc[0, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[0, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 19:
            curva_90_perda_r = df.loc[1, 'curva de 90°']
            curva_45_perda_r = df.loc[1, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[1, 'Registro gaveta']
            registro_globo_perda_r = df.loc[1, 'Registro de globo']
            retencao_leve_perda_r = df.loc[1, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[1, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 25:
            curva_90_perda_r = df.loc[2, 'curva de 90°']
            curva_45_perda_r = df.loc[2, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[2, 'Registro gaveta']
            registro_globo_perda_r = df.loc[2, 'Registro de globo']
            retencao_leve_perda_r = df.loc[2, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[2, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 32:
            curva_90_perda_r = df.loc[3, 'curva de 90°']
            curva_45_perda_r = df.loc[3, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[3, 'Registro gaveta']
            registro_globo_perda_r = df.loc[3, 'Registro de globo']
            retencao_leve_perda_r = df.loc[3, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[3, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 38:
            curva_90_perda_r = df.loc[4, 'curva de 90°']
            curva_45_perda_r = df.loc[4, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[4, 'Registro gaveta']
            registro_globo_perda_r = df.loc[4, 'Registro de globo']
            retencao_leve_perda_r = df.loc[4, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[4, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 50:
            curva_90_perda_r = df.loc[5, 'curva de 90°']
            curva_45_perda_r = df.loc[5, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[5, 'Registro gaveta']
            registro_globo_perda_r = df.loc[5, 'Registro de globo']
            retencao_leve_perda_r = df.loc[5, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[5, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 63:
            curva_90_perda_r = df.loc[6, 'curva de 90°']
            curva_45_perda_r = df.loc[6, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[6, 'Registro gaveta']
            registro_globo_perda_r = df.loc[6, 'Registro de globo']
            retencao_leve_perda_r = df.loc[6, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[6, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 75:
            curva_90_perda_r = df.loc[7, 'curva de 90°']
            curva_45_perda_r = df.loc[7, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[7, 'Registro gaveta']
            registro_globo_perda_r = df.loc[7, 'Registro de globo']
            retencao_leve_perda_r = df.loc[7, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[7, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 100:
            curva_90_perda_r = df.loc[8, 'curva de 90°']
            curva_45_perda_r = df.loc[8, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[8, 'Registro gaveta']
            registro_globo_perda_r = df.loc[8, 'Registro de globo']
            retencao_leve_perda_r = df.loc[8, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[8, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 125:
            curva_90_perda_r = df.loc[9, 'curva de 90°']
            curva_45_perda_r = df.loc[9, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[9, 'Registro gaveta']
            registro_globo_perda_r = df.loc[9, 'Registro de globo']
            retencao_leve_perda_r = df.loc[9, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[9, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 150:
            curva_90_perda_r = df.loc[10, 'curva de 90°']
            curva_45_perda_r = df.loc[10, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[10, 'Registro gaveta']
            registro_globo_perda_r = df.loc[10, 'Registro de globo']
            retencao_leve_perda_r = df.loc[10, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[10, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 200:
            curva_90_perda_r = df.loc[11, 'curva de 90°']
            curva_45_perda_r = df.loc[11, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[11, 'Registro gaveta']
            registro_globo_perda_r = df.loc[11, 'Registro de globo']
            retencao_leve_perda_r = df.loc[11, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[11, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 250:
            curva_90_perda_r = df.loc[12, 'curva de 90°']
            curva_45_perda_r = df.loc[12, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[12, 'Registro gaveta']
            registro_globo_perda_r = df.loc[12, 'Registro de globo']
            retencao_leve_perda_r = df.loc[12, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[12, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 300:
            curva_90_perda_r = df.loc[13, 'curva de 90°']
            curva_45_perda_r = df.loc[13, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[13, 'Registro gaveta']
            registro_globo_perda_r = df.loc[13, 'Registro de globo']
            retencao_leve_perda_r = df.loc[13, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[13, 'Válvula de retenção tipo pesado']
        elif diametro_recalque == 350:
            curva_90_perda_r = df.loc[14, 'curva de 90°']
            curva_45_perda_r = df.loc[14, 'curva de 45°']
            registro_gaveta_perda_r = df.loc[14, 'Registro gaveta']
            registro_globo_perda_r = df.loc[14, 'Registro de globo']
            retencao_leve_perda_r = df.loc[14, 'Válvula de retenção tipo leve']
            retencao_pesada_perda_r = df.loc[14, 'Válvula de retenção tipo pesado']



        L_virtual_succao = (float(campo_comprimento_succao.get()) + float(combo_curva_90_s.get()) * curva_90_perda_s + float(combo_curva_45_s.get()) * curva_45_perda_s
        + float(combo_registro_gaveta_s.get()) * registro_gaveta_perda_s + float(combo_registro_globo_s.get()) * registro_globo_perda_s + float(combo_crivo_s.get()) * valvula_crivo_perda_s)

        L_virtual_recalque = (float(campo_comprimento_recalque.get()) + float(combo_curva_90_r.get()) * curva_90_perda_r + float(combo_curva_45_r.get()) * curva_45_perda_r
        + float(combo_registro_gaveta_r.get()) * registro_gaveta_perda_r + float(combo_registro_globo_r.get()) * registro_globo_perda_r + float(combo_retencao_leve_r.get()) * retencao_leve_perda_r
        + float(combo_retencao_pesada_r.get()) * retencao_pesada_perda_r + 5)

        L_virtual_succao = round(L_virtual_succao, 2)
        L_virtual_recalque = round(L_virtual_recalque, 2)


        #Perda de carga da sucção e recalque

        perda_carga_succao = ((10.646 * vazao_ajustada_cubic_meters ** 1.852) * L_virtual_succao) / (125 ** 1.852 * (diametro_succao / 1000) ** 4.87)

        perda_carga_recalque = ((10.646 * vazao_ajustada_cubic_meters ** 1.852) * L_virtual_recalque) / (125 ** 1.852 * (diametro_recalque / 1000) ** 4.87)

        altura_man_succao = float(campo_altura_succao.get()) + perda_carga_succao
        altura_man_recalque = float(campo_altura_recalque.get()) + perda_carga_recalque

        altura_man_total = altura_man_succao + altura_man_recalque
        altura_man_total = round(altura_man_total, 2)


        abre_resultados()

        apagar_campos()






def apagar_campos():
    campo_altura_recalque.delete(0, END)
    campo_altura_succao.delete(0, END)
    campo_comprimento_recalque.delete(0, END)
    campo_comprimento_succao.delete(0, END)
    campo_vazao.delete(0, END)
    campo_horas.delete(0, END)

    combo_crivo_s.current(0)
    combo_curva_45_s.current(0)
    combo_curva_90_s.current(0)
    combo_registro_gaveta_s.current(0)
    combo_registro_globo_s.current(0)

    combo_curva_45_r.current(0)
    combo_curva_90_r.current(0)
    combo_registro_gaveta_r.current(0)
    combo_registro_globo_r.current(0)
    combo_retencao_leve_r.current(0)
    combo_retencao_pesada_r.current(0)

def abre_resultados():
    tela_res = Tk()
    tela_res.title("Resultado")
    tela_res.geometry("400x300")
    tela_res.resizable(width=False, height=False)
    tela_res.configure(bg='#0e89c7')




    label_txt_hm = Label(tela_res,bg='#0e89c7', text="Vazão:", font=("Arial", 15))
    label_txt_hm.place(x=10, y=40)

    label_hm_total = Label(tela_res, bg='#0e89c7', text=altura_man_total, font=("Arial", 15),)
    label_hm_total.place(x=80, y=40)

    label_m_cubico = Label(tela_res, bg='#0e89c7', text="m³/h", font=("Arial", 14))
    label_m_cubico.place(x=140, y=42)

    label_alt_man = Label(tela_res, bg='#0e89c7', text="Altura manométrica:", font=("Arial", 15))
    label_alt_man.place(x=10, y=10)

    label_unidade_m = Label(tela_res, text="m", bg='#0e89c7', font=("Arial", 14))
    label_unidade_m.place(x=245, y=10)

    label_vazao_calculada = Label(tela_res, bg='#0e89c7', text=vazao_ajustada_cubic_hours, font=("Arial", 15))
    label_vazao_calculada.place(x=195, y=10)



    janela.winfo_screen()






label01 = Label(janela, text="Vazão em (L/s)", bg='#0e89c7', font=('Arial bold', 10))
label01.place(x=20, y=20)

campo_vazao = Entry(janela, width=5)
campo_vazao.place(x=35, y=45)

label02 = Label(janela, text="Tempo de funcionamento (h)", bg='#0e89c7', font=('Arial bold', 10))
label02.place(x=200, y=20)

campo_horas = Entry(janela, width=5)
campo_horas.place(x=265, y=45)

label03 = Label(janela, text="Altura de sucção (m)", bg='#0e89c7', font=('Arial bold', 10))
label03.place(x=450, y=20)

campo_altura_succao = Entry(janela, width=5)
campo_altura_succao.place(x=490, y=45)

label04 = Label(janela, text="Altura de recalque (m)", bg='#0e89c7', font=('Arial bold', 10))
label04.place(x=700, y=20)

campo_altura_recalque = Entry(janela, width=5)
campo_altura_recalque.place(x=750, y=45)

label11 = Label(janela, text="L da sucção (m)", bg='#0e89c7', font=('Arial bold', 10))
label11.place(x=20, y=90)

campo_comprimento_succao = Entry(janela, width=5)
campo_comprimento_succao.place(x=35, y=130)

label12 = Label(janela, text="L do recalque (m)", bg='#0e89c7', font=('Arial bold', 10))
label12.place(x=240, y=90)

campo_comprimento_recalque = Entry(janela, width=5)
campo_comprimento_recalque.place(x=265, y=130)

# Criação dos Combobox e labels

label05 = Label(janela, text="Curvas de 90°", bg='#0e89c7', font=('Arial bold', 10))
label05.place(x=10, y=225)

combo_curva_90_s = ttk.Combobox(janela, width=3, height=5)
combo_curva_90_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_curva_90_s.current(0)
combo_curva_90_s.place(x=30, y=250)

label06 = Label(janela, text="Curvas de 45°", bg='#0e89c7', font=('Arial bold', 10))
label06.place(x=150, y=225)

combo_curva_45_s = ttk.Combobox(janela, width=3, height=5)
combo_curva_45_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_curva_45_s.current(0)
combo_curva_45_s.place(x=170, y=250)

label07 = Label(janela, text="Registro de gaveta", bg='#0e89c7', font=('Arial bold', 10))
label07.place(x=10, y=310)

combo_registro_gaveta_s = ttk.Combobox(janela, width=3, height=5)
combo_registro_gaveta_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_registro_gaveta_s.current(0)
combo_registro_gaveta_s.place(x=30, y=340)

label08 = Label(janela, text="Registro de globo", bg='#0e89c7', font=('Arial bold', 10))
label08.place(x=150, y=310)

combo_registro_globo_s = ttk.Combobox(janela, width=3, height=5)
combo_registro_globo_s['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_registro_globo_s.current(0)
combo_registro_globo_s.place(x=170, y=340)

label09 = Label(janela, text="Válvula de pé e crivo", bg='#0e89c7', font=('Arial bold', 10))
label09.place(x=10, y=400)

combo_crivo_s = ttk.Combobox(janela, width=3, height=5)
combo_crivo_s['values'] = (0, 1)
combo_crivo_s.current(0)
combo_crivo_s.place(x=30, y=435)

# Título de Sucção e Recalque

label10 = Label(janela, text="SUCÇÃO", bg='#0e89c7', font=('Arial bold', 15))
label10.place(x=75, y=170)

label19 = Label(janela, text="RECALQUE", bg='#0e89c7', font=('Arial bold', 15))
label19.place(x=500, y=170)

label13 = Label(janela, text="Curvas de 90°", bg='#0e89c7', font=('Arial bold', 10))
label13.place(x=450, y=225)

combo_curva_90_r = ttk.Combobox(janela, width=3, height=5)
combo_curva_90_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_curva_90_r.current(0)
combo_curva_90_r.place(x=465, y=250)

label14 = Label(janela, text="Curvas de 45°", bg='#0e89c7', font=('Arial bold', 10))
label14.place(x=600, y=225)

combo_curva_45_r = ttk.Combobox(janela, width=3, height=5)
combo_curva_45_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_curva_45_r.current(0)
combo_curva_45_r.place(x=620, y=250)

label15 = Label(janela, text="Registro de gaveta", bg='#0e89c7', font=('Arial bold', 10))
label15.place(x=450, y=310)

combo_registro_gaveta_r = ttk.Combobox(janela, width=3, height=5)
combo_registro_gaveta_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_registro_gaveta_r.current(0)
combo_registro_gaveta_r.place(x=465, y=340)

label16 = Label(janela, text="Registro de globo", bg='#0e89c7', font=('Arial bold', 10))
label16.place(x=600, y=310)

combo_registro_globo_r = ttk.Combobox(janela, width=3, height=5)
combo_registro_globo_r['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo_registro_globo_r.current(0)
combo_registro_globo_r.place(x=620, y=340)

label17 = Label(janela, text="Retenção leve", bg='#0e89c7', font=('Arial bold', 10))
label17.place(x=450, y=400)

combo_retencao_leve_r = ttk.Combobox(janela, width=3, height=5)
combo_retencao_leve_r['values'] = (0, 1)
combo_retencao_leve_r.current(0)
combo_retencao_leve_r.place(x=465, y=435)

label18 = Label(janela, text="Retenção pesada", bg='#0e89c7', font=('Arial bold', 10))
label18.place(x=600, y=400)

combo_retencao_pesada_r = ttk.Combobox(janela, width=3, height=5)
combo_retencao_pesada_r['values'] = (0, 1)
combo_retencao_pesada_r.current(0)
combo_retencao_pesada_r.place(x=625, y=435)

btn_calculo = Button(janela, width=10, bd=4, height=3, bg='#e6ebe7', text="CALCULAR", command=calculo)
btn_calculo.place(x=800, y=400)


janela.mainloop()

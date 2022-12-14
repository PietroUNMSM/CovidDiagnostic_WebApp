
from flask import *
import requests
import json

from traitlets import Float, Integer

import matplotlib.pyplot as plt
from io import StringIO
# from StringIO import StringIO
# from StringIO import *

import io
import base64
from funcionesMembresia import *
from fuzzificacion import *
from funcionesMembresia import conclu_negativa, conclu_positivo, conclu_cuarentena
from baseReglas import regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13, regla14, regla15, regla16, regla17
from defuzzificacion import defuzzy

app = Flask(__name__, template_folder="templates", static_folder="templates", static_url_path='')
#app = Flask(__name__)
app.config["SECRET_KEY"] = ""

@app.route('/')
# def IniciarAPP():
def home():
    return render_template('index.html')


@app.route('/resultado', methods=['GET','POST'])
def ObteniendoInputs():
    #apilando en una lista las entradas
    inputs_usuario = []
    
    inputs_usuario.append(int(request.form.get("age")))
    inputs_usuario.append((request.form.get("fiebre")))
    inputs_usuario.append((request.form.get("diabetes")))
    inputs_usuario.append((request.form.get("nameHist")))
    inputs_usuario.append((request.form.get("nameGarganta")))
    inputs_usuario.append((request.form.get("nameTos")))
    inputs_usuario.append((request.form.get("namePerdida")))
    inputs_usuario.append((request.form.get("nameRespira")))
    inputs_usuario.append(request.form.get("namePecho"))


    #salida en template de resultado.html
    inputEdad = inputs_usuario[0]
    inputFiebre = inputs_usuario[1]
    inputDiabetes = inputs_usuario[2]
    inputHist = inputs_usuario[3]
    inputGarganta = inputs_usuario[4]
    inputTos = inputs_usuario[5]
    inputPerdida = inputs_usuario[6]
    inputRespira = inputs_usuario[7]
    inputPecho = inputs_usuario[8]

    #lista de membresia de las entradas
    # memb_fiebre_lo, memb_fiebre_md, memb_fiebre_hi, memb_edad_men40, memb_edad_40_50, memb_edad_ma50, memb_diabetes_low, memb_diabetes_md, memb_diabetes_hi, memb_histViaje_low, memb_histViaje_md, memb_histViaje_hi, memb_garganta_low, memb_garganta_md, memb_garganta_hi,memb_tos_low, memb_tos_md, memb_tos_hi, memb_olfatoGusto_low, memb_olfatoGusto_md, memb_olfatoGusto_hi, memb_respira_low, memb_respira_md, memb_respira_hi, memb_pecho_low, memb_pecho_md, memb_pecho_hi = memb_fuzzy()

    membresia_inputs = []
    membresia_inputs.append(memb_fuzzy(inputFiebre, inputEdad, inputDiabetes, inputHist, inputGarganta, inputTos, inputPerdida, inputRespira, inputPecho))

    memb_Fiebre_lo = membresia_inputs[0][0]
    memb_fiebre_md = membresia_inputs[0][1]
    memb_fiebre_hi = membresia_inputs[0][2]
    
    memb_edad_men40 = membresia_inputs[0][3]
    memb_edad_40_50 = membresia_inputs[0][4]
    memb_edad_ma50 = membresia_inputs[0][5]
    
    memb_diabetes_low = membresia_inputs[0][6]
    memb_diabetes_md = membresia_inputs[0][7]
    memb_diabetes_hi = membresia_inputs[0][8]
    
    memb_histViaje_low = membresia_inputs[0][9]
    memb_histViaje_md = membresia_inputs[0][10]
    memb_histViaje_hi = membresia_inputs[0][11]
    
    memb_garganta_low = membresia_inputs[0][12]
    memb_garganta_md = membresia_inputs[0][13]
    memb_garganta_hi = membresia_inputs[0][14]
    
    memb_tos_low = membresia_inputs[0][15]
    memb_tos_md = membresia_inputs[0][16]
    memb_tos_hi = membresia_inputs[0][17]
    
    memb_olfatoGusto_low = membresia_inputs[0][18]
    memb_olfatoGusto_md = membresia_inputs[0][19]
    memb_olfatoGusto_hi = membresia_inputs[0][20]
    
    memb_respira_low = membresia_inputs[0][21]
    memb_respira_md = membresia_inputs[0][22]
    memb_respira_hi = membresia_inputs[0][23]
    
    memb_pecho_low = membresia_inputs[0][24]
    memb_pecho_md = membresia_inputs[0][25]
    memb_pecho_hi = membresia_inputs[0][26]

    #Funciones de la base de reglas
    #reglas 1 al 17
    conclu_activation_neg1 = regla1(memb_Fiebre_lo, memb_edad_men40, conclu_negativa)
    conclu_activation_cua1 = regla2(memb_fiebre_md, memb_edad_ma50, conclu_cuarentena)
    conclu_activation_cua2 = regla3(memb_fiebre_hi, memb_edad_ma50, memb_histViaje_md, conclu_cuarentena)
    conclu_activation_posi1 = regla4(memb_fiebre_hi, memb_edad_ma50, memb_histViaje_hi, conclu_positivo)
    conclu_activation_cua3 = regla5(memb_garganta_low, memb_edad_men40, memb_histViaje_md, conclu_cuarentena)
    conclu_activation_cua4 = regla6(memb_garganta_hi, memb_edad_40_50, memb_edad_ma50, memb_tos_md, conclu_cuarentena)
    conclu_activation_neg2 = regla7(memb_respira_low, memb_edad_40_50, memb_edad_ma50, memb_tos_md, conclu_negativa)
    conclu_activation_posi2 = regla8(memb_respira_hi, memb_edad_40_50, memb_edad_ma50, memb_tos_hi, conclu_positivo)
    conclu_activation_neg3 = regla9(memb_respira_low, memb_edad_40_50, memb_edad_ma50, conclu_negativa)
    conclu_activation_posi3 = regla10(memb_edad_men40, memb_histViaje_hi, memb_respira_hi, conclu_positivo)
    conclu_activation_posi4 = regla11(memb_edad_ma50, memb_histViaje_hi, memb_respira_hi, conclu_positivo)
    conclu_activation_posi5 = regla12(memb_edad_40_50, memb_edad_ma50, memb_histViaje_hi, memb_tos_hi, memb_respira_hi, conclu_positivo)
    conclu_activation_posi6 =  regla13(memb_edad_40_50, memb_edad_ma50, memb_diabetes_hi, memb_histViaje_md, memb_tos_md, memb_respira_hi, conclu_positivo)
    conclu_activation_posi7 = regla14(memb_edad_40_50, memb_edad_ma50, memb_diabetes_hi, memb_histViaje_md, conclu_cuarentena)
    conclu_activation_posi8 = regla15(memb_olfatoGusto_hi, memb_pecho_hi, conclu_positivo)
    conclu_activation_posi9 = regla16(memb_histViaje_md, memb_garganta_hi, memb_tos_hi, memb_pecho_hi, conclu_positivo)
    conclu_activation_neg4 = regla17(memb_edad_men40, memb_histViaje_low, memb_garganta_low, conclu_negativa)

    #Defuzzificacion
    concluX, concluY, casoNega, casoCuarent, casoPosi = defuzzy(conclu_activation_neg1, conclu_activation_cua1, conclu_activation_cua2, conclu_activation_posi1, conclu_activation_cua3, conclu_activation_cua4, conclu_activation_neg2, conclu_activation_posi2, conclu_activation_neg3, conclu_activation_posi3, conclu_activation_posi4, conclu_activation_posi5, conclu_activation_posi6, conclu_activation_posi7, conclu_activation_posi8, conclu_activation_posi9, conclu_activation_neg4)

    return render_template('resultado.html', inEdad=inputEdad, inFiebre=inputFiebre, 
        inDiabetes=inputDiabetes, inHist=inputHist, inGarganta=inputGarganta, inTos=inputTos,
        inPerdida=inputPerdida, inRespira=inputRespira, inPecho=inputPecho, 
        memb_Fiebre_lo=memb_Fiebre_lo, memb_fiebre_md=memb_fiebre_md, memb_fiebre_hi=memb_fiebre_hi,
        memb_edad_men40=memb_edad_men40, memb_edad_40_50=memb_edad_40_50, memb_edad_ma50=memb_edad_ma50, 
        memb_diabetes_low=memb_diabetes_low, memb_diabetes_md=memb_diabetes_md, memb_diabetes_hi=memb_diabetes_hi, 
        memb_histViaje_low=memb_histViaje_low, memb_histViaje_md=memb_histViaje_md, memb_histViaje_hi=memb_histViaje_hi,
        memb_garganta_low=memb_garganta_low, memb_garganta_md=memb_garganta_md, memb_garganta_hi=memb_garganta_hi,
        memb_tos_low=memb_tos_low, memb_tos_md=memb_tos_md, memb_tos_hi=memb_tos_hi,
        memb_olfatoGusto_low=memb_olfatoGusto_low, memb_olfatoGusto_md=memb_olfatoGusto_md, memb_olfatoGusto_hi=memb_olfatoGusto_hi,
        memb_respira_low=memb_respira_low, memb_respira_md=memb_respira_md, memb_respira_hi=memb_respira_hi,
        memb_pecho_low=memb_pecho_low, memb_pecho_md=memb_pecho_md, memb_pecho_hi=memb_pecho_hi,
        conclu_activation_neg1 = conclu_activation_neg1,  conclu_activation_cua1=conclu_activation_cua1, conclu_activation_cua2=conclu_activation_cua2,
        conclu_activation_posi1=conclu_activation_posi1, conclu_activation_cua3=conclu_activation_cua3, conclu_activation_cua4=conclu_activation_cua4,
        conclu_activation_neg2=conclu_activation_neg2, conclu_activation_posi2=conclu_activation_posi2, conclu_activation_neg3=conclu_activation_neg3,
        conclu_activation_posi3=conclu_activation_posi3, conclu_activation_posi4=conclu_activation_posi4, conclu_activation_posi5=conclu_activation_posi5, 
        conclu_activation_posi6=conclu_activation_posi6, conclu_activation_posi7=conclu_activation_posi7, conclu_activation_posi8=conclu_activation_posi8, 
        conclu_activation_posi9=conclu_activation_posi9, conclu_activation_neg4=conclu_activation_neg4,
        concluX=concluX, concluY=concluY, casoNega=casoNega, casoCuarent=casoCuarent, casoPosi=casoPosi)




def diagnostico():
    if request.method == 'POST':
        return render_template('resultado.html') #, shortcode=request.form['shortcode'])

if __name__ == '__main__':
    app.run(debug=True)
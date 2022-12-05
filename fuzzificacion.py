import skfuzzy as fuzz
from funcionesMembresia import *

#Rangos de valores
# vFiebre [36.67, 40]
# vEdad [10, 70]
# vDiabetes [140, 215]
# vHistviaje [0, 1]
# vGarganta [0, 1]
# vTos [0, 1]
# vOlfSabor [0, 1]
# vRespira [0, 1]
# vPecho [0,10]

#valores de prueba V1 --> negativo 0.0 || cuarentena 0.72 || positivo 0.03
# vFiebre = 39
# vEdad = 55
# vDiabetes = 150
# vHistviaje = 0.2
# vGarganta = 0.48
# vTos = 0.3
# vOlfSabor = 0.2
# vRespira = 0.4
# vPecho = 5.2


# valores de prueba V2 --> negativo 0.0 || cuarentena 0.2 || positivo 0.46
# vFiebre = 40
# vEdad = 78
# vDiabetes = 210
# vHistviaje = 0.89
# vGarganta = 0.9
# vTos = 0.87
# vOlfSabor = 0.9
# vRespira = 0.78
# vPecho = 9


#valores de prueba V5 --> negativo 0.64 || cuarentena 0.11 || positivo 0.0
vFiebre = 37
vEdad = 15
vDiabetes = 142
vHistviaje = 0
vGarganta = 0.3
vTos = 0.1
vOlfSabor = 0
vRespira = 0.2
vPecho = 0

# Con esto añadimos las funciones anteriores al dominio de cada variable de entrada
#Fuzzificaccion --> Dar un valor puntual a un conjunto difuso 

#Funcion de fuzzificacion
def fuzzyVar(rango, fiebre_tipo, val_input):
    return fuzz.interp_membership(rango, fiebre_tipo, val_input)


def memb_fuzzy(vFiebre, vEdad, vDiabetes, vHistviaje, vGarganta, vTos, vOlfSabor, vRespira, vPecho):
    #FIEBRE
    memb_fiebre_lo = fuzzyVar(x_fiebre, fiebre_low, vFiebre)
    memb_fiebre_md = fuzzyVar(x_fiebre, fiebre_medium, vFiebre)
    memb_fiebre_hi = fuzzyVar(x_fiebre, fiebre_high, vFiebre)

    # print('Pertenencia de fiebre baja: ',memb_fiebre_lo)
    # print('Pertenencia de fiebre media: ', memb_fiebre_md)
    # print('Pertenencia de fiebre alta: ',memb_fiebre_hi)


    #EDAD
    memb_edad_men40 = fuzzyVar(x_edad, edad_menos40, vEdad)
    memb_edad_40_50 = fuzzyVar(x_edad, edad_40_50, vEdad)
    memb_edad_ma50 = fuzzyVar(x_edad, edad_mas50, vEdad)

    # print('Pertenencia de fedad menor a 40: ',memb_edad_men40)
    # print('Pertenencia de edad entre 40 y 50: ', memb_edad_40_50)
    # print('Pertenencia de edad mayor a 50: ',memb_edad_ma50)


    #DIABETES
    memb_diabetes_low = fuzzyVar(x_diabetes, diabetes_low, vDiabetes)
    memb_diabetes_md = fuzzyVar(x_diabetes, diabetes_medium, vDiabetes)
    memb_diabetes_hi = fuzzyVar(x_diabetes, diabetes_high, vDiabetes)

    # print('Pertenencia de diabetes bajo: ',memb_diabetes_low)
    # print('Pertenencia de diabetes medio: ', memb_diabetes_md)
    # print('Pertenencia de diabetes alto: ',memb_diabetes_hi)


    #Historial Viajes
    memb_histViaje_low = fuzzyVar(x_histviaje, hist_no_infect, vHistviaje)
    memb_histViaje_md = fuzzyVar(x_histviaje, hist_moderado, vHistviaje)
    memb_histViaje_hi = fuzzyVar(x_histviaje, hist_infect, vHistviaje)

    # print('Pertenencia de viajero no infectado: ',memb_histViaje_low)
    # print('Pertenencia de viajero moderado: ', memb_histViaje_md)
    # print('Pertenencia de viajero infectado: ',memb_histViaje_hi)


    #Dolor garganta
    memb_garganta_low = fuzzyVar(x_garganta, garganta_low, vGarganta)
    memb_garganta_md = fuzzyVar(x_garganta, garganta_medium, vGarganta)
    memb_garganta_hi = fuzzyVar(x_garganta, garganta_high, vGarganta)

    # print('Pertenencia de dolor bajo de garganta: ',memb_garganta_low)
    # print('Pertenencia de dolor medio de garganta: ', memb_garganta_md)
    # print('Pertenencia de dolor alto de garganta: ',memb_garganta_hi)


    #Tos
    memb_tos_low = fuzzyVar(x_tos, tos_low, vTos)
    memb_tos_md = fuzzyVar(x_tos, tos_medium, vTos)
    memb_tos_hi = fuzzyVar(x_tos, tos_high, vTos)

    # print('Pertenencia de tos bajo: ',memb_tos_low)
    # print('Pertenencia de tos medio: ', memb_tos_md)
    # print('Pertenencia de tos alto: ',memb_tos_hi)


    #Perdida de gusto y olfato
    memb_olfatoGusto_low = fuzzyVar(x_olfato_sabor, olfato_gusto_low, vOlfSabor)
    memb_olfatoGusto_md = fuzzyVar(x_olfato_sabor, olfato_gusto_medium, vOlfSabor)
    memb_olfatoGusto_hi = fuzzyVar(x_olfato_sabor, olfato_gusto_high, vOlfSabor)

    # print('Pertenencia de perdida de olfato y gusto bajo: ',memb_olfatoGusto_low)
    # print('Pertenencia de perdida de olfato y gusto medio: ', memb_olfatoGusto_md)
    # print('Pertenencia de perdida de olfato y gusto alto: ',memb_olfatoGusto_hi)


    #Problema respiratorio
    memb_respira_low = fuzzyVar(x_respira, respira_low, vRespira)
    memb_respira_md = fuzzyVar(x_respira, respira_medium, vRespira)
    memb_respira_hi = fuzzyVar(x_respira, respira_high, vRespira)

    # print('Pertenencia de problema respiratorio bajo: ',memb_respira_low)
    # print('Pertenencia de problema respiratorio medio: ', memb_respira_md)
    # print('Pertenencia de problema respiratorio alto: ',memb_respira_hi)


    #Dolor en el pecho
    memb_pecho_low = fuzzyVar(x_precho, pecho_low, vPecho)
    memb_pecho_md = fuzzyVar(x_precho, pecho_medium, vPecho)
    memb_pecho_hi = fuzzyVar(x_precho, pecho_high, vPecho)

    # print('Pertenencia de dolor en el pecho bajo: ',memb_pecho_low)
    # print('Pertenencia de dolor en el pecho medio: ', memb_pecho_md)
    # print('Pertenencia de dolor en el pecho alto: ',memb_pecho_hi)

    return (memb_fiebre_lo, memb_fiebre_md, memb_fiebre_hi, memb_edad_men40, memb_edad_40_50, memb_edad_ma50,
        memb_diabetes_low, memb_diabetes_md, memb_diabetes_hi, memb_histViaje_low, memb_histViaje_md, memb_histViaje_hi,
        memb_garganta_low, memb_garganta_md, memb_garganta_hi,memb_tos_low, memb_tos_md, memb_tos_hi, 
        memb_olfatoGusto_low, memb_olfatoGusto_md, memb_olfatoGusto_hi, memb_respira_low, memb_respira_md, memb_respira_hi,
        memb_pecho_low, memb_pecho_md, memb_pecho_hi)
    

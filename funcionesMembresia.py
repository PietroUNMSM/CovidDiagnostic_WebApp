# import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

from rangosVar import *

# valor de fiebre
# membership function 1 (low) 
fiebre_low = fuzz.trimf(x_fiebre, [35.3, 36.7, 38])


# membership function 2 (medium)
fiebre_medium = fuzz.trimf(x_fiebre, [37, 38.3, 39.67])

# membership function 3 (high)
fiebre_high = fuzz.trimf(x_fiebre, [38.67, 40, 41.3])

def plotFiebre():
    plt.figure(figsize=(8,5))
    plotFiebre= plt.plot(x_fiebre, fiebre_low, color='b', label='Low')
    plotFiebre = plt.plot(x_fiebre, fiebre_medium, color='g', label ='Medium')
    plotFiebre = plt.plot(x_fiebre, fiebre_high, color='r', label ='High')
    plotFiebre = plt.title('Funciones de Membresía de Fiebre')
    plotFiebre = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.axis([36.7,40,0,1])
    plotFiebre.figure.savefig('templates/Imagenes/FuncionesMembresia/plotFiebre.png', bbox_inches='tight',dpi=100)

plotFiebre()

# valor de edad
# membership function 1 (<40) 
edad_menos40 = fuzz.trimf(x_edad, [-14, 10, 34])

# membership function 2 (40_50)
edad_40_50 = fuzz.trimf(x_edad, [16, 40, 64])

# membership function 3 (>50)
edad_mas50 = fuzz.trimf(x_edad, [46, 70, 94])

def plotEdad():
    plt.figure(figsize=(10,6))
    plotEdad = plt.plot(x_edad, edad_menos40, color='b', label='Edad <40')
    plotEdad = plt.plot(x_edad, edad_40_50, color='g', label ='Edad 40 y <=50')
    plotEdad = plt.plot(x_edad, edad_mas50, color='r', label ='Edad>50')
    plotEdad = plt.title('Funciones de Membresía de Edad')
    plotEdad = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.axis([10,70,0,1])
    # plotEdad
    plotEdad.figure.savefig('templates/Imagenes/FuncionesMembresia/plotEdad.png', bbox_inches='tight',dpi=100)

plotEdad()

# valor de diabetes
# membership function 1 (low) 
diabetes_low = fuzz.trimf(x_diabetes, [110, 140, 170])


# membership function 2 (medium)
diabetes_medium = fuzz.trimf(x_diabetes, [147.5, 177.5, 207.5])

# membership function 3 (high)
diabetes_high = fuzz.trimf(x_diabetes, [185, 215, 245])

def plotDiabetes():
    plt.figure(figsize=(10,6))
    plotDiabetes = plt.plot(x_diabetes, diabetes_low, color='b', label='Low')
    plotDiabetes = plt.plot(x_diabetes, diabetes_medium, color='g', label ='Medium')
    plotDiabetes = plt.plot(x_diabetes, diabetes_high, color='r', label ='High')
    plotDiabetes = plt.title('Funciones de Membresía de Diabetes')
    plotDiabetes = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotDiabetes
    plotDiabetes.figure.savefig('templates/Imagenes/FuncionesMembresia/plotDiabetes.png', bbox_inches='tight',dpi=100)

plotDiabetes()

# valor de historial de viajes
# membership function 1 (no_infectado) 
hist_no_infect = fuzz.trimf(x_histviaje, [-0.4, 0, 0.4])

# membership function 2 (moderado)
hist_moderado = fuzz.trimf(x_histviaje, [0.1, 0.5, 0.9])

# membership function 3 (infectado)
hist_infect = fuzz.trimf(x_histviaje, [0.6, 1, 1.4])

def plotHistViajes():
    plt.figure(figsize=(10,6))
    plotHistV = plt.plot(x_histviaje, hist_no_infect, color='b', label='No infectado')
    plotHistV = plt.plot(x_histviaje, hist_moderado, color='g', label ='Duda de infección')
    plotHistV = plt.plot(x_histviaje, hist_infect, color='r', label ='Infectado')
    plotHistV = plt.title('Funciones de Membresía de Historial de Viajes')
    plotHistV = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotHistV
    plotHistV.figure.savefig('templates/Imagenes/FuncionesMembresia/plotHistV.png', bbox_inches='tight',dpi=100)
    
plotHistViajes()

# valor de dolor de garganta
# membership function 1 (low) 
garganta_low = fuzz.trimf(x_garganta, [-0.4, 0, 0.4])

# membership function 2 (medium)
garganta_medium = fuzz.trimf(x_garganta, [0.1, 0.5, 0.9])

# membership function 3 (high)
garganta_high = fuzz.trimf(x_garganta, [0.6, 1, 1.4])

def plotGarganta():
    plt.figure(figsize=(10,6))
    plotGarganta = plt.plot(x_garganta, garganta_low, color='b', label='Low')
    plotGarganta = plt.plot(x_garganta, garganta_medium, color='g', label ='Medium')
    plotGarganta = plt.plot(x_garganta, garganta_high, color='r', label ='High')
    plotGarganta = plt.title('Funciones de Membresía de Dolor de Garganta')
    plotGarganta = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotGarganta
    plotGarganta.figure.savefig('templates/Imagenes/FuncionesMembresia/plotGarganta.png', bbox_inches='tight',dpi=100)
    
plotGarganta()

# valor de tos
# membership function 1 (low) 
tos_low = fuzz.trimf(x_tos, [-0.4, 0, 0.4])

# membership function 2 (medium)
tos_medium = fuzz.trimf(x_tos, [0.1, 0.5, 0.9])

# membership function 3 (high)
tos_high = fuzz.trimf(x_tos, [0.6, 1, 1.4])

def plotTos():
    plt.figure(figsize=(10,6))
    plotTos = plt.plot(x_tos, tos_low, color='b', label='Low')
    plotTos = plt.plot(x_tos, tos_medium, color='g', label ='Medium')
    plotTos = plt.plot(x_tos, tos_high, color='r', label ='High')
    plotTos = plt.title('Funciones de Membresía de Tos')
    plotTos = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotTos
    plotTos.figure.savefig('templates/Imagenes/FuncionesMembresia/plotTos.png', bbox_inches='tight',dpi=100)

plotTos()

# valor de perdida de olfato y gusto
# membership function 1 (low) 
olfato_gusto_low = fuzz.trimf(x_olfato_sabor, [-0.4, 0, 0.4])

# membership function 2 (medium)
olfato_gusto_medium = fuzz.trimf(x_olfato_sabor, [0.1, 0.5, 0.9])

# membership function 3 (high)
olfato_gusto_high = fuzz.trimf(x_olfato_sabor, [0.6, 1, 1.4])

def plotOlfatoGusto():
    plt.figure(figsize=(10,6))
    plotPerdida = plt.plot(x_olfato_sabor, olfato_gusto_low, color='b', label='Low')
    plotPerdida = plt.plot(x_olfato_sabor, olfato_gusto_medium, color='g', label ='Medium')
    plotPerdida = plt.plot(x_olfato_sabor, olfato_gusto_high, color='r', label ='High')
    plotPerdida = plt.title('Funciones de Membresía de Pérdida de Olfato y Gusto')
    plotPerdida = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotPerdida
    plotPerdida.figure.savefig('templates/Imagenes/FuncionesMembresia/plotPerdida.png', bbox_inches='tight',dpi=100)

plotOlfatoGusto()

# valor de problema de respiracion
# membership function 1 (low) 
respira_low = fuzz.trimf(x_respira, [-0.4, 0, 0.4])

# membership function 2 (medium)
respira_medium = fuzz.trimf(x_respira, [0.1, 0.5, 0.9])

# membership function 3 (high)
respira_high = fuzz.trimf(x_respira, [0.6, 1, 1.4])

def plotRespira():
    plt.figure(figsize=(10,6))
    plotRespira = plt.plot(x_respira, respira_low, color='b', label='Low')
    plotRespira = plt.plot(x_respira, respira_medium, color='g', label ='Medium')
    plotRespira = plt.plot(x_respira, respira_high, color='r', label ='High')
    plotRespira = plt.title('Funciones de Membresía de Problema Respiratorio')
    plotRespira = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotRespira
    plotRespira.figure.savefig('templates/Imagenes/FuncionesMembresia/plotRespira.png', bbox_inches='tight',dpi=100)

plotRespira()

# membership function 1 (low) 
pecho_low = fuzz.trimf(x_precho, [-4, 0, 4])


# membership function 2 (medium)
pecho_medium = fuzz.trimf(x_precho, [1, 5, 9])

# membership function 3 (high)
pecho_high = fuzz.trimf(x_precho, [6, 10, 14])

def plotPecho():
    plt.figure(figsize=(10,6))
    plotPecho = plt.plot(x_precho, pecho_low, color='b', label='Low')
    plotPecho = plt.plot(x_precho, pecho_medium, color='g', label ='Medium')
    plotPecho = plt.plot(x_precho, pecho_high, color='r', label ='High')
    plotPecho = plt.title('Funciones de Membresía de Dolor del Pecho')
    plotPecho = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotPecho
    plotPecho.figure.savefig('templates/Imagenes/FuncionesMembresia/plotPecho.png', bbox_inches='tight',dpi=100)

plotPecho()

# conclusion
# membership function 1 (negativo) 
conclu_negativa = fuzz.trimf(x_conclusion, [-0.4, 0, 0.4])


# membership function 2 (cuarentena)
conclu_cuarentena = fuzz.trimf(x_conclusion, [0.1, 0.5, 0.9])

# membership function 3 (positivo)
conclu_positivo = fuzz.trimf(x_conclusion, [0.6, 1.0, 1.4])

def plotConclusion():
    plt.figure(figsize=(10,6))
    plotConclu = plt.plot(x_conclusion, conclu_negativa, color='b', label='Negativo')
    plotConclu = plt.plot(x_conclusion, conclu_cuarentena, color='g', label ='Cuarentena')
    plotConclu = plt.plot(x_conclusion, conclu_positivo, color='r', label ='Positivo')
    plotConclu = plt.title('Funciones de Membresía de Conclusion')
    plotConclu = plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.axis([10,70,0,1])
    # plotConclu
    plotConclu.figure.savefig('templates/Imagenes/FuncionesMembresia/plotConclu.png', bbox_inches='tight',dpi=100)

plotConclusion()
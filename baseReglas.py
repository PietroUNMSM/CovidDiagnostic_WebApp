from fuzzificacion import *

# memb_fiebre_lo, memb_fiebre_md, memb_fiebre_hi, memb_edad_men40, memb_edad_40_50, memb_edad_ma50, memb_diabetes_low, memb_diabetes_md, memb_diabetes_hi, memb_histViaje_low, memb_histViaje_md, memb_histViaje_hi, memb_garganta_low, memb_garganta_md, memb_garganta_hi,memb_tos_low, memb_tos_md, memb_tos_hi, memb_olfatoGusto_low, memb_olfatoGusto_md, memb_olfatoGusto_hi, memb_respira_low, memb_respira_md, memb_respira_hi, memb_pecho_low, memb_pecho_md, memb_pecho_hi = memb_fuzzy()



# Regla 1
def regla1(memb_fiebre_lo, memb_edad_men40, conclu_negativa):
    active_rule1 = np.fmin(memb_fiebre_lo, memb_edad_men40)
    # Clipping en la regla 1
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_neg1 = np.fmin(active_rule1, conclu_negativa) # removed entirely to 0

    #def plotRegla1():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_neg1)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla1.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_neg1

# regla1()

# regla1 = plotRegla1()
# regla1

# Regla 2
def regla2(memb_fiebre_md, memb_edad_ma50, conclu_cuarentena):
    active_rule2 = np.fmin(memb_fiebre_md, memb_edad_ma50)

    # Clipping en la regla 2
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_cua1 = np.fmin(active_rule2, conclu_cuarentena) # removed entirely to 0

    # def plotRegla2():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_cua1)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla2.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_cua1

# regla2()

# Regla 3
def regla3(memb_fiebre_hi, memb_edad_ma50, memb_histViaje_md, conclu_cuarentena):
    # active_rule3 = np.fmin(memb_fiebre_hi, np.fmin(memb_edad_ma50,memb_histViaje_low))
    active_rule3 = np.fmin(memb_fiebre_hi, np.fmin(memb_edad_ma50,memb_histViaje_md))

    # Clipping en la regla 3
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_cua2 = np.fmin(active_rule3, conclu_cuarentena) # removed entirely to 0

    # def plotRegla3():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion, conclu_activation_cua2)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla3.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_cua2

# regla3()   


# Regla 4
def regla4(memb_fiebre_hi, memb_edad_ma50, memb_histViaje_hi, conclu_positivo):
    active_rule4 = np.fmin(memb_fiebre_hi, np.fmin(memb_edad_ma50, memb_histViaje_hi))

    # Clipping en la regla 4
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi1 = np.fmin(active_rule4, conclu_positivo) # removed entirely to 0

    # def plotRegla4():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion, conclu_activation_posi1)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla4.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi1


# Regla 5
def regla5(memb_garganta_low, memb_edad_men40, memb_histViaje_md, conclu_cuarentena):
    # active_rule5 = np.fmin(memb_garganta_low, np.fmin(memb_edad_men40, memb_histViaje_low))
    active_rule5 = np.fmin(memb_garganta_low, np.fmin(memb_edad_men40, memb_histViaje_md))

    # Clipping en la regla 5
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_cua3 = np.fmin(active_rule5, conclu_cuarentena) # removed entirely to 0

    # def plotRegla5():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_cua3)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla5.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_cua3


# Regla 6
def regla6(memb_garganta_hi, memb_edad_40_50, memb_edad_ma50, memb_tos_md, conclu_cuarentena):
    active_rule6 = np.fmin(memb_garganta_hi, np.fmin(
        np.fmax(memb_edad_40_50, memb_edad_ma50), memb_tos_md))

    # Clipping en la regla 6
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_cua4 = np.fmin(active_rule6, conclu_cuarentena) # removed entirely to 0

    # def plotRegla6():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_cua4)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla6.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_cua4


# Regla 7
def regla7(memb_respira_low, memb_edad_40_50, memb_edad_ma50, memb_tos_md, conclu_negativa):
    active_rule7 = np.fmin(memb_respira_low, np.fmin(
        np.fmax(memb_edad_40_50, memb_edad_ma50), memb_tos_md))

    # Clipping en la regla 7
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_neg2 = np.fmin(active_rule7, conclu_negativa) # removed entirely to 0

    # def plotRegla7():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_neg2)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla7.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_neg2


# Regla 8
def regla8(memb_respira_hi, memb_edad_40_50, memb_edad_ma50, memb_tos_hi, conclu_positivo):
    active_rule8 = np.fmin(memb_respira_hi, np.fmin(
        np.fmax(memb_edad_40_50, memb_edad_ma50), memb_tos_hi))

    # Clipping en la regla 8
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi2 = np.fmin(active_rule8, conclu_positivo) # removed entirely to 0

    # def plotRegla8():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi2)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla8.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi2


# Regla 9
def regla9(memb_respira_low, memb_edad_40_50, memb_edad_ma50, conclu_negativa):
    active_rule9 = np.fmin(memb_respira_low, np.fmax(memb_edad_40_50, memb_edad_ma50))

    # Clipping en la regla 9
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_neg3 = np.fmin(active_rule9, conclu_negativa) # removed entirely to 0

    # def plotRegla9():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_neg3)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla9.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_neg3



# Regla 10
def regla10(memb_edad_men40, memb_histViaje_hi, memb_respira_hi, conclu_positivo):
    active_rule10 = np.fmin(memb_edad_men40, np.fmin(memb_histViaje_hi, memb_respira_hi))

    # Clipping en la regla 10
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi3 = np.fmin(active_rule10, conclu_positivo) # removed entirely to 0

    # def plotRegla10():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi3)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla10.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi3


# Regla 11
def regla11(memb_edad_ma50, memb_histViaje_hi, memb_respira_hi, conclu_positivo):
    active_rule11 = np.fmin(memb_edad_ma50, np.fmin(memb_histViaje_hi, memb_respira_hi))

    # Clipping en la regla 11
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi4 = np.fmin(active_rule11, conclu_positivo) # removed entirely to 0

    # def plotRegla11():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi4)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla11.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi4


# Regla 12
def regla12(memb_edad_40_50, memb_edad_ma50, memb_histViaje_hi, memb_tos_hi, memb_respira_hi, conclu_positivo):
    active_rule12 = np.fmin(np.fmax(memb_edad_40_50, memb_edad_ma50), 
                            np.fmin(memb_histViaje_hi, np.fmin(memb_tos_hi, memb_respira_hi)))

    # Clipping en la regla 12
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi5 = np.fmin(active_rule12, conclu_positivo) # removed entirely to 0

    # def plotRegla12():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi5)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla12.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi5



# Regla 13
# active_rule13 = np.fmax(np.fmax(memb_edad_40_50, memb_edad_ma50),
#                         np.fmax(memb_diabetes_hi, np.fmax(memb_histViaje_low,
#                                                           np.fmax(memb_tos_md, memb_respira_hi))))
def regla13(memb_edad_40_50, memb_edad_ma50, memb_diabetes_hi, memb_histViaje_md, memb_tos_md, memb_respira_hi, conclu_positivo):
    active_rule13 = np.fmax(np.fmax(memb_edad_40_50, memb_edad_ma50),
                            np.fmax(memb_diabetes_hi, np.fmax(memb_histViaje_md,
                                                            np.fmax(memb_tos_md, memb_respira_hi))))

    # Clipping en la regla 13
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi6 = np.fmin(active_rule13, conclu_positivo) # removed entirely to 0

    # def plotRegla13():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi6)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla13.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi6


# Regla 14
# active_rule14 = np.fmin(np.fmax(memb_edad_40_50, memb_edad_ma50),
#                         np.fmin(memb_diabetes_hi, memb_histViaje_low))

def regla14(memb_edad_40_50, memb_edad_ma50, memb_diabetes_hi, memb_histViaje_md, conclu_cuarentena):
    active_rule14 = np.fmin(np.fmax(memb_edad_40_50, memb_edad_ma50),
                            np.fmin(memb_diabetes_hi, memb_histViaje_md))

    # Clipping en la regla 14
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi7 = np.fmin(active_rule14, conclu_cuarentena) # removed entirely to 0

    # def plotRegla14():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi7)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla14.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi7


# Regla 15
def regla15(memb_olfatoGusto_hi, memb_pecho_hi, conclu_positivo):
    active_rule15 = np.fmin(memb_olfatoGusto_hi, memb_pecho_hi)

    # Clipping en la regla 15
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi8 = np.fmin(active_rule15, conclu_positivo) # removed entirely to 0

    # def plotRegla15():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi8)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla15.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi8


# Regla 16
# active_rule16 = np.fmin(memb_histViaje_low, np.fmin(memb_garganta_hi,
#                                                     np.fmin(memb_tos_hi, memb_pecho_hi)))
def regla16(memb_histViaje_md, memb_garganta_hi, memb_tos_hi, memb_pecho_hi, conclu_positivo):
    active_rule16 = np.fmin(memb_histViaje_md, np.fmin(memb_garganta_hi,
                                                        np.fmin(memb_tos_hi, memb_pecho_hi)))

    # Clipping en la regla 16
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_posi9 = np.fmin(active_rule16, conclu_positivo) # removed entirely to 0

    # def plotRegla16():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_posi9)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla16.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_posi9


# Regla 17
def regla17(memb_edad_men40, memb_histViaje_low, memb_garganta_low, conclu_negativa):
    active_rule17 = np.fmin(memb_edad_men40, np.fmin(memb_histViaje_low, memb_garganta_low))

    # Clipping en la regla 17
    #Para unir antecedente y consecuente se usa np.fmin
    conclu_activation_neg4 = np.fmin(active_rule17, conclu_negativa) # removed entirely to 0

    # def plotRegla17():
    plt.style.use('default')
    fig=plt.figure(figsize=(6,2))
    plt.plot(x_conclusion,conclu_activation_neg4)
    # plt.axis([5,25,0,1])
    # plt.show()
    plt.savefig('templates/Imagenes/RuleBase/plotRegla17.png', bbox_inches='tight',dpi=100)
    plt.close()
    return conclu_activation_neg4



##################################################
##ORIGINAL
#########################

# from fuzzificacion import *

# memb_fiebre_lo, memb_fiebre_md, memb_fiebre_hi, memb_edad_men40, memb_edad_40_50, memb_edad_ma50, memb_diabetes_low, memb_diabetes_md, memb_diabetes_hi, memb_histViaje_low, memb_histViaje_md, memb_histViaje_hi, memb_garganta_low, memb_garganta_md, memb_garganta_hi,memb_tos_low, memb_tos_md, memb_tos_hi, memb_olfatoGusto_low, memb_olfatoGusto_md, memb_olfatoGusto_hi, memb_respira_low, memb_respira_md, memb_respira_hi, memb_pecho_low, memb_pecho_md, memb_pecho_hi = memb_fuzzy()



# # Regla 1
# active_rule1 = np.fmin(memb_fiebre_lo, memb_edad_men40)

# # Clipping en la regla 1
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_neg1 = np.fmin(active_rule1, conclu_negativa) # removed entirely to 0

# def plotRegla1():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_neg1)
#     # plt.axis([5,25,0,1])
#     plt.show()

# # regla1 = plotRegla1()
# # regla1

# # Regla 2
# active_rule2 = np.fmin(memb_fiebre_md, memb_edad_ma50)

# # Clipping en la regla 2
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_cua1 = np.fmin(active_rule2, conclu_cuarentena) # removed entirely to 0

# def plotRegla2():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_cua1)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 3
# # active_rule3 = np.fmin(memb_fiebre_hi, np.fmin(memb_edad_ma50,memb_histViaje_low))
# active_rule3 = np.fmin(memb_fiebre_hi, np.fmin(memb_edad_ma50,memb_histViaje_md))

# # Clipping en la regla 3
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_cua2 = np.fmin(active_rule3, conclu_cuarentena) # removed entirely to 0

# def plotRegla3():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion, conclu_activation_cua2)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 4
# active_rule4 = np.fmin(memb_fiebre_hi, np.fmin(memb_edad_ma50, memb_histViaje_hi))

# # Clipping en la regla 4
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi1 = np.fmin(active_rule4, conclu_positivo) # removed entirely to 0

# def plotRegla4():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion, conclu_activation_posi1)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 5
# # active_rule5 = np.fmin(memb_garganta_low, np.fmin(memb_edad_men40, memb_histViaje_low))
# active_rule5 = np.fmin(memb_garganta_low, np.fmin(memb_edad_men40, memb_histViaje_md))

# # Clipping en la regla 5
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_cua3 = np.fmin(active_rule5, conclu_cuarentena) # removed entirely to 0

# def plotRegla5():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_cua3)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 6
# active_rule6 = np.fmin(memb_garganta_hi, np.fmin(
#     np.fmax(memb_edad_40_50, memb_edad_ma50), memb_tos_md))

# # Clipping en la regla 6
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_cua4 = np.fmin(active_rule6, conclu_cuarentena) # removed entirely to 0

# def plotRegla6():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_cua4)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 7
# active_rule7 = np.fmin(memb_respira_low, np.fmin(
#     np.fmax(memb_edad_40_50, memb_edad_ma50), memb_tos_md))

# # Clipping en la regla 7
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_neg2 = np.fmin(active_rule7, conclu_negativa) # removed entirely to 0

# def plotRegla7():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_neg2)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 8
# active_rule8 = np.fmin(memb_respira_hi, np.fmin(
#     np.fmax(memb_edad_40_50, memb_edad_ma50), memb_tos_hi))

# # Clipping en la regla 8
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi2 = np.fmin(active_rule8, conclu_positivo) # removed entirely to 0

# def plotRegla8():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi2)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 9
# active_rule9 = np.fmin(memb_respira_low, np.fmax(memb_edad_40_50, memb_edad_ma50))

# # Clipping en la regla 9
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_neg3 = np.fmin(active_rule9, conclu_negativa) # removed entirely to 0

# def plotRegla9():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_neg3)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 10
# active_rule10 = np.fmin(memb_edad_men40, np.fmin(memb_histViaje_hi, memb_respira_hi))

# # Clipping en la regla 10
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi3 = np.fmin(active_rule10, conclu_positivo) # removed entirely to 0

# def plotRegla10():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi3)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 11
# active_rule11 = np.fmin(memb_edad_ma50, np.fmin(memb_histViaje_hi, memb_respira_hi))

# # Clipping en la regla 11
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi4 = np.fmin(active_rule11, conclu_positivo) # removed entirely to 0

# def plotRegla11():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi4)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 12
# active_rule12 = np.fmin(np.fmax(memb_edad_40_50, memb_edad_ma50), 
#                         np.fmin(memb_histViaje_hi, np.fmin(memb_tos_hi, memb_respira_hi)))

# # Clipping en la regla 12
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi5 = np.fmin(active_rule12, conclu_positivo) # removed entirely to 0

# def plotRegla12():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi5)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 13
# # active_rule13 = np.fmax(np.fmax(memb_edad_40_50, memb_edad_ma50),
# #                         np.fmax(memb_diabetes_hi, np.fmax(memb_histViaje_low,
# #                                                           np.fmax(memb_tos_md, memb_respira_hi))))

# active_rule13 = np.fmax(np.fmax(memb_edad_40_50, memb_edad_ma50),
#                         np.fmax(memb_diabetes_hi, np.fmax(memb_histViaje_md,
#                                                           np.fmax(memb_tos_md, memb_respira_hi))))

# # Clipping en la regla 13
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi6 = np.fmin(active_rule13, conclu_positivo) # removed entirely to 0

# def plotRegla13():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi6)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 14
# # active_rule14 = np.fmin(np.fmax(memb_edad_40_50, memb_edad_ma50),
# #                         np.fmin(memb_diabetes_hi, memb_histViaje_low))


# active_rule14 = np.fmin(np.fmax(memb_edad_40_50, memb_edad_ma50),
#                          np.fmin(memb_diabetes_hi, memb_histViaje_md))

# # Clipping en la regla 14
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi7 = np.fmin(active_rule14, conclu_cuarentena) # removed entirely to 0

# def plotRegla14():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi7)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 15
# active_rule15 = np.fmin(memb_olfatoGusto_hi, memb_pecho_hi)

# # Clipping en la regla 15
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi8 = np.fmin(active_rule15, conclu_positivo) # removed entirely to 0

# def plotRegla15():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi8)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 16
# # active_rule16 = np.fmin(memb_histViaje_low, np.fmin(memb_garganta_hi,
# #                                                     np.fmin(memb_tos_hi, memb_pecho_hi)))

# active_rule16 = np.fmin(memb_histViaje_md, np.fmin(memb_garganta_hi,
#                                                     np.fmin(memb_tos_hi, memb_pecho_hi)))

# # Clipping en la regla 16
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_posi9 = np.fmin(active_rule16, conclu_positivo) # removed entirely to 0

# def plotRegla16():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_posi9)
#     # plt.axis([5,25,0,1])
#     plt.show()


# # Regla 17
# active_rule17 = np.fmin(memb_edad_men40, np.fmin(memb_histViaje_low, memb_garganta_low))

# # Clipping en la regla 17
# #Para unir antecedente y consecuente se usa np.fmin
# conclu_activation_neg4 = np.fmin(active_rule17, conclu_negativa) # removed entirely to 0

# def plotRegla17():
#     plt.style.use('default')
#     fig=plt.figure(figsize=(6,2))
#     plt.plot(x_conclusion,conclu_activation_neg4)
#     # plt.axis([5,25,0,1])
#     plt.show()

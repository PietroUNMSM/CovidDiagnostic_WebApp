from baseReglas import *



#AGREGACION
def defuzzy(conclu_activation_neg1, conclu_activation_cua1, conclu_activation_cua2, conclu_activation_posi1, conclu_activation_cua3, conclu_activation_cua4, conclu_activation_neg2, conclu_activation_posi2, conclu_activation_neg3, conclu_activation_posi3, conclu_activation_posi4, conclu_activation_posi5, conclu_activation_posi6, conclu_activation_posi7, conclu_activation_posi8, conclu_activation_posi9, conclu_activation_neg4):

        aggregated = np.fmax(conclu_activation_neg1, 
                        np.fmax(conclu_activation_neg2, 
                                np.fmax(conclu_activation_neg3,
                                        np.fmax(conclu_activation_neg4,
                                                np.fmax(conclu_activation_cua1,
                                                        np.fmax(conclu_activation_cua2,
                                                                np.fmax(conclu_activation_cua3,
                                                                        np.fmax(conclu_activation_cua4,
                                                                                np.fmax(conclu_activation_posi1,
                                                                                        np.fmax(conclu_activation_posi2,
                                                                                                np.fmax(conclu_activation_posi3,
                                                                                                        np.fmax(conclu_activation_posi4,
                                                                                                                np.fmax(conclu_activation_posi5,
                                                                                                                        np.fmax(conclu_activation_posi6,
                                                                                                                                np.fmax(conclu_activation_posi7,
                                                                                                                                        np.fmax(conclu_activation_posi8, 
                                                                                                                                                conclu_activation_posi9))))))))))))))))

        # print(aggregated)
        #rango de conclusion
        x_conclusion = np.linspace(0, 1, 100)
        

        #la funcion de defuzzificacion son: lom, som,mom, centroid, bisector
        conclu = fuzz.defuzz(x_conclusion, aggregated, 'centroid')
        # print('\nEje x del centroide:',conclu) # eje x del centroide

        y = fuzz.interp_membership(x_conclusion, aggregated, conclu)
        # print('Eje y del centroide:',y) # eje y del centroide

#     def plotAgregacion():
        fig=plt.figure(figsize=(4,4))
        plt.plot(x_conclusion,aggregated)
        plt.plot(conclu, y, marker='o')
        # plt.axis([5,25,0,1])
        # plt.show()
        plt.savefig('templates/Imagenes/Conclusion/plotDefuzzy.png', bbox_inches='tight',dpi=100)

        # imgAgreg = plotAgregacion()
        # imgAgreg

        #Hallar el nivel de pertinencia en propina en bajo medio y alto
        casoNega = fuzz.interp_membership(x_conclusion, conclu_negativa, conclu)

        #print(a)
        casoCuarent = fuzz.interp_membership(x_conclusion, conclu_cuarentena, conclu)

        #print("{:.2f},".format(b))
        casoPosi = fuzz.interp_membership(x_conclusion, conclu_positivo, conclu)

        #print("{:.2f},".format(c))
        # print("El grado de pertenencia en Caso Negativo es {:.2f}".format(casoNega))
        # print("El grado de pertenencia en Caso de Cuarentena es {:.2f}".format(casoCuarent))
        # print("El grado de pertenencia en Caso Positivo es {:.2f}".format(casoPosi))
        return conclu, y, casoNega, casoCuarent, casoPosi
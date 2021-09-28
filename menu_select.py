"""
Fecha de creación: 24/sep/21
Autor: Cristopher Olivares 
"""
menu_select = {'Detalle: ' : {
                            'MESA: ': 3,
                            'COMENSAL: ' : 2, 
                            'ENTRADA: ' : 'Ensalada verde', 
                            'MEDIO: ' : 'Crema de zanahoria', 
                            'FUERTE: ': 'Filete',
                            'ADICIONALES: ' : 'Filete termino medio, la ensalda sin nigún tipo de semilla, adereso'
                            }
              }

llaves_menu = menu_select.keys()
llaves_detalle = menu_select['Detalle: '].keys()
for menu in llaves_menu:
    print( menu)
for detalle in llaves_detalle:
    print( detalle)
    print( menu_select['Detalle: '][detalle])

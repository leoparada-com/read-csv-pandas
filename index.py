import pandas as pd

# lectura de un archivo csv
# df = pd.read_csv("http://leoparada.com/data/data_frame_2.csv")
df = pd.read_csv("data_frame_2.csv")
#list(df) = ['nombre', 'apellido', 'rut', ' edad', 'curso']
cabeceras = list(df.columns)
# convertir a mayusculas el HEADER
count=0
for i in cabeceras:    
    cabeceras[count]=i.upper()
    count=count+1
    print(i)

#cabeceras = list(str(cabeceras).upper())
df.columns = cabeceras

# muestra las 2 primeras filas
# https://www.analyticslane.com/2019/06/21/seleccionar-filas-y-columnas-en-pandas-con-iloc-y-loc/
print('inicio')
print(cabeceras)
print('')
print('------------------------ muestra todo -------------------------------------')
print('')
print(df[:])
print('')
print('----------------- muestra las primeras dos filas --------------------------')
print('')
print(df[: 2])
print('')
print('-------------------- muestra solo algunas filas --------------------------')
print('')
print(df.iloc[1:4])
print('')
print('--------------------------------------------------------------------------')
print('muestra las cabeceras')
print(list(df))



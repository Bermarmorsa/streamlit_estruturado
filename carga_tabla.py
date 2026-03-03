import streamlit as st
import pandas as pd
import os


def guardar_archivo (uploadedfile):
    #crear directorio si no exisite
    if not os.path.exists('data'):
        os.makedirs('data')

    #guardar en directorio
    with open(os.path.join('data', uploadedfile.name), 'wb') as f:
        f.write(uploadedfile.getbuffer()) #getbuffer() $\rightarrow$ Crea un acceso directo a esos datos en la RAM. asi no se ocupa mas espacio

        return st.success(f'Archivo guardado, con nombre: {uploadedfile.name} en carpeta temp')




def cargar_csv():
    st.subheader('Cargar CSV')
    archivo_datos = st.file_uploader('Upload CSV o xslx Datos', type=['csv', 'xlsx'])
    if archivo_datos is not None:
        detalle_csv = {'nombre_archivo': archivo_datos.name,
                       'tipo_archivo': archivo_datos.type,
                       'filas_archivo': archivo_datos.size}
        st.write(detalle_csv)
        if archivo_datos.type == "text/csv":
            df = pd.read_csv(archivo_datos)


        elif archivo_datos.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(archivo_datos)

        else:
            df = pd.DataFrame()  # creamos un df vacio para que en la salida del if haya algo y no de error.
        st.dataframe(df.iloc[:20])
        guardar_archivo(archivo_datos)



import streamlit as st
from carga_tabla import cargar_csv
from texto import app_texto


def main():
    #titulo
    st.title('Aplicacion Principal')
    #creación de menu lateral
    menu=['Inicio','Carga Tabla','Texto','Conócenos']
    #guardamos la eleccion en una variable
    choice = st.sidebar.selectbox('Menú',menu)


    if choice == 'Inicio':
        st.subheader('Inicio')
    elif choice == 'Carga Tabla':
        cargar_csv()
    elif choice == 'Texto':
        app_texto()
    elif choice == 'Conócenos':
        st.subheader('Conócenos')




if __name__ == '__main__':
    main()






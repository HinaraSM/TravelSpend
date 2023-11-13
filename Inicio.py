# Importar librerías y módulos necesarios
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Personalizar el menú desplegable con el logo
st.set_page_config(
    page_title="TravelSpend",
    page_icon="images/logo.png",  # Icono en la pestaña del navegador
)

# Añadir el logo en la barra lateral
st.sidebar.title("TravelSpend")
st.sidebar.image("images/fondo2.png", width=285)

# Variable global para almacenar el DataFrame
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Categoria', 'Monto',
                                                'Fecha'])

# Título de la aplicación
st.title("Calculadora de Gastos de Viaje TravelSpend")

# Ingreso de gastos
st.header("Ingresar un nuevo gasto")
# Directorio local donde se almacenan las imágenes
image_directory = "images/"

categoria = st.selectbox("Categoría", ["Comida", "Alojamiento", "Transporte",
                                       "Actividades", "Otros"])
imagen_categoria = f"{image_directory}{categoria.lower()}.png"

# Cargar la imagen utilizando scikit-image
imagen = io.imread(imagen_categoria)

# Mostrar la imagen redimensionada
st.image(imagen, caption=categoria, width=150)

# Recibir inputs
monto = st.number_input("Monto", value=0.0)
fecha = st.date_input("Fecha")
fecha = fecha.strftime('%d/%m')

# Agregar gastos
if st.button("Agregar Gasto"):
    new_row = {'Categoria': categoria, 'Monto': monto, 'Fecha': fecha}
    st.session_state.df = pd.concat([st.session_state.df,
                                     pd.DataFrame(new_row, index=[0])],
                                    ignore_index=True)

    st.success("Gasto agregado con éxito")

# Resumen de Gastos
st.header("Resumen de Gastos")
if not st.session_state.df.empty:
    st.write("Gastos registrados:")
    st.write(st.session_state.df)
    # Calcular el gasto total
    total_gasto = np.sum(st.session_state.df['Monto'])
    st.write(f"Gasto Total: ${total_gasto:.2f}")

    # Calcular el máximo y mínimo de los gastos
    max_gasto = np.max(st.session_state.df['Monto'])
    min_gasto = np.min(st.session_state.df['Monto'])
    st.write(f"Gasto Máximo: ${max_gasto:.2f}")
    st.write(f"Gasto Mínimo: ${min_gasto:.2f}")

    # Calcular la categoría en la que más y menos se gastó dinero
    gasto_por_categoria = st.session_state.df.groupby('Categoria')[
        'Monto'].sum()
    categoria_max_gasto = gasto_por_categoria.idxmax()
    max_gasto = gasto_por_categoria.max()
    categoria_min_gasto = gasto_por_categoria.idxmin()
    min_gasto = gasto_por_categoria.min()
    st.write(f"Categoría en la que se gastó más dinero: {categoria_max_gasto}"
             f" (${max_gasto:.2f})")
    st.write(f"Categoría en la que se gastó menos dinero: "
             f"{categoria_min_gasto} (${min_gasto:.2f}")

    # Gráfico de barras de gastos por categoría utilizando Matplotlib
    st.header("Gráfico de Gastos por Categoría")
    fig, ax = plt.subplots()
    ax.bar(gasto_por_categoria.index, gasto_por_categoria)
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Monto")
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # Mostrar gasto por día en un gráfico de barras
    st.header("Gasto por Día")
    gasto_por_dia = st.session_state.df.groupby('Fecha')['Monto'].sum()
    fig, ax = plt.subplots()
    ax.bar(gasto_por_dia.index, gasto_por_dia.values)
    ax.set_xlabel("Fecha (día/mes)")
    ax.set_ylabel("Gasto")
    plt.xticks(rotation=45)
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
else:
    st.warning("No hay datos de gastos disponibles.")

# Exportar los datos
st.header("Exportar Datos")


# Define una función para descargar el archivo CSV
def download_csv():
    """
    Descarga el DataFrame en formato CSV como un archivo descargable.
    """
    csv = st.session_state.df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name="gastos_de_viaje.csv",
        key="download_button"
    )


# Muestra el botón de descarga
download_csv()

# Limpiar los datos
st.write("Presionar dos veces el botón de 'Limpiar Datos' si está seguro de "
         "querer borrarlos")
if st.button("Limpiar Datos"):
    st.session_state.df = pd.DataFrame(columns=['Categoria', 'Monto',
                                                'Fecha'])

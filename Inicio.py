import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Crear un DataFrame para almacenar los gastos
df = pd.DataFrame(columns=['Categoría', 'Monto', 'Fecha'])

# Título de la aplicación
st.title("Calculadora de Gastos de Viaje")

# Ingreso de gastos
st.header("Ingresar un nuevo gasto")
categoria = st.selectbox("Categoría", ["Comida", "Alojamiento", "Transporte", "Actividades", "Otros"])
monto = st.number_input("Monto", value=0.0)
fecha = st.date_input("Fecha")

if st.button("Agregar Gasto"):
    df = df.append({'Categoría': categoria, 'Monto': monto, 'Fecha': fecha}, ignore_index=True)
    st.success("Gasto agregado con éxito")

# Resumen de Gastos
st.header("Resumen de Gastos")
st.write("Gastos registrados:")
st.write(df)

# Calcular el gasto total
total_gasto = df['Monto'].sum()
st.write(f"Gasto Total: ${total_gasto:.2f}")

# Calcular el promedio de gastos diarios
dias_de_viaje = (df['Fecha'].max() - df['Fecha'].min()).days + 1
gasto_diario = total_gasto / dias_de_viaje
st.write(f"Gasto Promedio Diario: ${gasto_diario:.2f}")

# Gráfico de barras de gastos por categoría
"""st.header("Gráfico de Gastos por Categoría")
gastos_por_categoria = df.groupby('Categoría')['Monto'].sum()
fig, ax = plt.subplots()
ax.bar(gastos_por_categoria.index, gastos_por_categoria)
ax.set_xlabel("Categoría")
ax.set_ylabel("Monto")
st.pyplot(fig)"""

# Exportar los datos
st.header("Exportar Datos")
if st.button("Exportar a CSV"):
    df.to_csv("gastos_de_viaje.csv", index=False)
    st.success("Datos exportados a 'gastos_de_viaje.csv'")

# Limpiar los datos
if st.button("Limpiar Datos"):
    df = pd.DataFrame(columns=['Categoría', 'Monto', 'Fecha'])
    st.success("Datos limpiados")


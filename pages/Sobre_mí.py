# Importar librerías y módulos necesarios
import streamlit as st
from skimage import io, exposure, filters
from skimage.util import img_as_ubyte

# Cargar tu imagen desde el sistema de archivos
image_path = "images/hinara.jpg"  # Reemplaza con la ruta a tu imagen
image = io.imread(image_path)

# Aplicar el filtro de aumento de nitidez
sharpened_image = filters.unsharp_mask(image, radius=0.3, amount=50.0)

# Ajustar el rango de valores de la imagen a 0-255
sharpened_image = exposure.rescale_intensity(sharpened_image)

# Convertir la imagen a tipo de dato uint8 (necesario para mostrarla en
# Streamlit)
sharpened_image = img_as_ubyte(sharpened_image)

# Página "Sobre mí"
st.title("Calculadora de Gastos de Viaje TravelSpend")
st.write("¡Hola, soy Hinara Pastora Sánchez Mata!")

# Añadir el logo en la barra lateral
st.sidebar.title("TravelSpend")
st.sidebar.image("images/fondo2.png", width=285)

# Mostrar la imagen mejorada
st.image(sharpened_image, caption="Imagen con realce de bordes de mí",
         width=400)

st.write("¡Bienvenidos a mi aplicación de gastos de viaje! Soy una entusiasta "
         "de los viajes y amante de la organización, y esta aplicación es el "
         "resultado de mi pasión por ambas cosas. Aquí te cuento un poco "
         "sobre mí y la motivación detrás de esta herramienta.")


st.write("Desde que empecé a viajar, siempre he tenido la necesidad de llevar "
         "un registro de mis gastos para mantener mi presupuesto bajo control."
         " Esta aplicación nació de mi deseo de simplificar ese proceso y "
         "ayudar a otros viajeros como yo a administrar sus finanzas de "
         "manera efectiva durante sus aventuras por el mundo.")

st.write("Mi objetivo es proporcionarte una herramienta sencilla y útil para "
         "realizar un seguimiento y obtener información valiosa sobre tus "
         "patrones de gasto. Espero que esta aplicación te sea útil en tus "
         "viajes y te ayude a tener experiencias increíbles sin preocuparte "
         "demasiado por el dinero.")

st.write("Gracias por usar mi aplicación y formar parte de esta comunidad de "
         "viajeros que valoran la organización y el control de sus finanzas. "
         "Si tienes comentarios o sugerencias, no dudes en ponerte en "
         "contacto conmigo a través de mi correo hisanchezm@unal.edu.co. "
         "¡Felices viajes!")

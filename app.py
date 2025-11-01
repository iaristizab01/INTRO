import streamlit as st
from PIL import Image

st.title("🎀 Mi primera app de Hello Kitty 🎀")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales versión Hello Kitty 💕")

image = Image.open('hellokitty.webp')
st.image(image, caption='Hello Kitty hermosa')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario 💗")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('¡Correcto! 🎀')
  
with col2:
    st.subheader("Segunda columna")
    modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('👀 La vista es fundamental para tu interfaz')
    if modo == 'Auditiva':
       st.write('🎧 La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('🤚 El tacto es fundamental para tu interfaz')
        
st.subheader("Uso de Botones")
if st.button('Presiona el botón 🎀'):
    st.write('Gracias por presionar 💕')
else:
    st.write('No has presionado aún 😺')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "🔊 Reproducir audio"
elif in_mod == "Visual":
    set_mod = "🎬 Reproducir video"
elif in_mod == "Háptico":
    set_mod = "💓 Activar vibración"
st.write("La acción es:", set_mod)

with st.sidebar:
    st.subheader("🎀 Configura tu modalidad Hello Kitty 🎀")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )

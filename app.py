import streamlit as st
import json
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Título de la app
st.title("📋 Formulario de contacto inteligente")

# Campos del formulario
with st.form("contact_form"):
    nombre = st.text_input("Nombre completo:")
    correo = st.text_input("Correo electrónico:")
    telefono = st.text_input("Número de teléfono:")
    servicio = st.selectbox("Servicio de interés:", [
        "Asesoría Express ($150–$250)",
        "Asesoría Esencial ($500–$800 o $200–$300/mes)",
        "Asesoría Integral ($1,200–$2,500)",
        "Otro / Personalizado"
    ])
    mensaje = st.text_area("¿En qué podemos ayudarte?")
    enviado = st.form_submit_button("Enviar")

# Si el formulario se envía
if enviado:
    try:
        # Leer credenciales de secrets
        service_account_info = json.loads(st.secrets["gcp_service_account"])
        credentials = Credentials.from_service_account_info(service_account_info)

        # Acceder a Google Sheets
        gc = gspread.authorize(credentials)
        sheet = gc.open("Formulario Contacto Financiero").sheet1  # nombre del archivo y hoja

        # Datos del cliente
        data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nombre, correo, telefono, servicio, mensaje]
        sheet.append_row(data)

        st.success("✅ ¡Tu información fue enviada con éxito!")
    except Exception as e:
        st.error(f"❌ Error al enviar el formulario: {e}")

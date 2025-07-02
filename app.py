import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticación con Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

# Abrir hoja de cálculo por nombre (crear una hoja y pegar el nombre aquí)
spreadsheet = client.open("Formulario Asistente Financiero")
sheet = spreadsheet.sheet1

# Configuración de la app
st.title("Formulario de Contacto - Asistente Financiero")
st.write("Por favor, completa los siguientes datos para que podamos brindarte la asesoría adecuada.")

# Campos del formulario
nombre = st.text_input("Nombre completo")
correo = st.text_input("Correo electrónico")
telefono = st.text_input("Número de teléfono")
tipo_asesoria = st.selectbox("Tipo de asesoría", ["Express ($150-$250)", "Esencial ($500-$800)", "Integral ($1,200-$2,500)"])
presupuesto = st.text_input("¿Cuál es tu presupuesto estimado?")
mensaje = st.text_area("¿En qué podemos ayudarte?")

# Enviar información a Google Sheets
if st.button("Enviar"):
    if nombre and correo and telefono and mensaje:
        sheet.append_row([nombre, correo, telefono, tipo_asesoria, presupuesto, mensaje])
        st.success("✅ Tu información ha sido enviada con éxito. Pronto nos pondremos en contacto contigo.")
    else:
        st.warning("⚠️ Por favor, completa todos los campos antes de enviar.")
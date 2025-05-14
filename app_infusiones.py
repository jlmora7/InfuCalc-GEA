
import streamlit as st

# Diccionario de medicamentos con sus constantes (mcg/kg/min por ml/h)
meds_constantes = {
    "Norepinefrina": 1.33,
    "Propofol": 166.6,
    "Midazolam": 1.5,
    "Dexmedetomidina": 4.0,
    "Fentanil": 10.0,
    "Vasopresina": 0.0066,  # Puede no requerir peso
    "Dopamina": 33.3
}

# Diccionario de preparaciones
meds_preparacion = {
    "Norepinefrina": "8 mg aforar a 100 cc de solución glucosada al 5%",
    "Dopamina": "400 mg aforar a 250 cc de solución glucosada al 5%",
    "Dobutamina": "500 mg aforar a 250 cc de solución glucosada al 5%",
    "Amiodarona": "900 mg en 250 cc de solución glucosada al 5% para 24 h",
    "Vasopresina": "40 u aforadas en 100 cc de solución glucosada al 5%",
    "Fentanil": "1 mg (1000 mcg) aforar a 100 cc de solución salina 0.9%",
    "Midazolam": "300 mg en 200 cc de solución salina 0.9%",
    "Dexmedetomidina": "40 mcg en 100 cc de solución salina 0.9%",
    "Propofol": "No aplica",
    "Vecuronio": "40 mg en 100 cc de solución salina al 0.9%",
    "Rocuronio": "500 mg en 250 cc de solución salina al 0.9%"
}

st.title("Calculadora de Infusiones IV")

# Selección del medicamento
med = st.selectbox("Selecciona el medicamento a calcular", list(meds_constantes.keys()))

# Mostrar sugerencia de preparación si existe
if med in meds_preparacion:
    st.info(f"📃 Preparación sugerida: {meds_preparacion[med]}")

# Solicitar velocidad de infusión
velocidad = st.number_input("Velocidad de infusión (ml/h)", min_value=0.0, step=0.1)

# Mostrar o no peso según medicamento
requiere_peso = med != "Vasopresina"

peso = None
if requiere_peso:
    peso = st.number_input("Peso del paciente (kg)", min_value=0.0, step=0.1)

# Cálculo
constante = meds_constantes[med]
resultado = None

if velocidad > 0 and (not requiere_peso or (peso and peso > 0)):
    if requiere_peso:
        resultado = (velocidad * constante) / peso
        st.success(f"Dosis: {resultado:.2f} mcg/kg/min")
    else:
        resultado = velocidad * constante
        st.success(f"Dosis: {resultado:.4f} unidades/min")

# Mensaje final motivacional (como en el shortcut)
if resultado:
    st.info("🌟 Esa es la dosis por kg de tu infusión.\n\n✨ ¡Excelente! Tú puedes ✨")

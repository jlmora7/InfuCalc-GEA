import streamlit as st

# Diccionario centralizado con toda la información de cada medicamento
meds_info = {
    "Norepinephrine / Norepinefrina": {
        "constante": 1.33,
        "presentación": "4mg/4ml (1mg/ml)",
        "dosis_inicial": "0.1–0.5 mcg/kg/min IV",
        "dosis_mantenimiento": "0.02–1 mcg/kg/min IV",
        "preparación": "8 mg aforados en 100 cc de solución glucosada al 5%"
    },
    "Dopamine / Dopamina": {
        "constante": 33.3,
        "presentación": "200mg/5ml (40mg/ml)",
        "dosis_inicial": "Shock: 1–50 mcg/kg/min IV / Falla cardiaca: 0.5–2 mcg/kg/min",
        "dosis_mantenimiento": "1–5 mcg/kg/min / Bradicardia-vasopresor: 5–10 mcg/kg/min",
        "preparación": "400 mg aforados en 250 cc de solución glucosada al 5%"
    },
    "Midazolam": {
        "constante": 1.5,
        "presentación": "15mg/3ml (5mg/ml)",
        "dosis_inicial": "0.01–0.05 mg/kg",
        "dosis_mantenimiento": "0.02–0.2 mg/kg/h (↓ 50% si TFG <10%)",
        "preparación": "300 mg aforados en 200 cc de solución salina 0.9%"
    },
    "Dexmedetomidine / Dexmedetomidina": {
        "constante": 4.0,
        "presentación": "200mcg/2ml (100 mcg/ml)",
        "dosis_inicial": "80–100 mcg/kg IV",
        "dosis_mantenimiento": "0.8–1.2 mcg/kg/min",
        "preparación": "40 mcg aforados en en 100 cc de solución salina 0.9%"
    },
    "Fentanyl / Fentanilo": {
        "constante": 10.0,
        "presentación": "0.5mg/10ml (500 mcg/ml)",
        "dosis_inicial": "1–2 mcg/kg",
        "dosis_mantenimiento": "0.5–1 mcg/kg/h",
        "preparación": "1 mg (1000 mcg) aforados en 100 cc de solución salina 0.9%"
    },
    "Vasopressin / Vasopresina": {
        "constante": 0.0066,
        "presentación": "20UI/ml",
        "dosis_inicial": "No aplica",
        "dosis_mantenimiento": "0.1–0.07 UI/min",
        "preparación": "40 UI aforados en 100 cc de solución glucosada al 5%"
    },
    "Propofol": {
        "constante": 166.6,
        "presentación": "1g/100ml (10 mg/ml)",
        "dosis_inicial": "2–2.5 mg/kg",
        "dosis_mantenimiento": "25–75 mcg/kg/min IV",
        "preparación": "No aplica"
    }
}

# Diccionario de traducción
mensajes = {
    "Español": {
         "disclaimer": """
        <div style=\"background-color:#5c5727;padding:20px;border-radius:10px;color:white\">
            <span style=\"font-size:20px\">⚠️ <strong>Descargo de Responsabilidad:</strong></span>
            <ul style=\"font-size:16px;\">
                <li>Esta herramienta tiene fines <strong>exclusivamente educativos e informativos</strong>. <strong>No sustituye el juicio clínico de profesionales de la salud</strong>.</li>
                <li>Las decisiones relacionadas con el tratamiento deben ser tomadas únicamente por <strong>personal médico calificado</strong>, basándose en una <strong>evaluación integral del paciente</strong> y en los <strong>lineamientos de su institución</strong>.</li>
                <li><strong>No debe utilizarse esta calculadora como única referencia para decisiones médicas.</strong> Verifique siempre los resultados obtenidos y tenga en cuenta el contexto clínico completo</li>
                <li>Los autores declinan toda responsabilidad por el uso inapropiado de esta herramienta o por las consecuencias derivadas de su aplicación.</li>
            </ul>
        </div>
        """,
        "footer1": """
        <div style=\"text-align:center; padding-top: 30px; font-size: small; color: gray;\">
            © 2025 InfuCalc GEA.
        </div>
        """,
        "footer2": """
        <div style=\"text-align:center; padding-top: 30px; font-size: small; color: gray;\">
            Creado por José Luis Mora Loján
        </div>
        """,
        "descripción": "Aplicación médica construida para calcular dosis en mcg/kg/min o unidades/min a partir de la velocidad de infusión.",
        "motivacional": "💡 Esa es la dosis calculada de tu infusión. ¡Excelente! Tú puedes 💪",
        "titulo": "InfuCalc GEA 💉",
        "idioma": "Selecciona el idioma / Select language",
        "medicamento": "Selecciona el medicamento a calcular",
        "presentación": "📦 Presentación",
        "dosis_inicial": "💉 Dosis inicial",
        "dosis_mantenimiento": "🔁 Dosis mantenimiento",
        "preparación": "🧪 Preparación sugerida",
        "velocidad": "Velocidad de infusión (ml/h)",
        "peso": "Peso del paciente (kg)",
        "resultado_mcg": "Dosis: {valor:.2f} mcg/kg/min",
        "resultado_u": "Dosis: {valor:.4f} unidades/min"
    },
    "English": {
        "disclaimer": """
        <div style=\"background-color:#5c5727;padding:20px;border-radius:10px;color:white\">
            <span style=\"font-size:20px\">⚠️ <strong>Important Disclaimer:</strong></span>
            <ul style=\"font-size:16px;\">
                <li>This tool is intended for <strong>educational and informational purposes only</strong>. It does not replace clinical judgment by <strong>qualified healthcare professionals</strong>.</li>
                <li>Treatment decisions must be made solely by <strong>licensed medical personnel</strong> based on a <strong>comprehensive evaluation of the patient</strong> and <strong>institutional guidelines</strong>.</li>
                <li><strong>This calculator must not be used as the sole reference</strong> for medical decisions. Always verify the results and consider the full clinical context.</li>
                <li>The authors disclaim all responsibility for inappropriate use or consequences derived from the application of this tool.</li>
            </ul>
        </div>
        """,
        "footer1": """
        <div style=\"text-align:center; padding-top: 30px; font-size: small; color: gray;\">
            © 2025 InfuCalc GEA.
        </div>
        """,
        "footer2": """
        <div style=\"text-align:center; padding-top: 30px; font-size: small; color: gray;\">
            Created by José Luis Mora Loján
        </div>
        """,
        "descripción": "Medical app designed to calculate doses in mcg/kg/min or units/min based on infusion rate.",
        "motivacional": "💡 This is the calculated dose of your infusion. Excellent! You’ve got this 💪",
        "titulo": "InfuCalc GEA 💉",
        "idioma": "Select language / Selecciona el idioma",
        "medicamento": "Select the drug to calculate",
        "presentación": "📦 Presentation",
        "dosis_inicial": "💉 Initial dose",
        "dosis_mantenimiento": "🔁 Maintenance dose",
        "preparación": "🧪 Suggested preparation",
        "velocidad": "Infusion rate (ml/h)",
        "peso": "Patient weight (kg)",
        "resultado_mcg": "Dose: {valor:.2f} mcg/kg/min",
        "resultado_u": "Dose: {valor:.4f} units/min",
        "solución salina 0.9%": "NS 0.9%",
        "aforados": "assessed",
        "solución glucosada al 5%": "Dextrose 5%"
    }
}
# Selección de idioma
lang = st.selectbox(mensajes["Español"]["idioma"], ["Español", "English"])

st.title(mensajes[lang]["titulo"])

st.markdown(mensajes[lang]["descripción"])

# Selección del medicamento
med = st.selectbox(mensajes[lang]["medicamento"], list(meds_info.keys()))
info = meds_info[med]

# Mostrar información clínica y preparación
st.info(f"{mensajes[lang]['presentación']}: {info['presentación']}\n\n{mensajes[lang]['dosis_inicial']}: {info['dosis_inicial']}\n\n{mensajes[lang]['dosis_mantenimiento']}: {info['dosis_mantenimiento']}\n\n{mensajes[lang]['preparación']}: {info['preparación']}")

# Solicitar velocidad de infusión
velocidad = st.number_input(mensajes[lang]["velocidad"], min_value=0.0, step=0.1)

# Mostrar o no peso según medicamento
requiere_peso = med != "Vasopresina"
peso = st.number_input(mensajes[lang]["peso"], min_value=0.0, step=0.1) if requiere_peso else None

# Cálculo
resultado = None
if velocidad > 0 and (not requiere_peso or (peso and peso > 0)):
    if requiere_peso:
        resultado = (velocidad * info['constante']) / peso
        st.success(mensajes[lang]["resultado_mcg"].format(valor=resultado))
    else:
        resultado = velocidad * info['constante']
        st.success(mensajes[lang]["resultado_u"].format(valor=resultado))

# Mensaje final motivacional
if resultado:
    st.info(mensajes[lang]["motivacional"])

# Línea divisoria
st.markdown("---")

# Descargo de responsabilidad
with st.container():
    st.markdown(mensajes[lang]["disclaimer"], unsafe_allow_html=True)

# Pie de página
st.markdown(mensajes[lang]["footer1"], unsafe_allow_html=True)
st.markdown(mensajes[lang]["footer2"], unsafe_allow_html=True)


# 💉 Calculadora de Infusiones IV

Aplicación médica construida con **Streamlit** para calcular dosis en mcg/kg/min o unidades/min a partir de la velocidad de infusión. Pensada para el uso diario en **medicina interna, terapia intensiva y urgencias**.

## 🚀 ¿Qué hace esta app?

- Calcula dosis de medicamentos intravenosos según velocidad (ml/h) y peso.
- Incluye constantes predefinidas para fármacos como norepinefrina, dopamina, midazolam, propofol, etc.
- Muestra sugerencias de **preparación estándar** para cada infusión.
- Diseñada para uso clínico diario y enseñanza médica.

## 🧪 Medicamentos incluidos

| Fármaco            | Constante (mcg/kg/min por ml/h) | Preparación sugerida                                     |
|--------------------|----------------------------------|----------------------------------------------------------|
| Norepinefrina      | 1.33                             | 8 mg en 100 cc SG5%                                      |
| Dopamina           | 33.3                             | 400 mg en 250 cc SG5%                                    |
| Midazolam          | 1.5                              | 300 mg en 200 cc SS0.9%                                  |
| Dexmedetomidina    | 4.0                              | 40 mcg en 100 cc SS0.9%                                  |
| Fentanil           | 10.0                             | 1 mg en 100 cc SS0.9%                                    |
| Vasopresina        | 0.0066                           | 40 UI en 100 cc SG5%                                     |
| Propofol           | 166.6                            | No aplica                                                |

## 🧑‍💻 Cómo desplegar la app localmente

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/infusion-app.git
cd infusion-app

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la app
streamlit run app_infusiones.py
```

## ☁️ Despliegue en línea

Puedes ver la app en vivo (tras despliegue con Streamlit Cloud):

👉 [https://tu-usuario.streamlit.app](https://tu-usuario.streamlit.app)

---

## 🩺 Autor

Creado por José Luis Mora Loján

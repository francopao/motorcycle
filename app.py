import streamlit as st
import random

st.set_page_config(page_title="Moto Mecánica PRO")

st.title("🏍️ Motorcycle")

# ======================
# BASE DE DATOS
# ======================

componentes = {
    "Motor": {
        "ubicacion": "Centro",
        "funcion": "Genera potencia",
        "fallas": ["Pérdida de potencia", "Ruido metálico", "Humo"]
    },
    "Radiador": {
        "ubicacion": "Frente del motor",
        "funcion": "Enfriar motor",
        "fallas": ["Sobrecalentamiento"]
    },
    "Cadena": {
        "ubicacion": "Parte trasera",
        "funcion": "Transmitir potencia",
        "fallas": ["Tirones", "Ruido"]
    },
    "Freno delantero": {
        "ubicacion": "Rueda delantera",
        "funcion": "Frenado principal",
        "fallas": ["No frena", "Vibración"]
    },
    "Batería": {
        "ubicacion": "Bajo asiento",
        "funcion": "Sistema eléctrico",
        "fallas": ["No arranca"]
    }
}

# ======================
# NIVEL 2: DIAGNÓSTICO REALISTA
# ======================

st.header("🧠 Nivel 2: Diagnóstico Realista")

escenarios = [
    {
        "problema": "La moto pierde potencia y hace ruido",
        "opciones": ["Motor", "Cadena", "Radiador"],
        "correcto": "Motor"
    },
    {
        "problema": "La moto se calienta mucho",
        "opciones": ["Radiador", "Motor"],
        "correcto": "Radiador"
    },
    {
        "problema": "La moto da tirones al acelerar",
        "opciones": ["Cadena", "Motor"],
        "correcto": "Cadena"
    }
]

escenario = random.choice(escenarios)

st.write(f"🔍 Problema: {escenario['problema']}")

respuesta = st.selectbox("Selecciona causa probable", escenario["opciones"])

if st.button("Evaluar diagnóstico"):
    if respuesta == escenario["correcto"]:
        st.success("✅ Correcto — buen diagnóstico")
    else:
        st.warning(f"⚠️ No es la principal — revisa {escenario['correcto']}")

# ======================
# NIVEL 3: ÁRBOL DE DIAGNÓSTICO
# ======================

st.header("🌳 Nivel 3: Árbol de Diagnóstico")

problema_arbol = st.selectbox(
    "Selecciona síntoma principal",
    ["No arranca", "Se sobrecalienta", "Pierde potencia"]
)

if problema_arbol == "No arranca":
    paso1 = st.selectbox("¿Hace algún sonido al intentar arrancar?", ["Sí", "No"])
    
    if paso1 == "No":
        st.info("🔧 Posible causa: Batería")
    else:
        paso2 = st.selectbox("¿El motor gira?", ["Sí", "No"])
        if paso2 == "No":
            st.info("🔧 Posible causa: Motor de arranque / batería")
        else:
            st.info("🔧 Posible causa: Combustible o motor")

elif problema_arbol == "Se sobrecalienta":
    paso1 = st.selectbox("¿Tiene refrigerante?", ["Sí", "No"])
    
    if paso1 == "No":
        st.info("🔧 Problema: Radiador")
    else:
        st.info("🔧 Revisar bomba de agua o motor")

elif problema_arbol == "Pierde potencia":
    paso1 = st.selectbox("¿Hay ruidos extraños?", ["Sí", "No"])
    
    if paso1 == "Sí":
        st.info("🔧 Posible causa: Motor o cadena")
    else:
        st.info("🔧 Posible causa: Combustión o filtro")
        
        
        
        
        
# ======================
# RESUMEN VISUAL FINAL (IMAGEN + ÍNDICE)
# ======================

st.header("🗺️ Resumen Visual de Componentes")

# st.image("C:/Users/usuario/OneDrive/Desktop/Streamlit33/moto.png", use_container_width=True)
st.image("moto_componentes.png", use_container_width=True)

st.subheader("Índice rápido")

indice = [
    ("Engine (Motor)", "Genera la potencia"),
    ("Exhaust (Escape)", "Expulsa gases"),
    ("Drive Chain (Cadena)", "Transmite potencia"),
    ("Brake (Freno)", "Reduce velocidad"),
    ("Tire (Llanta)", "Contacto con el suelo"),
    ("Rim (Aro)", "Soporte de la llanta"),
    ("Rear Shocks (Suspensión trasera)", "Absorbe impactos"),
    ("Seat (Asiento)", "Soporte del conductor"),
    ("Gas Tank (Tanque de combustible)", "Almacena combustible"),
    ("Handle Bar (Manillar)", "Control de dirección"),
    ("Mirror (Espejo)", "Visión trasera"),
    ("Windscreen (Parabrisas)", "Reduce resistencia del aire"),
    ("Head Light (Faro)", "Iluminación frontal"),
    ("Front Forks (Horquilla delantera)", "Suspensión delantera"),
    ("Body Work / Fairings (Carenado)", "Protección y aerodinámica"),
    ("Foot Peg (Reposapiés)", "Apoyo de los pies")
]

for nombre, funcion in indice:
    st.write(f"• **{nombre}** → {funcion}")

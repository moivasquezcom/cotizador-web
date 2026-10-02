import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="Cotizador de Diseño Web", page_icon="💻", layout="centered"
)

# Estilos personalizados para darle un toque profesional
st.markdown(
    """
    <style>
    .main-title { text-align: center; color: #1E293B; margin-bottom: 5px; }
    .subtitle { text-align: center; color: #64748B; margin-bottom: 25px; }
    .price-card {
        background-color: #F8FAFC;
        border: 2px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    .price-amount { font-size: 36px; font-weight: bold; color: #0F172A; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 class='main-title'>Calcula tu Presupuesto Web</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='subtitle'>Selecciona las características de tu proyecto para obtener una cotización estimada al instante.</p>",
    unsafe_allow_html=True,
)

# Configura aquí tu número de WhatsApp (con código de país, ejemplo: 51987654321)
TU_NUMERO_WHATSAPP = "51942021673"

# 1. Selección de tipo de proyecto
tipo_web = st.selectbox(
    "1. Selecciona el tipo de proyecto:",
    [
        "Sitio web corporativo (Multipágina)",
        "Sitio web One Page (Una sola página)",
        "Landing Page",
        "Página de ventas",
        "Tienda online (E-commerce)",
        "Embudo de ventas (Funnel de conversión)",
        "Embudo de leads (Captación de prospectos)",
    ],
)

precio_total = 0.0
detalles = []

st.markdown("---")
st.subheader("2. Estructura y funcionalidades")

# 2. Lógica por cada tipo de web
if tipo_web == "Sitio web corporativo (Multipágina)":
    st.info(
        "Páginas habituales incluidas: Inicio, Nosotros, Servicios, Blog, Contacto."
    )
    secciones = st.number_input(
        "Número estimado de secciones en total:",
        min_value=5,
        max_value=40,
        value=15,
        step=1,
    )
    costo_secciones = secciones * 10
    precio_total += costo_secciones
    detalles.append(
        f"- Tipo: Sitio web corporativo ({secciones} secciones a $10 c/u): ${costo_secciones} USD"
    )

elif tipo_web == "Sitio web One Page (Una sola página)":
    secciones = st.number_input(
        "Número de secciones (ej. Hero, Beneficios, Servicios, Reseñas, Contacto):",
        min_value=3,
        max_value=15,
        value=6,
        step=1,
    )
    costo_secciones = secciones * 10
    precio_total += costo_secciones
    detalles.append(
        f"- Tipo: One Page ({secciones} secciones a $10 c/u): ${costo_secciones} USD"
    )

elif tipo_web in ["Landing Page", "Página de ventas"]:
    tarifa = 20
    secciones = st.number_input(
        f"Número de secciones de la {tipo_web}:",
        min_value=3,
        max_value=20,
        value=6,
        step=1,
    )
    costo_secciones = secciones * tarifa
    precio_total += costo_secciones
    detalles.append(
        f"- Tipo: {tipo_web} ({secciones} secciones a ${tarifa} c/u): ${costo_secciones} USD"
    )

elif tipo_web == "Tienda online (E-commerce)":
    secciones = st.number_input(
        "Número de secciones de diseño (Home, Catálogo, etc.):",
        min_value=4,
        max_value=25,
        value=10,
        step=1,
    )
    costo_secciones = secciones * 10
    precio_total += costo_secciones
    detalles.append(
        f"- Diseño: {secciones} secciones a $10 c/u: ${costo_secciones} USD"
    )

    base_woo = 200
    precio_total += base_woo
    detalles.append(
        f"- Configuración WooCommerce + Pasarelas de pago: ${base_woo} USD"
    )

    productos = st.number_input(
        "Cantidad de productos a cargar inicialmente ($3 USD c/u):",
        min_value=0,
        max_value=200,
        value=10,
        step=1,
    )
    if productos > 0:
        costo_prod = productos * 3
        precio_total += costo_prod
        detalles.append(
            f"- Carga de {productos} productos ($3 c/u): ${costo_prod} USD"
        )

elif tipo_web == "Embudo de ventas (Funnel de conversión)":
    secciones = st.number_input(
        "Número total de secciones a diseñar:",
        min_value=4,
        max_value=25,
        value=8,
        step=1,
    )
    costo_secciones = secciones * 20
    precio_total += costo_secciones
    detalles.append(
        f"- Diseño: {secciones} secciones a $20 c/u: ${costo_secciones} USD"
    )

    base_funnel = 200
    precio_total += base_funnel
    detalles.append(
        f"- Integración WooCommerce + CartFlows: ${base_funnel} USD"
    )

elif tipo_web == "Embudo de leads (Captación de prospectos)":
    st.info(
        "Estructura estándar recomendada: Landing Page + Thank You Page (TYP) + Página de Reserva de Cita."
    )
    secciones = st.number_input(
        "Número total de secciones sumando las 3 páginas:",
        min_value=3,
        max_value=20,
        value=6,
        step=1,
    )
    costo_secciones = secciones * 20
    precio_total += costo_secciones
    detalles.append(
        f"- Estructura de Captación ({secciones} secciones a $20 c/u): ${costo_secciones} USD"
    )

# 3. Muestra del resultado
st.markdown(
    f"""
    <div class='price-card'>
        <div style='color: #475569; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;'>Inversión Estimada</div>
        <div class='price-amount'>${precio_total:,.2f} USD</div>
    </div>
""",
    unsafe_allow_html=True,
)

st.subheader("📋 Resumen de la cotización:")
for item in detalles:
    st.write(item)

# 4. Botón para enviar por WhatsApp
st.markdown("---")
st.write("¿Te gustaría formalizar esta propuesta o coordinar detalles?")

texto_whatsapp = f"Hola, coticé en tu página web un proyecto:\n\n"
texto_whatsapp += f"*Proyecto:* {tipo_web}\n"
for item in detalles:
    texto_whatsapp += f"{item}\n"
texto_whatsapp += f"\n*Inversión estimada:* ${precio_total:,.2f} USD\n\n¿Podemos coordinar una llamada para ver los detalles?"

mensaje_codificado = urllib.parse.quote(texto_whatsapp)
url_whatsapp = (
    f"https://api.whatsapp.com/send?phone={TU_NUMERO_WHATSAPP}&text={mensaje_codificado}"
)

st.link_button(
    "📲 Enviar esta cotización por WhatsApp",
    url_whatsapp,
    type="primary",
    use_container_width=True,
)

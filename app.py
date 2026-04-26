import streamlit as st
import time

# ============================================================
#  CONFIGURACIÓN DE LA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Feliz cumpleaños, amor mío",
    page_icon="💖",
    layout="centered",
)

# ============================================================
#  CÓDIGOS DE DESBLOQUEO  ← EDITA AQUÍ TUS CONTRASEÑAS
# ============================================================
CODIGOS = {
    1: "Aprender a amar",      # Respuesta del paso 1
    2: "28sep",           # Respuesta del paso 2  (ej: fecha del primer beso)
    3: "La negra tomasa",         # Respuesta del paso 3
    4: "Guatape",      # Respuesta del paso 4
}

# ============================================================
#  ESTILOS CSS PERSONALIZADOS
# ============================================================
st.markdown("""
<style>
/* ── Importar fuentes elegantes ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400&display=swap');

/* ── Fondo general ── */
.stApp {
    background: linear-gradient(135deg, #fff0f3 0%, #ffe4e8 40%, #ffd6dc 100%);
    font-family: 'Lato', sans-serif;
}

/* ── Ocultar elementos de Streamlit ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Títulos principales ── */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #8b2252 !important;
}

/* ── Caja de contenido romántica ── */
.carta {
    background: rgba(255, 255, 255, 0.75);
    border: 1.5px solid #f4a7b9;
    border-radius: 20px;
    padding: 2rem 2.5rem;
    box-shadow: 0 8px 32px rgba(180, 50, 100, 0.12);
    backdrop-filter: blur(6px);
    margin: 1rem 0;
}

/* ── Separador decorativo ── */
.separador {
    text-align: center;
    color: #e07a9e;
    font-size: 1.4rem;
    letter-spacing: 8px;
    margin: 1.2rem 0;
    opacity: 0.7;
}

/* ── Texto de pista ── */
.pista {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.15rem;
    color: #6d2b4e;
    line-height: 1.8;
    text-align: center;
}

/* ── Número de paso ── */
.paso-badge {
    display: inline-block;
    background: linear-gradient(135deg, #e8537a, #c0395e);
    color: white;
    border-radius: 50%;
    width: 42px;
    height: 42px;
    line-height: 42px;
    text-align: center;
    font-weight: bold;
    font-size: 1.1rem;
    margin-right: 8px;
    box-shadow: 0 4px 12px rgba(192, 57, 94, 0.35);
}

/* ── Input de texto ── */
.stTextInput > div > div > input {
    border: 2px solid #f4a7b9 !important;
    border-radius: 12px !important;
    background: rgba(255,255,255,0.9) !important;
    color: #8b2252 !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1rem !important;
    text-align: center;
    padding: 0.6rem 1rem !important;
    transition: border-color 0.3s ease;
}
.stTextInput > div > div > input:focus {
    border-color: #e8537a !important;
    box-shadow: 0 0 0 3px rgba(232, 83, 122, 0.15) !important;
}

/* ── Botones ── */
.stButton > button {
    background: linear-gradient(135deg, #e8537a, #c0395e) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.65rem 2.5rem !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.5px;
    box-shadow: 0 6px 20px rgba(192, 57, 94, 0.35) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    cursor: pointer;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(192, 57, 94, 0.45) !important;
}

/* ── Mensaje de error ── */
.error-msg {
    background: rgba(255, 200, 210, 0.6);
    border-left: 4px solid #e8537a;
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    color: #8b2252;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    text-align: center;
    margin-top: 0.5rem;
}

/* ── Mensaje de éxito ── */
.exito-msg {
    background: rgba(255, 230, 235, 0.8);
    border-left: 4px solid #e8537a;
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    color: #6d2b4e;
    font-family: 'Playfair Display', serif;
    text-align: center;
    margin-top: 0.5rem;
}

/* ── Pantalla del tesoro ── */
.tesoro-titulo {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: #8b2252;
    text-align: center;
    line-height: 1.3;
}

.tesoro-cuerpo {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.15rem;
    color: #6d2b4e;
    line-height: 1.9;
    text-align: center;
}

/* ── Barra de progreso ── */
.progreso-texto {
    text-align: right;
    font-size: 0.8rem;
    color: #c0395e;
    font-family: 'Lato', sans-serif;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
#  INICIALIZAR SESSION STATE
# ============================================================
if "paso" not in st.session_state:
    st.session_state.paso = 0          # 0 = pantalla de inicio
if "error" not in st.session_state:
    st.session_state.error = False
if "exito_temporal" not in st.session_state:
    st.session_state.exito_temporal = False


# ============================================================
#  HELPERS
# ============================================================
def separador():
    st.markdown('<div class="separador">✦ ✦ ✦</div>', unsafe_allow_html=True)

def carta_inicio(contenido_html):
    st.markdown(f'<div class="carta">{contenido_html}</div>', unsafe_allow_html=True)

def validar_codigo(respuesta, paso):
    """Verifica si la respuesta coincide con el código del paso (sin importar mayúsculas)."""
    return respuesta.strip().lower() == str(CODIGOS[paso]).strip().lower()

def barra_progreso(paso_actual):
    total = 4
    porcentaje = int((paso_actual / total) * 100)
    st.markdown(f'<div class="progreso-texto">Paso {paso_actual} de {total} — {porcentaje}% completado 💌</div>', unsafe_allow_html=True)
    st.progress(paso_actual / total)


# ============================================================
#  PANTALLA 0 — INICIO
# ============================================================
def pantalla_inicio():
    st.markdown("<br>", unsafe_allow_html=True)

    carta_inicio("""
    <p style="text-align:center; font-size:3.5rem; margin-bottom:0.3rem;">💌</p>
    <h1 style="text-align:center; font-size:2rem; color:#8b2252; font-family:'Playfair Display',serif;">
        Una pequeña aventura<br><em>solo para ti</em>
    </h1>
    """)

    separador()

    # ── EDITA AQUÍ el mensaje de bienvenida ──
    st.markdown("""
    <div class="carta pista">
        Hola, mi amor...<br><br>
        He preparado esta búsqueda del tesoro para ti.
        Cada pista te llevará un paso más cerca de mí,
        de tu regalo y de algo que llevas tiempo esperando. 🌹<br><br>
        ¿Estás listo para descubrirlo?
    </div>
    """, unsafe_allow_html=True)

    separador()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Comenzar la aventura 💖"):
            st.session_state.paso = 1
            st.rerun()


# ============================================================
#  PANTALLA PASO 1
# ============================================================
def paso_1():
    barra_progreso(1)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<span class="paso-badge">1</span> **Primera Pista**', unsafe_allow_html=True)
    separador()

    # ── EDITA AQUÍ el mensaje del paso 1 ──
    st.markdown("""
    <div class="carta pista">
        Mi amor por ti empezó sin darme cuenta, sin avisar<br><br>
        Mi primer regalo para ti fue una sola palabra que prometí repetirte
        todos los días de mi vida...<br><br>
        <strong>Busca las cerezas</strong> 🌷
    </div>
    """, unsafe_allow_html=True)

    separador()

    # ── Pista adicional (opcional) ──
    with st.expander("¿Necesitas una pista? 🤫"):
        st.markdown("La has tocado para mí")  # EDITA AQUÍ

    respuesta = st.text_input("Escribe tu respuesta aquí:", key="input_1", placeholder="tu respuesta...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continuar ✨", key="btn_1"):
            if validar_codigo(respuesta, 1):
                st.session_state.error = False
                st.session_state.paso = 2
                st.rerun()
            else:
                st.session_state.error = True

    if st.session_state.error:
        st.markdown('<div class="error-msg"> En serio no te acuerdas???? Inténtalo de nuevo.</div>',
                    unsafe_allow_html=True)


# ============================================================
#  PANTALLA PASO 2
# ============================================================
def paso_2():
    barra_progreso(2)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<span class="paso-badge">2</span> **Segunda Pista**', unsafe_allow_html=True)
    separador()

    # ── EDITA AQUÍ el mensaje del paso 2 ──
    st.markdown("""
    <div class="carta pista">
        💫 Hay fechas que no se olvidan nunca...<br><br>
        El día en que todo cambió para mí fue aquel en que
        tus labios rozaron los míos por primera vez.<br><br>
        El mundo se detuvo, y yo solo quería que ese momento
        durara para siempre. ❤️<br><br>
        <strong>¿Quieres un dulcecito?</strong>
    </div>
    """, unsafe_allow_html=True)

    separador()

    with st.expander("¿Necesitas una pista? 🤫"):
        st.markdown("**")  # EDITA AQUÍ

    respuesta = st.text_input("Escribe tu respuesta aquí:", key="input_2", placeholder="número del día...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continuar ✨", key="btn_2"):
            if validar_codigo(respuesta, 2):
                st.session_state.error = False
                st.session_state.paso = 3
                st.rerun()
            else:
                st.session_state.error = True

    if st.session_state.error:
        st.markdown('<div class="error-msg">Mmm, no es ese... ¡Piensa bien! 💕</div>',
                    unsafe_allow_html=True)


# ============================================================
#  PANTALLA PASO 3
# ============================================================
def paso_3():
    barra_progreso(3)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<span class="paso-badge">3</span> **Tercera Pista**', unsafe_allow_html=True)
    separador()

    # ── EDITA AQUÍ el mensaje del paso 3 ──
    st.markdown("""
    <div class="carta pista">
        🌙 ¿Recuerdas esa noche que salimos a caminar sin rumbo?<br><br>
        Tú miraste al cielo y me dijiste que yo te recordaba a algo
        del universo... algo que brilla incluso en la oscuridad más profunda.<br><br>
        Ese fue uno de los momentos más bonitos que he vivido contigo. 🌟<br><br>
        <strong>¿A qué cosa del cielo te referiste esa noche?</strong>
    </div>
    """, unsafe_allow_html=True)

    separador()

    with st.expander("¿Necesitas una pista? 🤫"):
        st.markdown("*No es una estrella, ni el sol... es lo que nos ilumina las noches.*")  # EDITA AQUÍ

    respuesta = st.text_input("Escribe tu respuesta aquí:", key="input_3", placeholder="tu respuesta...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continuar ✨", key="btn_3"):
            if validar_codigo(respuesta, 3):
                st.session_state.error = False
                st.session_state.paso = 4
                st.rerun()
            else:
                st.session_state.error = True

    if st.session_state.error:
        st.markdown('<div class="error-msg">No es eso, cariño 💕 ¡Casi llegas!</div>',
                    unsafe_allow_html=True)


# ============================================================
#  PANTALLA PASO 4
# ============================================================
def paso_4():
    barra_progreso(4)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<span class="paso-badge">4</span> **Última Pista — Casi llegas...**', unsafe_allow_html=True)
    separador()

    # ── EDITA AQUÍ el mensaje del paso 4 ──
    st.markdown("""
    <div class="carta pista">
        🌹 Estás a un paso de descubrirlo todo, amor mío.<br><br>
        Si hay una palabra que describe cada aventura, cada abrazo,
        cada momento que hemos vivido juntos... esa palabra
        siempre empieza y termina con nosotros dos. 💞<br><br>
        No necesitas mapa cuando llevas esa palabra en el corazón.<br><br>
        <strong>¿Cuál es la palabra que completa esta frase?<br>
        "Solo quiero estar... ________ de ti."</strong>
    </div>
    """, unsafe_allow_html=True)

    separador()

    with st.expander("¿Necesitas una pista? 🤫"):
        st.markdown("*Empieza con 'con'... y termina donde tú estás ahora mismo.*")  # EDITA AQUÍ

    respuesta = st.text_input("Escribe tu respuesta aquí:", key="input_4", placeholder="tu respuesta...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("¡Descubrir el tesoro! 💎", key="btn_4"):
            if validar_codigo(respuesta, 4):
                st.session_state.error = False
                st.session_state.paso = 5
                st.rerun()
            else:
                st.session_state.error = True

    if st.session_state.error:
        st.markdown('<div class="error-msg">Tan cerca y tan lejos... ¡Vuelve a intentarlo! 💕</div>',
                    unsafe_allow_html=True)


# ============================================================
#  PANTALLA FINAL — EL TESORO
# ============================================================
def pantalla_tesoro():
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center; font-size:4rem; margin-bottom:0;">🎉</p>
    <div class="tesoro-titulo">¡Lo lograste, mi amor! 💖</div>
    """, unsafe_allow_html=True)

    separador()

    # ── EDITA AQUÍ el mensaje del tesoro final ──
    st.markdown("""
    <div class="carta tesoro-cuerpo">
        Desde el primer momento supe que contigo quería vivir
        cada aventura de esta vida.<br><br>
        Y hoy quiero regalarte una de verdad...<br><br>
        🗺️ <strong>Nos vamos de viaje.</strong><br><br>
        He reservado un fin de semana para los dos en
        <em>✨ [NOMBRE DEL PUEBLITO — EDITA AQUÍ] ✨</em><br><br>
        Calles empedradas, cielos estrellados,
        desayunos lentos y tú de la mano. 🌿<br><br>
        Porque mereces todo lo bonito que existe,
        y yo quiero ser quien te lo dé. 💌<br><br>
        <strong>Te amo más de lo que las palabras pueden decir.</strong>
    </div>
    """, unsafe_allow_html=True)

    separador()

    # ── Detalles del viaje (edita a tu gusto) ──
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="carta" style="text-align:center; padding:1rem;">
            🗓️<br>
            <strong style="font-family:'Playfair Display',serif; color:#8b2252;">Fecha</strong><br>
            <span style="color:#6d2b4e; font-style:italic;">[Agrega la fecha aquí]</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="carta" style="text-align:center; padding:1rem;">
            📍<br>
            <strong style="font-family:'Playfair Display',serif; color:#8b2252;">Destino</strong><br>
            <span style="color:#6d2b4e; font-style:italic;">[Nombre del pueblito]</span>
        </div>
        """, unsafe_allow_html=True)

    separador()

    st.markdown("""
    <p style="text-align:center; font-size:2rem;">🌹 💕 🌹</p>
    <p style="text-align:center; font-family:'Playfair Display',serif;
       font-style:italic; color:#8b2252; font-size:1.1rem;">
        Con todo mi amor, para siempre tuya/tuyo.
    </p>
    """, unsafe_allow_html=True)  # EDITA AQUÍ la firma

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💌 Volver al inicio"):
            for key in ["paso", "error", "exito_temporal"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()


# ============================================================
#  ROUTER PRINCIPAL
# ============================================================
def main():
    # Reiniciar error al cambiar de paso (excepto al validar)
    if "paso" not in st.session_state:
        st.session_state.paso = 0

    paso = st.session_state.paso

    if paso == 0:
        pantalla_inicio()
    elif paso == 1:
        paso_1()
    elif paso == 2:
        paso_2()
    elif paso == 3:
        paso_3()
    elif paso == 4:
        paso_4()
    elif paso == 5:
        pantalla_tesoro()

    # Pie de página decorativo
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align:center; color:#e07a9e; font-size:0.8rem; opacity:0.6;">'
        'Hecho con 💖 solo para ti</p>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()

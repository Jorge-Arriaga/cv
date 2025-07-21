# Configuración inicial
import streamlit as st

st.set_page_config(page_title="Mi CV", layout="wide")

# --- Título principal ---
st.title("📄 Curriculum Vitae Jorge Arriaga")

# --- Layout en columnas ---
col1, col2 = st.columns([1, 3])

# Columna izquierda: Foto de perfil
with col1:
    st.image("fotocv.jpg", width=250)

# Columna derecha: Encabezado y Perfil
with col2:
    st.markdown("""
    ## **Jorge Arriaga**
    **Data Scientist Junior**  
    📧 Jorge.Arriaga.Diaz@gmail.com | 📞 +34 661 049 397 | [LinkedIn](https://www.linkedin.com/in/jorge-arriaga-d%C3%ADaz/)
    """)
    
    st.subheader("👤 Perfil")
    st.markdown("""
    En constante cambio y desarrollo personal y profesional, encuentro en cada “piedra” en el camino una oportunidad de crecimiento.
    
    Por eso he decidido un cambio de rumbo hacia una profesión con futuro que me apasiona.

    Habituado a trabajar en entornos dinámicos, encuentro en ellos una oportunidad de desarrollo personal y profesional. 

    Disfruto de superar expectativas, promoviendo un ambiente enérgico donde cada interacción se convierta en un momento especial.
    """)

# --- Habilidades ---
st.subheader("🛠️ Skills Profesionales")

st.markdown("""
**🧠 Técnicas y Analíticas**
- Entrenamiento de modelos de machine learning y deep learning  
- Programación básica en Python  
- Uso de bases de Big Data  
- Uso de herramientas CRM  

**🧩 Organizativas y de Gestión**
- Organización y gestión: múltiples reservas, flujo de clientes y optimización de recursos  
- Resolución de incidencias  

**💬 Interpersonales**
- Comunicación efectiva  
- Capacidad de adaptación y aprendizaje  
""")


# --- Educación ---
st.subheader("🎓 Educación y Formación Complementaria")

st.markdown("""
**Hack a Boss**  
*Programa de Data Science*  
📍 Bootcamp intensivo (256h)

**Altia Formación**  
*Experto en Marketing Digital*  
📍 Certificación Profesional (250h)

**Iprodeco**  
*Operativas de Comercio y Marketing Internacional*  
📍 Formación especializada (250h)

**Junta de Andalucía – CCOO**  
*Administración de Empresas*  
📍 Curso Profesional (800h)

**C.E.I.P. María Inmaculada**  
*Técnico Superior en Comercio Internacional y Marketing*  
📍 Formación Profesional (2400h)
""")



# --- Experiencia ---
st.subheader("📁 Recorrido Profesional por Sectores")

# --- RECEPCIÓN Y TURISMO ---
st.markdown("### 🏨 Recepción y Turismo")

st.markdown("""
**Hotel La Posada del Molino (2024)**  
- Recepción de clientes  
- Gestión de reservas  
- Atención personalizada

**Hammam Al-Andalus Córdoba (2023)**  
- Recepción y acompañamiento de clientes  
- Atención al visitante  
- Coordinación con diferentes áreas

**Arriadh Hostel (2019)**  
- Gestión de entradas y salidas  
- Comunicación con clientes internacionales  

**Amerita Group (2018 - 2019)**  
- Reservas y coordinación de experiencias  
- Atención al cliente
""")

# --- VENTAS Y COMERCIAL ---
st.markdown("### 💼 Ventas y Comercial")

st.markdown("""
**Laboratorio Cosmético Europeo (2021 - 2022)**  
- Key Account Manager  
- Marketing y ventas  
- Gestión de cuentas mayoristas

**Comprastock - Grupo MGI (2021)**  
- Comercial y ampliación de cartera de clientes  
- Venta a proveedores mayoristas  

**Andalus Gourmet - Global Village, Dubái (2013 - 2014)**  
- Comercial en feria internacional  
- Asesoramiento y captación de nuevos clientes  
- Representación en eventos internacionales

**Mediamarkt (2013)**  
- Vendedor – atención al cliente  
- Asesoramiento técnico

**HC Córdoba (2012)**  
- Venta de software y videojuegos  
- Atención al cliente

**Estampaciones Casado (2014 - 2015)**  
- Manager de rutas comerciales  
- Dirección de equipo  
- Contacto con administraciones públicas  
- Técnico comercial
""")

# --- PROTOCOLO Y ACCESOS ---
st.markdown("### 🛡️ Protocolo y Acceso")

st.markdown("""
**Protocolo en Patios de Córdoba (2018 - 2021)**  
- Controlador de accesos  
- Atención al visitante  
- Coordinación en eventos locales
""")

# --- HOSTELERÍA Y CAMARERO ---
st.markdown("### 🍽️ Hostelería y Camarero")

st.markdown("""
**Restabus (1998 - 2008)**  
- Camarero  
- Recepción y gestión de reservas  
- Cobro y facturación  
- Venta de experiencias  
- Satisfacción del cliente  
- Comunicación interna
""")

# --- Otros Datos de Interés ---
st.subheader("📚 Otros Datos de Interés")
st.markdown("""
- 📖 **Autor publicado**: He escrito y publicado un libro "Córdoba, ciudad de leyenda", con la editorial Talón de Aquiles. Aportando una visión personal y creativa que refleja mis valores y mi capacidad comunicativa.
- 🏛️ **Secretario de asociación cultural**: Formo parte activa como secretario en la asociación cultural "Córdoba sólo hay una", coordinando actividades, comunicación y gestión administrativa.
- 🎗️ **Colaborador con la Asociación Española contra el Cáncer (AECC)**: He participado en acciones solidarias y eventos de concienciación, contribuyendo al impacto social de esta organización.
""")

# --- Descarga PDF  ---
with open("CV.pdf", "rb") as pdf_file:
     PDFbyte = pdf_file.read()
st.download_button(label="📥 Descargar CV en PDF", data=PDFbyte, file_name="CV.pdf", mime="application/pdf")

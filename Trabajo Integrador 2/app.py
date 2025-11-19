import streamlit as st
from PIL import Image
import numpy as np
import io
from gfpgan import GFPGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
import cv2
from transformers import pipeline

st.set_page_config(
    page_title="Mejora de Imágenes de Seguridad",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def cargar_gfpgan():
    gfpgan = GFPGANer(model_path='https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth', upscale=1, arch='clean', channel_multiplier=2)
    return gfpgan

@st.cache_resource
def cargar_realesrgan():
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
    upsampler = RealESRGANer(
        scale=4,
        model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth',
        model=model,
        tile=512,
        tile_pad=10,
        pre_pad=0,
        half=True
    )
    return upsampler

@st.cache_resource
def cargar_clip_classifier():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

@st.cache_resource
def cargar_detr_detector():
    return pipeline("object-detection", model="facebook/detr-resnet-50")

def reducir_ruido_imagen(imagen):
    img = np.array(imagen)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    denoised = cv2.cvtColor(denoised, cv2.COLOR_BGR2RGB)
    return Image.fromarray(denoised)

def restaurar_rostros(imagen, gfpgan):
    img_np = np.array(imagen)
    _, _, restored_img = gfpgan.enhance(img_np, has_aligned=False, only_center_face=False, paste_back=True)
    return Image.fromarray(restored_img)

def super_resolucion_general(imagen, upsampler):
    img = np.array(imagen)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    output, _ = upsampler.enhance(img, outscale=2)
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    return Image.fromarray(output)

def analizar_calidad_imagen(imagen, classifier):
    categorias = [
        "imagen de alta calidad",
        "imagen borrosa",
        "imagen con ruido",
        "imagen nítida y clara"
    ]
    resultado = classifier(imagen, candidate_labels=categorias)
    return resultado

def detectar_objetos(imagen, detector):
    resultados = detector(imagen)
    return resultados

st.title("🔍 Mejora de Imágenes para Cámaras de Seguridad")

st.markdown("""
<style>
    .main-header {color: #FF4B4B; font-size: 24px; font-weight: bold;}
    .sidebar .sidebar-content {background-color: #F0F2F6;}
</style>
""", unsafe_allow_html=True)

st.write("Sube una imagen para mejorarla y detectar mejor a los sospechosos.")

# Sidebar for options
with st.sidebar:
    st.header("Opciones de Procesamiento")
    apply_denoise = st.checkbox("Aplicar reducción de ruido", value=True)
    apply_faces = st.checkbox("Aplicar restauración de rostros", value=True)
    apply_sr = st.checkbox("Aplicar super-resolución", value=True)

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen Subida', use_container_width=True)

    progress = st.progress(0)
    status = st.empty()

    status.text("Cargando modelos...")
    try:
        # Cargar modelos según opciones
        gfpgan_model = cargar_gfpgan() if apply_faces else None
        realesrgan_model = cargar_realesrgan() if apply_sr else None
        progress.progress(10)
    except Exception as e:
        st.error(f"Error al cargar modelos: {e}")
        st.stop()

    status.text("Procesando...")

    # Aplicar pipeline de procesamiento
    processed_image = image.copy()
    step = 10

    # 1. Reducir ruido
    if apply_denoise:
        status.text("Reduciendo ruido...")
        processed_image = reducir_ruido_imagen(processed_image)
        step += 30
        progress.progress(step)

    # 2. Restauración de rostros
    if apply_faces:
        status.text("Restaurando rostros...")
        processed_image = restaurar_rostros(processed_image, gfpgan_model)
        step += 30
        progress.progress(step)

    # 3. Super-resolución general
    if apply_sr:
        status.text("Aplicando super-resolución...")
        processed_image = super_resolucion_general(processed_image, realesrgan_model)
        step += 30
        progress.progress(step)

    progress.progress(100)
    status.text("Procesamiento completado.")

    # Mostrar resultados lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original")
        st.image(image, use_container_width=True)
    with col2:
        st.header("Mejorada")
        st.image(processed_image, use_container_width=True)

    # Botón de descarga
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    buf.seek(0)
    st.download_button(
        label="Descargar imagen procesada",
        data=buf,
        file_name="imagen_mejorada.png",
        mime="image/png"
    )

    st.subheader("Análisis de la Imagen Procesada")
    # Load analysis models
    clip_model = cargar_clip_classifier()
    detr_model = cargar_detr_detector()

    # Analyze quality
    calidad = analizar_calidad_imagen(processed_image, clip_model)
    st.write("**Clasificación de Calidad:**")
    for item in calidad:
        st.write(f"- {item['label']}: {item['score']:.2f}")

    # Detect objects
    objetos = detectar_objetos(processed_image, detr_model)
    st.write("**Objetos Detectados:**")
    if objetos:
        for obj in objetos:
            st.write(f"- {obj['label']} (confianza: {obj['score']:.2f})")
    else:
        st.write("No se detectaron objetos.")

    st.subheader("Información sobre los modelos")
    st.write("""
    - **Reducción de ruido**: Usa OpenCV para eliminar ruido de la imagen.
    - **Restauración de rostros**: Emplea GFPGAN para mejorar la calidad de los rostros detectados.
    - **Super-resolución**: Aplica Real-ESRGAN para aumentar la resolución de la imagen en 2x.
    - **Análisis de calidad**: Utiliza CLIP para clasificar la calidad de la imagen procesada.
    - **Detección de objetos**: Emplea DETR para identificar objetos en la imagen mejorada.
    """)
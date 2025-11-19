
# Mejora de Imágenes para Cámaras de Seguridad

Esta aplicación web permite mejorar imágenes de cámaras de seguridad para una mejor detección de sospechosos. Utiliza modelos de IA avanzados para reducir ruido, restaurar rostros y aumentar la resolución.

## Características

- **Subida de imágenes**: Soporta formatos JPG, JPEG y PNG.
- **Procesamiento configurable**: Opciones para aplicar reducción de ruido, restauración de rostros y super-resolución.
- **Modelos utilizados**:
  - OpenCV para reducción de ruido.
  - GFPGAN para restauración de rostros.
  - Real-ESRGAN para super-resolución (2x).
- **Interfaz intuitiva**: Barra lateral para opciones, barra de progreso y comparación lado a lado.
- **Descarga**: Permite descargar la imagen procesada.

## Cómo ejecutar localmente

1. Clona este repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la app: `streamlit run app.py`

## Despliegue en Hugging Face Spaces

La app está configurada para desplegarse en Hugging Face Spaces. Sube los archivos `app.py` y `requirements.txt` a un Space con SDK Streamlit.

## Requisitos

- Python 3.10+
- GPU recomendada para mejor rendimiento (soporta CPU).

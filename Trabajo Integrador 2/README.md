
# Mejora de Imágenes para Cámaras de Seguridad

CamRestore es una aplicación enfocada en la mejora de imágenes provenientes de cámaras de seguridad, utilizando técnicas de visión por computadora y modelos de IA para recuperar detalles, mejorar rostros y aumentar la resolución.

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



📌 CamRestore – Mejora de Imágenes para Cámaras de Seguridad

Licencia: MIT









🎯 Objetivo del Proyecto

Problema: Las imágenes de cámaras de seguridad suelen tener ruido, baja resolución y rostros degradados, lo que complica la identificación.
Solución: Este sistema genera una imagen mejorada, de mayor resolución y rostros restaurados, combinando técnicas modernas de restauración y super-resolución.

🧠 Características Principales

✔ Subida de imágenes (JPG, JPEG, PNG)

✔ Reducción de ruido con OpenCV

✔ Restauración facial con GFPGAN

✔ Super-resolución 2× con Real-ESRGAN

✔ Pipeline configurable paso por paso

✔ Vista comparativa “Original → Mejorada”

✔ Descarga de la imagen final

✔ Carga de modelos desde URLs (sin archivos pesados en repo)

🏗️ Arquitectura del Sistema (Diagrama Simple)
                  ┌──────────────────┐
                  │     Imagen       │
                  │     Entrada      │
                  └────────┬─────────┘
                           │
             ┌─────────────┼────────────────┐
             │             │                │
             ▼             ▼                ▼
     Reducción de     Restauración       Super-
          Ruido         de Rostros      Resolución
      (OpenCV)          (GFPGAN)        (RealESRGAN)
             └─────────────┼────────────────┘
                           ▼
                  ┌──────────────────┐
                  │    Imagen        │
                  │   Mejorada       │
                  └──────────────────┘

💻 Tecnologías Utilizadas (Stack)

Python

Streamlit – interfaz web

OpenCV – reducción de ruido

GFPGAN – restauración facial

Real-ESRGAN / RRDBNet – super-resolución

NumPy / Pillow – procesamiento de imágenes

Torch – backend para modelos

🧩 Instalación
1. Clonar repositorio
git clone https://github.com/tu-usuario/camrestore.git
cd camrestore

2. Crear entorno virtual
python -m venv venv

3. Activar entorno

Windows PowerShell

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

4. Instalar dependencias
pip install -r requirements.txt

▶️ Ejecución
python -m streamlit run app.py


Streamlit abrirá la aplicación en tu navegador.

🧪 Métricas / Resultados Clave

Aunque no es un modelo entrenado por nosotros, el pipeline ofrece:

🔹 Recuperación facial estable con GFPGAN 1.4

🔹 Aumento de resolución efectivo con Real-ESRGAN x4

🔹 Mejoras visuales perceptibles incluso en imágenes muy ruidosas

🔹 Pipeline configurable según la necesidad del usuario

📸 Capturas del Sistema

(Coloca aquí tus imágenes. Ejemplo:)

📁 assets/
   ├── interfaz_1.png
   ├── interfaz_2.png
   ├── comparacion.png


En README:

🏛️ Estructura del Proyecto
camrestore/
│
├── app.py                # Aplicación Streamlit
├── requirements.txt      # Dependencias
├── README.md             # Documentación
└── assets/               # Imágenes y diagramas (opcional)

🧠 Modelos Utilizados
GFPGAN (Restauración Facial)

Versión: 1.4

Descarga directa desde TencentARC

Real-ESRGAN (Super-Resolución)

Modelo: RealESRGAN_x4plus

Arquitectura: RRDBNet

OpenCV

Método: FastNlMeansDenoisingColored

⚠️ Limitaciones del Sistema

❗ No mejora automáticamente imágenes extremadamente borrosas o quemadas

❗ La restauración facial puede generar ligeras variaciones estilizadas

❗ El desempeño depende de GPU/CPU disponible

❗ GFPGAN y Real-ESRGAN se descargan desde Internet la primera vez (puede demorar)

🌐 Despliegue en Hugging Face Spaces
1. Crear Space (tipo Streamlit)
2. Subir:

app.py

requirements.txt

README.md

carpeta assets/ (opcional)

Hugging Face instalará todo automáticamente.

Enlace del Space:
👉https://huggingface.co/spaces/KatherineML/CamRestore




👥 Autora

Proyecto desarrollado por:
Katherine S.


📜 Licencia MIT
MIT License

Copyright (c) 2025 [KATHERINE,S]

...

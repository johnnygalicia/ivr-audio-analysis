# IVR Audio Analysis Pipeline

Pipeline en Python para analizar grabaciones telefónicas (IVR), detectar calidad de audio, segmentar contenido útil y generar métricas operativas para análisis.

Este sistema permite identificar audios vacíos, silencios prolongados y grabaciones sospechosas mediante análisis de señal y reglas heurísticas.

---

## Problema

En sistemas IVR, grandes volúmenes de grabaciones contienen silencios, audios corruptos o de baja calidad, lo que dificulta el monitoreo y análisis operativo.

Este proyecto automatiza la evaluación de calidad de audio y la extracción de métricas relevantes para facilitar el análisis.

---

## Funcionalidad

- Procesamiento batch de audios
- Detección de duración total
- Segmentación en frases mediante detección de silencio
- Cálculo de audio útil vs total
- Extracción de features de señal (RMS, variabilidad)
- Clasificación de audios en:
  - `silencio_real`
  - `vacio`
  - `ivr_limpio`
  - `sospechoso`
  - `gris`
- Generación de resultados en CSV
- Análisis exploratorio en Excel (dashboard)

---

## Pipeline

Audio → Segmentación → Extracción de features → Clasificación → CSV → Dashboard

---

## Resultados

Se incluye un archivo Excel con:

- Métricas agregadas por clase
- Distribución de audios
- Promedios de audio útil
- Análisis de RMS
- Tablas dinámicas y visualizaciones

---

## Tecnologías

- Python
- Librosa
- Pandas
- NumPy

---

## Ejecución

```bash
pip install -r requirements.txt
python main.py

# Nota sobre datos 
Se incluyen solo algunos audios de ejemplo. 
El dataset completo no se incluye por tamaño. 

# Próxios pasos 
- Implementación de modelos de clasificación (ML) 
- Optimización del pipeline con paralelización (CUDA) 
- Mejora en extracción de features
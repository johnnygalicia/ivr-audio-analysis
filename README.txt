# IVR Audio Analysis Pipeline

Pipeline desarrollado en Python para el análisis automático de grabaciones telefónicas (IVR), enfocado en la evaluación de calidad de audio, detección de silencios y extracción de métricas operativas.

El sistema permite identificar grabaciones vacías, silencios prolongados y audios potencialmente problemáticos mediante técnicas de procesamiento digital de señales y análisis de características acústicas.

---

## Descripción del problema

Los sistemas IVR generan grandes volúmenes de grabaciones que frecuentemente contienen silencios extensos, audios incompletos o problemas de calidad. La revisión manual de estos archivos resulta costosa y poco escalable.

Este proyecto automatiza la evaluación de las grabaciones, proporcionando métricas objetivas que facilitan el monitoreo operativo y el análisis posterior de los datos.

---

## Funcionalidades

* Procesamiento batch de múltiples archivos de audio.
* Detección de duración total de las grabaciones.
* Segmentación automática mediante detección de silencios.
* Cálculo de tiempo útil de audio.
* Extracción de características acústicas.
* Análisis de energía RMS.
* Medición de variabilidad de señal.
* Clasificación automática de grabaciones.
* Generación de reportes en formato CSV.
* Exportación de resultados para análisis exploratorio en Excel.

---

## Categorías de clasificación

Las grabaciones son clasificadas en las siguientes categorías:

| Categoría     | Descripción                                        |
| ------------- | -------------------------------------------------- |
| silencio_real | Grabaciones compuestas principalmente por silencio |
| vacio         | Audio prácticamente inexistente o inválido         |
| ivr_limpio    | Grabación con contenido útil y calidad adecuada    |
| sospechoso    | Posibles anomalías o comportamientos atípicos      |
| gris          | Casos intermedios que requieren revisión           |

---

## Flujo de procesamiento

```text
Audio
  ↓
Preprocesamiento
  ↓
Detección de silencios
  ↓
Segmentación
  ↓
Extracción de características
  ↓
Clasificación heurística
  ↓
Generación de reportes
  ↓
CSV / Dashboard Excel
```

---

## Estructura del proyecto

```text
ivr-audio-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── reporte_audio.csv
│   └── reporte_audio.xlsx
│
├── pipeline/
│   └── batch_processing.py
│
├── src/
│   ├── processing.py
│   ├── segmentation.py
│   └── features.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Tecnologías utilizadas

* Python
* NumPy
* Pandas
* Librosa
* OpenPyXL

---

## Instalación

```bash
pip install -r requirements.txt
```

---

## Ejecución

```bash
python main.py
```

---

## Resultados

El sistema genera reportes estructurados que incluyen:

* Clasificación de grabaciones.
* Métricas de duración total.
* Porcentaje de audio útil.
* Estadísticas de energía RMS.
* Resúmenes agregados para análisis operativo.

Además, se exporta un archivo Excel que permite realizar análisis exploratorios, tablas dinámicas y visualizaciones.

---

## Habilidades demostradas

Este proyecto demuestra experiencia en:

* Procesamiento digital de señales.
* Análisis de audio en Python.
* Extracción de características acústicas.
* Automatización de procesos de análisis.
* Manipulación y análisis de datos con Pandas.
* Generación automática de reportes.
* Diseño modular de software científico.

---

## Nota sobre los datos

Por razones de tamaño y privacidad, el conjunto completo de grabaciones no se incluye en este repositorio.

Se proporcionan únicamente ejemplos representativos para demostrar el funcionamiento del pipeline.

---

## Próximos pasos

* Incorporar modelos de Machine Learning para clasificación automática.
* Paralelización del procesamiento utilizando CUDA o multiprocessing.
* Incorporar nuevas características acústicas.
* Implementar métricas avanzadas de calidad de audio.
* Generar dashboards interactivos para monitoreo operativo.

---

## Autor

Johnny Michael Galicia Orihuela


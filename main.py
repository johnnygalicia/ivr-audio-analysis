import os
from pipeline.batch_processing import run_batch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIO_DIR = os.path.join(BASE_DIR, "data", "raw")
OUTPUT_CSV = os.path.join(BASE_DIR, "outputs", "reporte_audio.csv")

def main():
    run_batch(AUDIO_DIR, OUTPUT_CSV)

if __name__ == "__main__":
    main()
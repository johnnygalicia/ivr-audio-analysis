import os
import pandas as pd
from src.processing import process_audio

def run_batch(audio_dir, output_csv):
    resultados = []

    for file in sorted(os.listdir(audio_dir)):
        if file.endswith((".wav", ".mp3", ".oga")):
            path = os.path.join(audio_dir, file)
            print(f"Procesando: {file}")

            res = process_audio(path)
            if res:
                resultados.append(res)

    df = pd.DataFrame(resultados)
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)

    print("\nProceso terminado")
    print(f"CSV guardado en: {output_csv}")
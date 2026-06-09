import librosa
import os

from src.segmentation import merge_segments
from src.features import volume_variation

SR = 16000
MIN_SILENCE = 0.7

def process_audio(file_path):
    try:
        y, sr = librosa.load(file_path, sr=SR, mono=True)
        duration = librosa.get_duration(y=y, sr=sr)

        segments = librosa.effects.split(y, top_db=35)
        merged = merge_segments(segments, sr, MIN_SILENCE)

        audio_util = sum((end - start) for start, end in merged) / sr
        porcentaje_audio = (audio_util / duration) * 100 if duration > 0 else 0
        num_frases = len(merged)

        if porcentaje_audio > 20 and num_frases >= 1:
            mean, std, dyn = volume_variation(y)
        else:
            mean, std, dyn = 0, 0, 0

        return {
            "archivo": os.path.basename(file_path),
            "duracion_total": duration,
            "audio_util": audio_util,
            "porcentaje_audio": porcentaje_audio,
            "num_frases": num_frases,
            "rms_mean": mean,
            "rms_std": std,
            "rango_dinamico": dyn
        }

    except Exception as e:
        print(f"Error procesando {file_path}: {e}")
        return None
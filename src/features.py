import librosa
import numpy as np

THRESHOLD = 0.05

def volume_variation(y):
    rms = librosa.feature.rms(y=y)[0]
    rms = rms[rms > THRESHOLD]

    if len(rms) == 0:
        return 0, 0, 0

    mean = np.mean(rms)
    std = np.std(rms)
    dynamic_range = np.max(rms) - np.min(rms)

    return mean, std, dynamic_range
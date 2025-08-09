# speak.py
import torch
import os
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig
from TTS.tts.models.xtts import XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig


torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    BaseDatasetConfig,
    XttsArgs
])



# Optional: fallback to CPU if GPU is unavailable
use_gpu = torch.cuda.is_available()

# Load XTTS-v2 model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=use_gpu)

# Confirm output path
output_path = "output.wav"

# Generate speech
tts.tts_to_file(
    text="This is a test of XTTS voice cloning. Let's see how it sounds.",
    file_path=output_path,
    speaker_wav="/data/TTS-public/_refclips/3.wav",  # Coqui's sample clip
    language="en"
)

# Play the audio if it was created
if os.path.exists(output_path):
    os.system(f"aplay {output_path}")
else:
    print("❌ output.wav was not created. Check for errors above.")

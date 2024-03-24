from pydub import pydub.AudioSegment
from pydub.playback import play

play(AudioSegment.from_file(file = "speech.wav", format = "wav"))
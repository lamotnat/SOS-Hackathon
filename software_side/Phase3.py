import torch
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import pyaudio
import wave


def string_to_wav(text):
    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

    embeddings_dataset = load_dataset(
        "Matthijs/cmu-arctic-xvectors", split="validation"
    )
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    # You can replace this embedding with your own as well.

    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})

    sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])


def play_wav():
    # open the wav file
    wav_file = wave.open("speech.wav", 'rb')
    pyaudio_obj = pyaudio.PyAudio()

    # open stream based on wav file
    stream = pyaudio_obj.open(format =
                pyaudio_obj.get_format_from_width(wav_file.getsampwidth()),
                channels = wav_file.getnchannels(),
                rate = wav_file.getframerate(),
                output = True)

    # read the data (with restriction on size of input)
    audio = wav_file.readframes(1024)

    # play stream
    while audio:
        # writing to the stream is what *actually* plays the sound.
        stream.write(audio)
        audio = wav_file.readframes(1024)


    # cleanup stuff.
    wav_file.close()
    stream.close()    
    pyaudio_obj.terminate()
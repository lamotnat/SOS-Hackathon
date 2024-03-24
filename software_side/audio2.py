import pyaudio
import wave
import sys

# open the wav file
wav_file = wave.open(sys.argv[1], "speech.wav")
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
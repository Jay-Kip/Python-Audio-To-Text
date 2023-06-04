from gtts import gTTS
import playsound

text = "Enter your text to be converted to an audio file"
language = "en"  # Replace "en" with the appropriate language code

sp = gTTS(text=text, lang=language, slow=False)

audio_file = 'speech.mp3'
sp.save(audio_file)
playsound.playsound(audio_file)
import speech_recognition as sr
import pyttsx3


audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say('Olá, eu sou a Atena')
maquina.say('Como posso ajudar?')
maquina.runAndWait()

try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt_BR')
        comando = comando.lower()

        if 'atena' in comando:
            print(comando)

except:
    print('Microfone não está OK')
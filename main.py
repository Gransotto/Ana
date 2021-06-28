from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify
# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def evaluate(text):
    #Reconhecer entidade do texto. 
    entity = classify(text)
    if entity == 'time|getTime':
        speak(core.SystemInfo.get_time())
    elif entity == 'time|getDate':
        speak(core.SystemInfo.get_date())

    #Cumprimentos
    elif entity == 'greetings|anna':
        speak('Olá Vitor')

    elif entity == 'greetings|bomdia':
        speak('Bom Dia Vitor')

    elif entity == 'greetings|bomdia':
        speak('Bom Dia Vitor')

    elif entity == 'greetings|bomdia':
        speak('Bom Dia Vitor')

    elif entity == 'greetings|boatarde':
        speak('Boa Tarde Vitor')

    elif entity == 'greetings|boanoite':
        speak('Boa Noite Vitor')

    elif entity == 'greetings|tudobem':
        speak('Estou bem e você?')

    elif entity == 'greetings|ajuda':
        speak('Do que precisa Vitor?')

    elif entity == 'greetings|bomdia':
        speak('Bom Dia Vitor')

    elif entity == 'greetings|ajuda':
        speak('O que você precisa?')


    # Abrir programas
    elif entity == 'open|notepad':
        speak('Abrindo o bloco de notas')
        os.system('notepad.exe')
    elif entity == 'open|navegador':
        speak('Abrindo o Navegador')
        os.system('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge"')
    elif entity == 'open|lol':
        speak('Abrindo Liga das Lendas')
        os.system('"C:\Riot Games\Riot Client\RiotClientServices"')

    print('Text: {}  Entity: {}'.format(text, entity))

# Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            evaluate(text)

            
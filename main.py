import speech_recognition as sr
import pyttsx3
import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source)
            print('ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'assistente' in comando:
                comando = comando.replace('assistente', '').strip()
                maquina.runAndWait()
    except:
        print('Microfone não está ok')

    return comando


def comando_voz_usuario():
    comando = executa_comando()
    match comando:
        case 'que horas são' | 'que horas tem' | 'horas':
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say(f'Agora são {hora}')
            maquina.runAndWait()


comando_voz_usuario()

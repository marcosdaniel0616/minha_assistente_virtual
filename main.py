import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

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
        case 'que horas são' | 'que horas tem' | 'horas' | 'hora':
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say(f'Agora são {hora}')
            maquina.runAndWait()

        case wiki if 'o que é' in comando:
            print(comando)
            procurar = comando.replace('procure por', '').replace('pesquise por', '').strip()
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            maquina.say(resultado)
            maquina.runAndWait()

comando_voz_usuario()

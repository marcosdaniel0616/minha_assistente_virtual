import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import urllib.request
import re
import webbrowser
import os
import pyautogui
from time import sleep

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
                comando = comando.replace('assistente ', '').strip()
                maquina.runAndWait()
            else:
                executa_comando()
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
            procurar = comando.replace('procure por', '').replace('pesquise por', '').strip()
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            maquina.say(resultado)
            maquina.runAndWait()

        case ytb if 'tocar' in comando or 'toque' in comando:
            video = comando.replace('tocar ', '').replace('toque ', '').replace(' ', '+').strip()
            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query=" + video)
            video_escolhido = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            link_video = "https://www.youtube.com/watch?v=" + video_escolhido[0]
            webbrowser.open(str(link_video))
            maquina.say('Tocando musica')
            maquina.runAndWait()

        case programas if 'abrir' in comando or 'abra' in comando:
            programa = comando.replace('abrir ', '').replace('abra ', '').strip()
            try:
                os.startfile(programa)

            except:
                pyautogui.press('win')
                sleep(1)
                pyautogui.write(programa)
                sleep(1)
                pyautogui.press('enter')
            finally:
                maquina.say(f'abrindo {programa}')
                maquina.runAndWait()


comando_voz_usuario()

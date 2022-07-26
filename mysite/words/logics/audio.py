import gtts
import os
from playsound import playsound
import pygame

from mysite.settings import BASE_DIR


class Audio:
    @staticmethod
    def create_sound(text, file_name):
        
        sound_file = os.path.join(BASE_DIR, 'static', 'sounds', f'{file_name}')
        
        tts = gtts.gTTS(text)
        tts.save(sound_file)
        
    @staticmethod
    def play_audio(file_path):
        playsound(file_path)
        os.remove(file_path)

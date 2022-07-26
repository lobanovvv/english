import gtts
import os
import pygame

from mysite.settings import BASE_DIR


class Audio:
    @staticmethod
    def create_start_sound(text):
        
        sound_file = os.path.join(BASE_DIR, 'static', 'sounds', 'start_sound.mp3')
        if os.path.exists(sound_file):
            os.remove(sound_file)

        tts = gtts.gTTS(text)
        tts.save(sound_file)

    @staticmethod
    def create_answer_sound(text):
        
        sound_file = os.path.join(BASE_DIR, 'static', 'sounds', 'answer_sound.mp3')
        if os.path.exists(sound_file):
            os.remove(sound_file)

        tts = gtts.gTTS(text)
        tts.save(sound_file)

    @staticmethod
    def play_audio(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

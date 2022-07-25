import gtts
import os

from mysite.settings import STATIC_URL


class Audio:
    @staticmethod
    def create_start_sound(text):
        
        sound_file = os.path.join('static', 'sounds', 'start_sound.mp3')
        if os.path.exists(sound_file):
            os.remove(sound_file)

        tts = gtts.gTTS(text)
        tts.save(sound_file)

    @staticmethod
    def create_answer_sound(text):
        
        sound_file = os.path.join('static', 'sounds', 'answer_sound.mp3')
        if os.path.exists(sound_file):
            os.remove(sound_file)

        tts = gtts.gTTS(text)
        tts.save(sound_file)
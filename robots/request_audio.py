from ibm_watson import TextToSpeechV1
import requests
import json

class RobotAudio(object):

    def __init__(self):
        self.voice = 'pt-BR_IsabelaV3Voice'
        self.auth()
    
    def auth(self):
        self.text_to_speech = TextToSpeechV1(
            # credenciais
        )

    def request_audio(self, text):
        # get voices
        # 
        # choose voice
        # voice = self.text_to_speech.get_voice('en-US_AllisonVoice').get_result()
        # print(json.dumps(voice, indent=2))
        filename= "teste"
        with open('audios/{}.wav'.format(filename).lower(), 'wb') as audio_file:
            audio_file.write(
                self.text_to_speech.synthesize(
                    text,
                    voice=self.voice,
                    accept='audio/wav'        
                ).get_result().content
            )

    def __get_voices(self):
        voices = self.text_to_speech.list_voices().get_result()

    def set_voice(self, voice):
        self.voice = voice

from ibm_watson import TextToSpeechV1
import requests
import json

class RobotAudio(object):
    
    def auth(self):
        self.text_to_speech = TextToSpeechV1(
            # cREDENCIAIS
        )

    def request_audio(self, text):
        # get voices
        # voices = self.text_to_speech.list_voices().get_result()
        # choose voice
        # voice = self.text_to_speech.get_voice('en-US_AllisonVoice').get_result()
        # print(json.dumps(voice, indent=2))
        filename= "teste"
        with open('audios/{}.wav'.format(filename).lower(), 'wb') as audio_file:
            audio_file.write(
                self.text_to_speech.synthesize(
                    text,
                    voice='pt-BR_IsabelaV3Voice',
                    accept='audio/wav'        
                ).get_result().content)

text = '<p><s>O Zen do Paithon<break time="300ms"/>, por Tim Peters<break time="700ms"/><prosody rate="-15%">Bonito é melhor que feio.</prosody><break time="400ms"/><prosody rate="-15%">Explícito é melhor que implícito.</prosody><break time="400ms"/><prosody rate="-15%">Simples é melhor que complexo.</prosody><break time="400ms"/><prosody rate="-15%">Complexo é melhor que complicado.</prosody><break time="400ms"/><prosody rate="-15%">Linear é melhor do que aninhado.</prosody><break time="400ms"/><prosody rate="-15%">Esparso é melhor que denso.</prosody><break time="400ms"/><prosody rate="-15%">Legibilidade conta.</prosody><break time="400ms"/><prosody rate="-15%">Casos especiais não são especiais o bastante para quebrar as regras.</prosody><break time="400ms"/><prosody rate="-15%">Ainda que praticidade vença a pureza.</prosody><break time="400ms"/><prosody rate="-15%">Erros nunca devem passar silenciosamente.</prosody><break time="400ms"/><prosody rate="-15%">A menos que sejam explicitamente silenciados.</prosody><break time="400ms"/><prosody rate="-15%">Diante da ambigüidade, recuse a tentação de adivinhar.</prosody><break time="400ms"/><prosody rate="-15%">Deveria haver um — e preferencialmente só um — modo óbvio para fazer algo.</prosody><break time="400ms"/><prosody rate="-15%">Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.</prosody><break time="400ms"/><prosody rate="-15%">Agora é melhor que nunca.</prosody><break time="400ms"/><prosody rate="-15%">Embora nunca freqüentemente seja melhor que já.</prosody><break time="400ms"/><prosody rate="-15%">Se a implementação é difícil de explicar, é uma má idéia.</prosody><break time="400ms"/><prosody rate="-15%">Se a implementação é fácil de explicar, pode ser uma boa idéia.</prosody><break time="400ms"/><prosody rate="-15%">Namespaces são uma grande idéia — vamos ter mais dessas!</prosody><break time="400ms"/><prosody rate="+15%">São filosofias extremamente simples e que podem soar óbvias,<break time="600ms"/> não é?<break time="400ms"/></prosody>Mas porque será que mesmo parecendo tão óbvias, existimos em não aplicá-las? </s></p>'
robot = RobotAudio()
robot.auth()
robot.request_audio(text)
import speech_recognition as sr
from moviepy.editor import VideoFileClip,AudioFileClip,CompositeAudioClip
from deep_translator import GoogleTranslator
from gtts import gTTS

class MovieManager:
    def get_audio(self, mp4_file, mp3_file):
        vc=VideoFileClip(mp4_file)
        ac=vc.audio
        ac.write_audiofile(mp3_file)

        ac.close()
        vc.close()
 

    def remove_audio(self,mp4_file,output_mp4):
        video=VideoFileClip(mp4_file)
        video_wa=video.without_audio()
        video_wa=video.without_audio()

        video_wa.write_videofile(output_mp4)
        video_wa.close()
        video.close()


    def get_wav_audio(self, mp4_file, war_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(war_file, codec ='pcm_s16le')
        ac.close()
        vc.close()

    def audio_to_text(selef, audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
                audio = r.record(source)
        try:
            text = r.recognize_google(audio, language='es')
            return text
        except :
            return 'unknow'
    def text_to_speech(self, to_translate, to_lang):
         translated = GoogleTranslator(source='auto',target=to_lang).translate(to_translate)
         print(translated)
         myobj = gTTS(text=translated,lang=to_lang,slow=False)
         myobj.save("welcome.mp3")

    def add_audio_to_video(self,mp4_file, mp3_file, out_mp4):
         videoclip = VideoFileClip(mp4_file)
         audioclip =  AudioFileClip(mp3_file)

         new_audioclip = CompositeAudioClip([audioclip])
         videoclip.audio = new_audioclip
         videoclip.write_videofile(out_mp4)



mm=MovieManager()
#mm.get_wav_audio('video.mp4','audio.wav')
#speech = mm.audio_to_text('audio.wav')
#mm.text_to_speech(speech, 'ru')
mm.add_audio_to_video('video.mp4','welcome.mp3','out.mp4')



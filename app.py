import streamlit as st
from keyfinder import Tonal_Fragment
import librosa
import librosa.display
from tempofinder import get_audio_tempo
from pytube import YouTube

def main():
    st.title('Audio Analysis')
    audio_input = st.text_input('Enter your youtube URL: ')
    

    if st.button('Analyze'):
        audio_input = YouTube(audio_input).streams.filter(only_audio=True).first()
        audio_input = audio_input.download(type='mp3')
        print(type(audio_input))
        st.audio(audio_input)
        
        y, sr = librosa.load(audio_input)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        unebarque_fsharp_min = Tonal_Fragment(y_harmonic, sr, tend=22)
        st.write(f"Likely key : {unebarque_fsharp_min.get_key()}")
        st.write('Estimated tempo: {:.2f} BPM'.format(get_audio_tempo(y, sr)))
        
if __name__ == '__main__':
    main()
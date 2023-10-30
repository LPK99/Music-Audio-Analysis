import streamlit as st
from keyfinder import Tonal_Fragment
import librosa
import librosa.display
from tempofinder import get_audio_tempo

def main():
    st.title('Audio Analysis')
    audio_input = st.file_uploader('Upload your adio file', type=['mp3'])

    if st.button('Analyze'):
        y, sr = librosa.load(audio_input)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        unebarque_fsharp_min = Tonal_Fragment(y_harmonic, sr, tend=22)
        st.write(f"Likely key : {unebarque_fsharp_min.get_key()}")
        st.write('Estimated tempo: {:.2f} BPM'.format(get_audio_tempo(y, sr)))
        
if __name__ == '__main__':
    main()
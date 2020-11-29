# ASR
CELA ASR solutions based on Deepspeech

## Installation
1. Creat python env:
>conda create -n asr python=3.7 -y

2. Install deep-speech:
>CPU-version: pip install deepspeech  
>GPU-version: pip install deepspeech-gpu

3. Download pretrained weights:
>wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.pbmm   
>wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.scorer

4. Run audio solutions:
>cd audio_solution  
>pip install -r requirements.txt  
For linux:
>sudo apt install portaudio19-dev
For mac:
>brew install portaudio  
If you want to run the asr algorithm on the whole audio clip:
>python mic_vad_streaming.py -f wav_file_here.wav -m deepspeech-0.8.1-models.pbmm -s deepspeech-0.8.1-models.scorer 
If you want to run the asr algorithm in a real-time microphone scenario:  
>python mic_vad_streaming.py -m deepspeech-0.8.1-models.pbmm -s deepspeech-0.8.1-models.scorer 

5. Run video solutions:

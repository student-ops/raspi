cd ~/voicevox_core-0.11.4/
python configure.py --ort_download_link https://github.com/VOICEVOX/onnxruntime-builder/releases/download/1.10.0.1/onnxruntime-linux-armhf-cpu-v1.10.0.tgz
pip install -r requirements.txt
pip install .
cd ~/voicevox_core-0.11.4/example/python/
pip install -r requirements.txt
cd ~/voicevox_core-0.11.4/example/python/
python run.py --text "おはようございます" --speaker_id 2 --root_dir_path="../../release"
sudo apt-get install mpg123
play おはようございます*.wav
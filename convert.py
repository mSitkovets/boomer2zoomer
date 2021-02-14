import os

command = 'ffmpeg -i "{}" -ar 16000 "{}"'

dataset_folders = ["Joanna_audio_dataset", "jadas audio", "kevin recordings", "marias_audio", "pranish_audio"]

for folder in dataset_folders:
    files = os.listdir(folder)
    for file in files:
        fpath = os.path.join(folder, file)
        opath = os.path.join(folder, file.replace(".wav", ".convert.wav"))
        os.system(command.format(fpath, opath))

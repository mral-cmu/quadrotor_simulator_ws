import gdown
import subprocess

gdown.download_folder("https://drive.google.com/drive/folders/1_Iy63933LSDAFZdt9toEsdA12QsyX1QP?usp=share_link")
subprocess.run("mv visualizer/*.bag .", shell=True)
subprocess.run("rm -rf visualizer", shell=True)

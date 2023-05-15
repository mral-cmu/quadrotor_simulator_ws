import gdown
import subprocess

gdown.download_folder("https://drive.google.com/drive/folders/1Z_4PCS9AbYPXwGazaJsFN91lkNcaOomQ?usp=share_link")
subprocess.run("mv Course-Data/*.bag .", shell=True)
subprocess.run("rm -rf Course-Data", shell=True)

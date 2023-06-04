import gdown
import subprocess

gdown.download_folder("https://drive.google.com/drive/folders/1q9DC6vNKfAzpLt9kNWUfWlhJqEJmBpEE?usp=share_link")
subprocess.run("mv assignment1/*.bag .", shell=True)
subprocess.run("rm -rf assignment1", shell=True)

import zipfile
import os

with zipfile.ZipFile("new.zip", 'r') as zip_ref:
    zip_ref.extractall(".")  # Root folder এ unzip

os.system("python TcP-FrEinD.py")

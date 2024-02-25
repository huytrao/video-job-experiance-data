import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Cài đặt thư viện google-cloud-storage
install("google-cloud-storage")
install("streamlit")
install("google.oauth2")
install("google-cloud-texttospeech")
install("plotly.express")

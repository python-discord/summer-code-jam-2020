import os

os.system("sudo docker build -t spydirweb -f Dockerfile .")
os.system(f"sudo docker run -e {os.getenv('API_KEY')} -it -p 8000:8000 spydirweb")

import os

os.system(f"sudo docker build -t spydirweb -f Dockerfile .")
os.system(f"sudo docker run -e {os.getenv('API_KEY')} -it -p 80:8888 spydirweb")
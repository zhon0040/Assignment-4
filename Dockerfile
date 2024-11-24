#Dockerfile, Image, Container
FROM python:3.12

ADD zhon0040-assignment4.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./zhon0040-assignment4.py"]
FROM python:3
ADD . /deveops-assignment
WORKDIR /deveops-assignment
EXPOSE 8080
CMD ["python", "./calculator.py"]

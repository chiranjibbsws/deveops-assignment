FROM python:3
ADD . /deveops-assignment
WORKDIR /deveops-assignment
CMD ["python", "./calculator.py"]

FROM python:3
ADD . /deveops-assignment
WORKDIR /deveops-assignment
RUN pip install -r requirements.txt
CMD ["python", "./calculator.py"]

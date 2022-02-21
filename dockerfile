FROM python:3

WORKDIR https://github.com/chiranjibbsws/deveops-assignment/blob/master/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./calculator.py"]

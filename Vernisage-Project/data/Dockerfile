FROM python:3.12
WORKDIR /app

COPY data/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY data/sqldata.py .

EXPOSE 3307

CMD ["python", "sqldata.py"]


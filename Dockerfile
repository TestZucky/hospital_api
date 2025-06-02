FROM python:3.10
EXPOSE 5000
WORKDIR /hospital_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "run.py"]
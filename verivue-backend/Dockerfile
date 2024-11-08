# Flask Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip  # Update pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]


FROM python:3.11-slim
WORKDIR /app
COPY main.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "main.py"]

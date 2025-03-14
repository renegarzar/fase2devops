FROM python:3.9
WORKDIR /app
WORKDIR /app
COPY . .
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app/main.py"]

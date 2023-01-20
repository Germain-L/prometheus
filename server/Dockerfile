FROM python:bullseye

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install -r requirements.txt

CMD ["python3", "server.py"]
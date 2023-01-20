FROM python:bullseye

# Set the working directory to /app
WORKDIR /app

# Copy requirements file and code
COPY . .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Run the server
CMD ["python3", "server.py"]
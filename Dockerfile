FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY requirements.txt requirements.txt
COPY myapi.py myapi.py

# Install the required Python libraries
RUN pip install -r requirements.txt

# Run the Python script when the container starts
 CMD ["uvicorn", "myapi:app", "--host", "0.0.0.0", "--port", "80"]
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Run log_analyzer.py when the container launches
ENTRYPOINT ["python", "src/log_analyzer.py"]
CMD ["--help"]
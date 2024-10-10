# Use an official Python image as a base
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Flask and Scikit-learn
RUN pip install flask scikit-learn joblib

# Expose the app port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

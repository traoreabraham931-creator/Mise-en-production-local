
# Use an official Python runtime as a parent image

FROM python:3.13
 
# Set working directory
WORKDIR /app
 

 
# Copy requirements and install Python dependencies
COPY requirements.txt /app/

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

# Copy application code
COPY /app/ .
COPY /models/ .
 
# Expose port
EXPOSE 8000
 
# Run the application
CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000"]







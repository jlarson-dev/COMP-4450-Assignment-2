
# Parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./app

# Expose port 8501 for this container
EXPOSE 8501

# Command to run when the container starts
CMD ["streamlit", "run", "app.py"]
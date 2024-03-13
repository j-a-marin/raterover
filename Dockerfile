# Use a s# Use a specific Python base image
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry --upgrade
RUN poetry config virtualenvs.create false

# Set the working directory in the Docker container
WORKDIR /code

# Copy the poetry files for installing Python dependencies
COPY pyproject.toml poetry.lock* ./

# Copy your packages into the container
# Make sure to replace 'packages/rag-chroma' with the correct path to your 'rag-chroma' package
COPY ./packages/rag-chroma /code/packages/rag-chroma

# Install the dependencies using Poetry
RUN poetry install --no-interaction --no-ansi --no-root

# Additionally, if you have requirements.txt, copy it and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY ./app ./app

# Finish Poetry installation if there are any local packages
RUN poetry install --no-interaction --no-ansi

# Expose the ports that your applications use
EXPOSE 8000 5000 8080

# CMD should be overridden by docker-compose, so this can be a placeholder
CMD ["echo", "Use docker-compose to run the services"]

# FROM python:3.11-slim

# RUN pip install poetry==1.6.1

# RUN poetry config virtualenvs.create false

# WORKDIR /code

# COPY ./pyproject.toml ./README.md ./poetry.lock* ./

# COPY ./package[s] ./packages

# RUN poetry install  --no-interaction --no-ansi --no-root

# COPY ./app ./app

# RUN poetry install --no-interaction --no-ansi

# EXPOSE 8080

# CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8080

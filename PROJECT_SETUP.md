# Project Setup Instructions

Welcome! This guide will walk you through the steps required to get the QA app running on your local system. I've also streamlined deployment using Docker, and this setup includes running both a LangChain service and a Flask application.

Prerequisites
Before you begin, ensure you have the following installed on your system:

- Git
- Docker
- Docker Compose
- Cloning the Repository
- Open a terminal on your computer

Clone the repository using Git:
```bash
git clone https://github.com/j-a-marin/raterover.git
cd raterover
```

# Running the LangChain Service

To run the LangChain service on port 8000, follow these steps:

In the current terminal window, execute the following command to start the service:

```bash
langchain serve --port 8000
```

Leave this terminal window open to keep the LangChain service running.

# Running the Flask Frontend

To run the Flask frontend, you will need to open another terminal window:

Ensure you are in the project directory; if not, use cd to navigate back to it.

Execute the Flask application by running:

```bash
python ./app/frontend/frontend.py
```
This command starts the Flask server on port 5000, which interacts with the LangChain service running on port 8000.

# Streamlined Deployment with Docker

For ease of deployment, we have provided Dockerfile and docker-compose.yml files. These files are designed to containerize the application and its services, making the deployment process more efficient and less dependent on the host environment.

To deploy using Docker, follow these steps:

Ensure Docker and Docker Compose are installed and running on your system.

Build and start the containers with Docker Compose:

```bash
docker-compose up --build
```

This command builds the Docker containers based on the instructions in the Dockerfile and docker-compose.yml files and starts the services as defined. The LangChain service and the Flask frontend will be started automatically in their respective containers.

# Additional Information

For more details on Docker and Docker Compose, please refer to the official documentation.
If you encounter any issues during the setup, ensure all prerequisites are properly installed and configured.
# End-to-End ML Project Workflows

This document outlines the steps and workflows involved in the machine learning project, from configuration updates to deployment on AWS using GitHub Actions.

## Project Setup and Configuration Updates

- **Update Configuration Files**: Ensure that `config.yaml`, `schema.yaml`, and `params.yaml` are up-to-date with the latest project specifications.
- **Update the Entity**: Make necessary adjustments to the entity definitions as per project requirements.
- **Update Configuration Manager**: Modify the configuration manager in `src/config` to reflect the latest project configurations.
- **Update Components**: Revise the project components for compatibility with the current configuration.
- **Update the Pipeline**: Adjust the pipeline settings to accommodate the latest project workflows.
- **Update `main.py`**: Ensure the main script is updated to run with the latest project setup.
- **Update `app.py`**: Modify the application script as necessary for the project.

## Running the Project

To run the project, follow these steps:

1. Create a new conda environment:

    ```bash
    conda create -n mlproj python=3.8 -y
    ```

2. Activate the conda environment:

    ```bash
    conda activate mlproj
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the application:

    ```bash
    python app.py
    ```

5. Access the application at `http://0.0.0.0:8080` in your browser.

## AWS CI/CD Deployment with GitHub Actions

### Initial AWS Setup

1. **Login to AWS Console** and create an IAM user for deployment with the following access:
   - EC2 Access
   - ECR (Elastic Container Registry)

### Deployment Description

- Build the Docker image of the source code.
- Push the Docker image to ECR.
- Launch an EC2 instance.
- Pull the Docker image from ECR onto the EC2 instance.
- Launch the Docker image on the EC2 instance.

### Policy Requirements

- `AmazonEC2ContainerRegistryFullAccess`
- `AmazonEC2FullAccess`

### Steps for Deployment

1. Create an ECR repository to store the Docker image.
   - **Note**: Save the URI: 654654584423.dkr.ecr.us-east-1.amazonaws.com/mlproject
2. Create an EC2 instance (preferably Ubuntu).
3. Install Docker on the EC2 instance:

    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade -y
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

4. Configure the EC2 instance as a self-hosted runner for GitHub Actions.

5. **Setup GitHub Secrets**:

    ```plaintext
    AWS_ACCESS_KEY_ID=<Your Access Key ID>
    AWS_SECRET_ACCESS_KEY=<Your Secret Access Key>
    AWS_REGION=us-east-1
    AWS_ECR_LOGIN_URI=<Your ECR Login URI>
    ECR_REPOSITORY_NAME=<Your Repository Name>
    ```

6. Update your `README.md` to reflect these instructions for future reference.

Remember to replace placeholders (e.g., `<Your Access Key ID>`) with your actual AWS credentials and repository details.

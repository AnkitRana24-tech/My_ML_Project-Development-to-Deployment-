# Iris Classifier (End-to-End)

<!-- Badges -->
![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Version](https://img.shields.io/badge/version-0.1.0-orange?style=flat-square)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey?style=flat-square)
![Language](https://img.shields.io/badge/language-python-blueviolet?style=flat-square)

> A lightweight Iris classifier that trains a scikit-learn model and serves it via FastAPI inside a Docker container—designed for easy testing, reproducible deployments, and seamless pushing to Azure container registries and services.

---

## Table of Contents

- [Overview](#overview)
- [Feature](#feature)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [Architecture](#architecture)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Overview

Concise overview of the project: Simple, production-ready ML deployment of an Iris classifier using FastAPI, Docker, and Azure-friendly container workflows.

- **What problem it solves:**
Provides a minimal, reproducible pattern for turning a simple ML model into a containerized prediction service you can reliably test, deploy, and push to Azure. It removes boilerplate and integration friction so you can focus on model iteration, CI/CD, and deployment workflows rather than wiring model serialization, API scaffolding, Docker, and registry pushes from scratch.  
- **Who it’s for:** 
ML engineers and data scientists who need a quick, production-adjacent example to learn or prototype model-serving workflows.   
DevOps engineers who want a lightweight reference for CI/CD pipelines that build, test, and push model containers.   
Educators and learners teaching deployment concepts with a small, well-known dataset.   
Small teams or startups that need a simple, auditable service to serve models with minimal infra overhead.    
- **Key design goals:**
Simplicity: minimal dependencies (scikit-learn, FastAPI), clear code structure, and tiny image size for fast iteration.   
Reproducibility: deterministic training script with seed control, saved model artifacts (joblib/pickle) and versioning-ready image tags.   
Testability: included unit tests for training and inference, and integration tests exercising the API endpoints.   
Portability: container-first design (Dockerfile optimized for small layers) to run locally, in CI, or in cloud platforms.   
Azure-ready: guidance and scripts for building, tagging, and pushing images to Azure Container Registry and deploying to Azure Container Instances / Web Apps / AKS.   
Observability & safety: simple health and readiness endpoints, structured JSON responses, and basic input validation for robust testing.   
Minimal footprint: small example using the Iris dataset to keep resource use low and onboarding fast.    

Example:

> This project packages a lightweight scikit-learn Iris classifier as a production-friendly service: it trains a deterministic model, exposes inference via FastAPI, and provides Docker, tests, and Azure deployment scripts—enabling fast, reproducible, and safe ML service deployments.

---

## Feature
-Train and serve a scikit-learn model (Iris dataset).     
-Serve predictions via FastAPI (serve_model.py).    
-Containerized app with Dockerfile for consistent deployment.    
-requirements.txt for reproducible environment.    
-Sample requests tested with Postman.    
-Dataset included: IRIS.csv and serialized model iris_model.pkl.

## Prerequisites
Before running or deploying this project, ensure the following tools and accounts are available:    

**Development Environment**   
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
- **Python 3.8 or higher**
- **Jupyter Notebook / JupyterLab**
  - Used for data exploration, model training, and experimentation
- **pip** (Python package manager)

**Containerization**   
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)
- **Docker**
  - Required to build and run the application container locally
  - Docker Desktop recommended for Windows/macOS

**Cloud Platform**   
![Azure](https://img.shields.io/badge/Microsoft%20Azure-Cloud-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
- **Microsoft Azure Account**
  - Used for deploying the containerized ML application
  - Access to one of the following services:
    - Azure Container Instances (ACI) **or**
    - Azure App Service (Container) **or**
    - Azure Kubernetes Service (AKS)

**Testing & Validation**   
![Postman](https://img.shields.io/badge/Postman-API%20Testing-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
- **Postman**
  - Used to test REST API endpoints after deployment
  - Validate request/response payloads for model predictions

**Optional (Recommended)**
- **Git**
  - Version control and collaboration
- **Azure CLI**
  - For local authentication and deployment automation

## Usage   

This project demonstrates an end-to-end machine learning workflow, from model development to cloud deployment and API-based inference.   

**1. Model Development & Training**
- The machine learning model is developed and trained using **Python** and **Jupyter Notebook**.
- Data exploration, preprocessing, and model training are performed locally.
- After training, the model is serialized and saved as a file (`iris_model.pkl`) for reuse during inference.

**2. Running the Application Locally (Docker)**
- The trained model is served through a REST API using a Python-based service.
- The application is containerized using **Docker** to ensure consistency across environments.
- The Docker container runs the inference service and exposes an API endpoint for predictions.

**3. Cloud Deployment on Azure**
- The Docker image is deployed to **Microsoft Azure** using container-based services.
- Azure hosts the application and exposes a public endpoint for accessing the prediction API.
- This enables scalable, cloud-ready access to the machine learning model.

**4. Testing the Deployment**
- **Postman** is used to test the deployed REST API.
- Requests are sent with feature values as input, and the API returns prediction results.
- This validates both the deployment and the model inference pipeline.

**5. Typical Workflow**
1. Train the model using Jupyter Notebook
2. Package the inference service using Docker
3. Deploy the container to Azure
4. Test API endpoints using Postman

## Example

This section demonstrates how to use the deployed machine learning service to get predictions from the trained IRIS model.   

**API Request (Prediction)**   

Once the application is running (locally via Docker or deployed on Azure), predictions can be obtained by sending a POST request to the inference endpoint.   
**Request Body (JSON)**      
json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}   
**API Response**      
{   
  "prediction": "Iris-setosa"   
}   

## Architecture
**Model Serving Architecture (Inference Phase)**   
  **1.Typical Flow:**   
HTTP Request   
        ↓   
serve_model.py   
        ↓   
iris_model.pkl   
        ↓   
Prediction Response   

**Containerization Architecture (Docker)**   
  **1.Logical Build Flow:**   
Base Python Image   
         ↓   
Install requirements.txt   
         ↓   
Copy serve_model.py,
Copy iris_model.pkl   
         ↓   
Expose Port (e.g. 5000 / 8000 / 80)   
         ↓   
Start API Server   

**End-to-End Flow Summary**   
   **1.Training Flow (Offline)**   
IRIS.csv   
      ↓   
IrisModel.py   
      ↓   
iris_model.pkl   

   **2.Inference Flow (Online)**   
Client Request   
      ↓   
Azure Endpoint   
      ↓   
Docker Container   
      ↓    
serve_model.py   
      ↓   
iris_model.pkl   
      ↓   
Prediction Response   

## Testing

Testing for this project focuses on validating the machine learning inference API after local and cloud deployment.   

**1. API Testing with Postman**   
- **Postman** is used to test the REST API endpoints exposed by the application.   
- Requests are sent to the `/predict` endpoint with input feature values in JSON format.   
- Responses are verified to ensure correct predictions and proper API behavior.      

**Test Coverage Includes:**   
- Successful prediction requests      
- Correct response format (JSON)   
- Model loading and inference validation   
- Endpoint accessibility after deployment   


**2. Local Testing (Docker)**   
- The Docker container is run locally to verify:   
  - Successful container startup     
  - Model loading from the serialized file   
  - API endpoint availability   
- Local testing ensures the container behaves consistently before cloud deployment.   


**3. Cloud Testing (Azure Deployment)**   
- After deploying the container to **Microsoft Azure**, the public endpoint is tested using Postman.   
- Validates:     
  - Cloud connectivity    
  - Deployment configuration   
  - End-to-end inference flow   
- Confirms that the application behaves the same in the cloud as it does locally.   


**4. Sample Test Scenario**   
- Send a POST request with valid feature values   
- Receive a predicted iris species as output   
- Verify HTTP status codes and response payload   


**5. Testing Outcome**   
- The application successfully processes input data and returns predictions.    
- REST API remains stable across local and Azure environments.   
- Deployment is verified as production-ready for inference usage.


## Deployment   
The application is deployed as a containerized machine learning inference service on **Microsoft Azure**, ensuring portability, scalability and consistency across environments.   

**Deployment Overview**    
- The trained machine learning model is packaged with the inference service using **Docker**.
- The Docker image is deployed to **Azure** using container-based services.
- Azure exposes a public endpoint to access the REST API for predictions.

**Deployment Steps:**  

1. **Build Docker Image**   
The application and model artifacts are packaged into a Docker image using the provided Dockerfile.   

2. **Push Image to Azure**   
The Docker image is pushed to an Azure-supported container registry (e.g., Azure Container Registry).   

3. **Deploy on Azure**   
The container image is deployed using one of the following Azure services:   
Azure Container Instances (ACI)   
Azure App Service (Container)   
Azure Kubernetes Service (AKS)   

4. **Expose API Endpoint**   
Azure assigns a public URL to the deployed container.   
The inference service becomes accessible via HΤΤΡ.   

**Post-Deployment Validation**   
The deployed REST API is tested using **Postman**.   
Requests are sent to the /predict endpoint with input feature values.   
Successful responses confirm correct deployment and model inference.   

**Deployment Benefits**   
Consistent runtime across local and cloud environments    
Easy scalability using Azure container services   
Cloud-ready, production-oriented ML deployment   
Simplified updates by rebuilding and redeploying the container   

## Contributing   
Contributions are Welcome!   
1. Fork the repository   
2. Create a feature branch
3. Commit changes with clear messages
4. Open a Pull Request

Please follow the existing code style and add tests where applicable.

## Contact   

**Author:** Ankit Rana   
**GitHub:** https://github.com/AnkitRana24-tech
For questions, feedback or collaboration opportunities, feel free to:   
-Open an issue in this repository   
-Reach out via GitHub, **E-mail:** ankitsrana0457@gmail.com

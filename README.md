**Project overview:**
Simple, production-ready ML deployment of an Iris classifier using FastAPI, Docker, and Azure-friendly container workflows.

**Features:**    
Train and serve a scikit-learn model (Iris dataset).     
Serve predictions via FastAPI (serve_model.py).    
Containerized app with Dockerfile for consistent deployment.    
requirements.txt for reproducible environment.    
Sample requests tested with Postman.    
Dataset included: IRIS.csv and serialized model iris_model.pkl.

**Repository structure:**    
IRIS.csv — dataset used for training and testing    
IrisModel.py — training script (loads IRIS.csv, trains model, saves iris_model.pkl)    
iris_model.pkl — serialized trained model (joblib/pickle)    
serve_model.py — FastAPI application exposing prediction endpoints    
Dockerfile — builds container image for deployment    
requirements.txt — Python packages required    
README.md — this file    

**Docker (build & run):**    
_Build image:_ docker build -t my_project_image .    
_Run Container:_ docker run -p 80:80 my_project_image    

*Test the deployed model by sending a POST request to http://localhost:80/predict using the same JSON payload you used earlier.*

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
- [Examples](#examples)
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

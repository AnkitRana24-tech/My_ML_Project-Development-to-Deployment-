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

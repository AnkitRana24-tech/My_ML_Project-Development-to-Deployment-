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

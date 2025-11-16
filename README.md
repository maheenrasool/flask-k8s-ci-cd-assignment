Flask Kubernetes CI/CD Assignment
Cloud MLOps (BS AI)
Assignment 3: End-to-End CI/CD Pipeline
 Project Overview


This project implements a complete CI/CD pipeline for a Python Flask application using Docker, GitHub Actions, Jenkins and Kubernetes running on Minikube.
It simulates a real industry DevOps workflow from development to automated testing, containerization and cluster deployment.


🛠 Technologies Used
Version Control

Git
GitHub
Branch Protection
Pull Requests
Milestones and Issues

Continuous Integration

GitHub Actions
Python environment setup
Dependency installation
flake8 linting
pytest unit testing
Docker image build

Continuous Delivery

Jenkins Declarative Pipeline
Automated Docker builds
Automatic Kubernetes deployment using kubectl

Containerization
Dockerfile
Local Docker runs

Kubernetes (Minikube)

Deployments
Rolling Updates
Replica scaling
Resource requests and limits
NodePort service for load balancing
Rollout and rollback verification

Running the Application Locally (Docker)
Clone the repository

git clone https://github.com/maheenrasool/flask-k8s-ci-cd-assignment
cd flask-k8s-ci-cd-assignment
Build the Docker image
docker build -t flask-app .
Run the container
docker run -p 5000:5000 flask-app
Open the application

http://localhost:5000

Deploying to Kubernetes Manually (Minikube)
Start Minikube
minikube start
Apply Kubernetes manifests
kubectl apply -f kubernetes/

Check resources

kubectl get pods
kubectl get services
kubectl get deployments

Open the app through Minikube
minikube service flask-service
Automated Deployment Using Jenkins
The Jenkins pipeline automatically deploys the application whenever the main branch is updated.


Pipeline Stages
1. Build Docker Image
docker build -t flask-app .


2. Deploy to Kubernetes
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml


3. Verify Deployment
kubectl rollout status deployment/flask-deployment
kubectl get pods
kubectl get services


If successful, Jenkins prints:
Pipeline executed successfully!


⚙ Kubernetes Features Used
Rolling Updates


Deployment includes:
maxSurge
maxUnavailable

Ensures smooth zero-downtime rollouts.
Scaling (Replicas)
Deployment uses multiple replicas for demonstration.

Scale manually:
kubectl scale deployment flask-deployment --replicas=5
Rollback Support

Undo a faulty update:
kubectl rollout undo deployment/flask-deployment
Load Balancing

NodePort service balances traffic across replicas automatically.

   Repository Structure
├── app/
│   ├── app.py
│   └── __init__.py
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── tests/
│   ├── test_app.py
│   └── __init__.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml

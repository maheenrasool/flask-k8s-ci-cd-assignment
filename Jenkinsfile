pipeline {
    agent any

    environment {
        KUBECONFIG = "C:\\ProgramData\\Jenkins\\.kube\\config"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat """
                docker build -t flask-app .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                bat """
                kubectl --kubeconfig=%KUBECONFIG% apply -f kubernetes/deployment.yaml --validate=false
                kubectl --kubeconfig=%KUBECONFIG% apply -f kubernetes/service.yaml --validate=false
                """
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment...'
                bat """
                kubectl --kubeconfig=%KUBECONFIG% rollout status deployment/flask-deployment
                kubectl --kubeconfig=%KUBECONFIG% get pods
                kubectl --kubeconfig=%KUBECONFIG% get services
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}

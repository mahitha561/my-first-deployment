pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-2"
        AWS_ACCOUNT_ID = "871700844971"
        ECR_REPO = "user-service"
        IMAGE_TAG = "${BUILD_NUMBER}"
        ECR_URI = "871700844971.dkr.ecr.us-east-2.amazonaws.com/${ECR_REPO}"
        KUBE_CONFIG = credentials('eks-kubeconfig')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mahitha561/my-first-deployment.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${ECR_REPO}:${IMAGE_TAG} .
                """
            }
        }

        stage('Login to ECR') {
            steps {
                sh """
                aws ecr get-login-password --region us-east-2 \
                | docker login --username AWS --password-stdin 871700844971.dkr.ecr.us-east-2.amazonaws.com
                """
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh """
                docker tag ${ECR_REPO}:${IMAGE_TAG} ${ECR_URI}:${IMAGE_TAG}
                docker tag ${ECR_REPO}:${IMAGE_TAG} ${ECR_URI}:latest
                docker push ${ECR_URI}:${IMAGE_TAG}
                docker push ${ECR_URI}:latest
                """
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh """
                export KUBECONFIG=${KUBE_CONFIG}
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml
                """
            }
        }
    }

    post {
        success {
            echo "Deployment successful 🚀"
        }
        failure {
            echo "Deployment failed ❌"
        }
    }
}
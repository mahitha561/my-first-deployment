pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mahitha561/my-first-deployment.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  docker stop myapp || true
                  docker rm myapp || true
                  docker run -d -p 80:80 --name myapp myapp
                '''
            }
        }
    }
}

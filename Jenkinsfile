pipeline {
    agent any

    stages {
        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['ec2-ssh']) {
                    sh '''
                      ssh -o StrictHostKeyChecking=no ubuntu@<TARGET_EC2_PUBLIC_IP> \
                      "hostname && docker ps"
                    '''
                }
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Create Webpage') {
            steps {
                bat '''
                mkdir site
                echo ^<!DOCTYPE html^> > site\\index.html
                echo ^<html^> >> site\\index.html
                echo ^<body^> >> site\\index.html
                echo ^<h1^>Jenkins Pipeline Successful^</h1^> >> site\\index.html
                echo ^</body^> >> site\\index.html
                echo ^</html^> >> site\\index.html
                '''
            }
        }

        stage('Publish Webpage') {
            steps {
                archiveArtifacts artifacts: 'site/index.html'
            }
        }
    }
}

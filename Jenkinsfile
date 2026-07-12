pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploying Flask Application to Staging'
            }
        }
    }
}

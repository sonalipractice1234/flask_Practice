pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                set -e
                export DEBIAN_FRONTEND=noninteractive
                export PATH="$HOME/.local/bin:$PATH"
                python3 --version
                python3 -m pip install --user --disable-pip-version-check --upgrade pip
                python3 -m pip install --user --disable-pip-version-check -r requirements.txt
                python3 -m pip install --user --disable-pip-version-check pytest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                set -e
                python3 -m pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying Flask Application to Staging"'
            }
        }
    }
}

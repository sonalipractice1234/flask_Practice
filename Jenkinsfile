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
                if command -v sudo >/dev/null 2>&1; then
                    sudo apt-get update
                    sudo apt-get install -y python3-venv python3-pip
                else
                    apt-get update
                    apt-get install -y python3-venv python3-pip
                fi
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                python -m pip install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
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

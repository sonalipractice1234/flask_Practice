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
                if [ ! -d venv ]; then
                    if command -v sudo >/dev/null 2>&1 && sudo -n true >/dev/null 2>&1; then
                        sudo -n apt-get update
                        sudo -n apt-get install -y python3-venv python3-pip
                    elif [ "$(id -u)" -eq 0 ]; then
                        apt-get update
                        apt-get install -y python3-venv python3-pip
                    else
                        echo "Unable to install system packages: sudo is not passwordless and this user is not root." >&2
                        exit 1
                    fi
                    python3 -m venv venv
                fi
                . venv/bin/activate
                python -m pip install --disable-pip-version-check --upgrade pip
                python -m pip install --disable-pip-version-check -r requirements.txt
                python -m pip install --disable-pip-version-check pytest
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

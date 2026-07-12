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
                python3 --version
                if [ ! -f venv/bin/activate ]; then
                    rm -rf venv
                    if python3 -m venv --help >/dev/null 2>&1; then
                        python3 -m venv venv
                    else
                        echo "python3 venv module is not available on this Jenkins agent" >&2
                        exit 1
                    fi
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
                set -e
                . venv/bin/activate
                python -m pytest
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

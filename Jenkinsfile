pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python venv') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                  pip install unittest-xml-reporting
                '''
            }
        }

        stage('Run Unittests') {
            steps {
                sh '''
                  . venv/bin/activate
                  python -m xmlrunner discover -s test -o test-results
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results/*.xml'
        }
    }
}
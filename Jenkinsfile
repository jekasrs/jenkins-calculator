pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install deps') {
            steps {
                sh '''
                  pip3 install --upgrade pip
                  if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi
                  pip3 install unittest-xml-reporting
                '''
            }
        }

        stage('Run Unittests') {
            steps {
                sh 'python3 -m xmlrunner discover -s test -o test-results'
            }
        }
    }

    post {
        always {
            junit 'test-results/*.xml'
        }
    }
}
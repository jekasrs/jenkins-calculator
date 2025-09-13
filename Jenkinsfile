pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Install deps') {
            steps {
                sh '''
                  pip install --upgrade pip
                  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                  pip install unittest-xml-reporting
                '''
            }
        }

        stage('Run Unittests') {
            steps {
                sh 'python -m xmlrunner discover -s test -o test-results'
            }
        }
    }

    post {
        always {
            junit 'test-results/*.xml'
        }
    }
}
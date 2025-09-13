pipeline {
    agent any

    environment {
        PROJECT_URL = 'https://github.com/jekasrs/jenkins-calculator.git'
        PROJECT_DIR = 'jenkins-calculator'
    }

    stages {
        stage('Clone repo') {
            steps{
                sh'''
                  echo "Клонируем репозиторий"
                  rm -rf $PROJECT_DIR
                  git clone $PROJECT_URL
                  cd $PROJECT_DIR
                '''
            }
        }
        stage('Install deps') {
            steps {
                sh '''
                  cd $PROJECT_DIR
                  pip3 install --upgrade pip
                  if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi
                  pip3 install unittest-xml-reporting
                '''
            }
        }

        stage('Run Unittests') {
            steps {
                sh '''
                cd $PROJECT_DIR
                export PYTHONPATH=$PWD
                python3 -m xmlrunner discover -s test -p "*.py" -o test-results
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
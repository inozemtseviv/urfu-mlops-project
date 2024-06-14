pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    dir("./") {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dir("./") {
                        sh "pytest"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    dir("./") {
                        sh "docker build -t mlops-project ."
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

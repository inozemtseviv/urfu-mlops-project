pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage('Install Dependencies') {
            agent {
                docker {
                    label 'docker'
                    image 'python:3.11'
                }
            }

            steps {
                script {
                    dir("./") {
                        sh 'python -m pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            agent {
                docker {
                    label 'docker'
                    image 'python:3.11'
                }
            }

            steps {
                script {
                    dir("./") {
                        sh "python -m pytest"
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

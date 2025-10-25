pipeline {
    agent any

    stages {
        stage('Checkout Git') {
            steps {
                echo 'Получение кода из GitHub...'
                git branch: 'main',
                url: 'https://github.com/Anna-Leb/student-data-generator.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Сборка Docker образа...'
                script {
                    dockerImage = docker.build("student-data-generator:latest")
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Тестирование приложения...'
                script {
                    def result = docker.image("student-data-generator:latest").run("--rm", "--name", "test-container")
                    sleep time: 5, unit: 'SECONDS'
                    sh "docker stop test-container || true"
                }
            }
        }
    }

    post {
        always {
            echo 'Сборка завершена.'
            sh 'docker container prune -f || true'
        }
        success {
            echo 'Сборка успешна! Образ student-data-generator:latest готов'
        }
        failure {
            echo 'Ошибка сборки'
        }
    }
}
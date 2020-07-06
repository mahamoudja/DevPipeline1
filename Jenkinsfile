pipeline {
    agent any

    stages {
        stage('Find and kill Process') {
            steps {
                 sh ''' var=$(pgrep -f hello)
                 kill -9 $var
                 '''
            }
        }
         stage('Pull Code2') {
            steps {
                sh 'git pull git@github.com:FDevBaig/DevPipeline1.git'
            }
        }
         stage('Build and run') {
            steps {
                sh ''' JENKINS_NODE_COOKIE=dontKillMe
                nohup python3 hello_pipeline1.py &
                '''
            }
        }
    }
}

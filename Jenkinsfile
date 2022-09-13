pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        withAWS([credentials:'aws_credentials')]){
        sh 'python3 ec2.py'
        }
      }
    }
  }
}

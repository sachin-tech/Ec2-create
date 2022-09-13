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
        withAWS(region:AWS_REGION, credentials:'aws_credentials'){
        sh 'python3 ec2.py'
        }
      }
    }
  }
}

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
        withAWS(region:AWS_REGION, credentials:'aws_creds'){
        sh 'python3 create_S3_Bucket.py'
        }
      }
    }
  }
}

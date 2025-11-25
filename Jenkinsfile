pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = credentials("AWS_SECRET_ACCESS_KEY")
        AWS_DEFAULT_REGION = "us-east-1"
    }

    stages {
        stage("Display AWS creds") {
            steps {
                echo "Using below AWS user"
                sh "aws sts get-caller-identity"
            }
        }
        stage("Deploy Stack") {
            steps {
                echo "Deploying cloudformation stack"
                sh """
                    aws cloudformation deploy \
                        --stack-name assignment-3 \
                        --template-file cft.yaml \
                        --parameter-overrides VPCId=vpc-0469328b35b6382b7 \
                        --capabilities CAPABILITY_IAM
                """
            }
        }
    }
}
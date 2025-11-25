pipeline {
    agent any

    parameters {
        string(name: 'VPC_ID', defaultValue: 'vpc-0469328b35b6382b7', description: 'VPC ID to pass to CFN')
    }

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
                echo "Deploying cloudformation stack with VPC ID: ${params.VPC_ID}"
                sh """
                    aws cloudformation deploy \
                        --stack-name assignment-3 \
                        --template-file cft.yaml \
                        --parameter-overrides VPCId=${params.VPC_ID} \
                        --capabilities CAPABILITY_IAM
                """
            }
        }
    }
}

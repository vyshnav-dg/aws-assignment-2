pipeline {
    agent any

    parameters {
        string(name: 'VPC_ID', defaultValue: 'vpc-0469328b35b6382b7', description: 'VPC ID to pass to CFN')
    }

    environment {
        AWS_ACCESS_KEY_ID = credentials("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = credentials("AWS_SECRET_ACCESS_KEY")
        AWS_DEFAULT_REGION = "us-east-1"
        S3_BUCKET = "vyshn-cfn-artifacts"
        LAMBDA_ZIP = "assignment-2-lambda.zip"
        LAMBDA_DIR = "lambda"
    }

    stages {

        stage("Display AWS creds") {
            steps {
                echo "Using below AWS user"
                sh "aws sts get-caller-identity"
            }
        }

        stage("Package Lambda") {
            steps {
                echo "Zipping Lambda code..."
                sh """
                    cd ${env.LAMBDA_DIR}
                    zip -r ../${env.LAMBDA_ZIP} .
                """
            }
        }

        stage("Upload Lambda to S3") {
            steps {
                echo "Uploading Lambda ZIP to S3..."
                sh """
                    aws s3 cp ${env.LAMBDA_ZIP} s3://${env.S3_BUCKET}/${env.LAMBDA_ZIP}
                """
            }
        }

        stage("Deploy Stack") {
            steps {
                echo "Deploying CloudFormation stack with VPC ID: ${params.VPC_ID}"
                sh """
                    set -e
                    aws cloudformation deploy \
                        --stack-name assignment-2 \
                        --template-file cft.yaml \
                        --parameter-overrides VPCId=${params.VPC_ID} \
                        --capabilities CAPABILITY_IAM
                """
            }
        }

    }
}

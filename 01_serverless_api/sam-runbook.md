# runbook sam
This runbook contains the steps to initialize and deploy a chalice application

# Resources
- [AWS SAM Specification](https://github.com/awsdocs/aws-sam-developer-guide/blob/main/doc_source/sam-specification.md)
- [AWS SAM Developer Guide](https://github.com/awsdocs/aws-sam-developer-guide/blob/main/doc_source/index.md)
- [AWS SAM](https://github.com/aws/serverless-application-model)
- [AWS Lambda Event Object](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format)
- [AWS Lambda Context Object](https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html)
- [AWS Lambda Proxy Integration Object](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)

# Installation

```
brew install aws-sam-cli

# upgrade
brew upgrade aws-sam-cli
```

# Initialize a new project

```
sam init

You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
	1 - AWS Quick Start Templates
	2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
	1 - Hello World Example
	2 - Multi-step workflow
	3 - Serverless API
	4 - Scheduled task
	5 - Standalone function
	6 - Data processing
	7 - Infrastructure event management
	8 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: y

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: y
X-Ray will incur an additional cost. View https://aws.amazon.com/xray/pricing/ for more details

Project name [sam-app]: sam_example

Cloning from https://github.com/aws/aws-sam-cli-app-templates (process may take a moment)

    -----------------------
    Generating application:
    -----------------------
    Name: sam_example
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .

    Next steps can be found in the README file at ./sam_example/README.md


    Commands you can use next
    =========================
    [*] Create pipeline: cd sam_example && sam pipeline init --bootstrap
    [*] Validate SAM template: sam validate
    [*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
```

# build the project the project

```
cd sam_example
sam build
Your template contains a resource with logical ID "ServerlessRestApi", which is a reserved logical ID in AWS SAM. It could result in unexpected behaviors and is not recommended.
Building codeuri: /Users/dnvriend/projects/20220512_codeguild_serverless/01_serverless_api/sam_example/hello_world runtime: python3.9 metadata: {} architecture: x86_64 functions: ['HelloWorldFunction']
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
[*] Deploy: sam deploy --guided
```

# deploy or upgrade the project

```
cd sam_example
sam deploy --guided

Configuring SAM deploy
======================

	Looking for config file [samconfig.toml] :  Not found

	Setting default arguments for 'sam deploy'
	=========================================
	Stack Name [sam-app]: sam-example
	AWS Region [eu-west-1]:
	#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
	Confirm changes before deploy [y/N]: y
	#SAM needs permission to be able to create roles to connect to the resources in your template
	Allow SAM CLI IAM role creation [Y/n]:
	#Preserves the state of previously provisioned resources when an operation fails
	Disable rollback [y/N]: y
	HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
	Save arguments to configuration file [Y/n]:
	SAM configuration file [samconfig.toml]:
	SAM configuration environment [default]:

	Looking for resources needed for deployment:
	 Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-kx70xen8l6tk
	 A different default S3 bucket can be set in samconfig.toml

	Saved arguments to config file
	Running 'sam deploy' for future deployments will use the parameters saved above.
	The above parameters can be changed by modifying samconfig.toml
	Learn more about samconfig.toml syntax at
	https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

Uploading to sam-example/0f39bb0eea4b1c938c1abd784149428e  452706 / 452706  (100.00%)

	Deploying with following values
	===============================
	Stack name                   : sam-example
	Region                       : eu-west-1
	Confirm changeset            : True
	Disable rollback             : True
	Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-kx70xen8l6tk
	Capabilities                 : ["CAPABILITY_IAM"]
	Parameter overrides          : {}
	Signing Profiles             : {}

Initiating deployment
=====================
Uploading to sam-example/e7990d36dc7c2137a0463a71878f00ae.template  1211 / 1211  (100.00%)

Waiting for changeset to be created..

CloudFormation stack changeset
-------------------------------------------------------------------------------------------------------------------------------------
Operation                         LogicalResourceId                 ResourceType                      Replacement
-------------------------------------------------------------------------------------------------------------------------------------
+ Add                             HelloWorldFunctionHelloWorldPer   AWS::Lambda::Permission           N/A
                                  missionProd
+ Add                             HelloWorldFunctionRole            AWS::IAM::Role                    N/A
+ Add                             HelloWorldFunction                AWS::Lambda::Function             N/A
+ Add                             ServerlessRestApiDeployment47fc   AWS::ApiGateway::Deployment       N/A
                                  2d5f9d
+ Add                             ServerlessRestApiProdStage        AWS::ApiGateway::Stage            N/A
+ Add                             ServerlessRestApi                 AWS::ApiGateway::RestApi          N/A
-------------------------------------------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:eu-west-1:452197817098:changeSet/samcli-deploy1652087629/9dfd52e4-edc1-413d-98a6-4449c0b7d57c


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

2022-05-09 11:14:09 - Waiting for stack create/update to complete

CloudFormation events from stack operations
-------------------------------------------------------------------------------------------------------------------------------------
ResourceStatus                    ResourceType                      LogicalResourceId                 ResourceStatusReason
-------------------------------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS                AWS::IAM::Role                    HelloWorldFunctionRole            -
CREATE_IN_PROGRESS                AWS::IAM::Role                    HelloWorldFunctionRole            Resource creation Initiated
CREATE_COMPLETE                   AWS::IAM::Role                    HelloWorldFunctionRole            -
CREATE_IN_PROGRESS                AWS::Lambda::Function             HelloWorldFunction                -
CREATE_IN_PROGRESS                AWS::Lambda::Function             HelloWorldFunction                Resource creation Initiated
CREATE_COMPLETE                   AWS::Lambda::Function             HelloWorldFunction                -
CREATE_IN_PROGRESS                AWS::ApiGateway::RestApi          ServerlessRestApi                 -
CREATE_COMPLETE                   AWS::ApiGateway::RestApi          ServerlessRestApi                 -
CREATE_IN_PROGRESS                AWS::ApiGateway::RestApi          ServerlessRestApi                 Resource creation Initiated
CREATE_IN_PROGRESS                AWS::Lambda::Permission           HelloWorldFunctionHelloWorldPer   -
                                                                    missionProd
CREATE_IN_PROGRESS                AWS::Lambda::Permission           HelloWorldFunctionHelloWorldPer   Resource creation Initiated
                                                                    missionProd
CREATE_IN_PROGRESS                AWS::ApiGateway::Deployment       ServerlessRestApiDeployment47fc   -
                                                                    2d5f9d
CREATE_IN_PROGRESS                AWS::ApiGateway::Deployment       ServerlessRestApiDeployment47fc   Resource creation Initiated
                                                                    2d5f9d
CREATE_COMPLETE                   AWS::ApiGateway::Deployment       ServerlessRestApiDeployment47fc   -
                                                                    2d5f9d
CREATE_IN_PROGRESS                AWS::ApiGateway::Stage            ServerlessRestApiProdStage        -
CREATE_IN_PROGRESS                AWS::ApiGateway::Stage            ServerlessRestApiProdStage        Resource creation Initiated
CREATE_COMPLETE                   AWS::ApiGateway::Stage            ServerlessRestApiProdStage        -
CREATE_COMPLETE                   AWS::Lambda::Permission           HelloWorldFunctionHelloWorldPer   -
                                                                    missionProd
CREATE_COMPLETE                   AWS::CloudFormation::Stack        sam-example                       -
-------------------------------------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
---------------------------------------------------------------------------------------------------------------------------------------
Outputs
---------------------------------------------------------------------------------------------------------------------------------------
Key                 HelloWorldFunctionIamRole
Description         Implicit IAM Role created for Hello World function
Value               arn:aws:iam::452197817098:role/sam-example-HelloWorldFunctionRole-17CXUVPB0JYIA

Key                 HelloWorldApi
Description         API Gateway endpoint URL for Prod stage for Hello World function
Value               https://89dr7hsfe2.execute-api.eu-west-1.amazonaws.com/Prod/hello/

Key                 HelloWorldFunction
Description         Hello World Lambda Function ARN
Value               arn:aws:lambda:eu-west-1:452197817098:function:sam-example-HelloWorldFunction-2FbtDlyf9mxV
---------------------------------------------------------------------------------------------------------------------------------------

Successfully created/updated stack - sam-example in eu-west-1
```

# Describe the CloudFormation Stack

```
aws cloudformation describe-stacks --stack-name=sam-example --region=eu-west-1
{
    "Stacks": [
        {
            "StackId": "arn:aws:cloudformation:eu-west-1:452197817098:stack/sam-example/56ad8400-cf78-11ec-822a-0acc9b486ab7",
            "StackName": "sam-example",
            "ChangeSetId": "arn:aws:cloudformation:eu-west-1:452197817098:changeSet/samcli-deploy1652087629/9dfd52e4-edc1-413d-98a6-4449c0b7d57c",
            "Description": "sam_example\nSample SAM Template for sam_example\n",
            "CreationTime": "2022-05-09T09:13:50.003000+00:00",
            "LastUpdatedTime": "2022-05-09T09:14:09.252000+00:00",
            "RollbackConfiguration": {},
            "StackStatus": "CREATE_COMPLETE",
            "DisableRollback": true,
            "NotificationARNs": [],
            "Capabilities": [
                "CAPABILITY_IAM"
            ],
            "Outputs": [
                {
                    "OutputKey": "HelloWorldFunctionIamRole",
                    "OutputValue": "arn:aws:iam::452197817098:role/sam-example-HelloWorldFunctionRole-17CXUVPB0JYIA",
                    "Description": "Implicit IAM Role created for Hello World function"
                },
                {
                    "OutputKey": "HelloWorldApi",
                    "OutputValue": "https://89dr7hsfe2.execute-api.eu-west-1.amazonaws.com/Prod/hello/",
                    "Description": "API Gateway endpoint URL for Prod stage for Hello World function"
                },
                {
                    "OutputKey": "HelloWorldFunction",
                    "OutputValue": "arn:aws:lambda:eu-west-1:452197817098:function:sam-example-HelloWorldFunction-2FbtDlyf9mxV",
                    "Description": "Hello World Lambda Function ARN"
                }
            ],
            "Tags": [],
            "EnableTerminationProtection": false,
            "DriftInformation": {
                "StackDriftStatus": "NOT_CHECKED"
            }
        }
    ]
}
```

# Delete the stack

```
aws cloudformation delete-stack --stack-name=sam-example --region=eu-west-1
```

# Testing

```
curl https://q7s565uyek.execute-api.eu-west-1.amazonaws.com/Prod/api/

curl https://q7s565uyek.execute-api.eu-west-1.amazonaws.com/Prod/api/hello/dennis

curl -X POST -H "Content-Type: application/json" -d '{"name":"dennis"}' https://q7s565uyek.execute-api.eu-west-1.amazonaws.com/Prod/api/users
```


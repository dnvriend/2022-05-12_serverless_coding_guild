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
```

# deploy or upgrade the project

```
sam deploy --guided
```

# Describe the CloudFormation Stack

```
aws cloudformation describe-stacks --stack-name=sam-example --region=eu-west-1
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


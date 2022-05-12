# runbook chalice
This runbook contains the steps to initialize and deploy a chalice application

# Resources
- [Chalice](https://github.com/aws/chalice)
- [Chalice Routing](https://aws.github.io/chalice/tutorials/basicrestapi.html)

# Installation

```
pip install chalice
```

# Initialize a new project

```
chalice new-project chalice_example
Your project has been generated in ./chalice_example
```

# deploy or upgrade the project

```
cd chalice_example
chalice deploy
Creating deployment package.
Creating IAM role: chalice_example-dev
Creating lambda function: chalice_example-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:eu-west-1:452197817098:function:chalice_example-dev
  - Rest API URL: https://d9sufpuw28.execute-api.eu-west-1.amazonaws.com/api/
```

# testing the API

```
curl https://d9sufpuw28.execute-api.eu-west-1.amazonaws.com/api/
{"hello":"world"}

curl https://d9sufpuw28.execute-api.eu-west-1.amazonaws.com/api/hello/dennis
{"hello":"dennis"}

curl -X POST -d '{"name": "dennis"}' -H "Content-Type: application/json" https://d9sufpuw28.execute-api.eu-west-1.amazonaws.com/api/users
{"user":{"name":"dennis"}}
```

# delete/destroy the project

```
cd chalice_example
chalice delete
Deleting Rest API: d9sufpuw28
Deleting function: arn:aws:lambda:eu-west-1:452197817098:function:chalice_example-dev
Deleting IAM role: chalice_example-dev
```

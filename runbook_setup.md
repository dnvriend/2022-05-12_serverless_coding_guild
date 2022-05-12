# runbook_python


You will need to have Python 3.9 installed as this version is supported by AWS Lambda
the easiest way to do this is by installing `pyenv`

```
# install
brew install pyenv

# upgrade
brew upgrade pyenv
```

# Installing Python

```
# install python 3.9.11
pyenv install 3.9.11

# check the installed Python versions
pyenv versions

# set your global python version to 3.9.11
pyenv global 3.9.11

# ask bash to show which python you are using
which python

# query the Python version from the Python runtime
python -V
```

# Install pipenv

Pipenv is a dependency manager for Python. Just like with Typescript, you 
create a Python environment using a specific version of Python, and 
the libraries that you need when coding your solution.

```
# install
pip install pipenv

# upgrade
pip install --upgrade pipenv
```

# Install aws-cli

The AWS CLI is the CLI tool for accessing, configuring and querying AWS resources
using the CLI. 

```
# install
brew install awscli

# upgrade
brew upgrade awscli
```

# Install chalice

Chalice is a framework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda. It comes with a CLI that you use to quickly create a chalice project. To install chalice type:

```
# install
pip install chalice

# upgrade
pip install --upgrade chalice
```

# Install SAM

- [AWS SAM Specification](https://github.com/awsdocs/aws-sam-developer-guide/blob/main/doc_source/sam-specification.md)
- [AWS SAM Developer Guide](https://github.com/awsdocs/aws-sam-developer-guide/blob/main/doc_source/index.md)
- [AWS SAM](https://github.com/aws/serverless-application-model)


The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax, enabling you to build serverless applications faster.

To get started with building SAM-based applications, use the AWS SAM CLI. SAM CLI provides a Lambda-like execution environment that lets you locally build, test, and debug applications defined by SAM templates or through the AWS Cloud Development Kit (CDK). You can also use the SAM CLI to deploy your applications to AWS, or create secure continuous integration and deployment (CI/CD) pipelines that follow best practices and integrate with AWS' native and third party CI/CD systems.

```
# install
brew install aws-sam-cli

# upgrade
brew upgrade aws-sam-cli
```

# Installing AWS CDK

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages. Although CDK can be used with many programming languages (Typescript, Javascript, Python, Java, C#), it is mostly used with Typescript, but we will use Python.

Provisioning cloud applications can be a challenging process that requires you to perform manual actions, write custom scripts, maintain templates, or learn domain-specific languages. AWS CDK uses the familiarity and expressive power of programming languages for modeling your applications. It provides high-level components called constructs that preconfigure cloud resources with proven defaults, so you can build cloud applications with ease. AWS CDK provisions your resources in a safe, repeatable manner through AWS CloudFormation. It also allows you to compose and share your own custom constructs incorporating your organization's requirements, helping you expedite new projects.

```
# install
brew install node
npm install -g aws-cdk

# upgrade
brew upgrade node
```


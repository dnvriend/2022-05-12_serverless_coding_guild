#!/usr/bin/env python
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.general import User

with Diagram("serverless_api_architecture", show=False, direction="LR") as diag:    
    with Cluster('eu-central-1'):
        user = User("a user")
        gw = APIGateway("api gateway")
        lambdas = Lambda('helloworld')

    user >> gw >> lambdas
    user << gw << lambdas

diag

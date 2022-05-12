#!/usr/bin/env python
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.general import User
from diagrams.aws.database import Dynamodb

with Diagram("serverless_crud_api", show=False, direction="LR") as diag:    
    with Cluster('eu-central-1'):
        user = User("a user")
        gw = APIGateway("api gateway")
        lambdas = Lambda('CRUD')
        dynamodb = Dynamodb("CRUD storage")


    user >> gw >> lambdas >> dynamodb
    user << gw << lambdas << dynamodb

diag

#!/usr/bin/env python
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client

with Diagram("serverless_event_handler", show=False, direction="LR") as diag:    
    with Cluster('eu-central-1'):
        client = Client("a client")
        s3_src = S3("img source")
        lambdas = Lambda('resize image')
        s3_dest = S3("img destination")

    client >> s3_src >> lambdas >> s3_dest    

diag

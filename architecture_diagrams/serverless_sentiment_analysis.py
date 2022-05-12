#!/usr/bin/env python
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda, ECS
from diagrams.aws.database import Dynamodb
from diagrams.aws.analytics import Quicksight
from diagrams.aws.integration import SNS

with Diagram("serverless_sentiment_analysis", show=False, direction="LR") as diag:    
    with Cluster('eu-central-1'):
        ecs = ECS("ECS tw.firehose")
        sns = SNS("sns topic")
        sentiment = Lambda("sentiment analysis")
        dynamo = Dynamodb('sentiment datastore')
        bi = Quicksight("Business Intelligence")

    ecs >> sns >> sentiment >> dynamo >> bi

diag

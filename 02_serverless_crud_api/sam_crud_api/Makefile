.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## build the lambda functions
	sam build

destroy: ## destroy the stack
	aws cloudformation delete-stack --stack-name=sam-crud-api --region=eu-west-1

deploy: ## deploy
	sam deploy

sync: ## watch the project and automatically redeploy
	sam sync --watch --stack-name sam-crud-api

logs: ## get all logs
	sam logs --tail

url: ## get the api url
	aws cloudformation describe-stacks --stack-name=sam-crud-api --region=eu-west-1 | jq -r '.Stacks[0].Outputs[0].OutputValue'

curl-list-zipcodes: ## get all zipcodes
	curl https://9mr391l8ph.execute-api.eu-west-1.amazonaws.com/Prod/zipcode/

list-tables: ## list tables
	aws dynamodb list-tables

describe-table: ## describe the zipcodes table
	aws dynamodb describe-table --table-name zipcodes --region eu-west-1

scan-table: ## show a list of items of zipcode table
	aws dynamodb scan --table-name zipcodes --region eu-west-1

drop-table: ## drop the zipcode table
	aws dynamodb delete-table --table-name zipcodes --region eu-west-1


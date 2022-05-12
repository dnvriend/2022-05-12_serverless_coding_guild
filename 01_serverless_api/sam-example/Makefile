.PHONY: help
.DEFAULT_GOAL := help
endpoint=https://bcipb11hoh.execute-api.eu-west-1.amazonaws.com/Prod/api

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## build the lambda functions
	sam build

destroy: ## destroy the stack
	aws cloudformation delete-stack --stack-name=sam-example --region=eu-west-1

deploy: ## deploy
	sam deploy

sync: ## watch the project and automatically redeploy
	sam sync --watch --stack-name sam-example

logs: ## get all logs
	sam logs --tail

url: ## get the api url
	aws cloudformation describe-stacks --stack-name=sam-example --region=eu-west-1 | jq -r '.Stacks[0].Outputs[1].OutputValue'

curl_root: ## curl root
	curl $(endpoint)

curl_hello_name: ## curl hello name
	curl $(endpoint)/hello/dnvriend

curl_post_user: ## curl users
	curl -X POST -d '{"name": "dennis"}' -H "Content-Type: application/json" $(endpoint)/users

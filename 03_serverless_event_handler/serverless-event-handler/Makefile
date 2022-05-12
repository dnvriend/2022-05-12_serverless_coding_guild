.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## build the lambda functions
	sam build

destroy: ## destroy the stack
	aws cloudformation delete-stack --stack-name=serverless-event-handler --region=eu-west-1

deploy-guided: ## deploy guided
	sam deploy --guided

deploy: ## deploy
	sam deploy

sync: ## watch the project and automatically redeploy
	sam sync --watch --stack-name serverless-event-handler


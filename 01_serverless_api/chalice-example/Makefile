.PHONY: help
.DEFAULT_GOAL := help
endpoint=https://vy8pu0ydeg.execute-api.eu-west-1.amazonaws.com/api/

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

destroy: ## destroy the stack
	chalice delete

deploy: ## deploy
	chalice deploy

url: ## get the api url
	chalice url

curl_root: ## curl root
	curl $(endpoint)

curl_hello_name: ## curl hello name
	curl $(endpoint)/hello/dnvriend

curl_post_user: ## curl users
	curl -X POST -d '{"name": "dennis"}' -H "Content-Type: application/json" $(endpoint)/users

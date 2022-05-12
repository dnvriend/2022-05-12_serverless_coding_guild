.PHONY: help
.DEFAULT_GOAL := help
environment = "example"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

gen: ## generate source code
	go generate ./...

fmt: gen ## formats code
	go fmt ./...

test: fmt ## test code
	go test ./...

build: test ## builds code
	go build

build-and-copy: build ## builds and copies
	mv cet /usr/local/bin

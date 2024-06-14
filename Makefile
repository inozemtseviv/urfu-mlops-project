.PHONY: up
up:
	docker-compose -f ./docker-compose.yaml -p urfu-mlops-project up --build

.PHONY: down
down:
	docker-compose -f ./docker-compose.yaml -p urfu-mlops-project down
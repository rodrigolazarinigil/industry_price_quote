SHELL := /bin/bash

db-up:
	docker-compose -f db/docker-compose.yml build postgres
	docker-compose -f db/docker-compose.yml up -d

build:
	docker-compose -f docker-compose.yml build industry-etl

run:
	make build
	docker-compose -f docker-compose.yml up
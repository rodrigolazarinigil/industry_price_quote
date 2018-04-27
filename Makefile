SHELL := /bin/bash

db-up:
	docker-compose -f db/docker-compose.yml build postgres
	docker-compose -f db/docker-compose.yml up -d

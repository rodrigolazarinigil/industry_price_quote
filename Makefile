SHELL := /bin/bash

db-up:
	docker-compose -f db/docker-compose.yml build postgres
	docker-compose -f db/docker-compose.yml up -d

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

start-airflow:
	export AIRFLOW_HOME=current_dir/airflow
	airflow initdb
	airflow webserver -p 8080
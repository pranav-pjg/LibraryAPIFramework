# Makefile for Library API Automation Framework
# This file provides shortcut commands for test execution and code quality.

.PHONY: install smoke regression negative allure-smoke allure-regression quality format lint clean

install:
	pip install -r requirements.txt

smoke:
	behave -D env=qa --tags=smoke

regression:
	behave -D env=qa --tags=regression

negative:
	behave -D env=qa --tags=negative

allure-smoke:
	rm -rf reports/allure-results/*
	rm -rf reports/allure-report/*
	behave -D env=qa --tags=smoke -f allure_behave.formatter:AllureFormatter -o reports/allure-results
	allure generate reports/allure-results -o reports/allure-report --clean
	python3 -m http.server 5050 --directory reports/allure-report

allure-regression:
	rm -rf reports/allure-results/*
	rm -rf reports/allure-report/*
	behave -D env=qa --tags=regression -f allure_behave.formatter:AllureFormatter -o reports/allure-results
	allure generate reports/allure-results -o reports/allure-report --clean
	python3 -m http.server 5050 --directory reports/allure-report

format:
	black utilities payloads resources features

lint:
	flake8 utilities payloads resources features

quality: format lint

clean:
	rm -rf reports/allure-results/*
	rm -rf reports/allure-report/*
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

#!/bin/bash

# run_smoke_allure.sh
# This script runs smoke tests and generates Allure report.

# Stop script execution if any command fails
set -e

# Move to project root directory
cd ~/projects/LibraryAPIFramework

# Activate Python virtual environment
source .venv/bin/activate

# Clean old Allure result and report files
rm -rf reports/allure-results/*
rm -rf reports/allure-report/*

# Run smoke tests with Allure formatter
behave -D env=qa --tags=smoke \
  -f allure_behave.formatter:AllureFormatter \
  -o reports/allure-results

# Generate Allure HTML report
allure generate reports/allure-results \
  -o reports/allure-report \
  --clean

# Start local HTTP server to view Allure report
# Open http://localhost:5050 in browser
python3 -m http.server 5050 --directory reports/allure-report

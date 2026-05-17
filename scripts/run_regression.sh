#!/bin/bash

# run_regression.sh
# This script runs regression test scenarios using Behave.

# Stop script execution if any command fails
set -e

# Move to project root directory
cd ~/projects/LibraryAPIFramework

# Activate Python virtual environment
source .venv/bin/activate

# Run regression test scenarios
behave -D env=qa --tags=regression

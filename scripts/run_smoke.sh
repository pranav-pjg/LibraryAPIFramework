#!/bin/bash

# run_smoke.sh
# This script runs smoke test scenarios using Behave.

# Stop script execution if any command fails
set -e

# Move to project root directory
cd ~/projects/LibraryAPIFramework

# Activate Python virtual environment
source .venv/bin/activate

# Run smoke test scenarios
behave -D env=qa --tags=smoke

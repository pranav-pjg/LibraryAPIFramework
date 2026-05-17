pipeline {
    agent any

    options {
        timestamps()
    }

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['qa', 'stage', 'prod'],
            description: 'Select environment to run tests'
        )

        choice(
            name: 'TEST_SUITE',
            choices: ['regression', 'smoke', 'negative'],
            description: 'Select test suite to run'
        )
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Verify WSL Ubuntu') {
            steps {
                echo 'Verifying WSL Ubuntu is accessible from Windows Jenkins...'
                bat '''
                    wsl -d Ubuntu bash -lc "echo WSL is working"
                    wsl -d Ubuntu bash -lc "python3 --version"
                '''
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                echo 'Creating Python virtual environment inside Jenkins workspace using WSL...'
                bat '''
                    for /f "delims=" %%i in ('wsl -d Ubuntu wslpath -a "%WORKSPACE%"') do set WSL_WORKSPACE=%%i

                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && python3 -m venv .venv"
                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && source .venv/bin/activate && python --version"
                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && source .venv/bin/activate && pip install --upgrade pip"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                bat '''
                    for /f "delims=" %%i in ('wsl -d Ubuntu wslpath -a "%WORKSPACE%"') do set WSL_WORKSPACE=%%i

                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && source .venv/bin/activate && pip install -r requirements.txt"
                '''
            }
        }

        stage('Clean Old Reports') {
            steps {
                echo 'Cleaning old Allure report files and creating runtime folders...'
                bat '''
                    for /f "delims=" %%i in ('wsl -d Ubuntu wslpath -a "%WORKSPACE%"') do set WSL_WORKSPACE=%%i

                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && mkdir -p logs"
                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && mkdir -p reports/allure-results"
                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && mkdir -p reports/allure-report"

                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && rm -rf reports/allure-results/*"
                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && rm -rf reports/allure-report/*"
                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && rm -f logs/execution.log"
                '''
            }
        }

        stage('Run Behave Tests') {
            steps {
                echo "Running ${params.TEST_SUITE} tests on ${params.ENVIRONMENT} environment..."
                bat '''
                    for /f "delims=" %%i in ('wsl -d Ubuntu wslpath -a "%WORKSPACE%"') do set WSL_WORKSPACE=%%i

                    wsl -d Ubuntu bash -lc "cd %WSL_WORKSPACE% && source .venv/bin/activate && behave -D env=%ENVIRONMENT% --tags=%TEST_SUITE% -f allure_behave.formatter:AllureFormatter -o reports/allure-results"
                '''
            }
        }
    }

    post {
        always {
            echo 'Publishing Allure report in Jenkins...'

            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'reports/allure-results']]
            ])

            archiveArtifacts artifacts: 'reports/allure-results/**', fingerprint: true, allowEmptyArchive: true

            echo 'Pipeline execution completed.'
        }

        success {
            echo 'Automation pipeline passed successfully.'
        }

        failure {
            echo 'Automation pipeline failed.'
        }
    }
}

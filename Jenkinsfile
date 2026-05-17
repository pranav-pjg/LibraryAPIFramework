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
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python --version
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                sh '''
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Clean Old Reports') {
            steps {
                echo 'Cleaning old Allure report files...'
                sh '''
                    rm -rf reports/allure-results/*
                    rm -rf reports/allure-report/*
                '''
            }
        }

        stage('Run Behave Tests') {
            steps {
                echo "Running ${params.TEST_SUITE} tests on ${params.ENVIRONMENT} environment..."
                sh '''
                    . .venv/bin/activate
                    behave -D env=${ENVIRONMENT} --tags=${TEST_SUITE} \
                    -f allure_behave.formatter:AllureFormatter \
                    -o reports/allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                sh '''
                    allure generate reports/allure-results \
                    -o reports/allure-report \
                    --clean
                '''
            }
        }
    }

    post {
        always {
            echo 'Archiving Allure reports...'

            archiveArtifacts artifacts: 'reports/allure-report/**', fingerprint: true

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

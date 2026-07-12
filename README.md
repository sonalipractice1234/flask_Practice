# Flask CI/CD Pipeline using Jenkins and GitHub Actions

## Project Overview

This project demonstrates the implementation of Continuous Integration and Continuous Deployment (CI/CD) for a Flask web application using **Jenkins** and **GitHub Actions**.

The CI/CD pipeline automates the following tasks:

* Installing project dependencies
* Running automated tests
* Building the application
* Deploying the application to a staging environment
* Triggering production deployment when a release tag is created

---

# Project Repository

Repository URL:

```
https://github.com/YOUR_GITHUB_USERNAME/flask_Practice
```

---

# Technologies Used

* Python 3
* Flask
* Jenkins
* GitHub Actions
* Git
* Docker
* Pytest
* Ubuntu (WSL)
* Windows 11

---

# Prerequisites

Before running this project, install the following software:

* Git
* Python 3.11 or later
* pip
* Docker Desktop
* Jenkins (Running in Docker)
* Ubuntu (WSL)
* GitHub Account

Verify installation:

```bash
python3 --version
git --version
docker --version
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/flask_Practice.git
```

Go to the project directory:

```bash
cd flask_Practice
```

---

## Create Virtual Environment

Linux / Ubuntu

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Install pytest

```bash
pip install pytest
```

---

# How to Run Locally

Start the Flask application:

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

The Flask application should load successfully.

---

# Run Unit Tests

Execute:

```bash
pytest
```

If all tests pass, the application is ready for deployment.

---

# Jenkins CI/CD Pipeline

The Jenkins pipeline is defined inside the **Jenkinsfile**.

Pipeline stages:

## Stage 1 – Build

* Install Python dependencies
* Prepare the application

Command executed:

```bash
pip install -r requirements.txt
```

---

## Stage 2 – Test

* Run automated unit tests using pytest

Command executed:

```bash
pytest
```

---

## Stage 3 – Deploy

If all tests pass, Jenkins deploys the application to the staging environment.

(Current deployment is demonstrated using an echo command for assignment purposes.)

---

# Jenkins Pipeline Flow

```
Developer
      │
      ▼
Git Push
      │
      ▼
Jenkins Trigger
      │
      ▼
Build
      │
      ▼
Test
      │
      ▼
Deploy
```

---

# GitHub Actions Workflow

Workflow file:

```
.github/workflows/ci.yml
```

The workflow automatically performs:

* Checkout repository
* Install Python
* Install project dependencies
* Run unit tests
* Build the application
* Deploy to Staging
* Deploy to Production

---

# Workflow Triggers

## Push to main

Runs:

* Build
* Test

---

## Push to staging

Runs:

* Build
* Test
* Deploy to Staging

---

## Release Tag

Creating a tag such as:

```bash
git tag v1.0
git push origin v1.0
```

Triggers:

* Build
* Test
* Deploy to Production

---

# Branch Strategy

This project uses two primary branches.

## main

* Production-ready code
* Runs Build and Test workflow

## staging

* Used for testing before production deployment
* Automatically deploys to the staging environment

---

# GitHub Secrets Configuration

The following repository secrets are configured under:

Settings → Secrets and Variables → Actions

Example secrets:

| Secret Name    | Purpose                   |
| -------------- | ------------------------- |
| AWS_ACCESS_KEY | AWS authentication        |
| AWS_SECRET_KEY | AWS authentication        |
| DEPLOY_KEY     | Deployment authentication |
| API_TOKEN      | API authentication        |

> Secret values are securely stored in GitHub and are never committed to the repository.

---

# Jenkins Configuration

Pipeline Type:

```
Pipeline from SCM
```

Repository:

```
https://github.com/YOUR_GITHUB_USERNAME/flask_Practice.git
```

Branch:

```
main
```

Script:

```
Jenkinsfile
```

---

# Email Notification

Jenkins is configured to send email notifications after every build.

Notifications include:

* Build Success
* Build Failure

SMTP Server:

```
smtp.gmail.com
```

Port:

```
587
```

---

# Project Structure

```
flask_Practice/
│
├── app.py
├── requirements.txt
├── Jenkinsfile
├── README.md
├── tests/
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

# Screenshots

Include the following screenshots in your repository or report:

### Jenkins

* Jenkins Dashboard
* Pipeline Configuration
* Successful Build
* Stage View (Build → Test → Deploy)

### GitHub Actions

* Workflow Run
* Build Job
* Test Job
* Deploy to Staging Job
* Deploy to Production Job

### GitHub

* Repository Home Page
* Branches (main and staging)
* GitHub Secrets (hide secret values)

---

# Future Improvements

Possible enhancements include:

* Docker image creation
* Docker Hub integration
* AWS EC2 deployment
* Kubernetes deployment
* SonarQube code quality analysis
* Automated security scanning

---

# Author

**Name:** Sonali Patil

**Project:** Jenkins CI/CD Pipeline & GitHub Actions for Flask Application

**Assignment:** CI/CD Implementation using Jenkins and GitHub Actions

# staging update

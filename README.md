# Project 1: Basic CI/CD Pipeline with GitHub Actions

## Overview

This project demonstrates setting up a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions. The project consists of a simple Flask application with a basic test suite using `pytest`. The GitHub Actions workflow automatically builds and tests the application whenever changes are pushed to the repository.

## Prerequisites

- A GitHub account
- Python installed on your local machine
- Git installed on your local machine
- Basic knowledge of Git and Python

## Project Structure

```
your-repository/
│
├── app.py
├── requirements.txt
├── test_app.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Step-by-Step Guide

### 1. Set Up Your GitHub Repository

1. Create a new repository on GitHub.
2. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

### 2. Create a Sample Flask Application

1. Create a file named `app.py` in the root of your project directory and add the following content:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return "Hello, World!"

   if __name__ == "__main__":
       app.run()
   ```

### 3. Create a `requirements.txt` File

1. Create a `requirements.txt` file in the root of your project directory with the following content:
   ```plaintext
   flask
   pytest
   ```

### 4. Write Tests for Your Application

1. Create a file named `test_app.py` in the root of your project directory and add the following content:
   ```python
   from app import app

   def test_home():
       with app.test_client() as client:
           response = client.get('/')
           assert response.data == b'Hello, World!'
   ```

### 5. Create GitHub Actions Workflow

1. In your repository, create a directory named `.github/workflows`:
   ```sh
   mkdir -p .github/workflows
   ```

2. Inside the `workflows` directory, create a file named `ci.yml` with the following content:
   ```yaml
   name: CI

   on:
     push:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout code
         uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.8'

       - name: Install dependencies
         run: |
           python -m venv venv
           . venv/bin/activate
           pip install -r requirements.txt

       - name: Run tests
         run: |
           . venv/bin/activate
           pytest
   ```

### 6. Commit and Push Your Changes

1. Stage, commit, and push your changes to GitHub:
   ```sh
   git add .
   git commit -m "Set up Flask app and GitHub Actions workflow"
   git push origin main
   ```

### 7. Verify Your GitHub Actions Workflow

1. Go to your GitHub repository on the web.
2. Click on the `Actions` tab to see the workflow run. You should see your tests being executed automatically whenever you push changes to the repository.

## Running Tests Locally

To ensure everything works correctly before pushing to GitHub, you can run your tests locally:

1. **Set up a virtual environment**:
   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```sh
   python app.py
   ```

5. **Run the tests**:
   ```sh
   pytest
   ```

You should see output indicating that the tests have passed.

## Conclusion

This project sets up a basic CI/CD pipeline using GitHub Actions to automatically build and test a simple Flask application whenever changes are pushed to the repository. By following the steps in this guide, you can ensure your application is continuously tested, improving code quality and reliability.

# Calc-py

The Calculator is a Python program that provides a command-line calculator with various mathematical operations. It was developed following CI/CD principles, 
ensuring continuous integration and delivery of the application. The project incorporates a Jenkins pipeline that is triggered by a WebHook on each commit to the designated branch. 
The pipeline includes steps to build a Docker image using the provided Dockerfile, run tests, and push the image to DockerHub.

## Features

The Calculator program offers the following features:

    Addition: Adds two numbers together.
    Subtraction: Subtracts one number from another.
    Multiplication: Multiplies two numbers.
    Division: Divides one number by another.
    Power: Raises a number to a given exponent.
    Square Root: Calculates the square root of a number.
    Sine: Calculates the sine of an angle.
    Cosine: Calculates the cosine of an angle.
    Tangent: Calculates the tangent of an angle.
    Logarithm: Calculates the logarithm of a number.
    
## Requirements

    Python 3.x
    Docker (for running the Jenkins pipeline)
    
## Usage
Clone the repository:

```
git clone https://github.com/Ryadhmd/Calc-py.git
```

Navigate to the project directory:

```
cd calculator
```

Run the calculator.py file:
```
python calculator.py
```

## Continuous Integration and Delivery (CI/CD)

The Calculator project incorporates CI/CD principles to ensure the development process is streamlined and reliable. The Jenkins pipeline defined in the Jenkinsfile automates the build, test, and deployment processes. Here's an overview of the pipeline steps:

    WebHook Trigger: The Jenkins pipeline is triggered by a WebHook upon each commit to the designated branch.
    Build: The Docker image is built using the provided Dockerfile.
    Test: The pipeline executes functional tests using pytest to validate the correctness of the Calculator program.
    Push: The built Docker image is pushed to DockerHub, making it accessible for deployment or further use.

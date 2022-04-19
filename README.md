# Behave project

# Make sure python environment setup correctly in your machine
# Python 3.10.2

# Commands to run before start test
pip install -r requirements.txt
sbase install chromedriver latest

# How to run single feature file
behave features\login.feature 

# How to run all feature files
behave features\

# Execute test and Generate report
behave -f allure_behave.formatter:AllureFormatter -o reports/ features

# Open Allure Report
allure serve reports/
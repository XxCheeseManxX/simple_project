## Automating tests with GitHub Actions

[Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) is a 
CI/CD platform that allows us to automate things like building our project, running tests and deployments

We will create a workflow to run pytest on a push or pull request

# Make the workflow directory

A workflow is a automated process that will run when a certain event occurs (like pull requests/push) 

In the project's root:
1. `mkdir .github`
2. `cd .github`
3. `mkdir workflows`
4. `cd workflows`

Create the YAML file (YAML is a markup language that is commonly used in configuration files)

`code pytest.yml`

# Creating the PyTest workflow

```
# The name of the workflow
name: Pytest

# Specifies the trigger for our workflow
on: [push, pull_request]

jobs:
    test:
        
      # Creates environment/vm using the latest version of Ubuntu
      runs-on: ubuntu-latest

      steps:
        # An action that checks out our repository into the environment
        - uses: actions/checkout@v4

        # Sets up Python in our environment
        - name: Set Up Python
          uses: actions/setup-python@v5
          with:
            python-version: '3.10'
        
        - name: Install dependencies
          # How we can run command line commands
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
            pip install -U pytest
            pip install -e .

        # Running Pytest!
        - name: Test with pytest
          run: |
            python -m pytest
```

# Pushing to the repo!

Navigate to project's root

1. `git add .github/`
2. `git add .github/workflows/pytest.yml`
3. `git commit -m "pytest github action"`
4. `git push`

The test will run!
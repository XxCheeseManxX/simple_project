## Setting up a linter & formatter!

**What is a linter?**

Linting is the verification of a code's style. Typically, Python linters verify your code's style
againt [PEP8](https://peps.python.org/pep-0008/), the official Python style. Pep8 is a style guide for Python

You don't have to lint. If you're working on a solo project and you understand the code you write, 
its fine not to. But if you're working with other developers on a shared codebase, linting helps keep
code readable and consistent, and can find logical bugs. Focuses on syntax errors, possible bugs, inefficient code, etc

**What is a formatter?**

A code formatter will automatically format your code to a consistent style. Concerned with the appearance of code,
like indentation, spacing, line breaks, etc

# Using Ruff!

[Ruff](https://github.com/astral-sh/ruff) is a Python linter and code formatter

**Installation**

`pip install ruff`

**Using**

Navigate to the root of the project

Create a config file for ruff, `ruff.toml`

Add this:
```
# ruff.toml
line-length = 79
select = ["ALL"]
```
Using `select = ["ALL"]` tells ruff to enforce all rules in the default config file(see on GitHub)


* To run the linter: `ruff check`

* To run the formatter: `ruff format`

* To see which files changed: `git status`

# Setting up ruff to run as a pre-commit hook!

A pre-commit hook is a script/command that runs automatically before a commit is make to the repo
Runs when we commit

Installing pre-commit: `pip install pre-commit`

Create a pre-commit yaml file in the project root:

* `code .pre-commit-config.yaml`

From the ruff github page, we copy this:
```
repos: 
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.4.10
  hooks:
    # Run the linter.
    - id: ruff
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
```

Install pre-commit:

* `pre-commit install`

Now, we should have the pre-commit working!


# Setting up to run ruff in GitHub Actions

1. `cd .github/workflows`
2. `code ruff.yaml`
3. Paste in the code from the Ruff GitHub:
```
name: Ruff
on: [ push, pull_request ]
jobs:
  ruff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: chartboost/ruff-action@v1
```

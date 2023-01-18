# conf42-2022-cicd-demo
Demo for my talk at Conf42 about universal CI/CD pipeline


## Notes

We use [`pyenv`](https://github.com/pyenv/pyenv) to pin the python version using `pyenv local <version>`. This generate a `.python-version` which is used to sync python version between the developer local environment and the CI environment.

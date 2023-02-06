# Getting Started

## Installation

```bash
pip install ppqq
```

## Usage
```python
from ppqq import Cleaner

clr = Cleaner()

inputs = [
    "Hello! my email address is user@email.com.",
    "I really like this website: www.random.website.com/resource/example",
]

print(clr.transform(inputs))
# ['hello my email address is emailtk', 'i really like this website urltk']
```

## Development

### Local

Required tools:
- [Poetry](https://python-poetry.org)
- [Python (pyenv)](https://github.com/pyenv/pyenv)


Install a compatible Python version.

```bash
pyenv install <python version>
```

Make it global.

```bash
pyenv global <python version>
```



Make poetry use the new python interpreter for virtualenv creation.

```bash
poetry env use $(which python)
```

Install the project and all its dependencies.

```bash
poetry install
```

Launch subshell if the environment doesn't activate automatically.

```bash
poetry shell
```

Install pre-commit hooks.

```bash
pre-commit install
```

### Docker

```bash
docker build \
    -t ppqq \
    --build-arg PYTHON_VERSION=<python version> \
    --build-arg WORKDIR=/workdir .
```
```bash
docker run \
    -i \
    --mount type=bind,source=$(pwd),target=/workdir \
    -t ppqq
```

Install the project and all its dependencies.

```bash
poetry install
```

Launch subshell if the environment doesn't activate automatically.

```bash
poetry shell
```

Install pre-commit hooks.

```bash
pre-commit install
```


## Testing
We use pytest for testing.

Run tests (this will look and run every testfile and function).

```
coverage run -m pytest
```

Or use the command

```
make test
```

Generate HTML coverage report.
```
coverage html
```

Open website to see code coverage.
```
open htmlcov/index.html
```

Or you can run both commands using

```
make coverage-report
```

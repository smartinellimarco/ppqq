ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

# Set working directory.
WORKDIR ${WORKDIR}

# Update dependencies.
RUN apt update -y
RUN apt upgrade -y

# Install poetry.
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add poetry binary folder to path.
ENV PATH="/root/.local/bin:${PATH}"

# Run newer shell.
CMD ["bash"]

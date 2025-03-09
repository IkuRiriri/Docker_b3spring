ARG PYTHON_VER="3.8-slim"
FROM python:${PYTHON_VER}

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY . /app/

CMD ["python3", "sample.py"]
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev \
    pkg-config

RUN export MYSQL_CFLAGS=$(mysql_config --cflags)
RUN export MYSQL_LIBS=$(mysql_config --libs)

COPY requirements.txt .

#RUN pip install -r requirements.txt
RUN pip3 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install --no-cache-dir -r requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "4"]

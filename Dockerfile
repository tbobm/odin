FROM python:3.8-slim
RUN apt-get -y update && apt-get install -y netbase build-essential libffi-dev python-dev

WORKDIR /app


# Install python deps first
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy sources
COPY ./ .

# Install package
RUN python setup.py install

ENTRYPOINT ["sh", "-c", "odin"]

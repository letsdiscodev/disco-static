FROM python:3.12.3
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install requirements.txt
COPY . /code/.
RUN python generate.py
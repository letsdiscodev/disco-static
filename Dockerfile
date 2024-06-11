FROM python:3.12.3
WORKDIR /site
COPY requirements.txt /site/requirements.txt
RUN pip install -r requirements.txt
COPY . /site/.
RUN python generate.py
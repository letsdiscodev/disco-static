FROM python:3.12.3

WORKDIR /site

# copy any files you need to install the project's requirements.
COPY requirements.txt /site/requirements.txt
RUN pip install -r requirements.txt

# done! copy all of the files to actually generate the site
COPY . /site/.
# generate the site.
RUN python generate.py
# done.

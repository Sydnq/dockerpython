FROM python:3.6.4-alpine3.7
ENV workdir = /dockerpython
COPY . $workdir
WORKDIR $workdir
RUN pip install -r requirements.txt
CMD ["python", "jsonld.py"]

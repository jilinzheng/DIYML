FROM python:3.12
WORKDIR /diyml
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
CMD python3 ./src/worker.py
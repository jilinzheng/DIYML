FROM python:3.12
WORKDIR /diyml
COPY . /diyml
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
CMD python ./src/diyml.py
FROM debian:12
RUN apt update
RUN apt install python3 python3-pip -y
RUN apt install python3.11-venv -y
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /diyml
COPY . /diyml
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
#EXPOSE 6379
RUN chmod a+x run.sh
#CMD python3 ./src/diyml.py
CMD ./run.sh
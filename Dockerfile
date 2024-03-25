FROM python:3.8-alpine
RUN apk update
RUN apk --update --upgrade add --no-cache gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev make automake gcc g++ subversion python3-dev gfortran
WORKDIR /diyml
COPY . /diyml/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./src/diyml.py
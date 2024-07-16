FROM python:3.9-alpine

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN ln -s /app/web /app/web/${FLASK_BASE_PATH}

RUN echo "FLASK_BASE_PATH=${FLASK_BASE_PATH}"

RUN apk update && apk add build-base linux-headers

CMD [ "python","./run.py" ]

EXPOSE 5000

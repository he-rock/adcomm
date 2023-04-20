FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./app .
COPY ./requirements.txt /tmp/

RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
	pip install -r /tmp/requirements.txt && \
	rm -rf /tmp && \
    apk del .tmp-build-deps && \
	adduser --disabled-password --no-create-home herock && \
	mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R herock:herock /vol && \
    chmod -R 755 /vol

USER herock
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
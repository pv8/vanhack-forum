FROM python:3.12.0a1-alpine

LABEL maintainer="Pablo Vieira <povieira@gmail.com>"

# stdout and stderr streams unbuffered
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && \
  apk add --no-cache bash && \
  apk add sqlite

WORKDIR /app
COPY ./requirements/ /app/requirements/
COPY ./docker/development/web/start.sh /bin/start.sh
COPY ./docker/development/web/entrypoint.sh /bin/entrypoint.sh

RUN chmod +x /bin/start.sh && chmod +x /bin/entrypoint.sh && \
  pip install -r /app/requirements/development.txt

EXPOSE 8000

ENTRYPOINT ["/bin/entrypoint.sh"]

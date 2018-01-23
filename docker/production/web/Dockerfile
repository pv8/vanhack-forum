FROM python:3.6-alpine

LABEL maintainer="Pablo Vieira <povieira@gmail.com>"

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && \
  apk add --no-cache bash postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY . /app
COPY ./docker/production/web/start.sh /bin/start.sh
COPY ./docker/production/web/entrypoint.sh /bin/entrypoint.sh

COPY ./docker/production/db/backup.sh /bin/backup.sh
COPY ./docker/production/db/list-backups.sh /bin/list-backups.sh
COPY ./docker/production/db/restore.sh /bin/restore.sh

# create 'vanhack' user
RUN addgroup -S vanhack && adduser -S -g vanhack vanhack && \
  chown -R vanhack /app && \
  # change helper scripts permissions
  chmod +x /bin/start.sh && chmod +x /bin/entrypoint.sh && \
  chmod +x /bin/backup.sh && chmod +x /bin/list-backups.sh && \
  chmod +x /bin/restore.sh && \
  # change helper scripts ownership
  chown vanhack /bin/start.sh && chown vanhack /bin/entrypoint.sh && \
  chown vanhack /bin/backup.sh && chown vanhack /bin/list-backups.sh && \
  chown vanhack /bin/restore.sh && \
  # install app dependencies
  pip install --no-cache-dir -r /app/requirements/production.txt && \
  # remove build dependencies
#  rm -rf /app/requirements && \
#  apk del postgresql-dev gcc python3-dev musl-dev
  echo "Done!"

USER vanhack

# ENTRYPOINT ["/bin/entrypoint.sh"]

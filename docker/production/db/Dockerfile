FROM postgres:10-alpine

COPY ./docker/production/db/backup.sh /bin/backup
COPY ./docker/production/db/restore.sh /bin/restore
COPY ./docker/production/db/list-backups.sh /bin/list-backups

RUN chmod +x /bin/backup && \
  chmod +x /bin/restore && \
  chmod +x /bin/list-backups
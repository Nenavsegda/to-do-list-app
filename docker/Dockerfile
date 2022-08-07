FROM python:3.8-bullseye

RUN mkdir -p var/www/to-do-list-app
COPY . var/www/to-do-list-app/
RUN cd var/www/to-do-list-app && pip install --no-cache-dir -r requirements.txt

WORKDIR var/www/to-do-list-app
RUN chmod +x docker/docker-entrypoint.sh

ENTRYPOINT ["docker/docker-entrypoint.sh"]

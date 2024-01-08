FROM node:6-alpine

LABEL Author="Virink <virink@outlook.com>"
LABEL Blog="https://www.virzz.com"

COPY files /tmp

RUN mkdir /app && \
	mv /tmp/*.js* /app/ && \
	cd /app/ && \
	yarn install && \
	chmod +x /tmp/docker-entrypoint && \
	mv /tmp/docker-entrypoint /usr/local/bin/docker-entrypoint

EXPOSE 3000

ENTRYPOINT ["sh","-c","docker-entrypoint"]
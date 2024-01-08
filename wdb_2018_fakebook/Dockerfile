FROM php:5.6-fpm-alpine

LABEL Author="Virink <virink@outlook.com>"
LABEL Blog="https://www.virzz.com"

COPY files /tmp/src

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
	&& apk update \
    && apk add --no-cache tar nginx mysql mysql-client \
    && docker-php-source extract \
    && docker-php-ext-install mysqli \
    && docker-php-source delete \
    && mysql_install_db --user=mysql --datadir=/var/lib/mysql \
    && sh -c 'mysqld_safe &' \
	&& sleep 5s \
    && mysqladmin -uroot password 'naiwjebfahjebfja' \
    && mysql -e "source /tmp/src/db.sql;" -uroot -pnaiwjebfahjebfja \
    && mkdir /run/nginx \
    && mv /tmp/src/docker-php-entrypoint /usr/local/bin/docker-php-entrypoint \
    && mv /tmp/src/nginx.conf /etc/nginx/nginx.conf \
    && mv /tmp/src/vhost.nginx.conf /etc/nginx/conf.d/default.conf \
    && cp /usr/local/etc/php/php.ini-production /usr/local/etc/php/php.ini \
    && sed -i -e 's/display_errors.*/display_errors = Off/' /usr/local/etc/php/php.ini \
    && mv /tmp/src/* /var/www/html \
    # && mkdir /var/www/html/upload \
    && chmod -R -w /var/www/html \
    # && chmod -R 777 /var/www/html/upload \
    && chown -R www-data:www-data /var/www/html \
    && chmod +x /usr/local/bin/docker-php-entrypoint \
    && rm -rf /var/www/html/db.sql \
    && rm -rf /tmp/* \
    && rm -rf /etc/apk

EXPOSE 80

VOLUME ["/var/log/nginx"]

CMD ["sh","-c","docker-php-entrypoint"]
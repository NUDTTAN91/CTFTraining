FROM php:5.6-fpm-alpine

LABEL Author="Virink <virink@outlook.com>"
LABEL Blog="https://www.virzz.com"

COPY files /tmp/src

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
	&& apk update \
    && apk add --no-cache nginx mysql mysql-client python py-pip chromium chromium-chromedriver \
    && pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com selenium requests \
    && docker-php-source extract \
    && docker-php-ext-install mysqli \
    && docker-php-source delete  \
    # Mysql
    && mysql_install_db --user=mysql --datadir=/var/lib/mysql \
    && sh -c 'mysqld_safe &' \
	&& sleep 5s \
    && mysqladmin -uroot password 'hyaiuehdbnhfuyoa' \
    && mysql -e "source /tmp/src/hctf2017.sql;" -uroot -phyaiuehdbnhfuyoa \
    && mkdir /run/nginx \
    # Move
    && mv /tmp/src/docker-php-entrypoint /usr/local/bin/docker-php-entrypoint \
    && mv /tmp/src/nginx.conf /etc/nginx/nginx.conf \
    && mv /tmp/src/vhost.nginx.conf /etc/nginx/conf.d/default.conf \
    && mv /tmp/src/bot.py /root/boy.py \
    && mv /tmp/src/* /var/www/html \
    && chown -R www-data:www-data /var/www/html \
    && chmod +x /usr/local/bin/docker-php-entrypoint \
    # Clear
    && rm /var/www/html/hctf2017.sql \
    && rm -rf /tmp/* /etc/apk /var/cache/apk

EXPOSE 80

VOLUME ["/var/log/nginx"]

CMD ["sh","-c","docker-php-entrypoint"]
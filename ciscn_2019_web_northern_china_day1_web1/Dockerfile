FROM ctftraining/base_image_nginx_mysql_php_56

LABEL Author="glzjin <i@zhaoj.in>" Blog="https://www.zhaoj.in"

COPY src /var/www/html

RUN chown -R www-data:www-data /var/www/html/uploads && \
    mv /var/www/html/flag.sh / && \
    chmod +x /flag.sh

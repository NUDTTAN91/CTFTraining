FROM phusion/baseimage
LABEL Author="Blaklis"
RUN apt-get update && apt-get install libapache2-mod-php -y
RUN echo "flag{a956dcd6-1ede-11e9-9dc1-1b6d60f1f212}" > /flag
RUN mkdir /var/www/html/users/
COPY index.php /var/www/html/
COPY php-entrypoint /etc/my_init.d/
COPY php.ini /etc/php/7.0/apache2/
COPY get_flag /
RUN chmod 400 /flag && chmod u+x+s /get_flag && rm /var/www/html/index.html && chmod +x /etc/my_init.d/php-entrypoint && chown -R www-data:www-data /var/www/html/ && service apache2 start
EXPOSE 80

FROM phusion/baseimage
LABEL Author="eboda"
RUN apt-get update && apt-get install libapache2-mod-php php-mbstring -y
RUN echo "9fb0103a-1d4e-11e9-9838-efba0d815406" > /flag
COPY get_flag /
COPY index.php /var/www/html/
COPY php-entrypoint /etc/my_init.d/
COPY apache2.conf /etc/apache2/
COPY php.ini /etc/php/7.0/apache2/
RUN chmod 400 /flag && chmod u+x+s /get_flag&& rm /var/www/html/index.html && a2enmod rewrite && mkdir /var/www/html/images/ && chmod +x /etc/my_init.d/php-entrypoint && chown -R www-data:www-data /var/www/html/ && service apache2 start
EXPOSE 80
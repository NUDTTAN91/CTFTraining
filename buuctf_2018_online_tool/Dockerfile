FROM ctftraining/base_image_nginx_php_56

LABEL Author="tan 91"
LABEL Blog="zxw-nudt.blog.csdn.net"

COPY ./files /var/www/
RUN apk add nmap
RUN chown -R www-data:www-data /var/www/
RUN chmod -R 777 /var/www/

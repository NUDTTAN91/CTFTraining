FROM phusion/baseimage
LABEL Author="Unknown"
RUN apt-get update && apt-get install apache2 python3 -y
RUN echo "flag{4ebb0f38-1de2-11e9-9c69-0f59b1c2ce2a}" > /var/www/flag
RUN mkdir /var/www/cgi-bin
RUN chown www-data:www-data  /var/www/flag
RUN a2enmod cgi
COPY pycalx.py /usr/lib/cgi-bin/
COPY pycalx2.py /usr/lib/cgi-bin/
RUN chmod +x /usr/lib/cgi-bin/pycalx.py /usr/lib/cgi-bin/pycalx2.py
COPY cgi-entrypoint /etc/my_init.d/
RUN chmod +x /etc/my_init.d/cgi-entrypoint
EXPOSE 80

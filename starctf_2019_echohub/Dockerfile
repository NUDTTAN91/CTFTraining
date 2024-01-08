FROM ubuntu:18.04

LABEL Author="Virink <virink@outlook.com>"
LABEL Blog="https://www.virzz.com"

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.ustc.edu.cn/g" /etc/apt/sources.list && \
    sed -i "/security.ubuntu.com/d" /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata software-properties-common && \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install vim apache2 && \
    apt-cache search "php" | grep "php7.3"| awk '{print $1}'| xargs apt-get -y install && \
    service --status-all | awk '{print $4}'| xargs -i service {} stop && \
    rm /var/www/html/index.html

# COPY randomstack.php /var/www/html/index.php
# COPY sandbox.php /var/www/html/sandbox.php

COPY source /var/www/html

RUN chmod 755 -R /var/www/html/ && \
    mv /var/www/html/flag /flag && \
    mv /var/www/html/readflag /readflag && \
    mv /var/www/html/run.sh /run.sh && \
    mv /var/www/html/php.ini /etc/php/7.3/apache2/php.ini && \
    chmod 555 /readflag && \
    chmod u+s /readflag && \
    chmod 500 /flag && \
    chmod 700 /run.sh

CMD ["/run.sh"]

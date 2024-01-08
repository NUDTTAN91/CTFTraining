FROM php:5.6-apache-jessie

COPY src/ /var/www/html/

RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
	sed -i '/security/d' /etc/apt/sources.list && \
	apt-get update -y \
    && apt install -y libwww-perl \
    && rm -rf /etc/apt/* \
    && mv /var/www/html/GET /usr/bin/GET \
    && mv /var/www/html/readflag /readflag \
    # sandbox
    && mkdir /var/www/html/sandbox \
    && chmod -R 777 /var/www/html/sandbox \
    # remote ip
    && echo 'RemoteIPHeader X-Forwarded-For' >> /etc/apache2/mods-available/remoteip.load \
    && echo 'RemoteIPProxiesHeader X-Forwarded-For' >> /etc/apache2/mods-available/remoteip.load \
    && a2enmod remoteip \
    && sed -i -e '3s/.*/echo ZXZhbCAic2VkIC1pIC1lIFwicy9SZW1vdGVJUEludGVybmFsUHJveHkuKi9SZW1vdGVJUEludGVybmFsUHJveHkgXCQoY2F0IC9ldGMvaG9zdHMgfCBhd2sgJ0VORCB7cHJpbnQgXCQxfScpXC8yNC9cIiAvZXRjL2FwYWNoZTIvbW9kcy1hdmFpbGFibGUvcmVtb3RlaXAubG9hZCI= | base64 -d | sh/' /usr/local/bin/docker-php-entrypoint \
		&& mv /var/www/html/start.sh /start.sh \
		&& chmod +x /start.sh

ENTRYPOINT ["/start.sh"]

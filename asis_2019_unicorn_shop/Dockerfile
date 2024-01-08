FROM python:2.7-alpine

LABEL Author="Tiaonmmn.ZMZ <tiaonmmn@live.cn>"

ADD src/ /app/

WORKDIR /app

RUN pip install -i https://pypi.douban.com/simple/ \
                -r /app/requirements.pip &&\
    chmod +x /app/main.py /app/sshop/models.py &&\
    python sshop/models.py &&\
    mv /app/start.sh / &&\
    chmod +x /start.sh

EXPOSE 6732

ENTRYPOINT ["/start.sh"]   

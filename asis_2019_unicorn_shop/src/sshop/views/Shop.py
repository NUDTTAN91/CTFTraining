# -*- coding:utf-8 -*-
import sys
import unicodedata
import urllib

from sqlalchemy.orm.exc import NoResultFound

from sshop.base import BaseHandler
from sshop.models import Commodity

reload(sys)
sys.setdefaultencoding('utf8')


class ChargeHandler(BaseHandler):

    def get(self, *args, **kwargs):
        commoditys = self.orm.query(Commodity) \
            .order_by(Commodity.price.asc()).all()
        return self.render('charge.html', commoditys=commoditys)

    def post(self, *args, **kwargs):
        commoditys = self.orm.query(Commodity)
        id = self.get_argument('id')
        price = str(self.get_argument('price'))
        try:
            price = urllib.unquote(price).decode('utf-8')
        except UnicodeDecodeError:
            return self.render('charge.html', danger=1, commoditys=commoditys,
                               dangermessage="Error parsing money!")
        if len(price) > 1:
            return self.render('charge.html', danger=1, commoditys=commoditys, dangermessage="Only one char(?) allowed!")
        try:
            unicodedata.numeric(price)
        except ValueError:
            return self.render('charge.html', danger=1, commoditys=commoditys, dangermessage="Error parsing money!")

        # return self.render('charge.html', danger=1, commoditys=commoditys, preview=page - 1, next=page + 1,
        #                    limit=limit,
        #                    dangermessage="测试专用。当前输入字符为：{0}，其Unicode名称为：{1}，其Unicode numeric为：{2}".format(price,
        #                                                                                                  unicodedata.name(
        #                                                                                                      price),unicodedata.numeric(price)))
        try:
            commoditys = self.orm.query(Commodity).filter(Commodity.id == id).one()
        except NoResultFound:

            return self.render('charge.html', danger=1, commoditys=commoditys,
                               dangermessage="No commodity found!")
        if commoditys.english == 'ultra unicorn':
            if unicodedata.numeric(price) >= commoditys.price:
                commoditys = self.orm.query(Commodity) \
                    .order_by(Commodity.price.asc()).all()
                return self.render('charge.html', success=1, commoditys=commoditys,
                                   successmessage="flag{aa4059c8-8d0b-442d-bc89-7f8d8846be26}")
            else:
                commoditys = self.orm.query(Commodity).all()
                return self.render('charge.html', danger=1, commoditys=commoditys,
                                   dangermessage="You don't have enough money!")
        else:
            commoditys = self.orm.query(Commodity).all()
            return self.render('charge.html', danger=1, commoditys=commoditys,
                               dangermessage="Wrong commodity!")

# coding=utf-8
import os
import sys

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import FLOAT, VARCHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

reload(sys)
sys.setdefaultencoding('utf8')
from settings import connect_str

BaseModel = declarative_base()
engine = create_engine(connect_str, echo=True, pool_recycle=3600)
db = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True))


class Commodity(BaseModel):
    __tablename__ = 'commoditys'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    price = Column(FLOAT, nullable=False)
    english = Column(VARCHAR(200), unique=True, nullable=False)
    spanish = Column(VARCHAR(500), default='no description')
    german = Column(VARCHAR(500), default='no description')
    russian = Column(VARCHAR(500), default='no description')

    def __repr__(self):
        return '<Commodity: %s>' % self.name

    def __price__(self):
        return self.price


if __name__ == "__main__":
    if os.access('sshop.db3', os.R_OK | os.F_OK):
        os.remove('sshop.db3')
    BaseModel.metadata.create_all(engine)

    db.add(Commodity(price=2.0, english="black and white unicorn", spanish="unicornio blanco y negro",
                     german="Schwarzweiss-Einhorn",
                     russian=u"черно-белый единорог"))
    db.add(Commodity(price=5.0, english="unicorn family", spanish="familia unicornio", german="Einhorn-Familie",
                     russian=u"семья единорога"))
    db.add(Commodity(price=8.0, english="warrior unicorn", spanish="guerrero unicornio", german="Krieger Einhorn",
                     russian=u"воин единорог"))
    db.add(Commodity(price=1337.0, english="ultra unicorn", spanish="ultra unicornio", german="ultra Einhorn",
                     russian=u"ультра единорог"))

    db.commit()

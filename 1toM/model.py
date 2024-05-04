from dataclasses import dataclass, field

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped

Base = declarative_base()
MYSQL_DB_CONNECT_URI = 'mysql+pymysql://root:@127.0.0.1:3306/data_db?charset=utf8mb4'
mysqlEngine = create_engine(MYSQL_DB_CONNECT_URI, echo=True)  # echo will echo the query fired to DB
MysqlSession = sessionmaker(bind=mysqlEngine)
mysqlSession = MysqlSession()


@dataclass
class Address(Base):
    __tablename__ = 'address'
    id = Column('id', Integer, primary_key=True)
    add = Column('add', String(255))
    user_id = Column('user_id', ForeignKey('users.id'))
    # user = relationship('User', uselist=False)

    '''
    # NOTE: ^^^ above user = relationship(blah-blah) is commented coz we shouldn't use relationship() in both the 
    # class (i.e User & Address) simultaneously
    # it'll cause infinte loop and if not used in both class then updating User with Address won't update the Address
    # Table automatically & vice-versa
    # NOTE: uselist=True (1:M) or uselist=False(1:1) represents whether it'll be a 1-to-Many or 1-to-1 relationship
    '''


    def __repr__(self):
        return 'id={}, add={}, user_id={}'.format(self.id, self.add, self.user_id)


@dataclass
class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    addresses = relationship('Address', uselist=True)
    # ^^^ also can use addresses: Mapped[list[Address]] = relationship('Address', uselist=True)

    def __repr__(self):
        return 'id={}, name={}, addresses[]={}'.format(self.id, self.name, self.addresses)


Base.metadata.create_all(mysqlEngine)

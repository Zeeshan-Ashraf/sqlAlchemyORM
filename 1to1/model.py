from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CheckConstraint
from dataclasses import dataclass
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
MYSQL_DB_CONNECT_URI = 'mysql+pymysql://root:@127.0.0.1:3306/data_db?charset=utf8mb4'  # use 'sqlite:///data.db' for local file storage

mysqlEngine = create_engine(MYSQL_DB_CONNECT_URI, echo=True)
mysqlSession = sessionmaker(bind=mysqlEngine)()


# mysqlSession = MysqlSession()


@dataclass
class Citizen(Base):
    __tablename__ = 'citizen'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)  # 255 is important
    adhar_id: int = Column(ForeignKey('adhar.id'))
    adhar = relationship('Adhar', uselist=False)  # uselist=False to enforce relationship of 1-1

    def __repr__(self):
        return 'id={}, name={} adhar_id={} adhar={}'.format(self.id, self.name, self.adhar_id, self.adhar)


@dataclass
class Adhar(Base):
    __tablename__ = 'adhar'
    id: int = Column(Integer, primary_key=True)
    mob: str = Column(String(100), CheckConstraint('length(mob)=10'))

    def __repr__(self):
        return 'id={}, mob={}'.format(self.id, self.mob)


Base.metadata.create_all(mysqlEngine)  # order of table class (or import) doesn't matter

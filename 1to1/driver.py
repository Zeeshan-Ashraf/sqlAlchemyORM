import logging
from model import mysqlSession, Citizen, Adhar

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger()


'''
getAll citizen & Adhar from table
'''
def getAllCitizenAndAdhar():
    citizens = mysqlSession.query(Citizen).all()
    adhars = mysqlSession.query(Adhar).all()
    mysqlSession.flush()
    mysqlSession.commit()

    logger.warning("All Citizens:")
    for citizen in citizens:
        logger.warning(citizen.__repr__())

    logger.warning("All adhars")
    for adhar in adhars:
        logger.warning(adhar.__repr__())


'''
create User and Adhar
'''
c1: Citizen = Citizen(name='Zee')
a1: Adhar = Adhar(mob="9339663495")
a2: Adhar = Adhar(mob="9339663497")
c1.adhar = a1
mysqlSession.add(c1)
mysqlSession.flush()
mysqlSession.commit()

getAllCitizenAndAdhar()

# close session at end [ must to flush all transaction ]
mysqlSession.close()
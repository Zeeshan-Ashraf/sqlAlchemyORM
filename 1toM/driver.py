"""
How Run:
1.  brew install mysql (if not already installed)
2.  start MySQL server in local 127.0.0.1
    (usually command for mac: brew services start mysql if mysql installed with brew)
    P.S root should be mysql user & without any password
3.  create database with name data_db (CMD FOR LOGIN: mysql -u root  CREATE DB CMD: create database if not exists data_db;)
4.  pip3 install dataclasses==0.6
5.  pip3 install SQLAlchemy==2.0.29
6.  cd sqlalchemy1to1_1toN_NtoN/1toM
7.  python3 driver.py
"""

from model import User, Address, mysqlSession
import logging

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger()



'''
query to get & print User & Address with ID=1 with user's associated Address
'''
def getUserAndAddressWithId_1():
    logger.info("Querying User and Address with ID 1")

    user: User = mysqlSession.get(User, 1)
    add: Address = mysqlSession.get(Address, 1)
    mysqlSession.commit()

    logger.warning("Address with id=1:" + add.__repr__())
    logger.warning("User with id=1:" + user.__repr__())


'''
Add User with Addresses [ relationship: User <-1--M-> Address ]
'''
u1 = User(name="Zee")
u2 = User(name='Ars')

a1 = Address(add='Kol')
a2 = Address(add='Pat')
u1.addresses = [a1, a2]

mysqlSession.add(u1)
mysqlSession.add(u2)
mysqlSession.commit()

logger.info("added U1 & U2")
# verify added Users
getUserAndAddressWithId_1()


'''
update to Add more addresses to User ID = 1
'''
user: User = mysqlSession.get(User, 1)
a3 = Address(add='Del')
user.addresses.append(a3)  # simply append will update the data
mysqlSession.commit()

logger.info("added Address=Del to User with ID 1")
getUserAndAddressWithId_1()  # verify updated user


'''
update exiting value of user with id =1
'''
logger.info("update User.name for User with ID 1")

user: User = mysqlSession.get(User, 1)
user.name = 'Zdoo'  # simply append will update the data
mysqlSession.commit()

logger.info("updated user.name User with ID 1")
getUserAndAddressWithId_1()  # check User if updated or not


# close session at end [ must to flush all transaction ]
mysqlSession.close()
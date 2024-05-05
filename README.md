# sqlAlchemyORM
basic CRUD operation with 1-1 1-M M-M relation using sqlAlchemy on MySQL DB running locally

## How to run
1.  `brew install mysql` (if not already installed)
2.  start MySQL server in local 127.0.0.1
    (usually command for mac: `brew services start mysql` if mysql installed with brew)
    P.S root should be mysql user & without any password
3.  create database with name data_db (TERMINAL CMD FOR LOGIN: `mysql -u root`  CREATE DB CMD: `create database if not exists data_db;`)
4.  `pip3 install dataclasses==0.6` (or install all directly by running `pip3 install -r requirements.txt`)
5.  `pip3 install SQLAlchemy==2.0.29` (or install all directly by running `pip3 install -r requirements.txt`)
6.  `cd sqlalchemy1to1_1toN_NtoN/1toM` (or 1to1 or MtoM)
7.  `python3 driver.py`

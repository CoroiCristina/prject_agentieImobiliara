import MySQLdb
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# specificarea datelor de conectare la baza de date MySQL
db_host = 'localhost'
db_name = 'agentiebd'
db_user = 'root'
db_pass = ''

# crearea unui motor SQLAlchemy pentru a realiza conexiunea la baza de date MySQL
engine = create_engine(f'mysql://{db_user}:{db_pass}@{db_host}:3307/{db_name}')


# testarea conexiunii la baza de date
try:
    connection = engine.connect()
    print('Conexiunea la baza de date a fost realizata cu succes!')
except:
    print('Eroare la conectarea la baza de date.')

def verif_date_existente():
    metadata = MetaData()
    apartament_table = Table('apartament', metadata, mysql_autoload=True, autoload_with=engine)

    with engine.connect() as conn:
        result = conn.execute(select(func.count()).select_from(apartament_table))
        count = result.scalar()
        if count > 0:
            print("Tabela Apartament are inregistrari.")
        else:
            print("Tabela Apartament nu are inregistrari.")

def inserare_DB(lista):
    Base = declarative_base()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


import MySQLdb
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DBAccess(Singleton):
    # specificarea datelor de conectare la baza de date MySQL
    db_host = 'localhost'
    db_name = 'agentiebd'
    db_user = 'root'
    db_pass = ''

    # crearea unui motor SQLAlchemy pentru a realiza conexiunea la baza de date MySQL
    engine = create_engine(f'mysql://{db_user}:{db_pass}@{db_host}:3307/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    apartament_table = Table('apartament', metadata, mysql_autoload=True, autoload_with=engine)
    extraOp_table = Table('extra_optiune', metadata, mysql_autoload=True, autoload_with=engine)
    complex_table = Table('complex', metadata, mysql_autoload=True, autoload_with=engine)
    contract_table = Table('contract', metadata, mysql_autoload=True, autoload_with=engine)
    client_table = Table('client', metadata, mysql_autoload=True, autoload_with=engine)
    vanzari_table = Table('vanzare', metadata, mysql_autoload=True, autoload_with=engine)
    inchirieri_table = Table('inchiriere', metadata, mysql_autoload=True, autoload_with=engine)
    cont_bancar_table = Table('cont_bancar', metadata, mysql_autoload=True, autoload_with=engine)
    Base = declarative_base()
    Base.metadata.create_all(engine)

    def Verif_connection(self):
        # testarea conexiunii la baza de date
        try:
            self.engine.connect()
            print('Conexiunea la baza de date a fost realizata cu succes!')
        except Exception:
            print('Eroare la conectarea la baza de date.')

    def verif_date_existente(self):
        with self.engine.connect() as conn:
            result = conn.execute(select(func.count()).select_from(self.apartament_table))
            count = result.scalar()
            if count > 0:
                date_ap = True
            else:
                date_ap = False
        with self.engine.connect() as conn:
            result = conn.execute(select(func.count()).select_from(self.extraOp_table))
            count = result.scalar()
            if count > 0:
                date_eo = True
            else:
                date_eo = False
        with self.engine.connect() as conn:
            result = conn.execute(select(func.count()).select_from(self.complex_table))
            count = result.scalar()
            if count > 0:
                date_c = True
            else:
                date_c = False
        return date_ap, date_eo, date_c

    def inserare_DB(self, elem):
        self.session.add(elem)
        self.session.commit()

    def extragereDateDB(self, Class):
        query = self.session.query(Class)
        lista = query.all()
        return lista

    def update_ApartamentDB(self, Class, atribut, statut):
        apartament = self.session.query(Class).filter(Class.id_ap == atribut).first()
        apartament.statut = statut
        # Salvare modificari
        self.session.commit()

    # def ExtragereNrContracteExistente(self, Class):
    #     lista = []
    #     rows = self.extragereDateDB(Class)
    #     for row in rows:
    #         lista.append(row[0])
    #     return lista
    
    def DeleteDB(self, nr_contract):
        connection = self.engine.connect()
        delete_statement = self.contract_table.delete().where(self.contract_table.c.nr_contract == nr_contract)
        connection.execute(delete_statement)

from typing import List
import sqlalchemy as sqlall
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from storage.base import StorageObject
from model.modelComplex import Complex
from model.modelApartament import Apartament
from model.modelExtraOptiune import ExtraOp
from model.modelClient import Client
from model.modelContract import Contract
from model.modelVanzare import Vanzare
from model.modelInchiriere import Inciriere
from model.modelInregistrareCcont import Inregistrare


def Singleton(cls):
    _instance = {}

    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    
    return get_instance

@Singleton
class DBAccess(StorageObject):
    # specificarea datelor de conectare la baza de date MySQL
    db_host = '0.0.0.0'
    db_name = 'agentiebd'
    db_user = 'root'
    db_pass = ''

    # crearea unui motor SQLAlchemy pentru a realiza conexiunea la baza de date MySQL
    
    engine = create_engine(f'mysql://{db_user}:{db_pass}@host.docker.internal:3307/{db_name}')
    #engine = create_engine(f'mysql://{db_user}:{db_pass}@{db_host}:3307/{db_name}')
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
    conn = engine.connect()
    lista_complexe = []
    lista_apartamente = []
    lista_extra = []

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
    
    def DeleteDB(self, nr_contract):
        connection = self.engine.connect()
        delete_statement = self.contract_table.delete().where(self.contract_table.c.nr_contract == nr_contract)
        connection.execute(delete_statement)
    #region Complex

    def get_complexe(self) -> List[Complex]:
        self.lista_complexe.clear()
        try:
            sql = sqlall.select(self.complex_table.columns)
            result = self.conn.execute(sql)
            for row in result:
                id_complex = row[0]
                denumire = row[1]
                strada = row[2]
                nr_blocuri = row[3]
                complex = Complex(id_complex=id_complex, denumire=denumire, strada=strada, nr_blocuri=nr_blocuri)
                self.lista_complexe.append(complex)
        except Exception as e:
            print("Probleme la functia get_complexe...")
            print(e)
        finally:
            return self.lista_complexe
        
    def get_complex_by_id(self, id_complex: int) -> List[Complex]:
        self.lista_complexe.clear()
        try:
            sql = sqlall.select(self.complex_table.columns).where(self.complex_table.columns.id_complex == id_complex)
            result = self.conn.execute(sql)
            for row in result:
                id_complex = row[0]
                denumire = row[1]
                strada = row[2]
                nr_blocuri = row[3]
                complex = Complex( id_complex=id_complex, denumire=denumire, strada=strada, nr_blocuri=nr_blocuri)
                self.lista_complexe.append(complex)
        except Exception as e:
            print("Probleme la functia get_complex_by_id...")
            print(e)
        finally:
            return self.lista_complexe
 
    def put_complex(self, complex: Complex) -> List[Complex]:
        self.lista_complexe.clear()
        try:
            sql = sqlall.insert(self.complex_table).values(id_complex=complex.id_complex, denumire=complex.denumire, strada=complex.strada, nr_blocuri=complex.nr_blocuri)
            self.conn.execute(sql)
        except Exception as e:
            print("problema la functia put_complex")
            print(e)
        finally:
            return self.lista_complexe
    # endregion

    #region apartmens

    def get_all_apartments(self) -> List[Apartament]:
        self.lista_apartamente.clear()
        try:
            sql = sqlall.select(self.apartament_table.columns)
            result = self.conn.execute(sql)
            for row in result:
                id_ap = row[0]
                id_complex = row[1]
                nr_bloc = row[2]
                nr_etaj = row[3]
                nr_ap = row[4]
                tip_ap = row[5]
                dimensiune = row[6]
                bloc_vanzare = row[7]
                statut = row[8]
                aparatament = Apartament(id_ap=id_ap, id_complex=id_complex, nr_bloc=nr_bloc, nr_etaj=nr_etaj, 
                                         nr_ap=nr_ap, tip_ap=tip_ap, dimensiune=dimensiune, bloc_vanzare=bloc_vanzare, statut=statut)
                self.lista_apartamente.append(aparatament)
        except Exception as e:
            print("Probleme la functia get_all_apartments...")
            print(e)
        finally:
            return self.lista_apartamente

    def get_apartments_by_strada(self, strada: str) -> List[Apartament]:
        self.lista_apartamente.clear()
        self.lista_complexe.clear()
        try:
            self.lista_complexe = self.get_complexe()
            for comp in self.lista_complexe:
                if comp.strada == strada:
                    sql = sqlall.select(self.apartament_table.columns).where(self.apartament_table.columns.id_complex == comp.id_complex)
                    result = self.conn.execute(sql)
                    for row in result:
                        id_ap = row[0]
                        id_complex = row[1]
                        nr_bloc = row[2]
                        nr_etaj = row[3]
                        nr_ap = row[4]
                        tip_ap = row[5]
                        dimensiune = row[6]
                        bloc_vanzare = row[7]
                        statut = row[8]
                        aparatament = Apartament(id_ap=id_ap, id_complex=id_complex, nr_bloc=nr_bloc, nr_etaj=nr_etaj, 
                                                 nr_ap=nr_ap, tip_ap=tip_ap, dimensiune=dimensiune, bloc_vanzare=bloc_vanzare, statut=statut)
                        self.lista_apartamente.append(aparatament)
        except Exception as e:
            print("Probleme la functia get_apartments_by_strada...")
            print(e)
        finally:
            return self.lista_apartamente
    
    def get_apartment_by_id(self, id_ap: int) -> List[Apartament]:
        self.lista_apartamente.clear()
        try:
            sql = sqlall.select(self.apartament_table.columns).where(self.apartament_table.columns.id_ap == id_ap)
            result = self.conn.execute(sql)
            for row in result:
                id_ap = row[0]
                id_complex = row[1]
                nr_bloc = row[2]
                nr_etaj = row[3]
                nr_ap = row[4]
                tip_ap = row[5]
                dimensiune = row[6]
                bloc_vanzare = row[7]
                statut = row[8]
                aparatament = Apartament(id_ap=id_ap, id_complex=id_complex, nr_bloc=nr_bloc, nr_etaj=nr_etaj, 
                                         nr_ap=nr_ap, tip_ap=tip_ap, dimensiune=dimensiune, bloc_vanzare=bloc_vanzare, statut=statut)
                self.lista_apartamente.append(aparatament)
        except Exception as e:
            print("Probleme la functia get_apartment_by_id...")
            print(e)
        finally:
            return self.lista_apartamente

    def update_apartment_statut(self, status: str, id_ap: int) -> List[Apartament]:
        self.lista_apartamente.clear()
        try:
            sql = sqlall.update(self.apartament_table).where(self.apartament_table.columns.id_ap == id_ap).values(statut=status)
            self.conn.execute(sql)
            # sql = sqlall.select(self.apartament_table.columns).where(self.apartament_table.columns.id_ap == ap.id_ap)
            # result = self.conn.execute(sql)
            # for row in result:
            #     id_ap = row[0]
            #     id_complex = row[1]
            #     nr_bloc = row[2]
            #     nr_etaj = row[3]
            #     nr_ap = row[4]
            #     tip_ap = row[5]
            #     dimensiune = row[6]
            #     bloc_vanzare = row[7]
            #     statut = row[8]
            #     aparatament = Apartament(id_ap=id_ap, id_complex=id_complex, nr_bloc=nr_bloc, nr_etaj=nr_etaj, 
            #                              nr_ap=nr_ap, tip_ap=tip_ap, dimensiune=dimensiune, bloc_vanzare=bloc_vanzare, statut=statut)
            #     self.lista_apartamente.append(aparatament)
        except Exception as e:
            print("Probleme la functia update_apartament_statut...")
            print(e)
        finally:
            return "Date inregistrate cu succes!"

    #endregion

    #region extra_options

    def get_all_extra_options(self) -> List[ExtraOp]:
        self.lista_extra.clear()
        try:
            sql = sqlall.select(self.extraOp_table.columns)
            result = self.conn.execute(sql)
            for row in result:
                id_op = row[0]
                denumire = row[1]
                pret = row[2]
                extraOptione = ExtraOp(id_op=id_op, denumire=denumire, pret=pret)
                self.lista_extra.append(extraOptione)
        except Exception as e:
            print("problema la functia get_all_extra_options")
            print(e)
        finally:
            return self.lista_extra
    
    def get_extra_option_by_id(self, id_op: int) -> List[ExtraOp]:
        self.lista_extra.clear()
        try:
            sql= sqlall.select(self.extraOp_table.columns).where(self.extraOp_table.columns.id_op == id_op)
            result = self.conn.execute(sql)
            for row in result:
                id_op = row[0]
                denumire = row[1]
                pret = row[2]
                extraOptione = ExtraOp(id_op=id_op, denumire=denumire, pret=pret)
                self.lista_extra.append(extraOptione)
        except Exception as e:
            print("problema la functia get_extra_option_by_id")
            print(e)
        finally:
            return self.lista_extra
        
    def put_extra_option(self, extra_optiune: ExtraOp) -> List[ExtraOp]:
        self.lista_extra.clear()
        try:
            sql = sqlall.insert(self.extraOp_table).values(id_op=extra_optiune.id_op, denumire=extra_optiune.denumire, pret=extra_optiune.pret)
            self.conn.execute(sql)
        except Exception as e:
            print("problema la functia put_extra_option")
            print(e)
        finally:
            return "Date inregistrate cu scucces"
    
    def delete_extra_option(self, id_op: int) -> List[ExtraOp]:
        self.lista_extra.clear()
        try:
            sql = sqlall.delete(self.extraOp_table).where(self.extraOp_table.columns.id_op == id_op)
            self.conn.execute(sql)
        except Exception as e:
            print("problema la functia get_extra_option_by_id")
            print(e)
        finally:
            return self.get_all_extra_options()
    #endregion
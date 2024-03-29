import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from os import environ


engine = sqlalchemy.create_engine("mariadb+mariadbconnector://"+environ.get("USER")+":"+environ.get("PSWD")+"@127.0.0.1:3306/climate")

Base = declarative_base()

class Temp(Base):
    __tablename__ = 'temperature'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.Date)
    time = sqlalchemy.Column(sqlalchemy.Time())
    temperature = sqlalchemy.Column(sqlalchemy.Float(precision=1))



class Connector:

    def __init__(self):
        Base.metadata.create_all(engine)
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

    def addTemperature(self, date,time,temperature):
        temp = Temp(date = date, time=time, temperature=temperature)
        self.session.add(temp)
        self.session.commit()

    def get_data(self):
        q = self.session.query(Temp)
        return pd.read_sql(q.statement,q.session.bind)

    def dates(self, first, last = None):
        if(last == None):
            q = self.session.query(Temp).filter_by(date = first)
            return pd.read_sql(q.statement,q.session.bind)

        q = self.session.query(Temp).filter(Temp.date.between(first, last))
        return pd.read_sql(q.statement,q.session.bind)
    
    def hours(self, low, high=None):
        if(high == None):
            q = self.session.query(Temp).filter_by(time = low)
            return pd.read_sql(q.statement,q.session.bind)

        q = self.session.query(Temp).filter(Temp.time.between(low, high))
        return pd.read_sql(q.statement,q.session.bind)

    def temp_range(self, low, high = None):
        if(high == None):
            q = self.session.query(Temp).filter_by(temperature = low)
            return pd.read_sql(q.statement,q.session.bind)

        q = self.session.query(Temp).filter(Temp.temperature.between(low, high))
        return pd.read_sql(q.statement,q.session.bind) 
        
    
    def max_temp(self,query,timeframe):
        df = pd.read_sql(query.statement,query.session.bind)
        return df.groupby([timeframe])['temperature'].max()

    def min_temp(self,query,timeframe):
        df = pd.read_sql(query.statement,query.session.bind)
        return df.groupby([timeframe])['temperature'].min()

    def avg_temp(self,query,timeframe):
        df = pd.read_sql(query.statement,query.session.bind)
        return df.groupby([timeframe])['temperature'].mean()

    def describe(self,query,timeframe):
        df = pd.read_sql(query.statement,query.session.bind)
        return df.groupby([timeframe])['temperature'].descibe()


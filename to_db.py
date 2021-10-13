import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://blunt:Zomboy8897@127.0.0.1:3306/tempdatabase")

Base = declarative_base()

class Temp(Base):
    __tablename__ = 'temperature'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.Date)
    time = sqlalchemy.Column(sqlalchemy.Time())
    temperature = sqlalchemy.Column(sqlalchemy.Float(precision=1))

Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def addTemperature(date,time,temperature):
    temp = Temp(date = date, time=time, temperature=temperature)
    session.add(temp)
    session.commit()
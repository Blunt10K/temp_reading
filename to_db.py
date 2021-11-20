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

    def dates(self, first, last = None):
        if(last == None):
            return self.session.query(Temp).filter_by(date = first)

        return self.session.query(Temp).filter(Temp.date.between(first, last))
    
    def hours(self, low, high=None):
        if(high == None):
            return self.session.query(Temp).filter_by(time = low)

        return self.session.query(Temp).filter(Temp.time.between(low, high))

    def temp_range(self, low, high = None):
        if(high == None):
            return self.session.query(Temp).filter_by(temperature = low)

        return self.session.query(Temp).filter(Temp.temperature.between(low, high))
    
    def max_temp(self):
        return #self.session.query(Temp).filter_by(temperature = low)

    def min_temp(self):
        return #self.session.query(Temp).filter_by(temperature = low)

    def avg_temp(self):
        return #self.session.query(Temp).filter_by(temperature = low)
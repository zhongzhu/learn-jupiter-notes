from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return "<User(id={}, name={}, age={})>".format(self.id, self.name, self.age)

Base.metadata.create_all(engine) # create db shcema

session = Session()

a_user = User(name='Mike', age=18)
session.add(a_user)
our_user = session.query(User).filter_by(name='Mike').first() # you can query but it's not in db yet
a_user.age = 20 # change it before session.commit()

session.add_all([User(name='Henry', age=19), User(name='Jack', age=17)])
session.commit()

print(session.query(User).all())
#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                self.name, self.fullname, self.nickname)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

#-----------------------------------------------------------------------

Base.metadata.create_all(engine)
print("=======================")

james = User(name='james', fullname='James Kariuki', nickname='jaymo')
sammy = User(name='sammy', fullname='Sammy Kariuki', nickname='sam')
tabby = User(name='tabby', fullname='Tabitha Kariuki', nickname='wambo')
eunice = User(name='eunice', fullname='Eunice Kariuki', nickname='kamson')
session.add_all([james, sammy, tabby, eunice])

print("!=======================\n")
query = session.query(User.fullname).order_by(User.fullname.asc())
ordered_names = query.all()
print(ordered_names)

james.addresses = [
        Address(email_address='jmkariuki@telkom.co.ke'),
        Address(email_address='jimmiemwaura001@gmail.com'),
        Address(email_address='karisjaymo99@gmail.com')
        ]
session.commit()

print('\n\n\n\n')
print(repr(james.addresses))

print('\n\n\n\n')
print(repr(james.addresses))

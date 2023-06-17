#!/usr/bin/python3
'''Search for a State object
'''
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if len(sys.argv) < 5:
    print("4 args required: <db-username> <db-passwd> <db-name> <state-name>")
    sys.exit()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == sys.argv[4])\
        .order_by(State.id.asc())
    result = query.first()
    if result:
        print(f'{result.id}')
    else:
        print("Not found")
    session.close()

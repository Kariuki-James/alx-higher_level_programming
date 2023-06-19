#!/usr/bin/python3
'''Retrieves States and cities with eager loading
'''
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, selectinload

from relationship_city import City
from relationship_state import Base, State

if len(sys.argv) < 4:
    print("3 args required: <db-username> <db-passwd> <db-name>")
    sys.exit()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).options(selectinload(State.cities))\
            .order_by(State.id)

    for state in query.all():
        print(f'{state.id}:', state.name)
        for city in state.cities:
            print(f'\t{city.id}:', city.name)

    session.close()

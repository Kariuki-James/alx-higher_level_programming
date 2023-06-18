#!/usr/bin/python3
'''Lists all cities from a database table
'''

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City


def list_cities():
    '''lists all cities in ascending-id order.
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).join(State).order_by(City.id.asc())
    for city, state in query.all():
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("3 args required: <db-username> <db-passwd> <db-name>")
        sys.exit()
    list_cities()

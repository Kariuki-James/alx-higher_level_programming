#!/usr/bin/python3
'''List all cities with State names
'''
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

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

    query = session.query(City).join(City.state).order_by(City.id)

    for city in query.all():
        print(f'{city.id}:', city.name, '->', city.state.name)

    session.close()

#!/usr/bin/python3
'''Search for a State object
'''
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

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

    query = session.query(State).filter(State.name.like('%a%'))
    del_states = query.all()
    if del_states:
        for state in del_states:
            session.delete(state)

        try:
            session.commit()
        except Exception as e:
            print("Failed to delete states:", str(e))
    else:
        print("No states found matching that criteria.")
    session.close()

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

    query = session.query(State).filter(State.id == 2)
    try:
        state = query.one()
        state.name = 'New Mexico'
        session.commit()
    except NoResultFound as e:
        print("State not found")
    except MultipleResultsFound as e:
        print("Multiple states found")
    except Exception as e:
        print("An error occured during the session")
    finally:
        session.close()

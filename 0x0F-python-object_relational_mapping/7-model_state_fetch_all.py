#!/usr/bin/python3
'''Lists all states in a table
'''

if __name__ == "__main__":
    import sys

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id.asc())
    for state in query.all():
        print(f'{state.id}:', state.name)

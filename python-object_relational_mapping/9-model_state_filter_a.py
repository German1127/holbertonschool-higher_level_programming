#!/usr/bin/python3

"""Lists all State objects that contain the letter
'a' from the database hbtn_0e_6_usa"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


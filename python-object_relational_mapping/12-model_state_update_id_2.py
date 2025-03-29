#!/usr/bin/python3

"""Changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_id = 2
    new_state_name = "New Mexico"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == state_id).first()
    if state:
        state.name = new_state_name
        session.commit()
    else:
        print("Not found")

    session.close()


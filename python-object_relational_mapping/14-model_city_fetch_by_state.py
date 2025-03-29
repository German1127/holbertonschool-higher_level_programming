#!/usr/bin/python3
"""Module that lists all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    # Bind the engine to the session and create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and their associated State objects
    cities = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Print each City object with its associated State name
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


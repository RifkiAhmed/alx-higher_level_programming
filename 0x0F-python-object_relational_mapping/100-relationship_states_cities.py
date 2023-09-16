#!/usr/bin/python3
"""
   Module to list all cities related to a state
   in hbtn_0e_100_usa database.
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    session.add(state)
    session.add(City(name="San Fransisco", state=state))
    session.commit()
    session.close()

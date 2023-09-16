#!/usr/bin/python3
"""
   Model to delete all state with a name containing the character 'a'
   from the hbtn_0e_6_usa database.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%")).all()
    if states:
        for state in states:
            session.delete(state)
        session.commit()
    session.close()

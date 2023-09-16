#!/usr/bin/python3
"""
   Model to list a state with name given as argument
   from the hbtn_0e_6_usa database.
   the script is safe from MySQL injections.
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
    session.add(State(name="Louisiana"))
    session.commit()
    state = session.query(State).order_by(State.id.desc()).first()
    print(state.id)
    session.close()

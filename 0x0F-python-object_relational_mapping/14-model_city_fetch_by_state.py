#!/usr/bin/python3
"""
   Module to list all cities in hbtn_0e_6_usa database.
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city_id, city in session.query(
            State.name, City.id, City.name).filter(
                    City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state, city_id, city))
    session.close()

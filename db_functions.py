from datetime import datetime
import psycopg 
import configparser



def getConfigItems():
    dbConfig = configparser.ConfigParser()
    config.read("postgres.conf")
    hostname = config['postgres']['hostname']
    username = config['postgres']['username']
    password = config['postgres']['password']
    database = config['postgres']['database']
    return hostname, username, password, database

def setupPG():
    hostname, username, password, database = getConfigItems()
    pgConn = psycopg.connect(
        host=hostname,
        user=username,
        password=password,
        dbname=database)
    cursor = pgConn.cursor()
    return pgConn, cursor

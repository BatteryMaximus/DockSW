from datetime import datetime
import psycopg 
import configparser



def getConfigItems():
    dbConfig = configparser.ConfigParser()
    dbConfig.read("postgres.conf")
    hostname = dbConfig['postgres']['hostname']
    username = dbConfig['postgres']['username']
    password = dbConfig['postgres']['password']
    database = dbConfig['postgres']['database']
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

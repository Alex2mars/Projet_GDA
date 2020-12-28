import json
import sys
import os
import psycopg2 as psy
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import subprocess


#Read file with loads instead of load in order to check if key exists
def read_file(file_to_open):
    input_from_file = {}
    file = open(file_to_open, 'r')
    input_from_file = json.loads(file.read())
    file.close()
    return input_from_file


def connect(host, database, user, password, port):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = dict()
        params['host'] = host
        params['database'] = database
        params['user'] = user
        params['password'] = password
        params['port'] = port

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psy.connect(**params)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    except (Exception, psy.DatabaseError) as error:
        print(error)
        print("Erreur")
        sys.exit()

        return conn


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        connection = sys.argv[1]
        gestion = sys.argv[2]
        # print(connection)
        # print(gestion)
    else:
        print("Usage : file1 (containing database connection), file 2 (containg explainations on what to do")
        sys.exit()

    bdd = read_file(connection)
    #print("BDD : ", bdd)

    if "db_name" not in bdd:
        bdd['db_name'] = 'postgres'
    
    connection = connect(bdd['host'], bdd['db_name'], bdd['username'], bdd['password'], bdd['server_port'])
    print(connection)
    print("Everything should be ok !")

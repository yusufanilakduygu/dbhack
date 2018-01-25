import mysql.connector
from dbhack_parser import *




def connect_database():
    global global_connect
    global_connect = mysql.connector.connect(user='anil',
                                      password='anil',
                                      host='127.0.0.1',
                                      database='DBHack')
    return 

def sd():
    c=global_connect.cursor()
    c.execute('Show databases;')
    result_set=c.fetchall()
    print(result_set)
    c.close
    return


def create_audit(args):
    parsed_command=parse_server_port(args+" ;")
    c=global_connect.cursor()
#    c.execute('Create database '+parsed_command[0]+' ;')
    return
    

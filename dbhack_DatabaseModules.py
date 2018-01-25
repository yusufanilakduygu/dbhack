import mysql.connector
from dbhack_parser import *
from tabulate import tabulate




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
    parsed_command=parse_create_audit(args+" ;")
    c=global_connect.cursor()
    
    try:
        c.execute('Create database '+parsed_command[0]+' ;')
        c.execute('commit;')
    except mysql.Error as err:
            print("Failed to create audit: {}".format(err))
            return
        
    print ( 'Audit created successfully')
    return
    
def delete_audit(args):
    parsed_command=parse_audit(args+" ;")
    c=global_connect.cursor()

    try:
        c.execute('Drop database '+parsed_command[0]+' ;')
        c.execute('commit;')
    except mysql.Error as err:
        print("Failed to drop audit: {}")
        return
        
    print ( 'Audit created successfully')
    
    return

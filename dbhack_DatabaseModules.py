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

    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
        
    try:
        c.execute('Create database '+parsed_command[0]+' ;')
        c.execute('commit;')
        c.close
    except mysql.Error as err:
            print("Failed to create audit: {}".format(err))
            return
        
    print ( 'Audit created successfully')
    return
    
def delete_audit(args):
    parsed_command=parse_audit(args+" ;")
    
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
    
    try:
        c.execute('Drop database '+parsed_command[0]+' ;')
        c.execute('commit;')
        c.close
    except mysql.connector.Error as err:
        print("Failed to drop audit: {}".format(err))
        return
        
    print ( 'Audit deleted successfully')
    
    return


def show_current_audit(args):
    
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
        
    try:
        c.execute('Select database() from dual ;')
        result_set=c.fetchall()
        print('Current Audit')
        print(tabulate(result_set,tablefmt="grid"))
        c.execute('commit;')
        c.close
    except mysql.Error as err:
            print("Failed SQL Statement in show_current_audit {}".format(err))
            return
        
    return


def use_audit(args):
    parsed_command=parse_audit(args+" ;")
    
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
    
    try:
        c.execute('use '+parsed_command[0]+' ;')
        c.execute('commit;')
        c.close
    except mysql.connector.Error as err:
        print("Failed statement {}".format(err))
        return
        
    print ( 'Audit changed')
    
    return

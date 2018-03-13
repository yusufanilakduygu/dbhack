import mysql.connector
from dbhack_parser import *
from tabulate import tabulate
global global_db_connect



def connect_database():
    global global_connect
    try:
        global_connect = mysql.connector.connect(user='anil',
                                          password='anil',
                                          host='127.0.0.1',
                                          database='DBHack')
    except Exception as error:
            print("Failed to connect to database")
            return ('NotConnected')

    print ( 'Successfully connected to the Database')
    
    return('Connected')



def create_audit(args):
    parsed_command=parse_create_audit(args+" ;")
    if parsed_command[0] == 'Error':
        return
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
        
    try:
        c.execute('Create database '+parsed_command[0]+' ;')
        

        add_audit = ("INSERT INTO DBHack.audit_info "
                     "(create_date, audit_name, info) "
                     "VALUES (CURDATE(), %s, %s)")
        
        data_audit=(parsed_command[0],parsed_command[1],)

        c.execute(add_audit,data_audit)
        c.execute('commit;')

        print('Create table ' +parsed_command[0]+'.ping_dbports_out')
        c.execute('Create table '+parsed_command[0]+'.ping_dbports_out(create_date datetime, server_name varchar(100),exp varchar(100), port  int,hit char(1));')
                 
        c.close
    except mysql.Error as err:
            print("Failed to create audit: {}".format(err))
            return
        
    print ( 'Audit created successfully')
    return
    
def delete_audit(args):
    parsed_command=parse_audit(args+" ;")
    if parsed_command[0] == 'Error':
        return
    
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
    
    try:
        statement="DELETE from DBHack.audit_info where audit_name = %s "
        delete_data=(parsed_command[0],)
        c.execute(statement,delete_data)
        
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
    if parsed_command[0] == 'Error':
        return
    
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


def show_audit(args):
    
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return
    
    try:
        c.execute('select * from DBHack.audit_info ;')
        result_set=c.fetchall()
        column_set=[('Create Date','Audit Name','Explanation')]
        print(tabulate(column_set+result_set,tablefmt="grid"))
        c.execute('commit;')
        c.close
    except mysql.connector.Error as err:
        print("Failed SQL Statement in show_audit: {}".format(err))
        return
    
    return


def insert_pingdbports_out(p_servername,p_port,p_exp,p_hit):
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return

    try:

        Statement = ("INSERT INTO ping_dbports_out"
                     "(create_date, server_name,exp,port,hit) "
                     "VALUES (now(),%s,%s,%s,%s)")
        
        Data =(p_servername,p_exp,p_port,p_hit,)

        c.execute(Statement,Data)
        c.execute('commit;')     
        c.close

    except mysql.connector.Error  as err:
            print("Failed to insert ping_dbports_out{}".format(err))
            return


def insert_ora_chk_out(p_servername,p_port,p_listener_name,p_db_version,p_hit):
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return

    try:

        Statement = ("INSERT INTO ora_chk_out"
                     "(create_date, server_name,port,listener_name,db_version,hit) "
                     "VALUES (now(),%s,%s,%s,%s,%s)")
        
        Data =(p_servername,p_port, p_listener_name,p_db_version,p_hit,)

        c.execute(Statement,Data)
        c.execute('commit;')     
        c.close

    except mysql.connector.Error as err:
            print("Failed to insert ora_chk_out{}".format(err))
            return



def insert_ora_sid_out(p_servername,p_port,p_sid_name,p_service_name,p_hit):
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return

    try:

        Statement = ("INSERT INTO ora_sid_out"
                     "(create_date, server_name,port,sid_name,service_name,hit) "
                     "VALUES (now(),%s,%s,%s,%s,%s)")
        
        Data =(p_servername,p_port, p_sid_name,p_service_name,p_hit,)

        c.execute(Statement,Data)
        c.execute('commit;')     
        c.close

    except mysql.connector.Error as err:
            print("Failed to insert ora_chk_out{}".format(err))
            return


def insert_ora_brute_out(p_server,p_port,p_sid,p_server_name,p_user,p_passwd,p_ORA_code,p_hit):
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return

    try:

        Statement = ("INSERT INTO ora_brute_out"
                     "(create_date,server_name,port,sid_name,service_name,user_name,passwd,ORA_code,hit) "
                     "VALUES (now(),%s,%s,%s,%s,%s,%s,%s,%s)")
        
        Data =(p_server,p_port,p_sid,p_server_name,p_user,p_passwd,p_ORA_code,p_hit,)

        c.execute(Statement,Data)
        c.execute('commit;')     
        c.close

    except mysql.connector.Error as err:
            print("Failed to insert ora_brute_out{}".format(err))
            return


def insert_ora_tns_poison_out(p_server,p_port,p_hit):
    try:
        c=global_connect.cursor()  
    except Exception as error:
        print(' Please Connect to the database with connect_database command')
        print('')
        return

    try:

        Statement = ("INSERT INTO ora_tns_poison_out"
                     "(create_date, server_name,port,hit) "
                     "VALUES (now(),%s,%s,%s)")
        
        Data =(p_server,p_port,p_hit,)

        c.execute(Statement,Data)
        c.execute('commit;')     
        c.close

    except mysql.connector.Error as err:
            print("Failed to insert ora_tns_poison_out{}".format(err))
            return


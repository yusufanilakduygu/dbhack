import socket
import itertools
import os
from dbhack_parser import *




def network_ping_run ( p_servername):
    response = os.system("ping -c 1 " + p_servername + " 1> /dev/null 2> /dev/null")
    if response == 0:
        return 0
    else:
        return 1

def network_ping_port(p_servername,p_port):
    sock= socket.socket()
    sock.settimeout(5)
    try:
        print('')
        print (' Connection : '+p_servername+' : '+str(p_port)+'...',end="")
        sock.connect((p_servername, p_port))
    except Exception as error:
        print(' Not Connected to the port ' + str(error))
        print("")
        sock.close()
        return
    print(' Connected to the port')
    print("")
    sock.close()
    
def network_ping(args):
    parsed_command=parse_server(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0]):
                response = network_ping_run (i[0])
                if response == 0:
                    print("")
                    print (" Connection : "+i[0]+" Ping Successfuly Responding" );
                else:
                    print("")
                    print (" Connection : "+i[0]+" Ping Not Responding" );
    return




def network_ping_ports(args):
    parsed_command=parse_server_port(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0],parsed_command[1]):
                network_ping_port(i[0],i[1])
    return




def network_ping_port_db(p_servername,p_port,p_exp):
    global globvar01
    sock= socket.socket()
    sock.settimeout(5)
    try:
        sock.connect((p_servername, p_port))
    except Exception as error:
        pass
        sock.close()
        return
    globvar01=globvar01+1
    print('   '+p_exp+' Detected on port '+str(p_port))
    sock.close()



def network_ping_special_port(args):
    global globvar01
    globvar01=0
    print('')
    print (' Connection : '+args)
    response = network_ping_run (args)
    if response == 0:
        
        network_ping_port_db(args,1521,'Oracle Net Listener')
        network_ping_port_db(args,1522,'Oracle Net Listener')
        network_ping_port_db(args,1523,'Oracle Net Listener')
        network_ping_port_db(args,1524,'Oracle Net Listener')
        network_ping_port_db(args,1525,'Oracle Net Listener')
        network_ping_port_db(args,1526,'Oracle Net Listener')
        network_ping_port_db(args,1433,'SQL Server Database Engine')
        network_ping_port_db(args,1434,'SQL Server Browser Service')
        network_ping_port_db(args,3306,'MySQL')
        network_ping_port_db(args,5432,'PostgreSQL')
        network_ping_port_db(args,27017,'MongoDB')
        network_ping_port_db(args,27018,'MongoDB')
        network_ping_port_db(args,27019,'MongoDB')
        
        if globvar01 == 0:
            print( ' No Default Database port is Detected on this server ')
            print("")
    else:
        print ("   Ping Not Responding;  Port Tests are not made" );

    return

def network_ping_dbports(args):
    parsed_command=parse_server(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0]):
                network_ping_special_port(i[0])
    return

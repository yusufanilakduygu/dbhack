import socket
import itertools
import os
from dbhack_parser import *

def network_ping_run ( p_servername):
    response = os.system("ping -c 1 " + p_servername + " > /dev/null ")
    if response == 0:
        print("")
        print (" Connection : "+p_servername+" Ping Successfuly Responding" );
    else:
        print("")
        print (" Connection : "+p_servername+" Ping Not Responding" );
    print("")

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
    parsed_command=parse_network_ping(args+" ;")
    if parsed_command[0] == 'Error':
            return
    else:
            for i in itertools.product( parsed_command[0]):
                network_ping_run (i[0])
    return

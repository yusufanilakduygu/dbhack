# tns poison addition

"""
This is the starting code for DBHack

"""
from dbhack_parser import *
import os
from dbhack_OracleModules import *
from cmd2 import Cmd
from dbhack_mssqlModules import *
import pyparsing
from dbhack_error_module import *
from dbhack_pingModules import *
from dbhack_pingModules import *
from dbhack_DatabaseModules import *


class REPL(Cmd):


    db_connect="Not_Connected"

    prompt = "dbhack> "
    
    
    
    def __init__(self):

        self.commentGrammars = pyparsing.Or([pyparsing.cStyleComment])
        Cmd.__init__(self)

    def do_commands(self,args):
        " Below you can see developed command names , type help command_name for more information "
        commands(args)
        

    def do_ora_chk (self,args):

        """

        Command Name : ora_chk
​
        Explanation
        ----------
        ora_chk pings a server with ports to check Oracle databases
        This command pings a server or servers or a network range
        Port can be a single port or ports or a port range
        Syntax
        ----------
        ora_chk -s  <servename1,servername2,...>  -p  <port01,port02 ...>
        ora_chk -s  < xxx.xxx.xxxx.xx-xxx> -p < port01-port02>
        Samples
        ---------
        ora_chk -s 192.168.0.27 -p 1521
        ora_chk -s 192.168.0.27 -p 1521-1522
        ora_chk -s 192.168.0.27-28  -p 1521,1522
        ora_chk -s 192.168.0.27, 192.168.15.28  -p 1521,1522
        ora_chk -s 192.168.0.27-30  -p 1521,1522
        ora_chk -s servername01  -p 1521,1522
        ora_chk -s servername01,servername01  -p 1521,1522

        """
        ora_chk(args,self.db_connect)

    def do_ora_tns_poison (self,args):

        """

        Command Name : ora_tns_poison
​
        Explanation
        ----------
        ora_tns_poison command checks database
        if there is tns poison vulnerability.
        This command checks a server or servers or a network range
        Port can be a single port or ports or a port range
        Syntax
        ----------
        ora_tns_poison -s  <servename1,servername2,...>  -p  <port01,port02 ...>
        ora_tns_poison -s  < xxx.xxx.xxxx.xx-xxx> -p < port01-port02>
        Samples
        ---------
        ora_tns_poison -s 192.168.0.27 -p 1521
        ora_tns_poison -s 192.168.0.27 -p 1521-1522
        ora_tns_poison -s 192.168.0.27-28  -p 1521,1522
        ora_tns_poison -s 192.168.0.27, 192.168.15.28  -p 1521,1522
        ora_tns_poison -s 192.168.0.27-30  -p 1521,1522
        ora_tns_poison -s servername01  -p 1521,1522
        ora_tns_poison -s servername01,servername01  -p 1521,1522

        """
        ora_tns_poison(args,self.db_connect)

    def do_mssql_chk_browser (self,args):
       
        """ 

        Command Name : mssql_chk_browser
​
        Explanation
        ----------
        mssql_chk_browser pings SQL Server Browser in any server.
	This command is used to know if the SQL server is running on a server.
	If SQL Server does nor respond to your request. It does not mean that
	SQL server is not running on this server. 

        Syntax
        ----------
        mssql_chk_browser  <server1,server2> 
        mssql_chk_browser -s  < xxx.xxx.xxxx.xx-xxx>  

        Samples
        ---------
        mssql_chk_browser -s 192.168.1.37  
        mssql_chk_browser -s 192.168.1.37-40
	mssql_chk_browser -s 192.168.1.37, 192.168.1.42
   
        """
        mssql_chk(args)

    def do_mssql_chk_odbc (self,args):
       
        """ 

        Command Name : mssql_chk_odbc
​
        Explanation
        ----------
        mssql_chk_odbc uses ODBC calls to check SQL Server.
        Simply, it tries to connect SQL server with a fake username and password.
        And then It controls returned message to decide
        if the SQL server is running on a server.
	PAY ATTENTION, This command uses ODBC connect
	Therefore you can be detected by database audit
	 

        Syntax
        ----------
        mssql_chk_odbc  -s  <servename1,servername2,...>  -p  <port01,port02 ...> 
        mssql_chk_odbc  -s < xxx.xxx.xxxx.xx-xxx> -p < port01-port02>

        Samples
        ---------
        mssql_chk_odbc -s 192.168.1.37  -p 1433,1434
        mssql_chk_odbc -s 192.168.1.37-40 -p 1433
	mssql_chk_odbc -s 192.168.1.37, 192.168.1.42 -p 1433
   
        """
        mssql_chk_odbc(args)

    def do_ora_sid (self,args):

        """

        Command Name : ora_sid
​
        Explanation
        -----------
        ora_sid tries to guess Oracle SID and SERVICE_NAME
        command first tries given names as a SID to guess SID 
	and then tries the same name  as  a SERVICE_NAME to guess service name
        You can scan servers and ports as ora_chk command
        SID or SERVICE_NAME names can be given in the command or they can be given in the file
	sid-list.txt file is added as a sample 
	this file is an updated version of http://www.red-database-security.com/scripts/sid.txt

        Syntax
        ----------
        ora_sid -s  <servename1,servername2,...>  -p  <port01,port02 ...> -sid <sid_name_list> | -sid_file <file_name>
        ora_sid -s  < xxx.xxx.xxxx.xx-xxx> -p < port01-port02> -sid <sid_name_list> | -sid_file <file_name>

        Samples
        ---------
        ora_sid -s 192.168.0.27  -p 1521,1522  -sid DB3,DB4
        ora_sid -s 192.168.0.27  -p 1521,1522  -sid_file sid-list.txt 
        """
        ora_chk_sid(args,self.db_connect)

    def do_ora_brute (self,args):

        """ 
        Command Name : ora_brute
​
        Explanation
        -----------
	ora_brute tries to connect Oracle database 
        with given usernames and passwords,
	Username and password pairs can be given in the command
	At the same time you can use username list file and password list file
	PAY ATTENTION, This command uses OCI calls
	Therefore you can be detected by database audit.

        Syntax
        ----------
        ora_brute -s <servername> ,-p  <port_number> , -sid <sid_name> -user <username_list> -passd <password_list>   
	ora_brute -s <servername> ,-p  <port_number> , -sid <sid_namet> -user_file <usernames-list-file > -passd_file <passwords-list-file>   

        Samples
        ---------
        ora_brute -s 192.168.1.34 -p 1521 -sid DB3 -user system,scott  -passwd oracle,tiger
        ora_brute -s 192.168.1.34 -p 1521 -sid DB3 -user_file username-list.txt -passwd_file passwd-list.txt
          
        """
        ora_connect(args, self.db_connect)
        
    def do_mssql_brute (self,args):

        """
        Command Name : mssql_brute
​
        Explanation
        -----------
	mssql_brute tries to connect MS SQL Server database 
        with given usernames and passwords,
	Username and password pairs can be given in the command
	At the same time you can use username list file and password list file
	PAY ATTENTION, This command uses ODBC connect
	Therefore you can be detected by database audit

        Syntax
        ----------
        mssql_brute -s <servername> ,-p  <port_number> , -db <db_name> -user <username_list> -passd <password_list>   
	mssql_brute -s <servername> ,-p  <port_number> , -db <db_name> -user_file <username_file > -passd_file <passwd_file>   

        Samples
        ---------
        mssql_brute -s 192.168.0.27 -p  1433 -db MASTER -user sa -passwd sa123 
        mssql_brute -s 192.168.0.27 -p  1433 -db MASTER -user sa -passwd sa,sa123,sa1
        mssql_brute -s 192.168.0.27 -p  1433 -db MASTER -user_file mssql_username-list.txt -passwd_file mssql_password-list.txt

        """
        mssql_connect(args)

    def do_mssql_brute_null_passwd (self,args):

        """ 
        Command Name : mssql_brute_null_passwd
​
        Explanation
        -----------
        mssql_brute_null_passwd tries to connect MS SQL Server database with null passwords.
        You only need to enter username list to test them with null password
	PAY ATTENTION, This command uses ODBC connect
	Therefore you can be detected by database audit

        Syntax
        ----------
        mssql_brute_null_passwd -s <servername> ,-p  <port_number> ,-user  <username_list>   
	 
        Samples
        ---------
        mssql_brute_null_passwd  -s 192.168.0.28 -p 1433  -user sa,nonsa,master
        
        """
        mssql_connect_null_passwd (args)
        
    def do_mssql_brute_file(self,args):

        """

        Command Name : mssql_brute_file
​
        Explanation
        -----------
        mssql_brute tries to connect MS SQL Server database  with given credential file
        This file contains; Username, Password pairs.
	PAY ATTENTION, This command uses ODBC connect
	Therefore you can be detected by database audit

        Syntax
        ----------
        mssql_brute_file -s <servername> ,-p  <port_number> , -db <db_name> -cred_file  <mssql_credential_file>   
	  

        Samples
        ---------
        mssql_brute_file  -s 192.168.0.28 -p 1433 -db MASTER -cred_file mssql-cred-file.txt
        
        """
        mssql_brute_with_file(args)

    def do_ora_brute_file (self,args):

        """ 
        Command Name : ora_brute_file
​
        Explanation
        -----------
	ora_brute tries to connect Oracle database 
        with given ucredential file
	This file contains; Username, Password pairs.
	PAY ATTENTION, This command uses OCI calls
	Therefore you can be detected by database audit.

	
        Syntax
        ----------
        ora_brute_file -s <servername> ,-p  <port_number> , -sid <sid_name> -cred_file  <usercredential_file>   
	  

        Samples
        ---------
        ora_brute_file  -s 192.168.1.34 -p 1521 -sid DB3 -cred_file oracle-cred-file.txt

        """
        ora_brute_with_file(args,self.db_connect)

    def do_ping (self,args):
       
        """ 

        Command Name : ping
​
        Explanation
        ----------
        ping command pings a server.
	This command is used to check the existense of a server.
	This is a ping command from operating system. If you want;
	you can use ! ping command with argument instead of this

        Syntax
        ----------
        ping -s  <server1,server2> 
        ping -s  < xxx.xxx.xxxx.xx-xxx>  

        Samples
        ---------
        ping -s 192.168.1.37  
        ping -s 192.168.1.37-40
	ping -s 192.168.1.37, 192.168.1.42
   
        """
        network_ping(args)

    def do_ping_port (self,args):
       
        """ 

        Command Name : ping_port
​
        Explanation
        ----------
        ping_port tries to open  a TCP socket connection with given ports
        You can open connection with a server or servers or a network range
        Port can be a single port or ports or a port range

        Syntax
        ----------
        ping_port -s  <servename1,servername2,...>  -p  <port01,port02 ...>
        ping_port -s  < xxx.xxx.xxxx.xx-xxx> -p < port01-port02>
        Samples
        ---------
        ping_port -s 192.168.0.27 -p 1521
        ping_port -s 192.168.0.27 -p 1521-1522
        ping_port -s 192.168.0.27-28  -p 1521,1522
        ping_port -s 192.168.0.27, 192.168.15.28  -p 1521,1522
        ping_port -s 192.168.0.27-30  -p 1521,1522
        ping_port -s servername01  -p 1521,1522
        ping_port -s servername01,servername01  -p 1521,1522
   
        """
        network_ping_ports(args)

    def do_ping_dbports (self,args):
       
        """ 

        Command Name : ping_dbports
​
        Explanation
        ----------
        ping_dbports tries to open a TCP socket connection with default database ports
        Which are given below.

        Ports      	Default Ports
        ------------    --------------------------
        1521 - 1526 	Oracle Net Listener
        1433  		SQL Server Database Engine
        1434  		SQL Server Browser Service
        3306  		MySQL
        5432  		PostgreSQL
        27017 - 27019 	MongoDBs

        Syntax
        ----------
        ping_dbports -s  <server1,server2> 
        ping_dbports  -s  < xxx.xxx.xxxx.xx-xxx>  

        Samples
        ---------
        ping_dbports -s 192.168.1.37  
        ping_dbports -s 192.168.1.37-40
	ping_dbports -s 192.168.1.37, 192.168.1.42
   
        """
        network_ping_dbports(args,self.db_connect)
        
    def do_version(self,args):
        print('')
        print(" dbhack ver 1.1 Developed bu Y. Anıl Akduygu at Sile/Istanbul ")
        print(" ")

    def do_connect_database(self,args):
        return_code=connect_database()
        if return_code=='Connected':
            self.db_connect="Connected"
        

    def do_create_audit(self,args):
        create_audit(args)

    def do_delete_audit(self,args):
        delete_audit(args)

    def do_show_current_audit(self,args):
        show_current_audit(args)

    def do_use_audit(self,args):
        use_audit(args)

    def do_show_audits(self,args):
        show_audit(args)
        
    def do_exit(self,args):
        exit()

if __name__ == '__main__':
    print(' ')
    print("DBHack program ver 1.1 Developed by Y. Anıl Akduygu in Sile - Istanbul")
    print(" ")
    commands(" ")
    print(" ")
    print("DBHack program ver 1.1 Developed by Y. Anıl Akduygu in Sile - Istanbul")
    app = REPL()

    app.cmdloop()

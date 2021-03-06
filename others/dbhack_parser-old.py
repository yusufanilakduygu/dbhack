from pyparsing import *

"""

General ping parser

ping -server,ip,servername -port port1,port2
ping -server xxx.xxx.xxx.xx-xx -port port1-port2
-server 192.178.45.12, 123.56.56.78  -port 123-678  ; 

print(parse_ping("-server x, y   -port 123-67; "))

return result['server']
return result['port']
"""

def parse_ping(pcmd):
    servername=Word(nums+alphas+".")
    portrange=Word(nums)+"-"+Word(nums)
    port=Word(nums)
    ipField = Word(nums, max=3)
    iprange = Combine( ipField + "." + ipField + "." + ipField + "." + ipField + "-" + ipField)

    server_parser="-server"+Group(Or([iprange, delimitedList(servername)])).setResultsName('server')

    port_parser="-port"+  Group(Or([ portrange ,delimitedList(port,",") ])).setResultsName('port')+";"

    Oracle_tnsping_parser=server_parser+port_parser
    try:
        result= Oracle_tnsping_parser.parseString(pcmd)
    except ParseException:
        print('')
        print ('Error No    : Error-01 ')
        print ('Module      : ParseException from dbhack_parser.parse_ping ')
        print ('Explanation : Your command can not be parsed please type')
        print ('              help command_name to see command samples')
        print('')
        result=['Error-01']
    return result














# read a shell name from <STDIN>
# test input shell name is sh shell or not
#                          --------    ----
#                               |        |__ not-matched
#                              matchedShell
#

'''
var=input("Enter a shell name:")
if var == 'sh':
    print("Yes input shell name is:{}".format(var))
else:
    print("Sorry input shell is not matched")
'''
# read a port number from <STDIN>
# test input port number is above 500 or not ?
#                           ---------    ------
#                            ValidPort   InvalidPort
#                              |              |___ service -->App2
#                  initialize service name is App1
port=input("Enter a port number:")
if int(port) >500:
    print("ValidPortNumber")
    service="App1"
else:
    print("Invalid PortNumber")
    service="App2"
    
print("Service name:{}".format(service))









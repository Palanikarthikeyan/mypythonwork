
var=input("Enter a shell name:")
if var == 'bash':
    fname='bashrc'
elif var == 'ksh':
    fname='kshrc'
elif var == 'psh':
    fname='winprofile'
else:
    print("Sorry your input shell name is not matched")
    print("we are assigning default shell name & profile filename")
    var='nologin'
    fname='/etc/profile'

print("Shell name:{}\t ProfileFilename:{}".format(var,fname))


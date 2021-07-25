ename=input("Enter a emp name:")
eid=input("Enter a emp id:")
ecost=input("Enter a emp cost:")
tax=float(ecost)*0.18
total=tax+float(ecost)

print("Emp name:{}\nEmp id:{}\nCost:{}".format(ename,eid,ecost))
print("-"*40)
print("Tax:{}\t Total:{}".format(tax,total))

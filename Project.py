def Save_Expenses(Expenses):
    file=open("Expenses_File.txt","w")
    for Category in Expenses:
        file.write(Category,":"+str(Expenses[Category])+"\n")
    file.close()

def Load_Expenses():
    Expenses={}
    try:
        file=open("Expenses_File.txt","r")
        for line in Expenses:
            Category,Amount=line.strip().split(",")
            Expenses[Category] = float(Amount)
        file.close()
    except FileNotFoundError:
        pass
    return Expenses
Expense=Load_Expenses()
n=int(input("How Many Expenses?"))
for i in range(n):
    Category=input("Enter Category of Expense:")
    Amount=float(input("Enter the Amount of Expense:"))
    if Category in Expense:
        Expense[Category]=Expense[Category]+Amount
    else:
        Expense[Category]=Amount
Save_Expenses(Expense)
import csv

def main():
    while True:    
        ask = input("enter: \n1: for billing\n2: for adding stock\n3: deleting stock\n4: viewing stock\n:")
        if ask in '1':
            billing()
        elif ask in '2':
            addStock()
        elif ask in '3':
            deleteStock()
        elif ask in '4':
            for i in loadMedicine():

                print(i)
        else:
            print("wrong input")

def loadMedicine():
    mainData=[]
    with open('med.csv', 'r') as csvfile:
        read = csv.reader(csvfile)
        for a in read:
            mainData.append(a)
    
    return mainData

def loadBillingMedicine():
    load = loadMedicine()
    mainData = []
    
    while True:
        name = input("enter medicine name: ")
        val = 0
        qt = False
        for row in load:
            if name in row[0]:
                print("Stock available: ",row[1])
                val = row[2]
                askStk = int(input("How much do you want: "))
                if int(askStk)<=int(row[1]):
                    Stk = askStk
                    a = [row[0], int(Stk), float(row[2])]
                    mainData.append(a)
                else:
                    print("Not enough medicine in stock")
                qt = True
                break
        if qt == False:
            print("Medicine not in stock")
        ask = input("Do you want to ask more: ")
        if ask in "NOnoNo":
            decreaseMemo(mainData)
            return mainData

def billing():
    mainData = loadBillingMedicine()
    val = 0
    ask = input("do you want to add discount? ")
    boo=True
    disc=0.0
    if ask in "yesYESYes":
        disc = float(input("how much discount percentage do you want to give? "))
    else:
        boo = False
        
    for a in mainData:
        print("Name:",a[0],"Quantity:",a[1],"Rate:",a[2],"Amount:",(float(a[2])*int(a[1])))
    
        val = val+(float(a[1])*float(a[2]))
    if boo == True:
        discountedPrice = val - val*disc/100.0
    else:
        discountedPrice = val
    
    print("Total =",discountedPrice)
    # print(discountedPrice)

def decreaseMemo(mainData):
    data = loadMedicine()
    mainData = mainData
    for a in mainData:
        for b in data:
            if a[0]==b[0]:
                b[1]=int(b[1])-int(a[1])
    totalMemo(data)

def addStock():
    mainData = loadMedicine()
    while True:
        
        med = input("enter the name of medicine: ")
        qty = int(input("enter the quantity of medicine: "))
        val = float(input("Enter the cost of the medicine: "))
        for a in mainData:
            if a[0]==med:
                qty=int(a[1])+qty
                mainData.remove(a)
                break
        data = [med, qty, val]
        mainData.append(data)
        totalMemo(mainData)
        
        ask = input("do you want to add more medicines to the stock? ")
        if ask in "YESYesyes":
            pass
        elif ask in "NOnoNo":
            break

def saveMemo(mainData):
    csvfile = open('med.csv', 'a', newline='')
    write = csv.writer(csvfile)
    write.writerow(mainData )
    csvfile.close()

def deleteStock():
    mainData = loadMedicine()
    while True:
        name = input("Enter the name of medicine: ")
        for a in mainData:
            if name in a:
                stk = int(input("enter the quantty of medicines: "))
                if stk>int(a[1]):
                    print("spoiled stock more than stored stock, breaking the function")
                    break
                else:
                    a[1]=int(a[1])-stk
        ask = input("do you want to remove more stock: ")
        if ask not in "YESYesyes":
            break
    totalMemo(mainData)

def totalMemo(mainData):
    with open('med.csv', 'w', newline='') as csvfile:
        write = csv.writer(csvfile)
        for a in mainData:
            write.writerow(a)

main()
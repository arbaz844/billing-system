items = {
		101:{'item_name':'Apple','Quantity_in_kgs':50,'Price_per_kg':200},
		102:{'item_name':'Banana','Quantity_in_kgs':30,'Price_per_kg':80},
		103:{'item_name':'Grapes','Quantity_in_kgs':25,'Price_per_kg':300},
		104:{'item_name':'Lemon','Quantity_in_kgs':20,'Price_per_kg':70},
}
trans={}
def stock_check():
    print("Item Name | Available Stock")
    for item_id in items:
        
        if items[item_id]['Quantity_in_kgs'] <= 5:
           
            print("----------------------------------------")
            print("| ",items[item_id]['item_name'], " | ",items[item_id]['Quantity_in_kgs']," |")
            print("----------------------------------------")
        else:
            print("| ",items[item_id]['item_name'], " | ",items[item_id]['Quantity_in_kgs']," |")
def add_new_item():
    item_ids = list(items.keys())
    item_id = max(item_ids) + 1
    item_name = input("Enter Item Name:")
    price = int(input("Enter Price Per Kilo Gram:"))
    quantiy = int(input("Enter Quantity"))
    item = {'item_name':item_name,'Quantity_in_kgs':quantiy,'Price_per_kg':price}
    items[item_id]= item
    print('Item Added')
    print('Item id | Item Name | Quantity | Price ')
    print(item_id, " | ", item_name, " | ", quantiy, " | ", price)
def update_item(item_id):
    quantiy = int(input("Enter Quantity"))
    items[item_id]['Quantity_in_kgs'] = items[item_id]['Quantity_in_kgs'] + quantiy
    print('Item Updated')
    print('Item id | Item Name | Quantity | Price ')
    print(item_id, " | ", items[item_id]['item_name'], " | ", items[item_id]['Quantity_in_kgs'], " | ", items[item_id]['Price_per_kg'] )
def add_item():
    item_name = input("Enter the Item Name")
    print("item id | item name")
    print("-----------------")
    for item in items:
        if item_name in items[item]['item_name']:
            print(item, " | ", items[item]['item_name'])
    
    item_id = int(input("Enter item id (if existing)/Enter 0 (if New)"))
    if item_id == 0:
        add_new_item()
    else:
        #Check for Valid Item ID
        while not item_id in items:
            print("Not Valid Item id")
            item_id = int(input("Enter item id:"))
        update_item(item_id)
def sale(trans_id):
    total = 0
    transaction_items = {}
    while True:
        item_id = int(input("Enter item id (0 if no item):"))
        if item_id == 0:
            break
        else:
            while not item_id in items:
                print("Not Valid Item id")
                item_id = int(input("Enter item id:"))
            quantity = int(input("Enter Quantity:"))
            amount = items[item_id]['Price_per_kg'] * quantity
            items[item_id]['Quantity_in_kgs'] = items[item_id]['Quantity_in_kgs'] - quantity 
            total += amount
            transaction_items[item_id] = [quantity,amount]
            print('Item id | Item Name | Quantity | Price | Amount')
            for item in transaction_items:
                print(item, "| ", items[item]['item_name'], " | ",transaction_items[item][0], " | ", items[item]['Price_per_kg'], " | ", transaction_items[item][1])
            print("---------------------------------------------------")
            print("Total:\t\t\t ", total)
    trans[trans_id] = transaction_items
#Main Function
while True:
    print("Billing System\n Enter Your Choice \n 1. Add Items \n 2. Sales \n 3. Check Stock \n 4. Exit ")
    choice = int(input("Your Choice:"))
    if choice == 1:
        add_item()
    elif choice == 2:
        
        trans_ids = list(trans.keys())
        if len(trans_ids) == 0:
            trans_id = 201
        else:
            trans_id = max(trans_ids) + 1
        sale(trans_id)
    elif choice == 3:
        stock_check()
    elif choice == 4:
        break
    else:
        print("Invalid Choice")
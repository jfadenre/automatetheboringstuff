#addToInventory.py

currentInventory = {'dagger': 1, 'gold coin': 45, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        if i in inventory:
            inventory[i] = inventory.get(i, 0) + 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(currentInventory)
print("")
currentInventory = addToInventory(currentInventory, dragonLoot)
print("New")
displayInventory(currentInventory)


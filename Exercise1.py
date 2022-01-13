def completeshoppinglist():
    
    otherlist = []
    drinklist = []
    foodlist = []
    shoppinglist = {
         'food': foodlist,
        'drink': drinklist,
        'other': otherlist,
    }
   
    while True:  

        item = input("Would you like to add an item/ delete an item or finish your shopping list? [add] [del] [done]: ")

        if item == 'add':
            
            type = input("what is the type of item you want? [food] [drink] [other]: ")
            
            if type == 'food':
                food = input("what food would you like to add to the shopping list? ")
                foodlist.append(food)
            elif type == 'drink':
                drink = input("what drink would you like to add to the shopping list? ")
                shoppinglist[type] = drink
                drinklist.append(drink)
            elif type == 'other':
                other = input("what other item would you like to add to the shopping list? ")
                shoppinglist[type] = other
                otherlist.append(other)
            else:
                food = input("That is not a valid item type. Try Again...")
                continue

        elif item == 'del':
            
            type = input("what was the type of item you want to delete? [food] [drink] [other]: ")

            if type == 'food':
                food = input("what food would you like to delete from the shopping list? ")
                foodlist.remove(food)
            elif type == 'drink':
                drink = input("what drink would you like to delete from the shopping list? ")
                drinklist.remove(drink)
            elif type == 'other':
                other = input("what other item would you like to delete from the shopping list? ")
                otherlist.remove(other)
            else:
                food = input("That is not a valid item type. Try Again...")
                continue

            
        elif item == 'done':
            are_you_sure = input("Are you sure you are done? [yes] [no] ")

            if are_you_sure == 'no':
                continue
            elif are_you_sure == 'yes':
                break
    
    print("Shopping List")
    for food_type in shoppinglist.keys():
        
        print(food_type.title() + ":")
        
        if food_type == 'food':
            for foods in foodlist:
                print(foods)

        elif food_type == 'drink':
            for foods in drinklist:
                print(foods)

        elif food_type == 'other':
            for foods in otherlist:
                print(foods)

completeshoppinglist()


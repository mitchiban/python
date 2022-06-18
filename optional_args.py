

coffees_sold = ["Espresso", "Espresso", "Latte", "Cappuccino", "Mocha", "Espresso", "Latte"]

#print(len(coffees_sold))

def coffee_sold(coffees, to_find="Espresso"):
    total_sold = coffees.count()
    type_sold = coffees.count(to_find)
    print("{}{} coffees were sold.".format(type_sold, "", to_find))
    print("{} coffee(s) were sold in total.".format(total_sold))

coffee_sold(coffees_sold, "Mocha")
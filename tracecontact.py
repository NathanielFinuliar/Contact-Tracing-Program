menu_ = ["Add items","Search items","Modify items","Delete items","Show all data","Exit program"]

main_dictionary = {"Jonathan Finuliar":{"Age":22,"Address":"Malabon","Phone Number":"09123456789","Vaccination Status": "Vaccinated"},
                   "Alyza Catambis":{"Age":15,"Address":"Valenzuela","Phone Number":"099991111234","Vaccination Status": "Unvaccinated"},
                   "Eve Campo":{"Age":18,"Address":"Navotas","Phone Number":"09988842314","Vaccination Status": "Boosted"}}

def display_menu(me):
    print("----Contact tracing!---")
    print("="*20)
    for i in range(len(me)):
        print(f"{i+1} -> {me[i]}")
    print("="*20)

def option_getter():
    while True:
        try:
            print()
            display_menu(menu_)
            option = int(input("What do you want to do? (1-6): "))
        except:
            print("Invalid input try again!")

loop_holder = True
first_run = True
while loop_holder:
    if first_run:
        option_getter()
        first_run = False
    else:
        con = input("Do you want to continue (y/n)? : ").lower()
        if con in ['y','n']:
            if con == 'n':
                loop_holder = False
            else:
                option_getter()
        else:
            print("Invalid input try again!")
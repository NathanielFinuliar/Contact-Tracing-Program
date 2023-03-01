menu_ = ["Add items","Search items","Modify items","Delete items","Show all data","Exit program"]

main_dictionary = {1:{"Name":"Jonathan Finuliar","Age":20,"Address":"Caloocan","Phone Number":"0809547458","Vaccination Status": "Vaccinated"},
                   2:{"Name":"Alyza Catambis","Age":15,"Address":"Zambales","Phone Number":"0804578514","Vaccination Status": "Unvaccinated"},
                   3:{"Name":"Eve Campo","Age":18,"Address":"Batangas","Phone Number":"0958474521","Vaccination Status": "Boosted"}}

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
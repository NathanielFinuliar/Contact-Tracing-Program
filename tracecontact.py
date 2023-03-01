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

def add_item(md):
    while True:
        try:
            name = input("Enter First name: ")
            sur_name = input("Enter Last name: ")
            fname = name+" "+sur_name
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            pnum = input("Enter Phone Number: ")
            vaccinated = input("Enter your Vaccination Status: ")
            break
        except:
            print("Invalid input!")
    sub_dictionary = {}
    key_forsubdict = ["Age", "Address", "Phone Number","Vaccination Status"]
    value_forsubdict = [age,address,pnum,vaccinated]
    for i,x in zip(key_forsubdict,value_forsubdict):
        sub_dictionary[i] = x
    md[fname] = sub_dictionary
    print("Your Contact Information is now Saved!")

def search_items(md):
    while True:
        if len(md.keys()) != 0:
            id_=["Age","Address","Phone Number","Vaccination Status"]
            f_name = input("Enter First name: ")
            l_name = input("Enter Last name: ")


def option_getter():
    while True:
        try:
            print()
            display_menu(menu_)
            option = int(input("What do you want to do? (1-6): "))
            if option != 6 and option in range(1,6):
                function_caller[option](main_dictionary)
            elif option == 6:
                function_caller[option]()
            else:
                print("Range exceeded!")
            return
        except:
            print("Invalid input try again!")

function_caller ={1:add_item,2:search_items}

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
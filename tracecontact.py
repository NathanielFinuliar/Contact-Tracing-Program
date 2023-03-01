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
            key_name = f_name + " " + l_name
            if key_name in md.keys():
                search_items = int(input("What are you looking for? \n1) Age\n2) Address\n3) Phone Number \n4) Vaccination Status\n5) All data\n: "))
                if search_items != 5:
                    print(f"{id_[search_items - 1].capitalize()} : {md[key_name][id_[search_items-1]]}")
                else:
                    print()
                    print(f"All datas contain for {key_name}:")
                    print("-"*20)
                    for i,x in md[key_name].items():
                        print(f"{i.capitalize()} : {x}")
                    print("-"*20)
                return
            else:
                print("Sorry, we can't find this data")
        else:
            print("This is no data available!")
            return 

def modify_items(md):
    while True:
        if len(md.keys()) != 0:
            f_name = input("Enter First name: ")
            l_name = input("Enter Last name: ")
            key_name = f_name + " " + l_name
            if key_name in md.keys():
                id_=["Age","Address","Phone Number","Vaccination Status"]
                modify_items = int(input("What do you want to modify? \n1) Name \n2) Age\n3) Address\n4) Phone Number \n5) Vaccination Status\n: "))
                if modify_items == 1:
                    newf_name = input("Enter New First name you want to modify: ")
                    newl_name = input("Enter New Last name you want to modify: ")
                    newkey_name = newf_name + " " + newl_name
                    md[newkey_name] = md[key_name]
                    del md[key_name]
                    print('Saved')
                    return
                elif modify_items == 5:
                    status = ["Vaccinated","Unvaccinated","Boosted"]
                    for i in range(len(status)):
                        print(f"{i+1}) {status[i]}")
                    state = int(input("Selected status that you want to update: "))

                    new_value = status[state - 1]
                else:
                    new_value = input("Please enter new value: ")
                set_type = {"Age":int,"Address":str,"Phone Number":str,"Vaccination Status":str}

def delete_items(md):
    while True:
        if len(md.keys()) == 0:
            print("There is no data to delete!")
            return
        else:
            f_name = input("Enter First name: ")
            l_name = input("Enter Last name: ")
            del_key = f_name + " " + l_name
            if del_key in md.keys():
                print(f"Trying to delete ID {del_key}...")
                del md[del_key]
                print("Successfully deleted!")
            else:
                print("Sorry, we couldn't delete this data , seem like it doesn't exist")
            return

def show_alldata(md):
    if len(md.keys()) == 0:
            print("There is no data to show!")
            return
    else:
        for num,data in md.items():
            print()
            print(f"* * * {num} * * *")
            for sub,element in data.items():
                print(f"{sub.capitalize()} : {element}")
            print("-"*40) 

def exit_():
    global loop_holder
    while True:
        ask = input("Exit ? (y/n) : ").lower()
        if ask in ['y','n']:
            if ask=='y':
                loop_holder = False
                print("Exiting...")
                print(" ")
                print("Thank you for using this program")
                print("Always take care and have a good day!")
                print(" ")
            else:
                option_getter()
                loop_holder = True
            return
        else:
            print("Invalid input try again!")

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

function_caller ={1:add_item,2:search_items,3:modify_items,4:delete_items,5:show_alldata,6:exit_}

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
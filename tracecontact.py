menu_ = ["Add items","Search items","Modify items","Delete items","Show all data","Exit program"]

main_dictionary = {"Jonathan Finuliar":{"Age":22,"Address":"Malabon","Phone Number":"09123456789","Vaccination Status": "Vaccinated"},
                   "Alyza Catambis":{"Age":15,"Address":"Valenzuela","Phone Number":"099991111234","Vaccination Status": "Unvaccinated"},
                   "Eve Campo":{"Age":18,"Address":"Navotas","Phone Number":"09988842314","Vaccination Status": "Boosted"}}

def display_menu(me):
    print("/"*39) 
    print("$"," "*16, " "*18, "$")  
    print("$"," "* 5, "CONTACT TRACING PROGRAM", " " *5,"$")
    print("$"," " * 3, "coded by Nathaniel Finuliar", " " *3,"$")
    print("$"," " * 12, "BSCOE 2-2", " " *12, "$")
    print("$"," "*16, " "*18, "$") 
    print("/"*39)
    print(" ")
    print(" "*8, "MENU", " "*8)
    print("="*23)
    for i in range(len(me)):
        print(f"{i+1} -> {me[i]}")
    print("="*23)

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
    sub_dictionary = {}    # Create dictionary to be value
    key_forsubdict = ["Age", "Address", "Phone Number","Vaccination Status"]  # Create list that contains key
    value_forsubdict = [age,address,pnum,vaccinated]   # Create list that contains value
    for i,x in zip(key_forsubdict,value_forsubdict): # Merge key and value using for loop combine with zip
        sub_dictionary[i] = x   # Assign value to key
    md[fname] = sub_dictionary  # Add new agrument to dictionary
    print("Your Contact Information is now Saved!")

def search_items(md):
    while True:
        if len(md.keys()) != 0:
            id_=["Age","Address","Phone Number","Vaccination Status"]  # Create list for user to pick option
            # Ask for name
            f_name = input("Enter First name: ") 
            l_name = input("Enter Last name: ")
            key_name = f_name + " " + l_name
            if key_name in md.keys():
                search_items = int(input("What are you looking for? \n1) Age\n2) Address\n3) Phone Number \n4) Vaccination Status\n5) All data\n: "))
                if search_items != 5:
                    # Print key as capotalized and value
                    print(f"{id_[search_items - 1].capitalize()} : {md[key_name][id_[search_items-1]]}")
                else:
                    print() # Show key name
                    print(f"All datas contain for {key_name}:")
                    print("-"*40)
                    # For loop to print all items
                    for i,x in md[key_name].items():
                        print(f"{i.capitalize()} : {x}")
                    print("-"*40)
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
                id_=["Age","Address","Phone Number","Vaccination Status"] # Create list for user to pick option
                modify_items = int(input("What do you want to modify? \n1) Name \n2) Age\n3) Address\n4) Phone Number \n5) Vaccination Status\n: "))
                if modify_items == 1:
                    newf_name = input("Enter New First name you want to modify: ")
                    newl_name = input("Enter New Last name you want to modify: ")
                    newkey_name = newf_name + " " + newl_name
                    md[newkey_name] = md[key_name]  # Assign new key name to dictionary
                    del md[key_name]   # Delete old key name from dictionary
                    print('Saved')
                    return # Return function to stop all progress
                elif modify_items == 5:
                    status = ["Vaccinated","Unvaccinated","Boosted"]
                    for i in range(len(status)):
                        print(f"{i+1}) {status[i]}")
                    state = int(input("Selected status that you want to update: "))

                    new_value = status[state - 1]
                else:
                    new_value = input("Please enter new value: ")
                # Auto type convert using key and function as value
                set_type = {"Age":int,"Address":str,"Phone Number":str,"Vaccination Status":str}
                new_value = set_type[id_[modify_items - 2]](new_value)
                md[key_name][id_[modify_items-2]] = new_value
                print("Saved!")
            else:
                print("Sorry, we can't find this data")
            return
        else:
            print("There is no data to modify")
            return

def delete_items(md):
    while True:
        if len(md.keys()) == 0: # Check if no data in dictionary
            print("There is no data to delete!")
            return
        else:
            f_name = input("Enter First name: ")
            l_name = input("Enter Last name: ")
            del_key = f_name + " " + l_name
            if del_key in md.keys():  # Check if user's input is valid in dictionary
                print(f"Trying to delete ID of {del_key}...")
                del md[del_key] # Delete an item    
                print("Successfully deleted!")
            else:
                print("Sorry, we couldn't delete this data , seem like it doesn't exist")
            return

def show_alldata(md):
    if len(md.keys()) == 0:
            print("There is no data to show!")
            return
    else:
        # For loop to print the data
        for num,data in md.items():
            print()
            print(f"✯ ✯ ✯ {num} ✯ ✯ ✯")
            for sub,element in data.items():
                # Print out value as capitalized key and follow by value
                print(f"{sub.capitalize()} : {element}") 
            print("."*35) 

def exit_():
    global loop_holder #  Declare global variables for later use
    while True:
        ask = input("Exit ? (y/n) : ").lower() # Ask user if user want to continue
        if ask in ['y','n']:
            if ask=='y':
                loop_holder = False
                print("Exiting...")
                print(" ")
                print("Thank you for using this program!")
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
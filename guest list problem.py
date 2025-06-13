# Initialize the guest list as an empty list
guest_list = []

while True:
    print("\n**** MENU ****")
    print("1. Add a guest")
    print("2. Remove a guest")
    print("3. Check if a guest is attending the party")
    print("4. View the final sorted guest list")
    print("5. Exit")
    print("-------------")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        guestname = input("Enter the guest name: ")
        guest_list.append(guestname)
        print(f"{guestname} is added to the guest list!")

    elif choice == 2:
        cancelledguest = input("Enter the name of the guest to remove: ")
        if cancelledguest in guest_list:
            guest_list.remove(cancelledguest)
            print(f"{cancelledguest} has been removed from the guest list!")
        else:
            print(f"{cancelledguest} is not in the guest list!")

    elif choice == 3:
        checkguest = input("Enter the guest name to check: ")
        if checkguest in guest_list:
            print(f"{checkguest} is attending the party!")
        else:
            print(f"{checkguest} is not attending the party!")

    elif choice == 4:
        if len(guest_list) == 0:
            print("The guest list is currently empty.")
        else:
            guest_list.sort()
            print("Here is your final sorted guest list:")
            print(guest_list)

    elif choice == 5:
        print("Exiting... Enjoy your party!")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 5.")

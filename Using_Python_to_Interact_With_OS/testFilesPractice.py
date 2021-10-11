# first line creates file called guests.txt and writes the contents of initial guests into it per line.

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

# loops through each line of guests.txt and prints it to the console.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# new guests to be appended to the guests.txt file.

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# outputs the updated contents to the console.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Names in checked_out are removed from the file. First, copy contents into the list, temp_list.

checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# outputs the edited file to the console.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Checks if Bob and Andrea are still listed in the file. First, copy contents to the list, checked_in.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

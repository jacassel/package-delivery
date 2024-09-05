# Joel Cassel Student ID: Student ID: 011777693
import csv
import package
import hash
# Runtime Complexity: O (N) Space Complexity: O (N) Creates hash table
package_hash = hash.HashTable()
# Runtime Complexity: O (N)^2 Space Complexity: O (N) Gathers data from Package File
with open('WGUPS_Package_File.csv', 'r') as csvfile:  # https://www.programiz.com/python-programming/reading-csv-files
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        package_object = package.Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        package_hash.insert(int(package_object.package_id), package_object)
# Runtime Complexity: O (N)^2 Space Complexity: O (N)^2 Gathers data from Distance Table
with open('WGUPS Distance Table.csv', 'r') as csvfile:  # https://www.programiz.com/python-programming/reading-csv-files
    reader = csv.reader(csvfile, delimiter=",")
    distance_lookup = []
    for row in reader:
        distance_lookup += [row]
# Runtime Complexity: O (N)^2 Space Complexity: O (N) Gathers data from the addresses
with open('addresses.csv', 'r') as csvfile:  # https://www.programiz.com/python-programming/reading-csv-files
    reader = csv.reader(csvfile, delimiter=",")
    address_lookup = []
    count = 0
    for row in reader:
        address_lookup += row
        count += 1


# Runtime Complexity: O (1) Space Complexity: O (1) Rounds the pseudo-time
def round_time(n):   # https://stackoverflow.com/questions/40070868/how-to-round-to-the-nearest-lower-float-in-python
    return int(n * 100)/100


# Variables that are used in the Truck Delivery Algorithms
truck_1 = [1, 4, 5, 7, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck_2 = [3, 6, 18, 21, 22, 23, 25, 26, 32, 33, 35, 36, 38, 39]
truck_3 = [2, 8, 9, 10, 11, 12, 17, 24, 27, 28]

truck_1_address = '4001 South 700 East'
truck_2_address = '4001 South 700 East'
truck_3_address = '4001 South 700 East'
hub_address = '4001 South 700 East'
low_package_id = 0
truck_1_total_miles = 0
truck_2_total_miles = 0
truck_3_total_miles = 0
total_miles = 0
current_time_truck_1 = 8.00
current_time_truck_2 = 9.08
current_time_truck_3 = 10.33

# Runtime Complexity: O (N)^3 Space Complexity: O (N)^2 Truck 1 Delivery Algorithm Greedy Sorting Algorithm
while len(truck_1) != 0:
    shortest_distance = 101.1
    for i in truck_1:
        package_address = package_hash.search(i).address
        package_hash.search(i).time_left_hub = 8.00
        package_hash.search(i).delivery_truck = 'Truck 1'
        address_1_index = address_lookup.index(package_address)
        address_2_index = address_lookup.index(truck_1_address)
        if address_1_index < address_2_index:
            index = address_1_index
            address_1_index = address_2_index
            address_2_index = index
        distance_1 = float(distance_lookup[address_1_index][address_2_index])
        if distance_1 < shortest_distance:
            shortest_distance = distance_1
            low_package_id = i

    truck_1_total_miles += shortest_distance
    current_time_truck_1 += shortest_distance / 18
    package_hash.search(low_package_id).delivery_time = round_time(current_time_truck_1)
    truck_1_address = package_hash.search(low_package_id).address
    truck_1.remove(low_package_id)

truck_address_1_index = address_lookup.index(truck_1_address)
hub_address_index = address_lookup.index(hub_address)
truck_1_total_miles += float(distance_lookup[truck_address_1_index][hub_address_index])
truck_1_address = hub_address


# Run time Complexity: O (N)^3 Space Complexity O (N)^2 truck 2 Delivery Algorithm Greedy Sorting Algorithm
while len(truck_2) != 0:
    shortest_distance = 101.1
    for i in truck_2:
        package_address_2 = package_hash.search(i).address
        package_hash.search(i).time_left_hub = 9.08
        package_hash.search(i).delivery_truck = 'Truck 2'
        address_1_index = address_lookup.index(package_address_2)
        address_2_index = address_lookup.index(truck_2_address)
        if address_1_index < address_2_index:
            index = address_1_index
            address_1_index = address_2_index
            address_2_index = index
        distance_1 = float(distance_lookup[address_1_index][address_2_index])
        if distance_1 < shortest_distance:
            shortest_distance = distance_1
            low_package_id = i

    truck_2_total_miles += shortest_distance
    current_time_truck_2 += shortest_distance / 18
    package_hash.search(low_package_id).delivery_time = round_time(current_time_truck_2)
    truck_2_address = package_hash.search(low_package_id).address
    truck_2.remove(low_package_id)

truck_address_2_index = address_lookup.index(truck_2_address)
hub_address_index = address_lookup.index(hub_address)
truck_2_total_miles += float(distance_lookup[truck_address_2_index][hub_address_index])
truck_2_address = hub_address

# Runtime Complexity: O (N)^3 Space Complexity: O (N)^2 Truck 3 Delivery Algorithm Greedy Sorting Algorithm
package_hash.search(9).address = '410 S State St'  # gives the correct address of package 9
while len(truck_3) != 0:
    shortest_distance = 101.1
    for i in truck_3:
        package_address = package_hash.search(i).address
        package_hash.search(i).time_left_hub = 10.33
        package_hash.search(i).delivery_truck = 'Truck 3'
        address_1_index = address_lookup.index(package_address)
        address_2_index = address_lookup.index(truck_3_address)
        if address_1_index < address_2_index:
            index = address_1_index
            address_1_index = address_2_index
            address_2_index = index
        distance_1 = float(distance_lookup[address_1_index][address_2_index])
        if distance_1 < shortest_distance:
            shortest_distance = distance_1
            low_package_id = i

    truck_3_total_miles += shortest_distance
    current_time_truck_3 += shortest_distance / 18
    package_hash.search(low_package_id).delivery_time = round_time(current_time_truck_3)
    truck_3_address = package_hash.search(low_package_id).address
    truck_3.remove(low_package_id)

truck_address_3_index = address_lookup.index(truck_3_address)
hub_address_index = address_lookup.index(hub_address)
truck_3_total_miles += float(distance_lookup[truck_address_3_index][hub_address_index])
total_miles = truck_1_total_miles + truck_2_total_miles + truck_3_total_miles
truck_3_address = hub_address


# Runtime Complexity: O(N)^2 Space Complexity: O(N) User Interface
input_start = True
user_time = 1.0
user_hours = 0
user_minutes = 0


while True:
    if input_start:
        print("Welcome to the WGUPS delivery program! "
              "\n type 'total' for the total miles the trucks traveled,"
              "\n type 'status' to view the status of the packages at that time"
              "\n followed by a time in HH:MM format between the times 0:00 and 23:59"
              "\n type 'help' for these directions to be repeated,"
              "\n type 'exit' to end the program ")
        input_start = False
    user_input = input("please enter a command: ")
    if user_input.upper() == 'TOTAL':
        print("Total Miles Traveled by Trucks: {}".format(total_miles))
    elif user_input.upper() == 'STATUS':
        user_time_input = input("please enter a time: ")
        user_time_split = user_time_input.split(":")
        user_hours = int(user_time_split[0])
        user_minutes = int(user_time_split[1]) / 60
        user_time = user_hours + user_minutes
        # Runtime Complexity: O (N) Space Complexity: O (1) Package Status
        for i in range(1, 41, 1):
            package_truck_location = package_hash.search(i).delivery_truck
            package_departure = package_hash.search(i).time_left_hub
            package_delivery = package_hash.search(i).delivery_time
            package_delivery_hours = int(package_delivery)
            package_delivery_minutes = int((package_delivery - package_delivery_hours) * 60)
            if package_delivery_minutes == 0:
                package_delivery_minutes = "00"
            elif 0 < package_delivery_minutes < 10:
                package_delivery_minutes = "0" + str(package_delivery_minutes)
            if user_time < package_delivery and user_time < package_departure:
                print("package {} still At Hub and located on {} and will be delivered at {}:{}".format
                      (i, package_truck_location, package_delivery_hours, package_delivery_minutes))
            elif user_time < package_delivery:
                print("package {} is In Route and located on {} and will be delivered at {}:{}".format
                      (i, package_truck_location, package_delivery_hours, package_delivery_minutes))
            elif user_time >= package_delivery:
                print("package {} was Delivered and was located on {} and was delivered at {}:{}".format
                      (i, package_truck_location, package_delivery_hours, package_delivery_minutes))

    elif user_input.upper() == 'HELP':
        print("Welcome to the WGUPS delivery program! "
              "\n type 'total' for the total miles the trucks traveled,"
              "\n type 'status' to view the status of the packages at that time"
              "\n followed by a time in HH:MM format between the times 0:00 and 23:59"
              "\n type 'help' for these directions to be repeated,"
              "\n type 'exit' to end the program ")
    elif user_input.upper() == 'EXIT':
        break
    else:
        print("I do not understand that please try 'total', 'status'"
              " followed by a time such as '08:00', 'help' for the directions or 'exit'")

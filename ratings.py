"""Restaurant rating lister."""


# put your code here
# key = restaurant name
# value = rating
# Define a function that is taking the input file 
# read the file that is given
# Next is read the rating from the file, we might have to separate the rating from restauarnt name
# Create an empty dictionary and then put the key value pair in it
# Then sort the dictionary in alphabtical order
# Return the new dictionary
# Give the user a prompt to enter restaurant name and rating in
# Add the new inputs into the dictionary (key and value)
# Print the sorted ratings  (including the new one's)

global_restaurant_dict = {}
def restaurant_rating(filename):
    file = open(filename)
    #print(file)
    for line in file: 
        rating = line.rstrip()
        print("This is rating after strip")
        print(rating)
        rating = rating.split(":")
        print("This is the rating after split")
        print(rating)

        global_restaurant_dict[rating[0]] = int(rating[1])

    print(f"Created a dictionary after splitting the name and restaurant:\n{global_restaurant_dict}\n")
    
    print(f"Print the items of dictionary:\n{global_restaurant_dict.items()}\n")

    sorted_restaurant = sorted(global_restaurant_dict.items())
    print(f"Our alphabetically sorted list is:\n {sorted_restaurant}")
    return sorted_restaurant


def get_user_input():
    user_restaurant_name = input("Enter the new restaurant name: ")
    user_restaurant_rating = input("Enter the restaurant rating: ")

    global_restaurant_dict[user_restaurant_name] = user_restaurant_rating
    new_restaurant_list = sorted(global_restaurant_dict.items())
    print(new_restaurant_list)
    return new_restaurant_list

restaurant_rating("scores.txt")
get_user_input()


 

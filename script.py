def print_student_info(data_structure):
    # Extract first name from the full name
    first_name = data_structure["full_name"].split()[0]
    # Print student info
    print(f"My name is {data_structure['full_name']}, but you can call me Miss {first_name}.")
    print(f"My student ID is {data_structure['student_id']}.")

def add_pizza_toppings(data_structure, toppings):
    # Add toppings to the pizza_toppings list
    data_structure["pizza_toppings"].extend(toppings)
    # Sort and convert toppings to lowercase
    data_structure["pizza_toppings"] = sorted([topping.lower() for topping in data_structure["pizza_toppings"]])

def print_pizza_toppings(data_structure):
    # Print the sentence
    print("My favourite pizza toppings are:")
    # Iterate through pizza toppings list and print each topping with a bullet point
    for topping in data_structure["pizza_toppings"]:
        print(f"- {topping}")

def print_movie_genres(data_structure):
    # Extract movie genres
    genres = [movie["genre"] for movie in data_structure["movies"]]
    # Print the sentence with comma-separated genres
    print(f"I like to watch {', '.join(genres[:-1])}, and {genres[-1]} movies.")

def print_movie_titles(movie_list):
    # Extract movie titles and capitalize the first letter of each word
    titles = [movie["title"].title() for movie in movie_list]
    # Print the sentence with comma-separated titles
    print(f"Some of my favourite movies are {', '.join(titles[:-1])}, and {titles[-1]}!")

    # Part 1: Starting with def main function and if statement
def main():

    # Part 2: Create a Complex Data Structure
    my_info = {
        "full_name": "Mahenur Master",
        "student_id": 10331036,
        "pizza_toppings": ["PINEAPPLE", "MUSHROOMS", "OLIVES"],
        "movies": [
            {"title": "The Beekeeper", "genre": "thriller"},
            {"title": "Mr Bean", "genre": "comedy"}
        ]
    }
    
    # Part 3: Add Another Movie to the Data Structure
    new_movie = {"title": "Men in Black", "genre": "sci-fi"}
    my_info["movies"].append(new_movie)

    # Part 4: Use a Function to Print Student Name and ID
    print_student_info(my_info)

    #Prints function before adding toppings 
    print_pizza_toppings(my_info)

    # Part 5: Use a Function to Add Pizza Toppings to the Data Structure
    additional_toppings = ("JALAPENO", "ONIONS")
    add_pizza_toppings(my_info, additional_toppings)

    # Part 6: Use a Function to Print a Bullet List of Pizza Toppings after adding toppings 
    print_pizza_toppings(my_info)

    # Part 7: Use a Function to Print a Comma-Separated List of Movie Genres
    print_movie_genres(my_info)

    # Part 8: Use a Function to Print a Comma-Separated List of Movie Titles
    print_movie_titles(my_info["movies"])

if __name__ == '__main__':
    main()

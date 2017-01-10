text_file = open('scores.txt')

restaurant_ratings = {}


def make_restaurant_dict(file_name):
    """ update dictionary with restaurant, score from file_name"""

    for line in text_file:
        name, score = line.rstrip().split(':')
        restaurant_ratings[name] = int(score)


def sort_restaurants():
    """Sorts and prints restaurant ratings dictionary"""

    sorted_ratings = sorted(restaurant_ratings.items())

    for restaurant, rating in sorted_ratings:
        print "%s is rated at %d." % (restaurant, rating)


def add_restaurant():
    """add user input restaurant and score to dictionary"""

    restaurant_name = raw_input("Enter restaurant name: ")
    restaurant_score = int(raw_input("Enter score: "))

    restaurant_ratings[restaurant_name] = restaurant_score


#main

make_restaurant_dict('scores.txt')

add_restaurant()

sort_restaurants()

text_file = open('scores.txt')

restaurant_ratings = {}

for restaurant_pair in text_file:
    rating_pair = restaurant_pair.rstrip().split(':')
    restaurant_ratings[rating_pair[0]] = rating_pair[1]

sorted_ratings = sorted(restaurant_ratings.items())

for restaurant, rating in sorted_ratings:
    print "%s is rated at %s." % (restaurant, rating)

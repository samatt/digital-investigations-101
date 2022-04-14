# source: https://first-web-scraper.readthedocs.io/en/latest/
# source: https://scrapism.lav.io/intro-to-python/

# make an empty list
my_list = []

# add something to our list with the "append" method
my_list.append("hi")  # the list will now look like this: ["hi"]

# add some more stuff
my_list.append(45)
my_list.append(100.2)
my_list.append("whatever")

# now our list will look like this:
# ["hi", 45, 100.2, "whatever"]

# get the length of a list
len(my_list)

# you can access individual items in the list by referrring to their index value
print(my_list[0])  # prints "hi"
print(my_list[2])  # prints 100.2

# use negative numbers to start at the back
print(my_list[-1])  # prints "6" - the last item

# you can access part of a list with a ":"
my_list[1:3]  # will be [45, 100.2, "whatever"]


# Tuples are a special type of list that cannot be changed once they are created. That’s not especially important right now.
# All you need to know is that they are declared with parentheses (). For now, just think of them as lists.
tuple_of_numbers = (1, 2, 3, 4, 5)


def melon_count(file_date, text):
    """Given the day and path, print the delivery report for items, count, and amount"""

    print(f"Day {file_date}:")

    # open file
    file = open(text)

    # iterate over lines in file
    for line in file:
        # remove any white space to the right
        line = line.rstrip()
        # split the line into a word list on the ('|')
        words = line.split('|')

        # assign variables for each item in the list
        melon = words[0]
        count = words[1]
        amount = words[2]
        # print results
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    # close the file
    file.close()


# run the code for each day
melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")


# *****************
# ORIGINAL CODE  #
# ****************


# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

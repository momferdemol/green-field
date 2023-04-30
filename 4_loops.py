
#-----------------------------------------------------
# for item in list_of_items:
#   do something for each item
#-----------------------------------------------------
# while something_is_true:
# do something until condition is false
#-----------------------------------------------------


def hello_world():
    # simple 'hello word' loop
    word = "Hello world"
    length = len(word)
    position = 0

    while position < length:
        print(word[position])
        position += 1


def average_height():
    # use a for-loop to calculate the average from a list of values
    student_heigths = input("Input a list of student heights, separated by a space.\n").split()
    heights_total = 0

    for height in range(0, len(student_heigths)):
        student_heigths[height] = int(student_heigths[height])
        heights_total += student_heigths[height]

    # can also use sum() to calculate list total
    heights_average = round(heights_total / (height + 1))
    print(f"\nYour input: {student_heigths}\n")
    print(f"The average height is: {heights_average}\n")


def highest_score():

    score_input = input("Input a list of student scores, separated by a space.\n").split()

    for score in range(0, len(score_input)):
        score_input[score] = int(score_input[score])

    for score in range(0, len(score_input)):
        a = score_input[score]
        # print(f"a: {a}")

        # can also use max() to find highest value in list
        if score != len(score_input) - 1:
            b = score_input[score + 1]
            # print(f"b: {b}")

            if a > b:
                high_score = a
    
    print(f"\nHighest score: {high_score}\n")

    # and now much simpler :-)

    highest_score = 0
    for score in score_input:
        if score > highest_score:
            highest_score = score
    
    print(f"Highest score: {high_score}\n")

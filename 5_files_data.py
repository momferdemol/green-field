
# open a file, read the contents, and automatically close the file
with open("your-file-here.txt") as file:
    contents = file.read()
    print(contents)

# open a file in write mode, write new text to file, and close the file
with open("your-file-here.txt", mode="w") as file:
    file.write("New text..")

# Absolute File Path
# /Users/John/WorkingFolder/

# Relative File Path (== working folder)
# ./my-file.txt

# module to work with csv files
import csv

# open a csv file and load into an object
with open("your-csvfile.csv") as data_file:
    data_object = csv.reader(data_file)
    for row in data_object:
        print(row)

# use the 'pandas' library via pip to work with csv file
# pandas library has lots of features for data analysis
# http://pandas.pydata.org/

# import pandas
# data = pandas.read_csv("your-file-here.csv")
# print(data["column_name"])

# list (and dictionary) comprehension
# change the value in a list without
# creating a loop and append the new value
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
# new_dict = {key:new_value for key in dictionary}
# new_dict = {key:new_value for key in dictionary if test}
# new_dict = {new_key:new_value for (key, value) in dictionary.items()}

# numbers = [1,2,3,4]
# new_list = [n + 1 for n in numbers]

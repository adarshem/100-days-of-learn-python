programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
# reading a key from the dictionary
print(programming_dictionary["Bug"])

# adding an item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over"
print(programming_dictionary)

# updating an item in the dictionary
programming_dictionary["Bug"] = "Updated text for the key Bug"
print(programming_dictionary)

# clearing a dictionary
# programming_dictionary = {}
# print(programming_dictionary)

test_item = {"z": "Test Z", "a": "test", "b" : "ttt"}
# test_item["b"] = "wow"
# test_item["b"] = "5"
print(test_item)
print(list(test_item)) # list all keys used in the dictionary ['z', 'a', 'b']
print(sorted(test_item)) # list all key used in the dictionary in sorted order ['a', 'b', 'z']
print("z" in test_item) # check if a key is present in the dictionary True

new_dictionary = dict([("a", "test-a")]) # create a dictionary using dict function
print(new_dictionary)



# loop through dictionary
for k,v in test_item.items():
    print(k, v)    

for key in programming_dictionary:
    print(programming_dictionary[key])


# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades.
#
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
#
# The final version of the student_grades dictionary will be checked.
#
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.
#
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    score =  student_scores[key]
    if 90 < score <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < score <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < score <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)

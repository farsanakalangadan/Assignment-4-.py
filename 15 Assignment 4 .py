#  Assignment 4 : Survey Feedback Analyzer

###############################################

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print(feedback_data)

# Add more feedbacks

# customer name

# written feedback

# Rating between 1 and 5

# the new serial numbers must start from 11

#  1. Ask how many feedbacks to add

n = int(input("How many more feedbacks do you want to add? "))

#  Enter 2 

#  2. repeat the process

for i in range(n):

    #  3.Get the customer's details

    name = input("Enter customer name: ")

    feedback = input("Enter written feedback: ")

    rating = int(input("Enter rating (1-5): "))

    #   4. Check the rating

    

    while rating < 1 or rating > 5:
        print("Invalid rating! Please enter a rating between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))

        #  5. Generate the serial number


    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)

    #  6. Append the new information

    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nUpdated Feedback Data:")
print(feedback_data)

# 1. Get each feedback

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    #  2. Remove punctuation

    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    #  3 Remove extra spaces

    text = ' '.join(text.split())

    # 4. Remove leading and trailing spaces

    text = text.strip()

    text = text.lower()

    feedback_data['Feedback'][i] = text

print("\nCleaned Feedback:")
print(feedback_data['Feedback'])

#   Word count insights
###############################

def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count

#    Final summary & Insights
####################################


print("\nWord Count Insights:")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

#  Part A : Display the cleaned dictionary

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))
print("\nFinal Cleaned Feedback Data:")

print(feedback_data)

#  Part B : Calculate the Average rating

total_rating = sum(feedback_data['Rating'])

total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))

# Part C : Find the longest comment
##################################

longest_feedback = ""
max_words = 0

for feedback in feedback_data['Feedback']:

    word_count = len(feedback.split())

    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback

print("\nLongest Feedback:")
print(longest_feedback)

print("Word Count:", max_words)

#  Part D : Find all unique words
#################################

unique_words = set()

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:
        unique_words.add(word)

print("\nUnique Words:")

print(sorted(unique_words))

# Optional task - Sort feedbacks by rating

#########################################

sorted_feedbacks = sorted(
    zip(
        feedback_data['S_No'],
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[3],
    reverse=True
)

print("\nFeedbacks Sorted by Rating:")

for item in sorted_feedbacks:
    print(item)


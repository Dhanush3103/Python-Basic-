#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment 

# ### Exercise 1: Prime Numbers
# ###### Write a Python program that checks whether a given number is prime or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# In[1]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# ### Exercise 2:Product of Random Numbers
# ###### Develop a Python program that generates two random numbers and asks the user to enter the product of these numbers. The program should then check if the user's answer is correct and display an appropriate message.

# In[3]:


import random

def multiplication_quiz():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    correct_product = num1 * num2
    
    user_answer = int(input(f"What is the product of {num1} and {num2}? "))
    
    # Check if the user's answer is correct
    if user_answer == correct_product:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct answer is {correct_product}.")
multiplication_quiz()


# ### Exercise 3: Squares of Even/Odd Numbers
# ###### Create a Python script that prints the squares of all even or odd numbers within the range of 100 to 200. Choose either even or odd numbers and document your choice in the code.

# In[4]:


def print_even_squares():
    for number in range(100, 201):
        if number % 2 == 0:  # Check if the number is even
            print(f"The square of {number} is {number ** 2}")

# Call the function to print the squares of even numbers
print_even_squares()



# In[7]:


def print_odd_squares():
    for number in range(100, 201):
        if number % 2 != 0:  # Check if the number is even
            print(f"The square of {number} is {number ** 2}")

# Call the function to print the squares of even numbers
print_odd_squares()


# ### Exercise 4: Word counter
# ###### write a program to count the number of words in a given text.
# ###### example:
# ###### input_text = "This is a sample text. This text will be used to demonstrate the word counter."
# ###### Expected output:
# ###### 'This': 2 
# ###### 'is': 1
# ###### 'a': 1
# ###### 'sample': 1
# ###### 'text.': 1

# In[ ]:


def count_words(input_text):
    words = input_text.split()
    word_counts = {}

    for word in words:
        word = word.lower()  
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

input_text = "My Name is Dhanush And I am From AP My Full Name is Dhanendranath"
word_counts = count_words(input_text)

for word, count in word_counts.items():
    print(f"'{word}': {count}")


# ### Exercise 5: Check for Palindrome
# ###### Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome, and False otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
# ###### Example:
# ###### Input: "racecar"
# ###### Expected Output: True

# In[11]:


def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
input_string = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(input_string):
    print("True")
else:
    print("False")


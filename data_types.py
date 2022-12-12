#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#first we want to check the data type 
# print(type(two_digit_number))

#assign varaiables to each digit
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

#transfor the string into integer, add it up and print it
print(int(first_digit) + int(second_digit))
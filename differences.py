# EXERCISE 1: 
# Get Name
# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

# get_name = input('What is your name?')
# print('Hello,' + get_name)


# EXERCISE 2:
# Reverse It
# Write a method that reverses a string. Here’s the javascript:


# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

# def reverse_it():
#     string = 'a man, a plan, a canal, frenemies!'
#     reverse = ''
#     for i in range(len(string)):
#         reverse += string[len(string) - (i + 1)]
    
#     print(reverse)
# reverse_it()


# EXERCISE 3:
# Swap Em
# Write a method that swaps the values of two variables around. Here’s the javascript:
# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

# def swap_em():
#     a = 10
#     b = 30
#     temp = None

#     temp = b
#     b = a
#     a = temp
#     print(f'a is now {a}, and b is now {b}')
# swap_em()


# EXERCISE 4:
# Multiply Array/List
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };


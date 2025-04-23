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

# def multiply_array(ary):
#     if len(ary) == 0:
#         return 1
#     total = 1
#     for numb in ary:
#         total *= numb
#     return total

# EXERCISE 5:
# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

# def fizzbuzzer(x):
#     if x % (3 * 5) == 0:
#         return 'fizzbuzz'
#     elif x % 3 == 0:
#         return 'fizz'
#     elif x % 5 == 0:
#         return 'buzz'
#     else:
#         return 'archer'
# result = fizzbuzzer(22)
# print(result)

# EXERCISE 6:
# Nth Fibonacci
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

# def nth_fibonacci_number():
#     fibs = [1, 1]
#     num = input('which fibonacci number do you want?')
#     num = int(num)
#     while len(fibs) < num:
#         length = len(fibs)
#         next_fib = fibs[length - 2] + fibs[length - 1]
#         fibs.append(next_fib)
#     print(f'{fibs[-1]} is the Fibonacci number at position {num}')
# nth_fibonacci_number()

# EXERCISE 7:
# Search Array/List
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def search_array(array, value):
    
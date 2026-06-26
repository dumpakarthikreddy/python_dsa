#Write a function that calculates the sum and product of all elements in a tuple of numbers.
"""
def sum_tuples(numbers):
   total_summ=0
    total_product=1

    for num in numbers:
        total_summ+=num
        total_product*=num
    return total_summ,total_product
print(sum_tuples((1,4,6,7,3,4)))    

"""

#Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
"""
def summ_tuples(tuple1,tuple2):
    if len(tuple1)!=len(tuple2):
        return ("the length of the tuple is not same")
    total1=0
    total2=0
    for i in tuple1:
        total1+=i
    for j in tuple2:
        total2+=j
    return total1+total2
print(summ_tuples((1,2,3,4,),(5,6,7,8)))    

"""
'''
#Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

def insert_tuplee(tuple1,value):
    return (value,) + tuple1
print(insert_tuplee((2,3,4),1))
'''
'''
#concating os strings using tuples
def concatting_tup(words):
    result=""
    for ch in words:
        result += ch + " "
    return result
print(concatting_tup(('Hello', 'World', 'from', 'Python')))
'''

def get_diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))
tup = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(tup)
print(output_tuple)

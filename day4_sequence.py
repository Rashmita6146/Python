# what is sequence : sequence methods in python are funtions and operators
# that apply to sequence data type, which includes lists,
# tuples , strings, and other ordered collections


'''


types of seuqence methods

1. common sequence methods
2. list- specific methods
3. string specific method

'''
text = "hello"    
print(len(text))

rashmita="hello, world!"   #string using len()
length_of_rashmita=len(rashmita)
print(length_of_rashmita)

numbers=[1,2,3,4,5]    #using len() with a list
length_of_numbers=len(numbers)
print(length_of_numbers)

a=(1,2,3,4,55,66,77,88,99) #using len() with a tuples
length_of_tuples=len(a)
print(length_of_tuples)

#using len() with an empty list

empty_list=[]
length_of_empty_list=len(empty_list)
print(length_of_empty_list)

#using len() with nested lists

nested_list=[[11,33,44],[1,2,3,4],[45,67,85]]
length_of_nested_list=len(nested_list)
print(length_of_nested_list)


#sorted sequence

letters=["b","a","e","c","d","f"]
print(sorted(letters))

#sum sequence
values=[20,60,100,10,5]
print(sum(values))   #output will be 195

#min and max sequence

rashmita=[8,2,0,5,6,7,100,44,7,5,6,9,3,2,1]  #list
print(min(rashmita))
print(max(rashmita))

rashmita1="abcde"   #string data type
largest_letter=min(rashmita1)
print(largest_letter)

mixed_data=["apple",5,10,"data_analyst"]
print(min(mixed_data))

# mixed data=["apple",5,10,"data_analyst"]  #this kind of value with string and int
#it will show error as it contain the different data type

#methods_list-strings

fruits=["apple" , "banana"]
fruits.append("cherry")
print(fruits)

numbers=[1,2,3,4,5]
numbers.append(6)
print(numbers)

rashmita2=["data","analyst","data_engineer"]
kiran.index("analyst")
print(rashmita2)






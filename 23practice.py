#extend 

fruits = ["grapes","mango","strawbeery"]
new_fruits = ["apple","cherry"]
fruits.extend(new_fruits)
print(fruits)

#remove
fruits = ["grapes","mango","strawbeery","grapes","mango", "grapes" ]
fruits.remove("grapes")
print(fruits)

#pop()
numbers = [50,100,150,fruits,300,20.0,False]
print(numbers.pop())

#ordering of elements
numbers = [50,100,150,fruits,300,20.0,False]
numbers.reverse()
print(numbers)
print(numbers[::-1])

#sort
numbers = [5,2,1,3,6,4,8,9,7,10]
numbers.sort()
print(numbers)

colours = ["red","black","white","purple"]
colours.sort()
print(colours)


colours = ["red","black","white","purple"]
colours.sort(reverse=True)
print(colours)

#aliasing and cloning

fruits = ["grapes","mango","strawbeery"]
fruits.append("mango")
before_id = id(fruits)
fruits.append("orange")
after_id = id(fruits)
print("ID before apending", before_id)
print("ID after apending", after_id)

#cloning by slice operator
new_numbers = [5,10,20]
cloned_numbers = list(new_numbers)
cloned_numbers.append(35)
print(new_numbers)
print(cloned_numbers)

new_numbers = [1,2,3,4,5]
cloned_numbers = new_numbers[:]
cloned_numbers[2] = 9
print(new_numbers)
print(cloned_numbers)
print(id(new_numbers))
print(id(cloned_numbers))


#cloning by copy function
numbers = [5,2,3,6,4,20]
n= numbers.copy()
n[1] = 10
print(numbers)
print(n)
print(id(numbers))
print(id(n))

#mathematical operator in list
numbers = [50,20,10,30]
numbers1 = [15,25,35]
print(numbers+numbers1)

#repetation 
print(numbers1*3)

#numbers = [50,20,10,30]
numbers1 = [15,25,35]
print(numbers<numbers1)
print(numbers>numbers1)
print(numbers==numbers1)

fruits = ["grapes","mango","strawbeery"]
fruits1 =["cherry","Guva"]
fruits2 = ["Grapes","mango"]
print(fruits==fruits2)
print(fruits==fruits1)
print(fruits!=fruits1)


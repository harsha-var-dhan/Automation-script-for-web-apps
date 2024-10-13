
values = [1, 2, "harsha", 4, 5]
#List is a data type that allows multiple values and can be different data types

print(values[0])  #1

print(values[3]) #4

print(values[-1]) #5
print(values[1:3]) #2 harsha
values.insert(3, "reddy")#[1, 2, 'harsha', 'reddy', 4, 5]
print(values)
values.append("End")#[1, 2, 'harsha', 'reddy', 4, 5, 'End']
print(values)

values[2] = "HARSHA" #Updating

del values[0] #deleting index

print(values)

#Tuple - Same as LIST data type but immutable
val = [1, 2, "harsha", 4.5]

print(val[1])

#val[2] = "HARSHA"

print(val)

#dictionary
dic = {"a":2, 4:"bcd", "c":"Hello World"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "Rahul"

dict["lastname"]= "Reddy"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])



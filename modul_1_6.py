my_dict={"Vasya":1975,"Egor":1999,"Masha":2002}
print(my_dict["Vasya"])
my_dict["Masha"]= 1985
print(my_dict["Masha"])
my_dict["Roman"]=1977
print(my_dict)
del my_dict["Roman"]
print(my_dict)
my_dict.update({"Anton":1980,"Max":1984})
print(my_dict)
my_dict["Lena"]=1988
print(my_dict)
del my_dict["Lena"]
print(my_dict)
my_set={1,"Яблоко",42.314}
print(my_set)
print(my_set.discard(1))
print(my_set)
print(my_set.remove("Яблоко"))
print(my_set)
print(my_set.add(5))
print(my_set)
print(my_set.add(6))
print(my_set)



shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(id(shopping_list))
print(id(another_list))

print(shopping_list)


a = b = c = d = e = another_list
print(a)

print("Adding Cream")
b.append("cream")
print(b)
print(c)
print(e)

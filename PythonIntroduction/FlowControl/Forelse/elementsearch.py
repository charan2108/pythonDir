group = [1, 2, 3, 4]
search =  int(input("enter the search group element:  "))
for element in group:
    if search == element:
        print("the element is found")
        break
    else:
        print("element not found")
sample_set = { "Yellow","Orange","Black"} 
sample_list = ["Blue", "Green","Red"]
sample_set.update(sample_list)
print(sample_set)

set1={10,20,30,40,50}
set2={30,40,50,60,70}
identical_items=set1.intersection(set2)
print(identical_items)

set1={10,20,30,40,50}
set2={30,40,50,60,70}
unique_items=set1.union(set2)
print(unique_items)

set1={10,20,30}
set2={20,40,50}
set1=set1-set2
print(set1)

set1={10,20,30,40,50}
set1=set1-{10,20,30}
print(set1)

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
result=set1.symmetric_difference(set2)
print(result)

set1={10,20,30,40,50}
set2={60,70,80,90,10}
common_elememts=set1.intersection(set2)
print(common_elememts)

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
set1=set1-set2 | (set2-set1)
print(set1)


set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
intersection=set1.intersection(set2)
print(intersection)

a={30,40,70,20}
b={20,50,60,40}
common_elememts=a.intersection(b)
print(common_elememts)

a={30,40,70,20}
b={20,50,60,40}
identical_items=a.union(b)
print(identical_items)

a={30,40,70,20,80,50}
b={20,50,60,40,90,10}
ab=a-b
ba=b-a
print("a_b:",ab)
print("b_a:",ba)
print()

X= {50, 20, 70, 40, 10, 60, 30} 
Y= {80, 50, 100, 70, 90, 60}
print("first method using differnce:")
diff1=X.difference(Y)
diff2=Y.difference(X)
print("difference of XandY:",diff1)
print("difference of XandY:",diff2)
print()
print("second method using operator:")
diff1=X-Y
diff2=Y-X
print("difference of XandY:",diff1)
print("difference of YandX:",diff2)
print()


def check_common_elements(set1, set2):
    return len(set1.intersection(set2)) == 0

a = {23,45,78,8,56}
b = {42,55,26,87}
z = {87,46}

print("Two given sets have no Elements in Common:")
print("Compare A and B: ", check_common_elements(a, b))
print("Compare B and Z: ", check_common_elements(b, z))
print("Compare A and Z: ", check_common_elements(a, z))
print()

a={23,45,17,8,56,10}
print("setA:",a)
print("maximum of A:",max(a))
print("minimum of A:",min(a))
print()
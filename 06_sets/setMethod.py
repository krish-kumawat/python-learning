


# s1 = {1,2,3,4}
# s2= {5,6,6,7}
# print(s1.union(s2))
# s1.update(s2)

# print(s1,s2)

cities1= {"Paris","London","New York","Tokyo"}
cities2= {"Berlin","Madrid","New York","Tokyo"}
cities3 = cities1.union(cities2)
print(cities3)
cities4 = cities1.intersection(cities2)
print(cities4)
cities5 = cities1.difference(cities2)
print(cities5)
print(cities1.issuperset(cities2))
cities6 = {"paris","london"}
print(cities6.issubset(cities1))
cities1.add("hentai city")
cities1.remove("hentai city")
print(cities1)

# ======================= LIST =======================
# can add/remove; maintains order
l = ["Bob", "Rolf", "Anne"]

# ======================= TUPLE =======================
# key difference between list & tuple is that you can not edit a tuple
t = ("Bob", "Rolf", "Anne")

# ======================= SET =======================
# can add/remove, but cannot have duplicates
# no order to input 
s = {"Bob", "Rolf", "Anne"}

# subscript notation can be used in lists & tuples 
# print(l[0])
l[0] = "Smith"
l.append("Kerri")
print(l)
l.remove("Rolf")
print(l)

s.add("Smith")
print(s)

# ======================= ADVANCED SET OPERATIONS =======================
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# take in set & remove elements from another
# //// DIFFERENCE ////
local_friends = friends.difference(abroad)
print(local_friends)

# //// DIFFERENCE ////
local = {"Rolf"}
gone = {"Bob", "Anne"}
peeps = local.union(gone)
print("peeps", peeps)

# //// INTERSECTION ////
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print("both", both)
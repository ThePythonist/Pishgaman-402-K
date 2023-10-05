pythons = ["milad", "javad", "yasna", "mahsa"]
icdls = ["javad", "navid", "kazem", "mahsa"]
common = [ i for i in pythons if i in icdls ]
print(common)

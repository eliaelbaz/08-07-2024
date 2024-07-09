##start
num_friends: int = int(input("Enter the number of friends who came to Danny: "));
num_triangles: int = int(input("Enter the number of pizza triangles ordered: "));
print (f"Each friend received {num_triangles // num_friends} pizza triangles.");
print (f"{num_triangles % num_friends} pizza triangles are left.");
##End
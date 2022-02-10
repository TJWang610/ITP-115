mylist = []
while True:
   c = input("Enter a letter:")
   if c == "s":
       break
   mylist.append(c)
   result = ",".join(mylist)

   print(result)
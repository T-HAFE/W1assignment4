try:
    n = input("Please, Enter  an integer : ")
    n = int(n)
except ValueError:
    print("Unpeacefully converted to integer!")
else:
    print("The result if the operation is successful!")

print ("time to say goodbye")
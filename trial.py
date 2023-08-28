print("This is the Hollow rectangle")
m = int(input("Enter the rows: "))
n = int(input("Enter the columns: "))
for a in range(1, m+1):
    for b in range(1, n+1):
        if a == 1 or a == m or a == n:
            print(" # ", end=" ")
        else:
            print(" # ", end=" ")
    print()


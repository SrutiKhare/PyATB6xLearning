# Learn the use of pass, break and continue :
for i in range(1,11):
    print(i)
    if i==5:
        break # kick you out of the loop
print("---------------")
for i in range(1,11):
    if i==6 or i==5:
        print(i)
    else:
        pass # pass is a placeholder statement that does nothing
print("---------------")
for i in range(10):
    if i==5:
        print(i)
    else:
        continue # skips the current iteration of the loop


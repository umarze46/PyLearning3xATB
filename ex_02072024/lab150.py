try:
    with open("testdat.txt", 'r') as file:
        data = file.read()
    print(data)
except Exception as e:
    print(e)

finally:
    print("closing the file any way")

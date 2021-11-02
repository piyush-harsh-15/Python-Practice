# Solution to Print Function Questionn of Hackerrank
# To print a series in a continous line, eg. n = 5
# series - 12345

n = int(input("Enter a number:"))

if 1 <= n <= 150:
    for i in range(1, n+1):
        print(i, end = '')
else:
    print("Enter within the range of 1 to 150")
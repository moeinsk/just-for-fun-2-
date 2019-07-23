#writed by mpspy
print("Enter Number:")
N = int(input())

numbers = []

for i in range(N):
    numbers.append("*")
    print(''.join(numbers))
    if i == N-1:
        for m in range(N):
            numbers.pop()
            print(''.join(numbers))
#thise is python's power           

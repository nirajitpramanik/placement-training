def generate_permutations(arr, start=0):
    if start == len(arr) - 1:
     
        return [arr[:]]
    
    permutations = []
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        permutations += generate_permutations(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]
    
    
    return permutations
    

p = list(map(int,input().split()))
perm = generate_permutations(p)
for i in perm:
    i = [str(j) for j in i]
    print(' '.join(i))

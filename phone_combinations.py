def combinations(letters1, letters2):
    result = []
    
    for i in letters1:
        for j in letters2:
            result.append(f"{i}{j}")
            
    return result

def generate_combinations(nums):
    d = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    
    if len(nums) == 1:
        letters = d[nums[0]]
        return [i for i in letters]
    
    letters1 = d[nums[0]]
    letters2 = d[nums[1]]
    
    result = combinations(letters1, letters2)
    
    counter = 2
    
    while counter < len(nums):
        result.extend(combinations(result, d[nums[counter]]))
        counter += 1
        
    result = [i for i in result if len(i) == len(nums)]
    return result
    
if __name__ == "__main__":
    inp = [int(i) for i in input()]
    
    print(" ".join(generate_combinations(inp)))

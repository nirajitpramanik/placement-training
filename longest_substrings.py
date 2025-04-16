def find_substring(string):
    max_str = ""
    max_len = 0
    temp = ""

    for i in string:
        if i not in temp:
            temp += i
            
            if len(temp) > max_len:
                max_len = len(temp)
                max_str = temp
            
        else:
            temp = f"{i}"

    return max_len

inp = input()

print(find_substring(inp))

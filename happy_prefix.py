def happy_prefix(string):
    current, temp = "", ""
    start, end = 0, len(string)

    while ((start < len(string)) and (end >= 0)):
        if string[0 : start] == string[end : len(string)]:
            current = string[0 : start]
        start += 1
        end -= 1
        
    return current

if __name__ == "__main__":
    string = input()
    print(happy_prefix(string))

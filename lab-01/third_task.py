def remove_plus(text: str) -> str:
    result = ""
    for i in range(len(text)):
        if text[i] == "+" and i + 1 < len(text) and text[i + 1].isdigit():
            continue
        result += text[i]
    return result

print(remove_plus("1+2+3"))
print(remove_plus("a+5, b+c, 2+3+x"))
print(remove_plus("x+"))


#b
def string_histogram(text):
    t = {}
    ext = text.lower()
    for ch in ext:
        ch2 = ch.isalpha()
        if ch2 == True:
            a=(ext.count(ch))
            t[ch] = a
    print(t)
    return(t)
print("b:")
string_histogram("Das ist ein Text")

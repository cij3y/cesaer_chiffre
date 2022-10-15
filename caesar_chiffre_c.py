
#b
def string_histogram(text):
    t = {}
    ext = text.lower()
    for ch in ext:
        ch2 = ch.isalpha()
        if ch2 == True:
            a=(ext.count(ch))
            t[ch] = a
    #print(t)
    return(t)
#print("b:")
string_histogram("Das ist ein Text")
#print()

#c
def frequencies(histogram):
    anzahl_values = 0
    for v in histogram.values():
        anzahl_values = anzahl_values + v
    #print(anzahl_values)

    liste = [0 for _ in range (97,123)]
    for k, v in histogram.items():
        k = k.lower()
        if k.isalpha() == True:
            index = ord(k) - 97                                                         #index in der Liste
            liste[index] = v/anzahl_values
    print(liste)

print("c:")
frequencies(string_histogram("Das ist ein Text"))
print()
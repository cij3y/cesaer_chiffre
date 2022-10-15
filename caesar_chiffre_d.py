exampletext = "I konw that virtue to be in you, Brutus, As well as I do know your outward favour. Well, honour is the subject of my story, I cannot what you and other men Think of this life; but for my single self, I had as lief not be as live to be In awe of such a thing as I myself. I was born free as Caesar; so were you: We both have fed as well, and we can both Endure the winter,s cold as well as he: For once, upon a raw and gusty day, The troubled Tiber chafing with her shores, Caesar said to me'Darest thou, Cassius, now Leap in with me into thisangry flood, And swim to yonder point?' Upon the world, Accoutred as i was, I plunged in And bade him follow; so indeed he did. The torrentt roar'd, and we did buffet it With lusty sinews, thowing it aside And stemming it with hearts of controversy; But ere we could arrive the point proposed, Caesar dried 'Hlp me, Cassius, or I sink!' I, as Aeneas, our great waves of Tiber Did I the flames of Troy upo his shoulder The old Anchises bear, so from the wretched creature and must bend his body, If Caesar carelessly but nod on him, He had a feverwhen he was in Spain, And when the fit was on him, I did mark How he did Shake: 'tis true, this god did shake; His cowardlips did from their colour fly, And that same eye whose bend doth awe the world Did lose his lustre: I did hear him groan: Ay, and that tongue of his that bade the Romans Mark him and write his speeches in  their books, Alas, it cried 'Give me some drink, Titinius, 'As a sick girl. Ye gods, it doth amaze me A man of such a feeble temper should So get the start of the majestic world And bear the palm alone."

text = "Reu if zk zj. Wfi kyzj kzdv Z nzcc cvrmv pfl: Kf-dfiifn, zw pfl gcvrjv kf jgvrb dv, Z nzcc tfdv yfdv kf pfl; fi, zw pfl nzcc, Tfdv yfdv kf dv, reu Z nzcc nrzk wfi pfl."

#exampletext = "Das ist ein Text"

#text = "Gdv lvw hlq Whaw"

def encode_text(text, key):
    s = int(key)
    for ch in text:
        ch3 = ord(ch)
        if ch3 <= 90 and ch3 >= 65:
            ch3 = int(ord(ch)) + s
            if ch3 > 90:
                ch3 =ch3 - 26
            elif ch3 < 65:
                ch3 = ch3 + 26
            else:
                ch3 = ch3
        elif ch3 <= 122 and ch3 >= 97:
            ch3 = int(ord(ch)) + s
            if ch3 > 122:
                ch3 = ch3 - 26
            if ch3 < 97:
                ch3 = ch3 + 26
            else:
                ch3 = ch3
        encode_text =chr(ch3)
        print(encode_text, end="")


def crack_caesar(exampletext, text):

    global chi_dict

#erstelung der exampletext_list

    dict_exampletext = {}
    exampletext_lower = exampletext.lower()
    for ch in exampletext_lower:
        ch2 = ch.isalpha()
        if ch2 == True:
            el_count=(exampletext_lower.count(ch))
            dict_exampletext[ch] = el_count
    anzahl_values = 0
    for v in dict_exampletext.values(): 
        anzahl_values = anzahl_values + v
    exampletext_list = [0 for _ in range (97,123)]
    for k, v in dict_exampletext.items():
        k = k.lower()
        if k.isalpha() == True:
            index = ord(k) - 97                                                         #index in der exampletext_list
            exampletext_list[index] = v/anzahl_values
    
#ende der erstelung der exampletext_list


#erstelung der text list

    crack_list = []

    len_text = []
    for ch in text:
        len_text.append(ch)
    s = 1
    while s < 27:
        global chi_list
        text2 = ""
        for ch in text:
            ch3 = ord(ch)
            if ch3 <= 90 and ch3 >= 65:
                ch3 = int(ord(ch)) + s
                if ch3 > 90:
                    ch3 =ch3 - 26
                elif ch3 < 65:
                    ch3 = ch3 + 26
                else:
                    ch3 = ch3
            elif ch3 <= 122 and ch3 >= 97:
                ch3 = int(ord(ch)) + s
                if ch3 > 122:
                    ch3 = ch3 - 26
                if ch3 < 97:
                    ch3 = ch3 + 26
                else:
                    ch3 = ch3
            text2 += chr(ch3)

            dict_text = {}
            text_lower = text2.lower()
            for ch in text_lower:
                ch2 = ch.isalpha()
                if ch2 == True:
                    tl_count =(text_lower.count(ch))
                    dict_text[ch] = tl_count
            anzahl_values = 0
            for v in dict_text.values(): 
                anzahl_values = anzahl_values + v
            text_list = [0 for _ in range (97,123)]
            for k, v in dict_text.items():
                k = k.lower()
                if k.isalpha() == True:
                    index = ord(k) - 97                                                         #index in der text_list
                    text_list[index] = v/anzahl_values

#ende der erstelung der exampletext_list

        for chi_ in range(26):
            if exampletext_list[chi_] == 0:
                chi = 0
            else:
                chi = ((text_list[chi_] - exampletext_list[chi_]) * (text_list[chi_] - exampletext_list[chi_])) / exampletext_list[chi_]
            chi_list.append(chi)
        crack = sum(chi_list[-26:-1])
        crack_list.append(crack)
        s = s + 1
    encode_key = min(crack_list)
    index = crack_list.index(encode_key)
    
    print("Der Entschlüsselte Text befindet sich unten:")
    for indexx in range(26):
        if crack_list[indexx] == encode_key: 
            encode_text(text, indexx + 1)
            print()
            print("key = " + str(indexx))


chi_dict = {}
chi_list = []
crack_caesar(exampletext, text)


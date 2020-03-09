def mixString(s1, s2):
    s2 = s2[::-1]
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    length  = lengthS1 if lengthS1 > lengthS2 else  lengthS2
    resultString=""
    for i in range(length):
            if(i < lengthS1):
                resultString= resultString+ s1[i]
                if(i < lengthS2):
                    resultString= resultString+ s2[i]
                    print(resultString)
s1 = "hloiy"
s2 = "avdle"
mixString(s1, s2)
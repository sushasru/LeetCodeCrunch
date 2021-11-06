#word count engine PRAMP
def word_count_engine(document):
    doc = {}
    words = document.split()
    print("\ndocument:{}\nwords:{}\n\n".format(words,document))

    
    for i in range(len(words)):
        w = words[i]
        wrd = "".join([c.lower() for c in w if c.isalpha()])
        print("\twrd:",wrd)
        if wrd in doc:
            doc[wrd] += 1
        else:
            doc[wrd] = 1


    #Bucket sort:
    maxidx = max(doc.values())
    print("maxidx:",maxidx)
    result = [[] for _ in range(maxidx + 1)]
    print("result:",result)
    
    for w in doc:
        word = w
        count = str(doc[w])
        print("word:",word)
        print(doc[w])
        result[doc[w]].append([word,count])
        print("\tresult:",result)
        
    print("\nResult:{}\n".format(result))

    res = [] 
    for w in range(maxidx,-1,-1):
        if result[w]:
            res += result[w]
        
    
    print("\nsorted result:",res)

    

    
    














document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
word_count_engine(document)

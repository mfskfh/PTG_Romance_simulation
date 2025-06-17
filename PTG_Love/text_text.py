def printText(word):
    for textNo in range(len(word)+1):
        if word[textNo-1:textNo] == "$":
            delayTime = word[textNo:textNo+5]
            print(f"| delay {delayTime} |")
            word = word.replace("$" + delayTime, "1", 1)
            continue
    
        print(word[0:textNo])

        if word[0:textNo] == word:
            return
        
printText("sigi$00300but")
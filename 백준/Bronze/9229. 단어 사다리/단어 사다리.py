def Corrector(a,b):
    # 1. 길이 체크
    answer = "Correct"
    if len(a) != len(b):
        answer = "Incorrect"
    # 2. 철자 체크
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    if count != len(a) - 1:
        answer = "Incorrect"
    # 3. return
    return answer

while 1:
    firstS = input()
    if firstS == "#":
        break
    else:
        L = [firstS]
        while 1:
            s = input()
            if s == "#":
                break
            else:
                L.append(s)
        
        answerL = []
        for i in range(1,len(L)):
            c = Corrector(L[i-1],L[i])
            answerL.append(c)
        if answerL.count("Incorrect") == 0:
            print("Correct")
        else:
            print("Incorrect")
            

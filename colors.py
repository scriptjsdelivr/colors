def player(array, answer):
    v=0
    v2=0
    for i in range(len(array)-1):
        if array[i] == answer[i]:
            v += 1
            array.remove(array[i])
            answer.remove(answer[i])
    for a in range(3):
        for b in answer:
            for c in array:
                if b==c:
                    v2+=1
                    array.remove(c)
                    answer.remove(b)
                    break
    return [v, v2]
def frontend():
    colors = [1, 2, 3, 4, 5, 6]
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    a4 = int(input())
    arr = [a1, a2, a3, a4]
    lis = []
    arrc = []
    for color in colors:
        c=0
        if sum(arrc) < 4:
            for i in range(4):
                print(color, end = " ")
            
            for i in arr:
                if i == color:
                    c+=1
            print(c)
            
        arrc.append(c)
        print("")
    answers = [
        [1, arrc[0]],
        [2, arrc[1]],
        [3, arrc[2]],
        [4, arrc[3]],
        [5, arrc[4]],
        [6, arrc[5]],
    ]
    m=[]
    for i in answers:
        for j in range(i[1]):
            m.append(i[0])
    answers = m
    import itertools
    perm_set = itertools.permutations(answers) 
    bu = []
    for i in perm_set:
        ar = [i[0],i[1],i[2],i[3]]
        if ar in bu:
            t=1
        else:
            print(f'{ar[0]} {ar[1]} {ar[2]} {ar[3]}')
            bu.append(ar)
            if ar == arr:
                print("SUCCESS")
                break
            print("")
frontend()

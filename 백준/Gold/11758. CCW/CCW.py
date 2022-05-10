def CCW(p1,p2,p3):
    A=p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]
    B=p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0]

    if A-B==0:
        return 0
    elif A-B>0:
        return 1
    else:
        return -1

pos1=list(map(int,(input().split())))
pos2=list(map(int,(input().split())))
pos3=list(map(int,(input().split())))

print(CCW(pos1,pos2,pos3))
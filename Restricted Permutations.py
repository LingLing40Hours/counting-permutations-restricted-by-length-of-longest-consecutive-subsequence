import copy;
import math;
from PIL import Image, ImageDraw;

def verify(nk,j):
    if P(nk,nk,j,False,False)==PBash(nk,nk,j,False,False) and P(nk,nk-1,j,False,False)==PBash(nk,nk-1,j,False,False):
        print("P1 \t correct");
    else:
        print("P1 \t error");
    if P(nk,nk,j,True,False)==PBash(nk,nk,j,True,False) and P(nk,nk-1,j,True,False)==PBash(nk,nk-1,j,True,False):
        print("P2 \t correct");
    else:
        print("P2 \t error");
    if P(nk,nk,j,True,True)==PBash(nk,nk,j,True,True) and P(nk,nk-1,j,True,True)==PBash(nk,nk-1,j,True,True):
        print("P3 \t correct");
    else:
        print("P3 \t error");
    if P(nk,nk,j,False,True)==PBash(nk,nk,j,False,True) and P(nk,nk-1,j,False,True)==PBash(nk,nk-1,j,False,True):
        print("P4 \t correct");
    else:
        print("P4 \t error");
    if Z0(nk,nk,j)==Z0Bash(nk,nk,j) and Z0(nk,nk-1,j)==Z0Bash(nk,nk-1,j):
        print("Z0 \t correct");
    else:
        print("Z0 \t error");
    if Zcol(nk,nk,j,1)==ZXyBash(nk,nk,j,j-2,1) and Zcol(nk,nk-1,j,1)==ZXyBash(nk,nk-1,j,j-2,1):
        print("Z1[] \t correct");
    else:
        print("Z1[] \t error");
    if Zsqu(nk,nk,j)==ZBash(nk,nk,j) and Zsqu(nk,nk-1,j)==ZBash(nk,nk-1,j):
        print("Zsqu \t correct");
    else:
        print("Zsqu \t error");
    if S0(nk,nk,j)==SBash(nk,nk,j) and S0(nk,nk-1,j)==SBash(nk,nk-1,j):
        print("S0 \t correct");
    else:
        print("S0 \t error");
    if Scol(nk,nk,j)==SXBash(nk,nk,j,j-2) and Scol(nk,nk-1,j)==SXBash(nk,nk-1,j,j-2):
        print("Scol \t correct");
    else:
        print("Scol \t error");
    if O0(nk,nk,j)==OBash(nk,nk,j) and O0(nk,nk-1,j)==OBash(nk,nk-1,j):
        print("O0 \t correct");
    else:
        print("O0 \t error");
    if U0(nk,nk,j)==UBash(nk,nk,j) and U0(nk,nk-1,j)==UBash(nk,nk-1,j):
        print("U0 \t correct");
    else:
        print("U0 \t error");

def printAll(j, size):
    headers = ["P1(n, k)","P2(n, k)","P3(n, k)","P4(n, k)","Z0(n, k)","Z1[](n, k)","Zsqu(n, k)","S0(n, k)","Scol(n, k)","O0(n, k)","U0(n, k)"];
    superTriangle = [];
    for n in range(size):
        superRow = [];
        for k in range(n+1):
            superValue = [];
            superValue.append(P(n,k,j,False,False));
            superValue.append(P(n,k,j,True,False));
            superValue.append(P(n,k,j,True,True));
            superValue.append(P(n,k,j,False,True));
            superValue.append(Z0(n,k,j));
            superValue.append(Zcol(n,k,j,1));
            superValue.append(Zsqu(n,k,j));
            superValue.append(S0(n,k,j));
            superValue.append(Scol(n,k,j));
            superValue.append(O0(n,k,j));
            superValue.append(U0(n,k,j));
            superRow.append(superValue);
        superTriangle.append(superRow);
    for triangle in range(11):
        print(headers[triangle]);
        for n in range(size):
            row = "";
            for k in range(n+1):
                row += str(superTriangle[n][k][triangle]) + '\t';
            print(row);
    return;

def P(n, k, j, wrap, cyclic):
    if k>n or n<0 or k<0:
        return 0;
    if k==0:
        return 1;
    if (wrap==False and cyclic==False): #Pj1
        return P(n,k,j,True,False)+B(n,k,j);
    elif (wrap==True and cyclic==False): #Pj2
        #actually 0 if n==2 and k==2 and j==2
        return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
    elif (wrap==True and cyclic==True): #Pj3
        #actually n*(n-3) if k==2 and j==2 and n>2
        #if n==3 and k==3 and j==3:
        #    return 0;
        #attempt 1,2
        if n==2 and k==2 and j==2:
            return 0;
        if n==j and k==j:
            return n*(P(n-1,k-1,j,False,False) - 2*Zxy(n,k,j,0,j-2) - sum(sum(Zxy(n-1,k-1,j,x,y) for y in range(j-3-x,j-1)) for x in range(0,j-1))) - 2*j;
        #attempt 3
        #if k==2:
        #    if n==2:
        #        return 0;
        #    return n*(n-3);
        return n*(P(n-1,k-1,j,False,False) - 2*Zxy(n,k,j,0,j-2) - sum(sum(Zxy(n-1,k-1,j,x,y) for y in range(j-3-x,j-1)) for x in range(0,j-1)));
    elif (wrap==False and cyclic==True): #Pj4
        #actually (n-1)*(n-2) if k==2
        #if k==2:
        #    return (n-1)*(n-2);
        return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));

def Z0(n, k, j):
    if k>n or n<0 or k<0:
        return 0;
    #attempt 1
    if n==1 and k==1:
        return 0;
    #attempt 2
    #if n==2 and k==2:
    #    return 0;
    return Zcol(n,k,j,0) - sum(Zxy(n,k,j,0,i) for i in range(1,j-1));

def Zxy(n, k, j, x, y):
    if x<0 or y<0:
        return 0;
    return Z0(n-x-y,k-x-y,j);

#unused; see UC
def ZCxy(n, k, j, x, y, xPrev, yPrev):
    if x<0 or y<0:
        return 0;
    if n == k and xPrev+yPrev>=j and n-x-y==1:
        nPrev = n+xPrev+yPrev+1;
        if xPrev==j-1 and yPrev==j-1 and nPrev==2*j:
            return 1;
        if nPrev==xPrev+yPrev+2:
            return 2;
    return Zxy(n, k, j, x, y);

#x->[j-2]-
def Zcol(n, k, j, x):
    if k>n or n<0 or k<0:
        return 0;
    if x==1:
        #attempt 1
        if n==2 and k==2:
            return 2;
        return Zsqu(n-1,k-1,j) - sum(Zcol(n-1,k-1,j,i) for i in range(1,j-1));
    return Zcol(n-x+1,k-x+1,j,1);

def Zsqu(n, k, j):
    if k>n or n<0 or k<0:
        return 0;
    if n==2 and k==2 and j==2:
        return 0;
    return Scol(n-1,k-1,j)-Zcol(n-1,k-1,j,j-2);

def S0(n, k, j):
    if k>n or n<0 or k<0:
        return 0;
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);

def Sx(n, k, j, x):
    return S0(n-x,k-x,j);

def Scol(n, k, j):
    if k>n or n<0 or k<0:
        return 0;
    return 2*P(n-1,k-1,j,False,False) - Sx(n-1,k-1,j,j-2);

def O0(n, k, j):
    if k>n or n<2 or k<2:
        return 0;
    return int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,False)) - 2*sum(sum(Oxy(n,k,j,x,y) for y in range(1-x,j-1-x)) for x in range(0,j-1)) + sum(sum(Oxy(n,k,j,x,y) for y in range(1-x,j)) for x in range(0,j));

def Oxy(n, k, j, x, y):
    if x<0 or y<0:
        return 0;
    return O0(n-x-y,k-x-y,j);

def B(n, k, j):
    return sum(sum(Oxy(n,k,j,x,y) for y in range(j-2-x,j-1)) for x in range(0,j-1));

def U0(n, k, j):
    if k>n or n<2 or k<2:
        return 0;
    if n==2 and k==2 and j==2:
        return 0;
    t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
    t2 = sum(sum((UC(n-x-y,k-x-y,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
    return int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);

#exception for reducing into degenerate polygons
def UC(n, k, j, xPrev, yPrev):
    if n==k and xPrev+yPrev>=j and n==2:
        return 0;
    return U0(n, k, j);

def Uxy(n, k, j, x, y):
    if x<0 or y<0:
        return 0;
    return U0(n-x-y,k-x-y,j) - sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-1,j-1)) - sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-y-1,j-1));

def L(n, k, j):
    return sum(sum(Uxy(n,k,j,x,y) for y in range(j-2-x,j-1)) for x in range(0,j-1));


def PBash(n, k, j, wrap, cyclic):
    answer = 0;
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, wrap, cyclic) < j:
            answer += 1;
    return answer;

def PList(n, k, j, wrap, cyclic):
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, wrap, cyclic) < j:
            print(p);

def consecutivity(n, permutation, wrap, cyclic):
    k = len(permutation);
    if k==0:
        return 0;
    if wrap==False and cyclic==False:
        answer = 1;
        temp = 1;
        for i in range(1,k):
            if abs(permutation[i]-permutation[i-1])!=1: #end streak
                if temp > answer:
                    answer = temp;
                temp = 1;
            elif i==k-1: #force end streak
                temp += 1;
                if temp > answer:
                    answer = temp;
            else:
                temp += 1;
        return answer;
    if wrap==True and cyclic==False:
        answer = 1;
        temp = 1;
        for i in range(1,k):
            diff = abs(permutation[i]-permutation[i-1]);
            if diff!=1 and diff!=n-1: #end streak
                if temp > answer:
                    answer = temp;
                temp = 1;
            elif i==k-1: #force end streak
                temp += 1;
                if temp > answer:
                    answer = temp;
            else:
                temp += 1;
        return answer;
    if wrap==True and cyclic==True:
        answer = 1;
        temp = 1;
        start = 0;
        end = 1;
        for i in range(1,k):
            diff = abs(permutation[i]-permutation[i-1]);
            if diff!=1 and diff!=n-1: #end streak
                if i==temp: #is starting streak
                    start = temp;
                if temp > answer:
                    answer = temp;
                temp = 1;
            elif i==k-1: #force end streak
                temp += 1;
                end = temp;
                if temp > answer:
                    answer = temp;
            else:
                temp += 1;
        diffSE = abs(permutation[0]-permutation[-1]);
        if (diffSE==1 or diffSE==n-1) and start+end > answer:
            answer = start+end;
        return answer;
    if wrap==False and cyclic==True:
        answer = 1;
        temp = 1;
        start = 0;
        end = 1;
        for i in range(1,k):
            diff = abs(permutation[i]-permutation[i-1]);
            if diff!=1: #end streak
                if i==temp: #is starting streak
                    start = temp;
                if temp > answer:
                    answer = temp;
                temp = 1;
            elif i==k-1: #force end streak
                temp += 1;
                end = temp;
                if temp > answer:
                    answer = temp;
            else:
                temp += 1;
        diffSE = abs(permutation[0]-permutation[-1]);
        if diffSE==1 and start+end > answer:
            answer = start+end;
        return answer; 

def useBase(n, permutation):
    for i in range(1, len(permutation)):
        if abs(permutation[i]-permutation[i-1]) == n-1:
            return True;
    return False;

def backToBase(n, permutation):
    if len(permutation)==0:
        return False;
    if abs(permutation[0]-permutation[-1]) == n-1:
        return True;
    return False;

def backToAnywhere(n, permutation):
    if len(permutation)==0:
        return False;
    if permutation[0] in (1,n):
        if len(permutation)==1:
            return True;
        if abs(permutation[1]-permutation[0])==1:
            return False;
        return True;
    return False;

def zeroToZero(n, permutation):
    if len(permutation)<=1:
        return False;
    if abs(permutation[0]-permutation[-1]) == n-1 and abs(permutation[0]-permutation[1])!=1 and abs(permutation[-1]-permutation[-2])!=1:
        return True;
    return False;

def useBaseIndependently(n, permutation):
    k = len(permutation);
    for i in range(1, k):
        if abs(permutation[i]-permutation[i-1]) == n-1:
            if i+1 < k and abs(permutation[i+1]-permutation[i])==1:
                return False;
            if i-2 >= 0 and abs(permutation[i-1]-permutation[i-2])==1:
                return False;
            return True;
    return False;

#check if neither (1, n-1) and (n, 2) are used
def useBaseInxependently(n, permutation):
    k = len(permutation);
    for i in range(1, k):
        if abs(permutation[i]-permutation[i-1]) == n-1: #use base
            if i+1 < k and abs(permutation[i]-permutation[i+1])==n-2: #not inxependently
                return False;
            if i-2 >= 0 and abs(permutation[i-1]-permutation[i-2])==n-2: #not inxependently
                return False;
            return True;
    return False;

#check if permutation uses [n-1, 1, n] or [2, n, 1] (in that order) independently
def useBaseInvependently(n, permutation):
    k = len(permutation);
    for i in range(2, k):
        if abs(permutation[i]-permutation[i-1])==n-1 and abs(permutation[i-1]-permutation[i-2])==n-2: #use V
            if i+1 < k and abs(permutation[i+1]-permutation[i])==n-2: #not invependently
                return False;
            if i-3 >= 0 and abs(permutation[i-2]-permutation[i-3])==1: #not invependently
                return False;
            return True;
    return False;

#1_0, 0_1
def useBaseWithBuddy(n, permutation):
    k = len(permutation);
    for i in range(1, k):
        if abs(permutation[i]-permutation[i-1]) == n-1: #use base
            sideCount = 0;
            if i+1 < k and abs(permutation[i+1]-permutation[i])==1:
                if i+2 >= k:
                    sideCount += 1;
                elif i+2 < k and abs(permutation[i+2]-permutation[i+1])!=1:
                    sideCount += 1;
                else: #two sides in a row
                    return False;
            if i-2 >= 0 and abs(permutation[i-1]-permutation[i-2])==1:
                if i-3 < 0:
                    sideCount += 1;
                elif i-3 >= 0 and abs(permutation[i-2]-permutation[i-3])!=1:
                    sideCount += 1;
                else: #two sides in a row
                    return False;
            if sideCount==1:
                return True;
            return False;
    return False;

#1_1
def useBaseWithBuddies(n, permutation):
    k = len(permutation);
    for i in range(1, k):
        if abs(permutation[i]-permutation[i-1])==n-1: #use base
            sideCount = 0;
            if i+1 < k and abs(permutation[i+1]-permutation[i])==1:
                if i+2 >= k:
                    sideCount += 1;
                elif i+2 < k and abs(permutation[i+2]-permutation[i+1])!=1:
                    sideCount += 1;
                else:
                    return False;
            if i-2 >= 0 and abs(permutation[i-1]-permutation[i-2])==1:
                if i-3 < 0:
                    sideCount += 1;
                elif i-3 >= 0 and abs(permutation[i-2]-permutation[i-3])!=1:
                    sideCount += 1;
                else:
                    return False;
            if sideCount==2:
                return True;
            return False
    return False;


#Combinatorics functions with DP optimization

def listKPermutationsDP(k, list, mem):
    if k==0:
        return [[]];
    if len(list)==0:
        return [];
    #search mem
    for i in mem[k]:
        if i[0]==list:
            return copy.deepcopy(i[1]);
    
    shortList = list.copy();
    del shortList[0];
    #exclude first
    ansList = listKPermutationsDP(k, shortList, mem);
    #include first
    prevPerms = listKPermutationsDP(k-1, shortList, mem);
    for permutation in prevPerms:
        for position in range(k):
            temp = permutation.copy();
            temp.insert(position, list[0]);
            ansList.append(temp);
    mem[k].append((list, copy.deepcopy(ansList)));
    return ansList;

#call with nested comprehension list
#listCombinationsDP(k ,list, [[] for _ in range(k+1)];
#copy.deepcopy() necessary for nested lists
def listCombinationsDP(k, list, mem):
    if k==0:
        return [[]];
    if len(list)==0:
        return [];
    #search mem
    for i in mem[k]:
        if i[0]==list:
            return copy.deepcopy(i[1]);
    
    shortList = list.copy();
    del shortList[0];
    list2 = listCombinationsDP(k, shortList, mem);
    list1 = listCombinationsDP(k-1, shortList, mem);
    for i in list1:
        i.insert(0, list[0]);
    ansList = join(list1, list2);
    mem[k].append((list, copy.deepcopy(ansList)));
    return ansList;


#Combinatorics functions without DP optimization

def join(list1, list2):
    ansList = [];
    for i in list1:
        ansList.append(i);
    for i in list2:
        ansList.append(i);
    return ansList;

def listPermutations(list):
    if len(list)==0:
        return [[]];

    ansList = [];
    shortList = list.copy();
    del shortList[0];
    prevPerms = listPermutations(shortList);
    for permutation in prevPerms:
        for position in range(len(list)):
            temp = permutation.copy();
            temp.insert(position, list[0]);
            ansList.append(temp);
    return ansList;

def listKPermutations(k, list):
    if k==0:
        return [[]];
    if len(list)==0:
        return [];
    
    shortList = list.copy();
    del shortList[0];
    #exclude first
    ansList = listKPermutations(k, shortList);
    #include first
    prevPerms = listKPermutations(k-1, shortList);
    for permutation in prevPerms:
        for position in range(k):
            temp = permutation.copy();
            temp.insert(position, list[0]);
            ansList.append(temp);
    return ansList;

def listCombinations(k, list):
    if k==0:
        return [[]];
    if len(list)==0:
        return [];
    shortList = list.copy();
    del shortList[0];
    list2 = listCombinations(k, shortList);
    list1 = listCombinations(k-1, shortList);
    for i in list1:
        i.insert(0, list[0]);
    return join(list1, list2);

def listSubsets(list):
    if len(list)==0:
        return [[]];

    ansList = [];
    shortList = list.copy();
    del shortList[0];
    prevSubsets = listSubsets(shortList);
    #exclude first
    for i in prevSubsets:
        ansList.append(i);  
    #include first
    for i in prevSubsets:
        c = i.copy();
        c.insert(0, list[0]);
        ansList.append(c);
    return ansList;


def ZBash(n, k, j):
    answer = 0;
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, False)<j and backToBase(n,p):
            answer += 1;
    return answer;

def OBash(n, k, j):
    answer = 0;
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, False)<j and useBaseIndependently(n,p):
            answer += 1;
    return answer;

def SBash(n, k, j):
    answer = 0;
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, False)<j and backToAnywhere(n,p):
            answer += 1;
    return answer;

def UBash(n, k, j):
    answer = 0;
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseIndependently(n,p):
            answer += 1;
    return answer;

#none of (1, 2), (n, n-1), (1, n-1), (n, 2) are used, [1, n] as longest sub-block
def UXBash(n, k, j):
    answer = 0;
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseIndependently(n,p) and useBaseInxependently(n,p):
            answer += 1;
    return answer;

#[n-1, 1, n] or [2, n, 1] as longest sub-block
def UVBash(n, k, j):
    answer = 0;
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseInvependently(n,p): #independence is guaranteed
            answer += 1;
    return answer;

def UList(n, k, j):
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseIndependently(n,p):
            print(p);

def MBash(n, k, j):
    answer = 0;
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseWithBuddy(n,p):
            answer += 1;
    return answer;

def MList(n, k, j):
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseWithBuddy(n,p):
            print(p);

def NBash(n, k, j):
    answer = 0;
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseWithBuddies(n,p):
            answer += 1;
    return answer;

def ZxyBash(n, k, j, x, y):
    return Z0Bash(n-x-y, k-x-y, j);

def Z0Bash(n, k, j):
    answer = 0;
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, False)<j and zeroToZero(n,p):
            answer += 1;
    return answer;

def ZXYBash(n, k, j, x, y):
    ans = 0;
    for i in range(x+1):
        for h in range(y+1):
            ans += Z0Bash(n-i-h, k-i-h, j);
    return ans;

def ZXyBash(n, k, j, x, y):
    ans = 0;
    for i in range(x+1):
        ans += Z0Bash(n-i-y, k-i-y, j);
    return ans;

def SXBash(n, k, j, x):
    ans = 0;
    for i in range(x+1):
        ans += SBash(n-i, k-i, j);
    return ans;


#drawing polygons
#https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/
def drawPath(image, pathPerm, vertexCoords, thickness, plumpness):
    draw = ImageDraw.Draw(image);
    for i in range(1, len(pathPerm)):
        draw.line(vertexCoords[pathPerm[i-1]-1] + vertexCoords[pathPerm[i]-1], width=thickness, fill='black');
    startCoord = vertexCoords[pathPerm[0]-1];
    endCoord = vertexCoords[pathPerm[-1]-1];
    startBox = (startCoord[0]-plumpness/2, startCoord[1]-plumpness/2, startCoord[0]+plumpness/2, startCoord[1]+plumpness/2);
    endBox = (endCoord[0]-plumpness/2, endCoord[1]-plumpness/2, endCoord[0]+plumpness/2, endCoord[1]+plumpness/2);
    draw.ellipse(startBox, fill='black');
    draw.ellipse(endBox, outline='black', width=1, fill=(0,0,0,0));
        
def polygonCoords(n, xCenter, yCenter, radius):
    dtheta = 2*math.pi/n;
    theta = -math.pi/2 - dtheta/2;
    answer = [];
    for i in range(n):
        theta += dtheta;
        x = xCenter + radius*math.cos(theta);
        y = yCenter - radius*math.sin(theta);
        answer.append((x, y));
    return answer;

def drawPolygon(image, vertexCoords, thickness):
    draw = ImageDraw.Draw(image);
    for i in range(len(vertexCoords)-1):
        draw.line(vertexCoords[i] + vertexCoords[i+1], width=thickness, fill='black');
    draw.line(vertexCoords[-1] + vertexCoords[0], width=thickness, fill='black');

def largestFitSize(image, pathCount):
    size = image.size;
    dxy = min(size[0], size[1]);
    xFit = 1;
    yFit = 1;
    while pathCount > xFit*yFit:
        dXy = size[0]/(xFit+1);
        dxY = size[1]/(yFit+1);
        if dXy > dxY:
            dxy = dXy;
            xFit += 1;
        else:
            dxy = dxY;
            yFit += 1;
    return dxy, xFit, yFit;

#pathPerms contains all pre-calculated paths
def drawPaths(image, n, pathPerms, PPF):
    pathCount = len(pathPerms);
    dxy, xFit, yFit = largestFitSize(image, pathCount);
    for i in range(pathCount):
        x = i%xFit;
        y = int(i/xFit);
        xCenter = (x+0.5)*dxy;
        yCenter = (y+0.5)*dxy;
        vertexCoords = polygonCoords(n, xCenter, yCenter, dxy*PPF/2);
        drawPolygon(image, vertexCoords, 1);
        drawPath(image, pathPerms[i], vertexCoords, 4, 10);

def MDraw(n, k, j):
    #find paths
    pathPerms = [];
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseWithBuddy(n,p):
            pathPerms.append(p);

    #draw paths
    im = Image.new(mode = 'RGBA', size = (1920,1080));
    drawPaths(im, n, pathPerms, 0.85);
    im.save("/Users/admin/Desktop/MDraw("+str(n)+', '+str(k)+', '+str(j)+').png', 'PNG');
    im.show();

def PDraw(n, k, j, wrap, cyclic):
    #find paths
    pathPerms = [];
    listN = list(range(1,n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, wrap, cyclic) < j:
            pathPerms.append(p);

    #draw paths
    im = Image.new(mode = 'RGBA', size = (1920,1080));
    drawPaths(im, n, pathPerms, 0.85);
    im.save("/Users/admin/Desktop/PDraw("+str(n)+', '+str(k)+', '+str(j)+', '+str(wrap)+', '+str(cyclic)+').png', 'PNG');
    im.show();

def UDraw(n, k, j):
    pathPerms = [];
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseIndependently(n,p):
            pathPerms.append(p);

    im = Image.new(mode = 'RGBA', size = (1920,1080));
    drawPaths(im, n, pathPerms, 0.85);
    im.save("/Users/admin/Desktop/UDraw("+str(n)+', '+str(k)+', '+str(j)+').png', 'PNG');
    im.show();

def UXDraw(n, k, j):
    pathPerms = [];
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseIndependently(n,p) and useBaseInxependently(n,p):
            pathPerms.append(p);

    im = Image.new(mode = 'RGBA', size = (1920,1080));
    drawPaths(im, n, pathPerms, 0.85);
    im.save("/Users/admin/Desktop/UXDraw("+str(n)+', '+str(k)+', '+str(j)+').png', 'PNG');
    im.show();

def UVDraw(n, k, j):
    pathPerms = [];
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, True)<j and useBaseInvependently(n,p): #independence is guaranteed
            pathPerms.append(p);

    im = Image.new(mode = 'RGBA', size = (1920,1080));
    drawPaths(im, n, pathPerms, 0.85);
    im.save("/Users/admin/Desktop/UVDraw("+str(n)+', '+str(k)+', '+str(j)+').png', 'PNG');
    im.show();

def Z0Draw(n, k, j):
    pathPerms = [];
    listN = list(range(1, n+1));
    listKPerms = listKPermutations(k, listN);
    for p in listKPerms:
        if consecutivity(n, p, False, False)<j and zeroToZero(n,p):
            pathPerms.append(p);

    im = Image.new(mode = 'RGBA', size = (1920,1080));
    drawPaths(im, n, pathPerms, 0.85);
    im.save("/Users/admin/Desktop/Z0Draw("+str(n)+', '+str(k)+', '+str(j)+').png', 'PNG');
    im.show();

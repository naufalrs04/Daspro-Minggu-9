# NAMA = NAUFAL RIZKI SAPUTRA
# NIM = 24060122120011

# IsEmpty
def is_empty_LoL(S):
    return S==[]

def is_empty_LoL(S):
    return S==[]

L1=[]
L2=[[]]
L3=[['s',2,3],2,[5,'b']]

print ("IsEmpty ?")
print(is_empty_LoL(L1))
print(is_empty_LoL(L2))
print(is_empty_LoL(L3))
print()

# IsAtom
def jml_elemen_list(S) :
    return len(S)

def is_atom(S):
    return not(is_empty_LoL(S)) and jml_elemen_list(S)==1

def is_atom(S):
    return not(is_empty_LoL(S)) and jml_elemen_list(S)==1

L1=['a']
L2=['b',5]
L3=[['s',2,3],2,[5,'b']]

print ("IsAtom ?")
print(is_atom(L1))
print(is_atom(L2))
print(is_atom(L3))
print()

# IsOneElmt
def IsOneElmt(S) :
    return len(S) == 1

# IsList
def is_List(S):
    return not(is_atom(S))

L1=['a']
L2=['b',5]
L3=[['s',2,3],2,[5,'b']]

print ("Islist ?")
print(is_List(L1)) 
print(is_List(L2))
print(is_List(L3))
print()

# KONSLO
def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L]+S
L1=['a']
L2=['b',5]
print ("KonsLo")
print (konso_LoL(L1,L2))
print()

# KONSL.
def konsi_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return S+[L]
L1=['a']
L2=['b',5]
print ("KonsL.")
print (konsi_LoL(L1,L2))
print()

# FIRST LIST
def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

L3=[['s',2,3],2,[5,'b']]
L4=[[2,"b"],["a","z"],4,9]

print ("FirstList")
print(first_List(L3)) 
print(first_List(L4))
print()

# TAIL LIST
def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]

X1=['a',['b','c','e']]
X2=[['a','b'],'e']

print ("Tail List")
print (tail_List(X1))
print (tail_List(X2))
print()

# LAST LIST
def last_list(S) :
    if not(is_empty_LoL(S)):
        return S[-1]

X1=['a',['b','c','e']]
X2=[['a','b'],'e']

print ("Last List")
print (last_list(X1))
print (last_list(X2))
print()

# HEAD LIST
def head_List(S):
    if not(is_empty_LoL(S)):
        return S[:-1]

X1=['a',['b','c','e']]
X2=[['a','b'],'e',['d','c']]

print ("Head List")
print (head_List(X1))
print (head_List(X2))
print()

# CONTOH 1
def IsEqS(S1,S2) :
    if is_empty_LoL(S1) and is_empty_LoL(S2) :
        return True
    elif not is_empty_LoL(S1) and is_empty_LoL(S2) : 
        return False
    elif is_empty_LoL(S1) and not is_empty_LoL(S2) : 
        return False
    elif not is_empty_LoL(S1) and not is_empty_LoL(S2) :
        if is_atom(first_List(S1)) and is_atom(first_List(S2)) :
            return first_List(S1) == first_List(S2) and IsEqS(tail_List(S1),tail_List(S2))
        elif is_List(first_List(S1)) and is_List(first_List(S2)) :
            return IsEqS(first_List(S1),first_List(S2)) and IsEqS(tail_List(S1), tail_List(S2))
        else :
            return False

# IMPLEMENTASI CONTOH 1
S1 = ["a",["b","c"],"d",["e"]]
S2 = ["a",["b","c"],"d",["e"]]

print ("IsEqS ?")
print (IsEqS(S1,S2))
print ()

# CONTOH 2
def IsMemberS (A,S) :
    if is_empty_LoL (S) :
        return False 
    elif not is_empty_LoL(S) :
        if is_atom (first_List(S)) :
            return A == first_List(S)
        elif is_List(first_List(S)) :
            return IsMemberS (A,first_List(S)) or IsMemberS (A,tail_List(S))

# IMPLEMENTASI CONTOH 2
x1 = "c"
x2 = ["c",["a","d","e"],"b"]

print ("IsMemberS ?")
print (IsMemberS (x1,x2))
print ()

# CONTOH 3
def IsMemberLS (L,S) :
    if is_empty_LoL (L) and is_empty_LoL(S) :
        return True 
    elif not is_empty_LoL (L) and is_empty_LoL (S) :
        return False
    elif is_empty_LoL (L) and not is_empty_LoL (S) :
        return False
    elif not is_empty_LoL (L) and not is_empty_LoL (S) :
        if is_atom(first_List(S)) :
            return IsMemberLS(tail_List(L,S))
        else :
            if IsEqS (L,first_List(S)) :
                return True 
            else :
                return IsMemberLS (L,tail_List(S))

# IMPLEMENTASI CONTOH 3
L = ["c","d"]
S = [["a","b"],["c","d"],["e","f","g","h"]]

print ("IsMemberLS ?")
print (IsMemberLS(L,S))
print ()

# CONTOH 4
def Rember (a,S) :
    if is_empty_LoL(S) :
        return S
    else :
        if is_List(first_List(S)) :
            return konso_LoL(Rember(a,first_List(S)), Rember(a,tail_List(S)))
        else :
            if first_List(S) == a :
                return Rember (a,tail_List(S))
            else :
                return konso_LoL(first_List(S),Rember (a,tail_List(S)))

# IMPLEMENTASI CONTOH 4
a = "b"
s = ["a","b",["c","d"]]

print ("Rember ?")
print (Rember(a,s))
print ()

# CONTOH 5
def Max2 (a,b) :
    if a>= b :
        return a
    else :
        return b

def Max (S) :
    if IsOneElmt(S) :
        if is_atom(first_List(S)) :
            return first_List(S)
        else :
            return Max(first_List(S))
    else :
        if is_atom(first_List(S)) :
            return Max2(first_List(S),Max(tail_List(S)))
        else :
            return Max2(Max(first_List(S)),Max(tail_List(S)))

# IMPLEMENTASI CONTOH 5
a = [3]
b = [6]
print ("Max2 ?")
print (Max2(a,b))
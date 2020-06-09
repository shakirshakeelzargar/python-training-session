#Print lowest integer value
a,b,c,d=[20,23,17,8]
try:
    if a<b and a<c and a<d:
        print(f"lowest value : {a}")
    elif b<a and b<c and b<d:
        print(f"lowest value : {b}")
    elif c<a and c<b and c<d:
        print(f"lowest value : {c}")
    elif d<a and d<b and d<c:
        print(f"lowest value : {d}")
    else :
        if a==b and a==c and a==d:
            raise Exception(f"all values are equal {a}")
except Exception as e:
    print(f"error occured : {e}")
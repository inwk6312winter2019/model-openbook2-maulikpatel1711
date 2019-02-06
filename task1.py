#Read the StreetCenterlines.csv and return the following

f1 = open("Street_Centrelines.csv",'r')

def give_tuple():
    for v in f1:
       v = v.split(",")
       t = (v[2], v[4], v[6], v[7])
       print(t)

def maintenance():
    hist = dict()
    for f in f1:
        f = f.split(",")
        if f[12] not in hist:
            hist[f[12]] = 1
        else :
            hist[f[12]] += 1
    print(hist)

def unique_owner():
    own_list = f1[11]
    new_list = []
    for u in f1:
        u = u.split(",")
        if u[11] not in new_list:
            new_list.append(u[11])
    print(new_list)

give_tuple()
maintenance()
unique_owner()


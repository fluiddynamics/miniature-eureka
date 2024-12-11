def fold1(f, l):
    ff0 = f(l[0])
    z = [[ff0]]
    for ll in l:
        ff = f(ll)
        if ff == ff0:
            z[-1].append(ll)
        else:
            z.append([ff, ll])
        ff0 = ff
    return z

def foldn(rules, l):
    if rules == []:
        return l

    m = None
    if isinstance(rules[0],int):
        m = rules[0]
        rules[0] = lambda x: rules[1](x) // m

    z = []
    for zz in fold1(rules[0], l):
        zz0 = zz[0]
        zzi = foldn(rules[1:], zz[1:])
        z.append([zz0] + zzi)
    
    if m:
        start,end = int(z[0][1][0]),int(z[-1][-1][0])
        z[0] = [z[0][0]] + [None]*(start%m) + z[0][1:]
        z[-1] = z[-1] + [None]*(m-end%m-1)
        return z
    else:
        return z


def remove_head(i, l):
    if i == 0:
        return [ll[1:] if ll is not None else None for ll in l]
    else:
        z = []
        for zz in l:
            zz0 = zz[0]
            zzi = remove_head(i-1, zz[1:])
            z.append([zz0] + zzi)
        return z

def main():
    jd = [i for i in range(3, 22)]
    import pprint
    z = foldn([
        3,
        lambda x:x//6+100,
        lambda x:x//3+1000,
    ], jd)

    # どの深さにヘッダがあるかを意識する必要がある
    # 最初はすべての深さにヘッダがある
    # その時点でmapをかける
    # remove_headをするとその階層のヘッダが消えるが、remove_headの対象より前の階層はすべてヘッダ付きとする
    import pprint
    z0 = remove_head(0, z)
    pprint.pp(z)
    pprint.pp(z0)

main()

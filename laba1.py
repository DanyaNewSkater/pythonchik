sts = """Артур Васильков
Борис Годунов
Василий Иванов
Григорий Морев
Дарья Измайлова
Елена Прекрасная"""

s = list()
sts = sts.split("\n")
for i in sts:
    s.append(i.split())

def add_st(n:str, f:str):
    pair = list({n, f})
    s.append(pair)
    s.sort()
    return s

def get_st(f:str, n=None):
    lst = list()
    if n is None:
        for j in s:
            if j[1] == f:
                lst.append(j)
        if len(lst) == 0:
            return False
        else:
            return lst
    else:
        for ij in s:
            if ij[1] == f and ij[0] == n:
                return True
        return False

def ch_inf(on:str,of:str, nn = None, nf = None):
    if nn is None and nf is None:
        return "Nothing has happened"
    for ii in range(len(s)):
        if s[ii][0]==on and s[ii][1]==of:
            if nn is not None:
                s[ii][0] = nn
            if nf is not None:
                s[ii][1] = nf
    s.sort()
    return s

def rem_st(f:str, n = None):
    if n is None:
        ss = input(f"Выберите имя из списка {get_st(f)} ")
        for op in range(len(s)):
            if s[op][0]==ss and s[op][1]==f:
                t = s.pop(op)
                return t
        return "no such student"
    else:
        for op1 in range(len(s)):
            if s[op1][0] == n and s[op1][1] == f:
                t = s.pop(op1)
                return t
        return "no such student"

print(add_st("Иван","Золочёв"))
print(get_st("Годунов"))
print(ch_inf("Василий","Иванов","Пётр"))
print(rem_st("Годунов"))
print(s)

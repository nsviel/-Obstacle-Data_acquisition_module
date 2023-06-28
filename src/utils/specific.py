#---------------------------------------------

def mean(lst):
    return sum(lst) / len(lst)

def list_stack(lst, val, number):
    lst.append(val)
    if(len(lst) > number):
        lst.pop(0)

def find_nth(string, what, n):
    start = string.find(what)
    while start >= 0 and n > 1:
        start = string.find(what, start+len(what))
        n -= 1
    return start

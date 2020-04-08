def lar(s):
    if len(s) == 0 or s == None:
       return ""
    pr = s[0]
    lenpr = len(pr)
    for i in s[1:]:
        while pr != i[0:lenpr]:
            pr = pr[0:lenpr-1]
            lenpr -= 1
    return pr




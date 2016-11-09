#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    word1 = ".xyz"
    word2 = "xyz"
    newstr = str.replace(word1,"")
    if word2 in newstr:
        return True
    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))

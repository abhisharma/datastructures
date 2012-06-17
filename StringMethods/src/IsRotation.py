def IsRotation(s1,s2):
    isRot = False;
    if len(s1) == len(s2) and len(s1) > 0 and (s1+s1).find(s2) != -1:
        isRot = True
    return isRot

print(IsRotation("abcdef", "cdefab"))
print(IsRotation("abcdef", "cdehab"))
print(IsRotation("abcdef", "cdeab"))
print(IsRotation("acdef", "cdefab"))
        
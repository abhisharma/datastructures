def CheckAnagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False

print(CheckAnagrams("Hello", "Holle"))
print(CheckAnagrams("orchestra", "carthorse"))
print(CheckAnagrams("orchestra", "carthopse"))
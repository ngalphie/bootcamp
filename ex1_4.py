def longcomstr(s1, s2):
    """Find the longest common substring between two strings"""
    s = ' '
    longest = ' '
    for i in range(len(s1)):
        for j in range(len(s1)):
            s = s1[i:j]
            if s2.count(s)>0 and len(s)>len(longest):
                longest = s
    return longest

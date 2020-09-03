def mutate_string(s, p, c):
    string = s[0:p] + c + s[p+1::]
    return string

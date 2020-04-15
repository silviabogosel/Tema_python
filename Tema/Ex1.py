
vector={'p': 3,
 'y': 2,
 't': 1,
 'h': 1,
 'o': 3,
 'n': 1,
 ' ': 3,
 'g': 1,
 'i': 1,
 'v': 1,
 'e': 3,
 's': 3,
 'u': 2,
 'r': 2,
 'w': 1,
 '.': 1}

def letter_count(sir):
    s=sir.lower()
    dim=len(s)
    i=0;
    nr=0;
    while i<dim:
        nr=nr+vector[s[i]]

        i=i+1;
    return nr
    pass


print(letter_count('Python gives you superpowers.'))


import time

def create_bad_match_table(pat):
    res = {}
    m = len(pat)
    print(pat)
    for i in range(m-1):
        pos = m - i - 1
        character = pat[i]
        res[character] = pos
    return res


def locate(pat, txt, with_preprocessing=False):
    tic = time.time()
    positions = []
    
    table = create_bad_match_table(pat)
    m = len(pat)
    n = len(txt)
    i = 0

    if not with_preprocessing:
        tic = time.time()
    
    while(i < n-m):
        current_txt = txt[i:i+m]
        j = m - 1

        while(current_txt[j] == pat[j]):
            if j == 0:
                break
            j -= 1
        
        if j == 0:
            positions.append((i, i+m))
            i += 1
        else:
            bad_character = current_txt[j]
            shift = table.get(bad_character, m)
            i += shift

    toc = time.time()
    measured = toc - tic
                
    return positions, measured
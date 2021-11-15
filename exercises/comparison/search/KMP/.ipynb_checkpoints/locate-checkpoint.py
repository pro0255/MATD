import time

def build_LPS(pat, M, lps):
    pos = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i]== pat[pos]:
            pos += 1
            lps[i] = pos
            i += 1
        else:
            if pos != 0:
                pos = lps[pos-1]  
            else:
                lps[i] = 0
                i += 1


def locate(pat, txt, with_preprocessing=False):

    tic = time.time()

    positions = []
    
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0
    build_LPS(pat, M, lps)  

    if not with_preprocessing:
        tic = time.time()

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            positions.append((i-j, i))
            j = lps[j-1]
  
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
    toc = time.time()
    measured = toc - tic

    return positions, measured
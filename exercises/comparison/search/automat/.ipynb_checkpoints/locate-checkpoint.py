from buildTable import build_table

def locate(pattern, text):
    table, alphabet = build_table(pattern)
    state = 0
    
    positions = []
    
    for position, c in enumerate(text):
        if c not in alphabet:
            state = 0
            continue
            
        state = table[state][c]        
        is_founded = state == len(table) - 1
        
        if is_founded:
            
            end = position
            start = end - len(pattern) + 1
            positions.append((start, end))

    return positions
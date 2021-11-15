import time

def locate(pattern, text, with_preprocessing=True):
    
    tic = time.time()

    positions = []
    
    for i in range(len(text)):
        founded = True
        for j in range(len(pattern)):
             
            
            current_i = i + j
            
            if current_i > len(text) - 1:
                founded = False
                break
                
            current_j = j
            
            current_text_char = text[current_i]
            current_pattern_char = pattern[current_j]
            
            if current_text_char != current_pattern_char:
                founded = False
                break
            
        if founded:
            positions.append((i, i+len(pattern)))
            
    toc = time.time()
    measured = toc - tic

    return positions, measured
def unique(a = None):
    if a == None:
        pass
    else:
        return list(set(a))
    
def value_counts(a):
    val_counts = {}
    for element in a:
        if element in val_counts:
            val_counts[element] += 1
        else:
            val_counts[element] = 1
    return val_counts

def probabilities(a):
    vals = value_counts(a)
    total = sum(vals.values())
    for element in vals:
        vals[element] = float(vals[element])/total
    return vals

def kl_divergence(a = None, b = None):
    import numpy as np
    a.extend(b)
    unique_values = unique(a)
    prob_a = probabilities(a)
    prob_b = probabilities(b)
    additive_element = []
    for x in unique_values:
        if x not in prob_a:
            prob_a[x] = 0
        if x not in prob_b:
            prob_b[x] = 0
        
        condition = (prob_a[x] == 0) or (prob_b[x] == 0)
        if condition == False:
            new_element = prob_a[x]*np.log(prob_a[x]/prob_b[x])/np.log(2)
            additive_element.append(new_element)
    return sum(additive_element)

    

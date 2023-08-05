def maxValue(n, x):
    neg_flag = False
   
    if n[0] == '-':
        neg_flag = True
        # delete - off of int
        n = n[1:]
            
    # add to the front to set first max
    return_val = str(x) + n
    for pos in range(0, len(n)+1):
        # rebuild string
        compare_val = n[:pos] + str(x) + n[pos:]
        # convert str --> int
        compare_int = int(compare_val)
        return_val_int = int(return_val)
        # set to the min
        if neg_flag:
            if return_val_int > compare_int:
                return_val_int = compare_int
        else:
            # set to the max
            if return_val_int < compare_int:
                return_val_int = compare_int
        # compare ints        
        return_val = str(return_val_int)

    if neg_flag:
        return_val = '-'+str(return_val)
    else:
        return_val = str(return_val)

    return return_val
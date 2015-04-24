def FeatureMapping(HEADINGS,X,degree):
    import numpy as np
    draft_array                 = np.array(X)
    draft_headings              = np.array(HEADINGS)    
    FirstColindex               = 0
    colIndex                    = 1

    while FirstColindex < X.shape[1] - 1: 
        for d in range(1,degree+1):            
            for j in range(d+1):
                r               = (X[:,FirstColindex]**(d-j)) * (X[:,colIndex]**j)
                r               = np.array([r]).T
                draft_array     = np.append(draft_array,r,axis = 1)
                
                if d-j == 1 and j == 1:
                    h           =  str(HEADINGS[FirstColindex]) + str(HEADINGS[colIndex])
                elif d-j != 0 and j != 0:
                    if d-j == 1:
                        h       =  str(HEADINGS[FirstColindex]) + str(HEADINGS[colIndex]) + '^' + str(j)
                    elif j == 1:
                        h       =  str(HEADINGS[FirstColindex]) + '^' + str(d-j) + str(HEADINGS[colIndex])
                    else:    
                        h       =  str(HEADINGS[FirstColindex]) + '^' + str(d-j) + str(HEADINGS[colIndex]) + '^' + str(j)
                elif j == 0:
                    if d-j == 1:
                        h       =  str(HEADINGS[FirstColindex])
                    else:
                        h       =  str(HEADINGS[FirstColindex]) + '^' + str(d-j)
                elif d-j == 0:
                    if j == 1:
                        h       = str(HEADINGS[colIndex])
                    else:
                        h       = str(HEADINGS[colIndex]) + '^' + str(j)
                draft_headings  = np.append(draft_headings, h)
        
        if colIndex == X.shape[1] - 1:
            FirstColindex       = FirstColindex + 1
            colIndex            = FirstColindex + 1
        else:
            colIndex                = colIndex + 1 
    # Remove duplicates
    print 'Removing duplicates'
    mapped_array                = np.ones((X.shape[0],1))
    mapped_headings             = np.array(['    '])
    unique_col_chek_array_draft = np.mean(draft_array, axis = 0) + np.sum(draft_array, axis = 0) + np.max(draft_array, axis = 0) + np.min(draft_array, axis = 0) 
    unique_col_chek_array_draft = unique_col_chek_array_draft.tolist()
    unique_col_chek_array       = []
    
    for i,el in enumerate(unique_col_chek_array_draft):
        try:
            unique_col_chek_array.index(el)
        except:
            r                   = np.array([draft_array[:,i]]).T
            mapped_array        = np.append(mapped_array,r, axis = 1)
            mapped_headings     = np.append(mapped_headings,draft_headings[i]) 
            unique_col_chek_array.append(el)
    return mapped_headings,mapped_array   

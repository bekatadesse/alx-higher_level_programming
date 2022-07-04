def new_in_list(my_list, idx, new_element):
    length = len(my_list)
    new_list=my_list
    if idx < 0:
        return(new_list)
    if idx> length:
        return(new_list)
      
    
    new_list[idx]=new_element
    return(new_list)
    

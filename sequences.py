def remove_duplicates(input_list):
    singles_list = []
    for element in input_list:
        if input_list.count(element) == 1:
            singles_list.append(element)
    return singles_list
   
 # singles_list = [element for element in input_list if input_list.count(element) == 1]
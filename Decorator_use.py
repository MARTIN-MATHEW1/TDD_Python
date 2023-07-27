import operator



def Age_sorter(func):
        def sort_on_age(inp_list):
             return (map(func,sorted(inp_list, key=operator.itemgetter(3))))
        return sort_on_age

@Age_sorter
def name_Format(Name_Details_list):
      
    return (('Mr' if Name_Details_list[2] == 'M' else 'Mrs') 
            + Name_Details_list[0]
            + " " 
            + Name_Details_list[1])



def Name_and_Details(inp_list):
    return (*name_Format(inp_list))





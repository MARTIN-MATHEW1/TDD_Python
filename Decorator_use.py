import operator


def Age_sorter(func):
        def sort_on_age(inp_list):
             return (map(func,sorted(inp_list, key=operator.itemgetter(3))))
        return sort_on_age

@Age_sorter
def name_Format(Name_Details_list):
    intermediate_result = (('Mr.' if Name_Details_list[2] == 'M' else 'Mrs.') 
            + Name_Details_list[0]
            + " " 
            + Name_Details_list[1])
    # print(intermediate_result)
    return (intermediate_result)

def Name_and_Details(inp_list):
    return list(name_Format(inp_list))

# details_list = [
#     ["John", "Doe", "M", 30],
#     ["Jane", "Smith", "F", 25],
#     ["Michael", "Johnson", "M", 40]
# ]

# formatted_names = Name_and_Details(details_list)
# for name in formatted_names:
#     print(name)



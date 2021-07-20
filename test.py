def flatten(l):
    def is_flat(l):
        return any(filter(lambda x:type(x)==list, l))
    
    def level(l):
        flat_list = []
        for i in l:
            if type(i) == list:
                flat_list.extend(i)
            else:
                flat_list.append(i)
        return flat_list
    
    while is_flat(l):
        l = level(l)

    return l


l = [1,2,3,[[[[6]]]], [9,8,[7]]]

print(flatten(l))
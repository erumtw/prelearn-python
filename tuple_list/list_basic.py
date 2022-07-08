def list_op():
    flowers = ['ivy', 'sunflower', 'lupin']
    print(flowers)
    
    # add 
    flowers += ['forget me not', 'moonflower']
    print(flowers)
    flowers.append("gypso")
    print(flowers)
    
    # delete
    del flowers[1]
    print(flowers)
    flowers.remove('ivy')
    print(flowers)
    
    # sort
    sorted_flower = sorted(flowers)
    print(sorted_flower)
    print(flowers)
    flowers.sort()
    print(flowers)
    
    
list_op() 
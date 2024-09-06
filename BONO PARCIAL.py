'''Tenemos dos listas sencillamente encadenadas solamente con referencia al primero.
my_list = {
"first":...,
"size:...
}

new_list = {
"first":...,
"size":...
}

La idea es implementar una función que, dado un índice, una lista original y una lista nueva, devuelva una lista en la que la lista nueva se inserte 
en la lista original según la posición indicada. De esta manera, el primer elemento de la lista nueva quedará en la posición especificada, y el último 
elemento de la lista nueva apuntará al elemento que previamente ocupaba la posición pos + 1 en la lista original.
'''
def insert_list(my_list, new_list, pos):
    nodo = my_list['first']
    nodoNL = new_list['first']
    
    if pos == 0:
        if nodo == None:
            nodo = nodoNL
        else:
            nodo["next"] = nodo
            nodo["first"] = nodoNL
        my_list["size"] += 1
    elif pos == my_list["size"]:
     
        if my_list["size"] == 0:
            my_list["first"] = nodoNL
        else: 
            my_list["last"]["next"] = nodoNL
        my_list["size"] += 1
    else:
        count = 0
        act = my_list["first"]
        while count < pos - 1:
            count += 1
            act = act["next"]
        nodoNL['next'] = act['next']
        act['next'] = nodoNL
        my_list['size'] += 1
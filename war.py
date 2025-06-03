def python_snake(xs):
    n = xs
    head = "H"
    body = "X"
    tail = "T"
    longitud = len(xs)
    columnas = max(xs)
    matrix=[]
    for i in range(longitud):
        row = []
        for x in range(columnas):
            row.append('h')
            
        matrix.append(row)
    return matrix  
                 
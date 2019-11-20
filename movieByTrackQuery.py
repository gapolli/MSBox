from rdflib import Graph, Literal

g = Graph()
filename = 'msbox.ttl'
g.parse(filename, format='turtle')

track = input("Please input the track name: ")
track = Literal(track)

"""Pesquisa de tracks dos filmes"""
ans = """SELECT ?x ?y
        WHERE {
                ?d mo:track ?x .
                ?d foaf:name ?y .
        }"""

ans2 = """SELECT ?x ?y ?z ?w ?t ?n
        WHERE {
                ?d rdf:type ?x .
                ?d mo:album ?y .
                ?y mo:track ?t .
                ?d owl:sameAs ?z .
                ?d dbo:musicComposer ?w .
                ?w owl:sameAs ?n .
                FILTER (?x = dbo:Movie)
        }"""

result = g.query(ans, initBindings={"x": track})

print()
for row in result:
        print("Track:", row.x)
        print("Album:", row.y)
        '''
        A pesquisa tem de ser feita dentro do for para obter os dados do filme que 
        estão relacionados a track escolhida pelo usuário.
        '''
        result2 = g.query(ans2, initBindings={"t": track})
        for row2 in result2:
                print("Present in movie:", row2.z)
                print("Composer:", row2.n)
        print()

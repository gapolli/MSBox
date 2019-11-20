from rdflib import Graph

g = Graph()
filename = 'msbox.ttl'
g.parse(filename, format='turtle')
g.bind('dbo', 'http://dbpedia.org/ontology/')
g.bind('mo', 'http://purl.org/ontology/mo/')
g.bind('owl', 'http://www.w3.org/2002/07/owl#')

"""Pesquisa de soundtracks relacionadas aos filmes"""
ans = """SELECT ?x ?y ?z ?w
        WHERE {
                ?d rdf:type ?x .
                ?d owl:sameAs ?w .
                FILTER (?x = dbo:Movie)
        }"""

ans2 = """SELECT ?y ?z ?w
        WHERE {
                ?d owl:sameAs ?w .
                ?d mo:album ?y .
                ?y mo:track ?z .
        }"""

result = g.query(ans)

for row in result:
        print("From movie:", row.w)
        print("The soundtracks are:")
        '''
        A pesquisa tem de ser feita dentro do for para obter as soundtracks do filme que 
        está sendo exibido na tela na iteração atual.
        '''
        result2 = g.query(ans2, initBindings={"w": row.w})
        for row2 in result2:
                print("*", row2.z)
        print()

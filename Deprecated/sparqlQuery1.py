from rdflib import Graph

g = Graph()
filename = 'msboxprototype.ttl'
g.parse(filename, format='turtle')
g.bind('msbox', 'http://www.msbox.com/#')

"""Pesquisa de compositores relacionados aos filmes"""
ans = g.query(
    """SELECT ?x ?y ?z
        WHERE {
        ?a dbo:composer ?x .
        ?x rdf:label ?y }"""
)

for row in ans:
    print(row.x, ":", row.y)

#Se importa las librerías
import networkx as nx
import matplotlib.pyplot as plt

#Se crea un grafo vacio
G=nx.Graph()
vertice_a = ["0. Pereira","6. Manizales","8. Irra","12. Belalcazar","2. Belén de Umbría","1. Mistrato","9. Anserma","5. Riosucio","7. Medellín"]
vertice_b = vertice_a.copy()
vertice_b.pop(0)
vertice_b.append(vertice_a[0])
union = zip(vertice_a, vertice_b)
aristas = list(union)

#Se crean los nodos
G.add_nodes_from(vertice_a)
G.add_edges_from(aristas) 
#Se dibuja el grafo
nx.draw(G, with_labels=True)
#Se muestra en pantalla
plt.show()

#Se muestra información de los nodos (cantidad, nodos)
print("Nodos: ", G.number_of_nodes(), G.nodes())
#Se muestra información de los enlaces (cantidad, enlaces)
print("Enlaces: ", G.number_of_edges(),G.edges())

#Importamos la líbreria Queue
from queue import Queue
#Creamos nueva clase
class Grafo:
    '''Constructor
    Con la funcion def se define la identificación'''
    def __init__(self, num_de_nodos, dirigido=True): 
        '''Especifiar el atributo de la instancia'''
        self.m_num_de_nodos = num_de_nodos 
        '''La función range es el ranfo qu eva a retorna'''
        self.m_nodos = range(self.m_num_de_nodos) 
		
        ''' Diriguido  y no dirigido'''
        self.m_dirigido = dirigido
		
        ''' Representación gráfica- lista de adyacencia
         Usamos un diccionario para implementar una lista de adyacencia'''
        self.m_lista_calificativo = {nodo: set() for nodo in self.m_nodos}      
	
    # Agregar borde al gráfico
    def add_arista(self, nodo1, nodo2, peso=1):
         #Especifiar el atributo de la instancia de acuerdo a los nodos 
        self.m_lista_calificativo[nodo1].add((nodo2, peso))
        ''' Condicion para un nodo que no esta dirigido'''
        if not self.m_dirigido:
            self.m_lista_calificativo[nodo2].add((nodo1, peso))
    
    # Imprimir la representación gráfica y contiene el parámetro
    def impri_lista_calificativo(self):
        '''Es para recorrer los elementos del objeto, para asi poder ejecutar un bloque de código
        y poder imprimir la lista de nodos especificados'''
        for key in self.m_lista_calificativo.keys():
            print("nodo", key, ": ", self.m_lista_calificativo[key])

    '''Función que imprime el recorrido BFS
     De un vértice fuente dado. bfs_transversal(int s)
     Atraviesa vértices accesibles desde s.'''
    def bfs_traversal(self, inicio_nodo):
        # Conjunto de nodos visitados para evitar bucles
        vista = set()
        queue = Queue()

        ''' Agregue inicio_nodo a la cola y la lista visitada
        El put se utiliza para modificar los datos al momento que va recorriendo al  nodo de inicio'''
        queue.put(inicio_nodo)
        vista.add(inicio_nodo)
        #Control de flujo para ejecutar el bloque de instrucciones
        while not queue.empty():
            # De queue un vértice de
            # queue and print it
            nodo_actual = queue.get()
            print(nodo_actual, end = " ")

            '''Obtener todos los vértices adyacentes 
             dequeued vértice. un If a adyacente
             no ha sido visitado, entonces márcalo
             visited and enqueue it'''
            for (siguiente_nodo, peso) in self.m_lista_calificativo[nodo_actual]:
                if siguiente_nodo not in vista:
                    #El put se utiliza para modificar los datos al momento que va recorriendo al siguiente nodo
                    queue.put(siguiente_nodo)
                    vista.add(siguiente_nodo)

#Para ejecutar un archivo
if __name__ == "__main__":
    #### EJEMPLO #####

    '''Crear una instancia de los Grafos clase
    Este grafo no está dirigido y tiene 5 nodos el cual realizara su respectiva recorrido'''
    g = Grafo(9, dirigido=False)
    
    '''Ejemplo del caso unitario prueba 1
     g.add_arista(1, 2)
    g.add_arista(2, 4)
    g.add_arista(2, 5)
    g.add_arista(5, 6)
    g.add_arista(3, 6)
    g.add_arista(3, 1)
    g.add_arista(3, 7)
    g.add_arista(3, 8)
   '''
   
    '''Ejemplo del caso unitario prueba 2
    g.add_arista(2, 1)
    g.add_arista(2, 3)
    g.add_arista(1, 6)
    g.add_arista(1, 3)
    g.add_arista(3, 4)
    g.add_arista(4, 5)
    g.add_arista(4, 6)
    g.add_arista(6, 5)
   '''

    '''Agregue bordes al grafo con determinado  peso = 1 
    Estas lineas de codigo es para añadir los elementos de los nodos
    que tenemos que van recorriendo en cadena'''
    g.add_arista(2, 1)
    g.add_arista(2, 3)
    g.add_arista(1, 6)
    g.add_arista(1, 3)
    g.add_arista(3, 4)
    g.add_arista(4, 5)
    g.add_arista(4, 6)
    g.add_arista(6, 5)
    
   
   


    ''' Imprimir lista de adyacencia en el nodo de formulario n: {(nodo, peso)}'''
    g.impri_lista_calificativo()
    '''Imprimir el mensaje y la ubicación de donde empieza los grafos a recorrer'''
    print ("A continuación se muestra el reccorrido en amplitud"
                    " (Comenzando desde el vertice 0)")
    g.bfs_traversal(2)
    #Muestra la información por pantalla, ya sea números, texto
    print()
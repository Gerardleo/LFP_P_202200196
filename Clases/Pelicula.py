class Pelicula:
    def __init__(self, nombre, year,genero):
        self.nombre = nombre
        self.actores = []
        self.year = year
        self.genero = genero

    def agregar_actor(self, actor):
        self.actores.append(actor)

    def eliminar_actor(self, actor):
        self.actores.remove(actor)

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_year(self, year):
        self.year = year

    def set_genero(self, genero):
        self.genero = genero

    def get_nombre(self):
        return self.nombre
    
    def get_year(self):
        return self.year
    
    def get_genero(self):
        return self.genero
    
    def get_actores(self):
        return self.actores
  
    def mostrarPelicula(self):
        return self.nombre

   


    
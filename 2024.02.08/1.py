class Tetrahedron:
    
    def __init__(self, edge: float):
        self.edge = edge
        
    def surface(self) -> float:
        """площадь поверхности"""
        return (self.edge**2) * (3**0.5)
    def volume(self) -> float:
        """объём тела"""  
        return (self.edge**3) /12 * (2**0.5)

#>>> t2 = Tetrahedron(5)
#>>> t2.edge
#5
#>>> t2.surface()
#43.30127018922193
#>>> t2.edge = 6
#>>> t2.surface()
#62.35382907247958
#>>> t2.volume()
#25.455844122715714        
class Ordenacao():
    
    def __init__(self, array_para_ordenar:[]):
        self.lista = array_para_ordenar
    
    def ordena(self):
        for i in range(1, len(self.lista)):
            pivo = self.lista[i]
            pos_ant = i - 1
            while pos_ant >= 0 and self.lista[pos_ant] > pivo:
                self.lista[pos_ant + 1] = self.lista[pos_ant]
                pos_ant -= 1
            self.lista[pos_ant + 1] = pivo
    
    def to_string(self):
        lista_convertida = str(self.lista[0])
        for elemento in self.lista[1:]:
            lista_convertida += ',' + str(elemento)
        return lista_convertida
        
    
a = Ordenacao([4, 3, 2, 1, 5])
a.ordena()
print(a.to_string())
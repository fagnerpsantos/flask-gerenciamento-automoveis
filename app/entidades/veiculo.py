class Veiculo():
    def __init__(self, modelo, cor, marca, potencia):
        self.__modelo = modelo
        self.__cor = cor
        self.__marca = marca
        self.__potencia = potencia

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, potencia):
        self.__potencia = potencia
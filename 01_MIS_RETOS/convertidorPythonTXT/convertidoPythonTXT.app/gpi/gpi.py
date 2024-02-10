class Casa:
    def __init__(self, uso_suelo="🔸Sin valores", certificado_propiedad="🔸Sin valores", libre_de_gravamen="🔸Sin valores", avaluo="🔸Sin valores", registro_publico="🔸Sin valores", aviso_preventivo="🔸Sin valores", escrituracion="🔸Sin valores"):
        self.Uso_suelo = uso_suelo
        self.Certificado_propiedad = certificado_propiedad
        self.Libre_de_gravamen = libre_de_gravamen
        self.Avaluo = avaluo
        self.Registro_publico = registro_publico
        self.Aviso_preventivo = aviso_preventivo
        self.Escrituracion = escrituracion
    def __str__(self):
        return f"Uso_suelo: {self.Uso_suelo}, Certificado_propiedad: {self.Certificado_propiedad}, Libre_de_gravamen: {self.Libre_de_gravamen}, Avaluo: {self.Avaluo}, Registro_publico: {self.Registro_publico}, Aviso_preventivo: {self.Aviso_preventivo}, Escrituracion: {self.Escrituracion}"


molino = Casa(uso_suelo="Residencial")
molino.Avaluo = "1,000,000"


print(molino)

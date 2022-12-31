class titulo:
    def __init__(self,nom="UNEM",ruc="0999999999",tel="0962745197"):
        self.nombre=nom
        self.ruc=ruc
        self.tel=tel
        
if __name__ == '__main__':
    org = titulo()
    print("="*10)
    print(org.nombre)
    print(org.ruc)
    print(org.tel)
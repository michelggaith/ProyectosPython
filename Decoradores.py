def decorador(funcionComun):
    def funcionDecorada(*args, **kwargs): #Indica que le puedo pasar tantos parametros como quiera
        print('Mi primer decorador')
    return funcionDecorada

@decorador #estoy "decorando" la funcion, modificando su comportamiento
def funcionComun():
    print('Mi funcion Comun')

funcionComun()
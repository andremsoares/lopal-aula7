produto = "Mouse Gamer WIFI"

valores = [20, 71, 100, 30]

if "mouse".lower() in produto.lower():
    print("Produto encontrado")
else:
    print("Produto não encontrado")
    
def dobrar(valor):
    resultado = valor * valor
    return resultado

print(dobrar(11))


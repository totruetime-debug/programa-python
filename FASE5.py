#CARLOS EDUARDO VANEGAS REDONDO
#Fase 5 - Evaluación Final POA
#Fundamentos de Programación
#CODIGO FUENTE: Autoria Propia

#Ejercio 3

""" Ejercicio 3 Se requiere una herramienta para auditar el inventario y
decidir qué artículos necesitan ser reabastecidos. La información se
encuentra en una matriz: [Código Artículo, Nombre, Stock Actual, Stock
Mínimo Requerido].
"""
# Matriz de inventario: 
#[Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 12, 8],
    ["A103", "Monitor", 3, 6],
    ["A104", "USB", 20, 15],
    ["A105", "Audífonos", 2, 5],
    ["A106", "Disco Duro", 5, 2],
    ["A107", "Cable HDMI", 8, 4]
]

# Función para calcular pedido
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Programa principal
print("========================================")
print("   REPORTE DE REABASTECIMIENTO")
print("========================================\n") 

# Recorrer la matriz del inventario
for articulo in inventario:

    # Extraer datos de la matriz
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamar la función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    if cantidad_pedir > 0:
        # Mostrar resultados
        print("Código: ", codigo, " - Artículo: ", nombre)
        print("Stock actual:", stock_actual, " - Stock mínimo:", stock_minimo, " - Cantidad a pedir:", cantidad_pedir)
        print("----------------------------------------")
    
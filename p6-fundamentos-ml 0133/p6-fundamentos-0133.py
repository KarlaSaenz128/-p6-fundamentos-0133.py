print("Karla Saenz 0133")
# Ejemplo 1: 
nombre = "Carlos"
edad = 25
print(nombre, edad)
print("+-+-++-+-+-+-++-+--+-+-+-+-+")
# Ejemplo 2: 
precio = 19.99
es_activo = True
print("Precio:", precio, "| Activo:", es_activo)
print("+-+-+-+-+-+--+-+-+-+-+--+-+-+-+--+-+")
# Ejemplo 3: 
x = 10
x = "Ahora soy un texto"
print(x)
print("+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-++--+")
# Ejemplo 1: A
fruta, color, cantidad = "Manzana", "Rojo", 5
print(fruta, color, cantidad)
print("+-+--+-+-+-+-+-+-+-+-+-+-+-++--+-++-+-+-+-")
# Ejemplo 2: 
a = b = c = 100
print(a, b, c)
print("-++--+-+-+-++--+-+-+-++-+-+--++-+-+-+-++-+")
# Ejemplo 3: Desempaquetar una lista (Unpack)
frutas = ["Naranja", "Plátano", "Cereza"]
x, y, z = frutas
print(x, y, z)
print("-+-+-++-+-+--+-+--+-++-++-+-+-++-+-+-+-+-+")
# Ejemplo 1: Tipos numéricos y texto (int, float, str)
texto = "Hola Mundo"
entero = 42
decimal = 3.14
print(type(texto), type(entero), type(decimal))
print("-+-+-+-+-+-+-+-+--++-+--+-+-+-+-+-+-+-+-+-+")
# Ejemplo 2: Colecciones (list, tuple, dict)
lista = [1, 2, 3]
tupla = ("A", "B", "C")
diccionario = {"nombre": "Ana", "edad": 30}
print(type(lista), type(tupla), type(diccionario))
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 3: Tipo booleano y conversión explícita de tipos (Casting)
es_valido = True
numero_str = str(100)  
print(type(es_valido), type(numero_str))
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
# Ejemplo 1: Suma, resta y multiplicación
suma = 15 + 5
resta = 20 - 8
multiplicacion = 4 * 3
print("Suma:", suma, "| Resta:", resta, "| Mult:", multiplicacion)

# Ejemplo 2: División estándar y división entera
division = 10 / 3        
division_entera = 10 // 3 
print("División:", division, "| División entera:", division_entera)

# Ejemplo 3:
modulo = 10 % 3          
potencia = 2 ** 4        
print("Módulo:", modulo, "| Potencia:", potencia)
print("+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+")
# Ejemplo 2: 
puntuacion = 85
print(puntuacion > 50)  # True
print(puntuacion < 70)  # False
print("-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-")
# Ejemplo 3: 
limite = 18
edad_usuario = 18
print(edad_usuario >= limite)  # True
print(edad_usuario <= 15)      # False
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+--+")
# Ejemplo 1: 
tiene_clave = True
es_admin = True
print(tiene_clave and es_admin)  # True
print("-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-")
# Ejemplo 2: 
es_fin_de_semana = False
es_feriado = True
print(es_fin_de_semana or es_feriado)  
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+")
# Ejemplo 3: 
esta_lloviendo = False
print(not esta_lloviendo)  
#!/bin/python3
import json #Para lectura de datos
import os #Para crear la carpeta 'plots'
import matplotlib.pyplot as plt #Para dibujar el PNG
#Preparar las listas
temperaturas = []
gases = []

#Preparar carpeta
if not os.path.exists("plots"):
	os.makedirs("plots")

with open("mqtt_capture.log", "r") as file: 
	for linea in file: 
		if "Payload:" in linea:
			texto_limpio = linea.split("Payload: ")[1]
			datos = json.loads(texto_limpio)
			if "AmbientTemperature" in datos:
				#Si tiene temperatura, la sacamos del diccionario y lo metemos a la lista
				temperaturas.append(datos["AmbientTemperature"])
			elif "GM102B" in datos: 
				#Si tien gas, lo metemos en la otra lista
				gases.append(datos["GM102B"])
#Funcion para la gráfica
def dibujar_ascii(valores, titulo):
	muestras = len(valores)
	if muestras <= 1:
		return
	print(f"\n=== {titulo} Plot (ASCII) ===")
	y_min= min(valores)
	y_max= max(valores)
	print(f"muestras={muestras} | y_min={y_min:.2f} | y_max={y_max:.2f} | archivo=mqtt_capture.log\n")
	Alto = 10 
	Ancho = muestras *2 #espacio de los asteriscos
	matriz = [[" " for _ in range(Ancho)] for _ in range(Alto)]

	#Calcular coordenadas de cada asteriscos
	for i in range(muestras):
		valor = valores[i]
		if y_max != y_min:
			fila = int((valor - y_min) / (y_max - y_min) * (Alto - 1))
		else:
			fila = 0
		#Invertir para que la terminal imprima bien
		fila = (Alto -1) - fila
		columna = i * 2
		matriz[fila][columna] = "*"
	#Imprimir el tablero con el eje y
	for r in  range(Alto):
		if r ==0:
			prefijo = f"{y_max:7.2f} | "
		elif r == Alto -1:
			prefijo = f"{y_min:7.2f} | "
		else:
			prefijo = "        | "
		print(prefijo + "".join(matriz[r]))
	#Imprimir el eje x
	print("          +" + "-" * Ancho)
	texto_fin = str(muestras - 1)
	espacios = Ancho - len(texto_fin) - 1
	if espacios <0: espacios = 0
	print("      0" + " " * espacios + texto_fin)

	#Ultimos valores
	Ultimos = ", ".join(f"{v:.2f}" for v in valores[-10:])
	print(f"\nÚltimos valores: {Ultimos}")
#Dibujar gráfica de Temperaturas
if len(temperaturas) > 0:
	plt.figure()
	plt.plot(temperaturas, marker='o', color = 'red')
	plt.title("Evolución de la Temperatura")
	plt.xlabel("Muestras")
	plt.ylabel("Grados Celsius")
	plt.grid(True)
	#Guardar la carpeta creada
	plt.savefig("plots/grafica_temperatura.png")
	plt.close()



#Dibujar gráfica de gases
if len(gases) > 0:
	plt.figure ()
	plt.plot(gases, marker= 's', color='blue')
	plt.title("Evolución del Gas GM102B")
	plt.xlabel("Muestras")
	plt.ylabel("Nivel de gas")
	plt.grid(True)
	#Guardar en la carpeta creada
	plt.savefig("plots/grafica_gas.png")
	plt.close()

#Imprimir la Gráfica ASCII
if len(gases)>0:
	dibujar_ascii(gases, "MQTT Payload")

if len(gases)>0:
	dibujar_ascii(temperaturas, "MQTT payload")

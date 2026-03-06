# Practica 1 Sistemas Operativos 

## 1. Descripción
Este repositorio contiene la práctica 1 de Sistemas Operativos, con el objetivo de aplicar y demostrar la automatización de tareas en Linux combinando Bash y Python. 
El proyecto captura datos de sensores, que son de temperatura y de gases. Transmitidos a través del MQTT en formato JSON, los procesa y genera visualizaciones de los datos tanto en la propia terminal con una gráfica ASCII y exportando imagenes PNG.

## 2. Estructura del repositorio
```text
.
|-- capture_mqtt.sh #Script principal en Bash (control de procesos)
|-- plot_mqtt.py #Script de python (lectura en JSON y gráficas) 
|-- mqtt_subscribe_emqx_linux # Ejecutable MQTT para Linux
|--mqtt_capture.log #Archivo de registro (generado automáticamente) 
|-- plots #Carpeta de salida para las gráficas (png)
```
## 3. Requisitos del sistema 
* Sistema operativo: Linux (Ubuntu / WSL)
* Intérpretes necesarios:
	* bash
	* python3

## 4. Dependencias externas
El script de python requiere la libreria "matplotlib", para generar las imagenes "png"
Para instalarla: 
sudo apt update
sudo apt install python3-matplotlib 

## 5. Compilación 
Al tratarse de scripts interpretados en Bash y python no requiere compilación. Solo es necesario otorgar permisos de ejecucion al script principal.

chmod +x capture_mqtt.sh

## 6. Ejecución
Para iniciar el programa, ejecuta el script principal desde la raiz del repositorio:

./capture_mqtt.sh

El programa pedirá el tiempo de captura en segundos.

## 7. Salida esperada
Al ejecutar correctamente el programa:
1. Se iniciará el proceso de captura MQTT en segundo plano.
2. Pasado el tiempo, el proceso se detendrá de forma limpia.
3. Se mostrará por consola dos gráficas ASCII con la evolución del gas y la temperatura.
4. Se generarán dos archivos en la carpeta "plots", uno de temperaturas y otro de gases.

## 8. Problemas comunes
* No se generan gráficas, la conexion con los sensores suele fallar.
## 9. Autoría 
* ** Alumno :** Fernando Moran Fernandez
* ** Asignatura:** Sistemas Operativos 

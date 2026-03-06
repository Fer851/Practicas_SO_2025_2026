#!/bin/bash

#Pedir al usuario el tiempo de captura
echo "Introduce el tiempo de captura que desee para guardar los datos:"
read tiempo

if [ "$tiempo" == "" ]; then
	tiempo=10
fi
echo "[1/4] Ejecutando ./mqtt_subscribe_emqx_linux y guardando salida en mqtt_capture.log durante ${tiempo}s"
#Llamamos a  ./mqtt_subscribe_emqx_linux y lo metemos a un archivo
./mqtt_subscribe_emqx_linux > mqtt_capture.log  2>&1 &
#Guardar el PID
PID=$!
echo "[INFO] PID del programa: ${PID}"
for (( i=0; i<tiempo; i++ )); do
	if kill -0 $PID; then
		sleep 1
	else
		echo "El programa ya se ha ejecutado por completo"
		break
	fi
done 
#Mandar al programa que se cierre limpiamente
kill -15 $PID
#Ejecutar python de hola mundo
python3 <<'PY'
print("Hola mundo desde python ejecutado dentro de bash")
PY
echo "[3/4] Parseando datos desde mqtt_capture.log y graficando en terminal..."
python3 plot_mqtt.py
echo "[4/4] Listo"
echo "log guardado en: mqtt_capture.log"

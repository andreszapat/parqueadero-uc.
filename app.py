# Cantidad de vehiculos que se intentaran registrar
N = int(input("Ingrese la cantidad de vehiculos: "))

# contadores
vehiculos_validos = 0
total_recaudado = 0
total_horas = 0

estudiantes = 0
docentes = 0
visitantes = 0

i = 0

while i < N and vehiculos_validos < 30:

    print("VEHICULO", i + 1, " ")
    
    placa = input("Ingrese la placa: ")
    tipo = input("Tipo de usuario (E/D/V): ")
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas = float(input("Horas de permanencia: "))

    if hora_entrada < 0 or hora_entrada > 23 or horas <= 0:
        print("Error: hora de entrada o permanencia invalida.")
        print("Este vehiculo no sera contado.")
    else: 
        if tipo != "E" and tipo != "D" and tipo != "V":
            print("Advertencia: tipo invalido. Se registrara como visitante.")
            tipo = "v"

        #Tarifas
        tarifa = 0
        
        if tipo == "E":

            estudiantes = estudiantes + 1

            # Primeras 2 horas gratis
            if horas <= 2:
                tarifa = 0
            else:
                tarifa = (horas - 2) * 800

        elif tipo == "D":

            docentes = docentes + 1

            tarifa = horas * 500

        else:

            visitantes = visitantes + 1

            # Primera hora $1500
            if horas <= 1:
                tarifa = 1500
            else:
                tarifa = 1500 + ((horas - 1) * 1200)

        if hora_entrada >= 19 or hora_entrada < 6:
            tarifa = tarifa * 0.90
    
            # Redondear a 2 decimales
            tarifa = round(tarifa, 2)
    
    
            vehiculos_validos = vehiculos_validos + 1
            total_recaudado = total_recaudado + tarifa
            total_horas = total_horas + horas
    
            print("Vehiculo registrado")
            print("Tarifa: ", tarifa)
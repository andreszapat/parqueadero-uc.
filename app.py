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

# Ciclo principal
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

# DFMDP
# Ejercicio Final de Operadores
# Datos del estudiante ingresados por el sistema
nombre_estudiante = "Laura Gómez"
promedio = 78
matricula_pagada = True
activo = True

# Datos institucionales
estudiante_registrado = nombre_estudiante
registro_oficial = nombre_estudiante  # misma referencia
alumnos_autorizados = ["Laura Gómez", "Carlos Méndez", "Ana Ruiz"]

# Validaciones
promedio_valido = promedio >= 75                              # Comparación
estado_valido = matricula_pagada and activo                   # Lógicos
mismo_registro = estudiante_registrado is registro_oficial    # Identidad
autorizado = nombre_estudiante in alumnos_autorizados         # Pertenencia

# Resultados
print("Promedio válido:", promedio_valido)
print("Estado de cuenta y activo:", estado_valido)
print("¿Es el mismo registro oficial?", mismo_registro)
print("¿Está en la lista de autorizados?", autorizado)

# Validación final combinada
puede_presentar_examen = promedio_valido and estado_valido and mismo_registro and autorizado
print("¿Puede presentar el examen final?", puede_presentar_examen)
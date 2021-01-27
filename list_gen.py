from pyexcel_ods3 import get_data, save_data
from collections import OrderedDict

# -------- Constantes
FILENAME_SRC = "listado_orig.ods"
FILENAME_TARGET = "listado-1.ods"
SHEET_TARGET = "Notas"

# --- Indices para la informacion en archivo fuente
CABECERA = 0
NOMBRE = 1
DNI = 2
MAT = 3
CONV = 4

#-- Nombre dado a la pestaña donde esta la informacion en 
#-- el fichero fuente
SHEET_SRC = "archivo"

# -- Leer el fichero ods
data = get_data(FILENAME_SRC)

# -- Obtener los datos de la pestaña con los datos
sheet = data[SHEET_SRC]

# -- Crear una lista solo con los nombre
# -- En el original hay filas vacias
entry_src = [ row for row in sheet if row != [] ]

# -- Eliminar la primera fila (cabecera)
entry_src = entry_src[1:]

#-- Obtener el numero total de estudiantes
print(f"Estudiantes Totales: {len(entry_src)}\n")

# -- Formato de la hoja destino
entry_dst = [["Mat", "Conv", "DNI", "Nombre"]]

# -- Leer la informacion de la hoja fuente 
# -- y añadirla en la hoja destino
for estudiante in entry_src:
    mat = estudiante[MAT]
    conv = estudiante[CONV]
    dni = estudiante[DNI]
    name = estudiante[NOMBRE]
    print(f"{mat} {conv} {dni} {name} ")
    row_dst = [mat, conv, dni, name]
    entry_dst.append(row_dst)

print(entry_dst)

# -- Write the destination sheet
data_dst = OrderedDict()
data_dst.update({SHEET_TARGET: entry_dst})
save_data(FILENAME_TARGET, data_dst)

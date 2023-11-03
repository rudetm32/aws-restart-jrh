import re

# Lee el archivo preproinsulin-clean.txt
with open('/home/ec2-user/environment/practicas/preproinsulin-clean.txt', 'r') as archivo:
    texto = archivo.read()

# Divide el texto en aminoácidos 1-24, 25-54, 55-89 y 90-110
aminoacidos_1_24 = texto[:24]
aminoacidos_25_54 = texto[24:54]
aminoacidos_55_89 = texto[54:89]
aminoacidos_90_110 = texto[89:110]

# Verifica que los archivos tengan las longitudes correctas
if len(aminoacidos_1_24) == 24:
    # Guarda los aminoácidos 1-24 en lsinsulin-seq-clean.txt
    with open('/home/ec2-user/environment/practicas/lsinsulin-seq-clean.txt', 'w') as archivo_l1_24:
        archivo_l1_24.write(aminoacidos_1_24)
    print("Aminoácidos 1-24 (lsinsulin-seq-clean.txt) guardados. Longitud: 24 caracteres")

if len(aminoacidos_25_54) == 30:
    # Guarda los aminoácidos 25-54 en binsulin-seq-clean.txt
    with open('/home/ec2-user/environment/practicas/binsulin-seq-clean.txt', 'w') as archivo_l25_54:
        archivo_l25_54.write(aminoacidos_25_54)
    print("Aminoácidos 25-54 (binsulin-seq-clean.txt) guardados. Longitud: 30 caracteres")

if len(aminoacidos_55_89) == 35:
    # Guarda los aminoácidos 55-89 en cinsulin-seq-clean.txt
    with open('/home/ec2-user/environment/practicas/cinsulin-seq-clean.txt', 'w') as archivo_l55_89:
        archivo_l55_89.write(aminoacidos_55_89)
    print("Aminoácidos 55-89 (cinsulin-seq-clean.txt) guardados. Longitud: 35 caracteres")

if len(aminoacidos_90_110) == 21:
    # Guarda los aminoácidos 90-110 en ainsulin-seq-clean.txt
    with open('/home/ec2-user/environment/practicas/ainsulin-seq-clean.txt', 'w') as archivo_l90_110:
        archivo_l90_110.write(aminoacidos_90_110)
    print("Aminoácidos 90-110 (ainsulin-seq-clean.txt) guardados. Longitud: 21 caracteres")

# Copia el texto original (secuencia completa) a preproinsulin-seq-clean.txt
with open('/home/ec2-user/environment/practicas/preproinsulin-seq-clean.txt', 'w') as archivo_preproinsulin_clean:
    archivo_preproinsulin_clean.write(texto)
    print("Secuencia completa copiada a preproinsulin-seq-clean.txt")

if len(texto) == 110:
    print("El archivo preproinsulin-seq-clean.txt tiene 110 caracteres en minúscula, que representan los aminoácidos en la secuencia de la preproinsulina.")
else:
    print("El archivo preproinsulin-seq-clean.txt no tiene la longitud correcta.")

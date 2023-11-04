# Secuencia de preproinsulina humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Secuencias de insulina humana
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Combinar las cadenas B y A para formar la secuencia completa de la insulina
insulin = bInsulin + aInsulin

# Imprimir la secuencia de preproinsulina humana
print("La secuencia de preproinsulina humana:")
print(preproInsulin)

# Imprimir la secuencia de la cadena A de la insulina humana
print("La secuencia de la insulina humana, cadena A:", aInsulin)

# Diccionario de pesos moleculares de aminoácidos
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
             'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
             'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
             'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Calcular el número de cada aminoácido en la secuencia de insulina
aaCountInsulin = {aa: float(insulin.upper().count(aa)) for aa in aaWeights.keys()}

# Calcular el peso molecular de la insulina
molecularWeightInsulin = sum(aaCountInsulin[aa] * weight for aa, weight in aaWeights.items())

# Imprimir el peso molecular estimado de la insulina
print("El peso molecular estimado de la insulina:", molecularWeightInsulin)

# Peso molecular real de la insulina
molecularWeightInsulinActual = 5807.63

# Calcular y imprimir el porcentaje de error
error_porcentaje = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
print("Porcentaje de error:", error_porcentaje)

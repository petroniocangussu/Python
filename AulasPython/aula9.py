frase = 'Curso em Vídeo Python'
print(frase[:13])
print(frase[3:13])
print(frase[1:15:2])
print(frase[::2])
print(frase[5])
print("""BiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBilu
BiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBilu
BiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBilu
BiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBilu
BiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBiluBilu""")
print(frase)
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
#Para mudar frase = frase.replace('Python', 'Android')
print(frase)
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
print(frase[-1:])
def calcular_media(notas):
  soma = sum(notas)
  media = soma / len(notas)
  return media
  
def verificar_situacao(media):
  if media < 7:
    print("Reprovado")
  elif media == 10:
    print("Parabéns, sua média é 10")
  else:
    print("Aprovado")
    
notas = []
while True:
  nota = input("Digite uma nota (ou 'fim' para terminar): ")
  if nota == 'fim':
    break
  else:
    notas.append(float(nota))
    
media = calcular_media(notas)
print("Sua média é:", media)
verificar_situacao(media)

import collections
Texto = 'cadena de caracteres, para separar, para , tenerlos de forma separar. Para,'

def cuentapalabras(textoA):
  TextoA=Texto.replace(",","").replace(".","").upper()
  separador=" "
  TextoB=collections.Counter(TextoA.split(separador))
  return (TextoB)

print(cuentapalabras(Texto))

def operacao(v1, v2):

  pt = v1 ** v2

  mt = v1 * v2

  dv = v1 / v2

  di = v1 // v2

  res = v1%v2

  print("%i\n%i\n%0.2f\n%i\n%i" %(pt, mt, dv, di, res))

def hour(x):
    x+=14
    time = x%24
    print(time)

def hour(x, ha):

  x+=ha

  tim = x%24

  if tim<=12:

    print("%i da manha" %tim)

  else:

    tim-=12

    print("%i da tarde/noite" %tim)

def ferias(dm, ds, df):

  df+=dm

  rt = df%30

  rs = rt%7

  print("Dia do mes = %i\ndia da semana = %i" %(rt, rs))

def juros(p, r, n, t):

  a = p*((1+((r/100)/n))**(n*t))

  print("%0.2f" %a)

def area(rc):

  ac = 3.14 * (rc**2)

  print("%0.2f" %ac)

def retangulo(ab, ah):

  at = ab * ah

  print(at)

def consumo(km, gas):

  con = km / gas

  print("%0.3f km/l" %con)

def fahrenheit(fh):

  ce = (fh-32)/1.8

  print("%0.1f celcius" %ce)

def celcius(cel):

  fhr = (cel * 1.8) + 32

  print("%0.1f fahrenheits" %fhr)


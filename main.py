'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n == 1 :
    return False
  if n % 2 == 0:
    return False
  for i in range(3,n//2+1,2):
    if n % i == 0:
      return False
  return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
  p = 1
  for i in lst:
    p=p*i
  return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
  if x == y :
    return x
  while x != y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
  if x == y:
    return x
  while y != 0:
    r = x % y
    x = y
    y = r
  return x


def main():
  while True:
    print("1.Sa se stabileasca daca un numar este prim.")
    print("2.Sa se calculeze produsul a n numere naturale.")
    print("3.Sa se calculeze CMMDC a doua numere date.")
    print("4.Sa se calculeze CMMDC a doua numere date printr-o alta metoda.")
    print("x.Inchidere meniu.")
    optiune = input("Dati optiunea:")
    if optiune == "1":
      numar = int(input("Dati numarul n:"))
      if is_prime(numar):
        print("Numarul dat este prim")
      else:
        print("Numarul dat nu este prim")
    elif optiune == "2":
      nr=int(input("Dati numarul n:"))
      lst=[]
      for i in range(nr):
        lst.append(int(input("Dati numar:")))
      produs=get_product(lst)
      print("Produsul numerelor date:",produs)
    elif optiune == "3":
      nr1=int(input("Dati primul numar:"))
      nr2=int(input("Dati al doilea numar:"))
      cmmdc1=get_cmmdc_v1(nr1,nr2)
      print("CMMDC-ul este:",cmmdc1)
    elif optiune == "4":
      nr1 = int(input("Dati primul numar:"))
      nr2 = int(input("Dati al doilea numar:"))
      cmmdc2 = get_cmmdc_v2(nr1, nr2)
      print("CMMDC-ul este:",cmmdc2)
    elif optiune == "x":
      print("Meniul se va inchide.")
      break
    else:
      print("Optiune gresita. ALegeti din nou!")


if __name__ == '__main__':
  main()

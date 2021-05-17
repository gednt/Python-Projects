import math;
a = float(input("Digite o valor de A:"));
b = float(input("Digite o valor de B:"));
c = float(input("Digite o valor de C:"));
delta = (b*b)-4*a*c;
if delta>0:
    x1 = ((b*-1) + math.sqrt(delta))/2*a;
    x2 = ((b*-1) - math.sqrt(delta))/2*a;
    print("Valor de X1",x1);
    print("Valor de X2",x2);

elif delta==0:
    print("Raiz é 0");
    x = -b + math.sqrt(delta/2*a);

else:
    print("Raiz menor que 0");

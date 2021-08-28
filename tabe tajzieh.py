def maghsoom_elayh(n, l):
    for i in range (1, n):
        if n % i == 0:
            l.append(i)
    
def aval_boodan(n, avalha, avamel):
    for x in avamel:
        m = 0
        for i in range(1, x+1):
            if x % i == 0:
                m += 1
        if m == 2:
            avalha.append(x)
            
n = int(input())
avamel = []
avalha = []
maghsoom_elayh(n, avamel)
aval_boodan(n, avalha, avamel)
print(avalha)

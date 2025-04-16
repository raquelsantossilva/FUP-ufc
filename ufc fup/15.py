s=int(input())
horas=s//3600
rh=s%3600
minutos=rh//60
rm=rh%60
print(f'{horas}\n{minutos}\n{rm}')
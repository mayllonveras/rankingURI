#!/usr/bin/python3
import urllib.request
import csv
alunos = []
while(True):
	try:
		a = []
		p = input()
		p = p.split("\t")
		a.append(p[0])
		a.append(p[1])
		print("\n\nAcessando perfil de "+a[0]+"...")
		f = urllib.request.urlopen("https://www.urionlinejudge.com.br/judge/pt/profile/"+p[3])
		b = f.read()
		s = b.decode("utf8")
		f.close()
		l = s.split('\n')
		for x in range(len(l)):
			# Futuramente o nome será coletado do perfil
			#if("pb-username" in l[x]):
			#	a.append(l[x+2].split('>')[1].split('<')[0])
			if("Posição:" in l[x]):
				v = l[x+1].strip().split('&')[0].split('.')
				a.append(int(v[0]+v[1]))
			if("Resolvido:" in l[x]):
				a.append(l[x+1].split('<')[0].strip())
		a.append(p[2])
		print(a)
		alunos.append(a)
	except(EOFError):
		break
alunos.sort(key=lambda x: x[2])
with open('ranking.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Loc', 'Nome', 'Turma', 'URI', 'QR', 'Mentor'])
    for x in range(len(alunos)):
    	spamwriter.writerow([str(x+1)+'º']+alunos[x])
print("\nAnalise concluída.\n Arquivo: ranking.csv gerado com sucesso.\n")
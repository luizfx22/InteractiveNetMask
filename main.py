from utils.utils import getClass, getDefaultMask

ip = str(input("Digite o IP: "))

getClass(ip)

splittedIP = [_ for _ in ip.split('.')]

ipPrefix = ".".join(splittedIP[:3]) + '.'

mask = str(input("Digite a máscara desejada: "))

splittedMASK = [int(_) for _ in mask.split('.')]

splittedA = '.'.join("{0:<08b}".format(splittedMASK[3])).split('.')

bitT = 0
bitZ = 0
for bit in splittedA:
    if int(bit) == 1:
        bitT += 1
    else:
        bitZ += 1

numRedes = 2**bitT
numHost = (2**bitZ) - 2

redeEnds = []
broads = []
print()
print("Número de redes:", numRedes)
print("Número de hosts:", numHost)
print()

lastBroadcast = 0
redeAtual = 0

redes = []

for _ in range(numRedes):

    redeAtual = lastBroadcast + 1

    broadcastAtual = 1 + numHost + lastBroadcast

    lastBroadcast = broadcastAtual + 1

    print()
    print("Rede:", redeAtual - 1)
    print("Broadcast:", broadcastAtual)
    print()

    # print(endereco)

from utils.utils import getClass, getDefaultMask

ip = "192.168.0.0"
host = 50

splittedIP = [_ for _ in ip.split('.')]

mask = str(input("Digite a máscara desejada: "))

splittedMASK = [int(_) for _ in mask.split('.')]

splittedA = '.'.join("{0:<08b}".format(splittedMASK[3])).split('.')

print(splittedA)

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

print("Número de redes:", numRedes)
print("Número de hosts:", numHost)

lastBroad = 0

for _ in range(numRedes):
    if splittedIP[3] == str(0):
        ipTgds = ".".join(splittedIP)
        redeEnds.append(ipTgds)
    
    splittedIP_ = ip.split('.')
    splittedIP_.pop()

    brdcst = 1 + numRedes + lastBroad # Broadcast
    network = brdcst + 1
    lastBroad
    print(brdcst)

    splittedIP_.append(str())
    
    ipTgds = ".".join(splittedIP_)

    redeEnds.append(ipTgds)


# print("Endereços de rede:", redeEnds)
# print("Endereços de brds:", broads)

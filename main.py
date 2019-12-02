from utils.utils import getClass, getDefaultMask, getMaskFromSlash

ip = str(input("Digite o IP: "))                                                    # Usuário insere o ip
mask = str(input("Digite o barramento desejado: "))                                 # Usuário insere o barramento /24, /26, etc
slash = int(mask) if ("/" not in mask and "\\" not in mask) else int(mask[1:])      # Transforma o barramento em valor numérico

splittedIP = [_ for _ in ip.split('.')]
ipPrefix = ".".join(splittedIP[:int(slash / 8)]) + '.'  # Aqui foi necessário trocar porque o prefixo é relativo ao barramento. Deixando [:3] só funcionaria para classe C

numSubRedes = 2 ** (slash % 8)          # Ele pega o barramento e faz modulo de 8, ou seja, /9 % 8 = 1 portanto foi usado 1 bit para divisão de subrede, 2¹ = 2 subredes
numHost = 2 ** (32 - slash) - 2         # Pra calcular host é necessário tirar todos bits que são de rede (o barramento) e transformar o bit mais significativo na potência de 2
                                        # supondo que seja /9, então, 32 - 9 = 23, portanto, número de hosts é 2²³ ... quanto menor o barramento, maior o número de host e menor o número de redes

mask = getMaskFromSlash(slash)          # Funçãozinha que retorna o ip da máscara em decimal

print()
print("Número de sub redes:", numSubRedes)
print("Número de hosts por rede:", numHost)
print("Máscara: ", mask)
print()

netRange = 2 ** (8 - slash % 8)         # NetRange é o intervalo que cada rede terá ... Isso depende de quantos bits foram usados para subrede
                                        # se /9, ficaria assim: 11111111 100000000 0 ... Não estamos interessados no primeiro octeto, pois é só para rede
                                        # daí, então, devemos calcular quanto é 10000000 por isso faço 8 - 9 % 8, 9 % 8 = 1, 8 - 1 = 7, sete é valor do expoente

# Cada vez que rodar aqui temos um index = i. Ele é utilizado para saber onde começa a subrede atual
# suponto netRange = 64, então, a primeira rede é 64 * 0 = 0, a segunda é 64 * 1 = 64, etc
for i in range(numSubRedes):
    currentNetAddr = ipPrefix + str(netRange * i)
    currentBroadcastAddr = ipPrefix + str(netRange * i + netRange - 1)

    workingOnOctate = len(currentNetAddr.split("."))                        # Usado para adicionar os .0 ou .255 na quantidade correta relativo ao prefixo
        
    for _ in range(4 - workingOnOctate):
        currentNetAddr += ".0"
        currentBroadcastAddr += ".255"

    print()
    print("Rede:", currentNetAddr)
    print("Broadcast:", currentBroadcastAddr)
    print()
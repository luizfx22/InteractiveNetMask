
def getClass(ip):
    
    iplist = ip.split('.')

    classe = ""

    faixa = int(iplist[0])

    if any(int(i) >= 255 for i in iplist):
        raise ValueError(f"IP {ip} is an ivalid IP address")

    if 1 <= faixa <= 127:
        classe = "A"

    elif 127 <= faixa <= 191:
        classe = "B"

    elif 192 <= faixa <= 223:
        classe = "C"

    elif 224 <= faixa <= 239:
        classe = "D"

    elif 240 <= faixa <= 247:
        classe = "E"

    else:
        raise ValueError(f"IP {ip} is an ivalid IP address")
    
    return classe

def getMaskFromSlash(slash):
    mask = ""
    fullOctates = int(slash / 8)

    for _ in range(fullOctates):
        mask += "255."
    
    while(fullOctates < 4):
        bits = slash - 8 * fullOctates
        currentValue = 128
        result = 0

        for _ in range(bits):
            result += currentValue
            currentValue /= 2

        mask += str(int(result)) + "." if fullOctates < 3 else str(int(result))
        fullOctates += 1

    return mask

def getDefaultMask(ipclass):
    mask = ""
    if ipclass == "A":
        mask = "255.0.0.0"
    
    elif ipclass == "B":
        mask = "255.255.0.0"
    
    elif ipclass == "C":
        mask = "255.255.255.0"
    
    elif ipclass == "D":
        mask = "255.255.255.255"
    
    else:
        mask = "Invalid class!"
    
    return mask
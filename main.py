def son_anagramas(cadenaUno:str, cadenaDos:str) -> bool:
    cadenaUno_min=cadenaUno.lower()
    cadenaDos_min=cadenaDos.lower()
    
    temp_cadenaUno=[]
    for caracter in cadenaUno_min:
            if not caracter.isspace():
                temp_cadenaUno.append(caracter)
    cadenaUno="".join(temp_cadenaUno)

    temp_cadenaDos=[]
    for caracter in cadenaDos_min: 
        if not caracter.isspace():
            if not caracter.isspace():
                temp_cadenaDos.append(caracter)
    cadenaDos="".join(temp_cadenaDos)
    if len (cadenaUno) != len(cadenaDos):
        return False
    conteo={}
    for caracter in cadenaUno:
         conteo[caracter]=conteo.get(caracter,0)+1
         
soy_un_buleano=son_anagramas("Amor", "Roma")

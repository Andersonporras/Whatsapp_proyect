import pywhatkit

numecel= input("digite el numero de celular: +57")
mensaje= input("digite el mensaje")
hora= int(input("digite lahora :"))
minuto=int(input("digite el minuto :"))
tiempo_de_espera=int(input("digite el tiempo de espera"))
segundos_de_cierre=int(input("digite los segundos de cierre: "))

cerrar= input("Desea cerrar la pestaña ? (s/n)")

if cerrar=="s":
    pywhatkit.sendwhatmsg(numecel,mensaje,hora,minuto,tiempo_de_espera,True,segundos_de_cierre)
else:
    pywhatkit.sendwhatmsg(numecel,mensaje,hora,minuto,tiempo_de_espera,False,segundos_de_cierre)
import subprocess 


#Almaceno la salida de la consola de la ruta de perfiles de wlan, decodifico para print y la separo en \n en una lista
Data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")

#Almaceno separando por : iterando sobre la data de la linea de profiles
Wifis = [line.split(':')[1][1:-1] for line in Data if ("Perfil de todos los usuarios" or "All User Profiles") in line]

#itera sobre los wifis
for Wifi in Wifis:

    #Almaceno la salida de la consola de la ruta de perfil iterado con contraseña abierda, decodifica en cp850 por que el otro no da y los splitea
    Results = subprocess.check_output(["netsh" , "wlan" , "show" , "profile" , Wifi , "key=clear"]).decode("cp850").split("\n")
    
    
    Results = [line.split(':')[1][1:-1] for line in Results if ("Contenido de la clave" or "Key Content") in line]
    try:
        print(f"Nombre: {Wifi} Contraseña: {Results[0]} ")
    except IndexError:
        print(f"Nombre: {Wifi} Contraseña: No se pudo leer ")

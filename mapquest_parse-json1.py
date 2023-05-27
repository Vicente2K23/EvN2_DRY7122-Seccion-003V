import urllib.parse
import requests
import time

 

hora_actual = time.strftime("%H:%M:%S")  # Obtiene la hora actual en formato HH:MM:SS
mensaje_bienvenida = f"Bienvenido! La hora local es {hora_actual}."
print(mensaje_bienvenida)

 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "O7MjTcqHf89C0VccPJquKj2RU18VeZeO"

 

while True:

    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "m":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "m":
        break

   

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direccion desde " + (orig) + " Hacia " + (dest))
        print ("Duracion de viaje: "+ (json_data["route"]["formattedTime"]))
        print("Kilometros       " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")

 

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str ("{:.2f}".format((each["distance"])*1.61) + "km)"))
            print("=============================================")
import requests
if __name__ == '__main__':
    
    latitud = str(input("escriba una latitud: "))
    longitud = str(input("escriba una longitud: "))


    url = f"https://api.darksky.net/forecast/b53a0dfde5afd58b3f93e6f71e15371c/{latitud},{longitud}"
    response = requests.get(url)

    txt = open("data.txt","w")
 
    txt.write("Content-Type: " + str(response.headers["Content-Type"]))
     
    txt.write(" Content-Encoding: " + str(response.headers["Content-Encoding"]))

    txt.write(" Estado de la peticion: "+ str(response.status_code))

    if (response.status_code == 200):
        
        print(response.status_code)

        txt.write(" Respuesta "+ str(response.content))        
        
        print(response.content)


     


        
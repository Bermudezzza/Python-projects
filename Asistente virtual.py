import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
 

#Escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():
    
    #Almacenar recognizer en una variable
    r = sr.Recognizer()
    
    #Configurar el microfono 
    with sr.Microphone() as origen:
        
        #Tiempo de espera
        r.pause_threshold = 0.8
        
        #Informo que comenzo la grabacion
        print("Ya puedes hablar")
        
        #Guardar lo que se escucho
        audio = r.listen(origen)
        
        try:
            #Buscar en google lo que se escucho
            pedido = r.recognize_bing(audio, languaje ="es-ar")
            
            #Prueba de que pudo ingresar
            print("Dijiste: " + pedido)
            
            #Devolver pedido 
            return pedido
        
        #En caso de que no comprenda el audio
        except sr.UnknownValueError:
            
            #Prueba de que no comprendio el audio
            print("Ups, no entendi")
            
            #Devolver error
            return "Sigo esperando"
        
        #En caso de no resolver el pedido 
        except sr.RequestError:
            
            #Prueba de que no comprendio el audio
            print("Ups, no hay servicio")
            
            #Devolver error
            return "Sigo esperando"
        
        #Error inesperado
        except:
            #Prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")
            
            #Devolver error
            return "Sigo esperando"            
 
        
#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    
    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    
    #Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
 
 
#Informar el dia de la semana
def pedir_dia():
    
    #Crear la varibale con datos de hoy
    dia = datetime.date.today()
    print(dia)
    
    #Crear variable para dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    
    #Diccionario para los dias
    calendario = {0:"Lunes",
                  1:"Martes",
                  2:"Miércoles",
                  3:"Jueves",
                  4:"Viernes",
                  5:"Sábado",
                  6:"Domingo"}
    
    #Decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")
  
        
#Informar hora
def pedir_hora():   
    
    #Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute}"
    
    #Decir la hora 
    hablar(hora) 
    
    
#Funcion saludo inicial
def saludo_inicial():
    
    #Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else: 
        momento = "Buenas tardes"
        
    #Decir el saludo
    hablar(f"{momento} soy sigma, tu asistente personal. En que te puedo ayudar el dia de hoy")   
    
    
#Funcion central del asistente
def pedir_cosas():
    
    #Activar saludo inicial
    saludo_inicial()
    
    #Variable de corte para el loop
    comenzar = True
    
    #Loop central
    while comenzar:
        
        #Activar el microfono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        
        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo Yoytube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in pedido:
            hablar("Claro, estoy en eso")
            webbrowser.open("https://www.google.com.")
            continue
        elif "que día es hoy" in pedido:
            pedir_hora()
            continue
        elif "que día es hoy" in pedido:
            pedir_dia()
            continue
        elif "Busca en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace("Busca en Wikipedia", " ")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar("Wikipedia dice lo siguiente")
            hablar(resultado)
            continue
        elif "Busca en internet" in pedido:
            hablar("Buscando eso en internet")
            pedido = pedido.replace("Busca en internet", " ")
            pywhatkit.search("pedido")
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Buena idea, ya lo busco")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google":"GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontré, el precio es {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdón no la he encontrado")
                continue
        elif "adios" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break
        
pedir_cosas()

        
        
            
        
    
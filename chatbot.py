from tkinter import *
import random
import re
import time

def getResponse(entradaUsuario):
    split_message = re.split(r'\s|[,:;.?!-_*+]\s*',entradaUsuario.lower())
    respuesta = revisarMsjs(split_message)
    return respuesta


def probMensaje(msgUsuario, palReconocidas, respuestaSimple=False, palRequeridas=[]):
    message_certainty = 0
    has_required_words = True
    for word in msgUsuario:
        if word in palReconocidas:
            message_certainty += 1
    percentage = float(message_certainty / float(len(palReconocidas)))
    for word in palRequeridas:
        if word not in msgUsuario:
            has_required_words = False
            break
    if has_required_words or respuestaSimple:
        return int(percentage * 100)
    else:
        return 0


def send(event):
    salir = ["Salir", "Adios","Hasta luego","Terminar"]
    if(e.get() in salir):
        txt.insert(END, "\nBot => Hasta Luegooo...")
        time.sleep(3)        
        exit(-1)        
    else:
        send = "You => " + e.get()
        txt.insert(END,"\n" + send)   
        txt.insert(END,"\nBot => " + getResponse(e.get()))
        e.delete(0, END) 

def send2():
    salir = ["Salir", "Adios","Hasta luego","Terminar"]
    if(e.get() in salir):
        txt.insert(END, "\nBot => Hasta Luegooo...")
        time.sleep(3)        
        exit(-1)        
    else:
        send = "You => " + e.get()
        txt.insert(END,"\n" + send)   
        txt.insert(END,"\nBot => " + getResponse(e.get()))
        e.delete(0, END) 
   

def revisarMsjs(mensaje):
    highest_prob = {}

    def respuesta(respuestaBot, listaPalabras, respuestaSimple=False, palRequeridas=[]):
        nonlocal highest_prob
        highest_prob[respuestaBot] = probMensaje(mensaje, listaPalabras, respuestaSimple, palRequeridas)

    # Saludos y Despedida
    # 1
    respuesta(saludo(), ['hola','alo','saludos','wenas','buen','dia','ola'], respuestaSimple=True)
    # 2
    respuesta('Mi nombre es ' + nombreBot + ' y soy su asistente virtual dedicado a las artesan??as, m??s concretamente en las mexicanas. Puede hacerme cualquier pregunta sobre ellas.',['quien','eres','haces'], respuestaSimple=True)
    #3
    todoBien = ['Me encuentro bien y usted?','Hoy estoy bien','Podria estar mejor pero no me quejo','Todo bien por ac??'][random.randrange(4)]
    respuesta(todoBien, ['como','estas','te','va','vas','encuentras','sientes','todo','bien'], respuestaSimple=True)
    #4
    alegroBien = ['Me alegro que se encuentre bien','Que bueno!','Es bueno de escucharlo','Estupendo!'][random.randrange(4)]
    respuesta(alegroBien,['bien','me','gracias','siento'],respuestaSimple=True)
    #5
    alegroMal = ['Oh lamento escucharlo','Vendr??n mejores tiempos','Comase un snickers'][random.randrange(3)]
    respuesta(alegroMal,['siento','mal','me'],respuestaSimple=True)  
    #6
    respuesta('Me llamo '+ nombreBot , ['como','te','llamas','cual','es','tu','nombre'],palRequeridas=['llamas'])
    #7
    ayudaUsuario = ['Claro estoy a la orden','En que puedo ayudarle?','En que puedo servirle?','Hoy no, AAAAAAAh se crea, claro que si, en que lo apoyo'][random.randrange(4)]
    respuesta(ayudaUsuario, ['me','puedes','ayudar','ayudarme','apoyar','apoyarme'], respuestaSimple=True)

    # Preguntas De las Artesan??as
    #1. ??Que son las artesanias?
    respuesta('Las artesan??as mexicanas son resultado del trabajo de un artesano. Cada una es caracter??stica de cada regi??n',['que','es'], palRequeridas=['artesania'])
    #2. ??De que estan hechas las artesanias? 
    respuesta('Son elaboradas, regularmente, con materiales de origen natural como la madera, el barro, las telas, las semillas, piedras y metales',['de','que','estan','hechas','compuestas','elaborar'],palRequeridas=['hechas','artesanias'])
    #3. ??Que es un artesano?
    respuesta('Estas personas crean lo que son las artesanias, realizan su trabajo a mano o con distintos instrumentos.',['que','es','hace','artesano'],palRequeridas=['artesano'])
    #4. ??Me puedes dar un ejemplo de artesania?  
    respuesta('Claro, algunos ejemplos de artesanias pueden ser los sarapes, talaberas, alegr??as, rebozos, plater??a, juguetes entre otros',['ejemplo','artesania'],respuestaSimple=True)
    #5. ??Qu?? es una Talavera?
    respuesta('La talavera es un tipo de may??lica proveniente de los estados de Puebla y Tlaxcala',['que','es','talavera'], palRequeridas=['talavera'])
    #6. ??Que es may??lica?
    respuesta('Es el nombre que se la da desde la epoca del renacimiento a un tipo de decoraci??n cer??mica con un esmalte de plomo con esta??o en el cual se decoran',['que','es','mayolica'],palRequeridas=['mayolica'])
    #7.??De donde proviene la talavera?
    respuesta('La talavera proviene de los estados de Tlaxcala y Puebla',['de','donde','es','proviene','viene','talavera'],respuestaSimple=True)
    #8. ??Que es la plater??a?
    respuesta('Es el oficio donde se realizan todas las actividades relacionadas con el arte de trabajar la plata. Un dato interesante es que la plater??a mexicana es reconocida en todo el mundo!',['que','es','plateria'],palRequeridas=['plateria'])
    #9. ??De donde proviene la plateria?
    respuesta('La plateria se lleva a cabo en el estado de Guerrero, m??s en concreto en el municipio de Taxco',['de','donde','es','proviene','viene','plateria'],respuestaSimple=True)
    #10. ??Qu?? es un rebozo?
    respuesta('Un rebozo es una prenda de vestir, muy similar a un chal, usada en M??xico, Centroam??rica y algunas zonas de Am??rica del Sur.',['que','es','rebozo','reboso','rebozos','rebosos'], palRequeridas=['rebozo'])
    #11. ??De donde proviene el rebozo?
    respuesta('Los reobozos provienen de los municipios de Tenancingo en el Estado de M??xico y del municipio de Santa Mar??a del R??o en San Luis Potos??',['de','donde','es','proviene','provienen','viene','vienen','rebozo','reboso','rebozos','rebosos'], respuestaSimple=True)
    #12. ??Qu?? es un sarape?
    respuesta('El sarape o jorongo es una prenda ??nica, llena de pasi??n y cultura que ha acompa??ado a los mexicanos desde tiempos coloniales y ha sido utilizada por campesinos, hacendados, artesanos, charros, revolucionarios, generales e incluso artistas a lo largo de la historia.',['que','es','jorongo','zarape','sarape'], respuestaSimple=True)
    #13. ??De donde proviene el sarape?
    respuesta('El sarape proviene de Saltillo, Coahuila, aunque cada estado tiene su propio estilo, a veces cambiando la forma de elaboraci??n, el dise??o, etc.', ['de','donde','es','proviene','provienen','viene','vienen','sarape','zarape','jorongo'], respuestaSimple=True)
    #14. ??Qu?? es un ??rbol de la vida?
    respuesta('Son coloridas esculturas de barro que se elaboran tradicionalmente en las regiones monta??osas del centro de M??xico',['que','es','arbol','vida'], palRequeridas=['arbol','vida'])
    #15. ??De donde proviene el arbol de la vida?
    respuesta('El arbol de la vida proviene de Metepec, Estado de M??xico',['de','donde','es','proviene','provienen','viene','vienen','arbol','vida'], palRequeridas=['arbol','vida','donde'])
    #16. ??Qu?? es un alebrije?
    respuesta('Los alebrijes son seres imaginarios conformados por elementos fison??micos de animales diferentes, una combinaci??n de varios animales, no solo fant??sticos sino tambi??n reales que forman un ser fant??stico. Estos seres se representan como artesan??as fabricadas con cart??n o papel, y estructura de alambre, o con madera, que se pintan con colores mayormente alegres y vibrantes',['que','es','alebrije'],palRequeridas=['alebrije'])
    #17. ??De donde provienen los alebrijes?
    respuesta('Los alebrijes son originarios de la Ciudad de M??xico m??s concretamente del barrio de la Merced. Sin embargo, actualmente su elaboraci??n es m??s popular en el estado de Oaxaca',['de','donde','es','proviene','provienen','viene','vienen'],palRequeridas=['alebrije','donde'])
    #18. ??La guayabera es una artesan??a mexicana?
    respuesta('Por supuesto ya que son originarias de los estados de Veracruz y Yucat??n, esta prenda adem??s de c??moda, es un ejemplo de la dedicaci??n en la confecci??n de los artesanos de esas regiones',['la','es','artesania'],palRequeridas=['guayabera'])
    #19. ??Cu??les son los juguetes que se fabrican de forma artesanal?
    respuesta('Son varios, algunos ejemplos son el trompo, la pirinola, la matraca, el balero o la divertida loter??a, adem??s de coches y camiones de madera o un sinf??n de mu??ecas entre las que destacan las t??picas de trenzas y colores vivos',['cuales','son','juguetes','artesanal'],palRequeridas=['juguetes','fabrican'])
    #20 ??De que est??n hechos los sombreros de charro?
    respuesta('Los sombreros de charro son elaborados con piel de conejo, es necesaria una t??cnica de planchado precisa para lograr esa textura resistente. Posteriormente se borda a mano con uno o varios colores.',['de','que','estan','hechos','sombreros','sombreros'], palRequeridas=['sombrero'])
    #21 ??Que son las pi??atas?
    respuesta('Una pi??ata  es una olla de barro o de cart??n cubierta de papel mach??, adornada de papel de colores y usualmente con 7 picos, que en su interior contiene frutas, dulces u otros premios, dependiendo de la celebraci??n',['que','es','pi??ata','pi??atas'], palRequeridas=['pi??atas'])
    #22 ??Las pi??atas son artesan??as?
    respuesta('Claro, estas creaciones han sido elaboradas por artesanos desde tiempos de su abuelo o visabuelo. Su elaboraci??n es considerada artesanal ya que los maestros pi??ateros se han podido adaptar a los cambios en la cultura popular y ahora se pueden encontrar pi??atas con forma dibujos animados, de tendencias o incluso algunas sat??ricas',['pi??atas','son'], respuestaSimple=True)
    #23 ??Tu has estado en Oaxaca?
    respuesta('Claro que si, he visitado el centro de Oaxaca, incluso he ido al ??rbol del Tule. Es uno de los estados m??s ricos en cuanto a las artesan??as se refieren, adem??s de que la comida es exquisita.',['has','vistado','dices','oaxaca','estado','en','me'], respuestaSimple=True)
    #24 ??Que me dices de Puebla?
    respuesta('Claro, el centro de la ciudad de Puebla es uno de los m??s bonitos a lo largo de la rep??blica, adem??s de que ahi tambi??n se puede comer muy bien, solo que cuidado si lo visitas, dicen que la gente se tropieza con ciclovias xD',['has','vistado','dices','puebla','estado','en','me'], respuestaSimple=True)
    #25 ??Que son las hamacas?
    respuesta('Una hamaca es una lona o red constituida por bramante o cuerda fina que se fija a dos puntos firmes. Estos por lo regular se tratan de troncos de ??rboles. Es utilizada para dormir o descansar',['que','es'], palRequeridas=['hamaca'])
    best_match = max(highest_prob, key=highest_prob.get)

    # print(highest_prob)
    if highest_prob[best_match] < 1:
        return unknown(mensaje)
    else:
        return best_match
  
  
def unknown(message_db):
    respuesta = ['Puedes decirlo de nuevo?','No estoy seguro de lo que quieres', 'No tengo ese conocimiento a??n, lo siento :c','No te he entendido','Solo entiendo el espa??ol','Me lo puedes repetir porfavor?'][random.randrange(6)]

    with open('question_bank.txt', 'a') as file:
        file.write('B'+' '.join(message_db) + '\n')

    return respuesta


def saludo():
    respuesta = ['Hola','Buen dia','En que puedo ayudarlo','Bienvenido','Que bonito est?? el clima','??Que hay de nuevo?'][random.randrange(5)]
    return respuesta

if __name__ == '__main__':
    nombreBot = 'Bot'
    nombreUsuario = 'Usuario'
    inicio = 'Bienvenido a su asistente de Artesan??as Mexicanas'
    siQuiero = ["s","y","si"]
    root = Tk()
    root.resizable(False, False)
    txt = Text(root, bg='#85C1E9')   
    txt.insert(END,"**** " + inicio + " ****")
    txt.grid(row=1,column=1,columnspan=2)
    e = Entry(root, width=80, bg='#B3B6B7')
    e.focus()
    root.bind('<Return>', send)
    boton = Button(root,text="Enviar",command=send2, bg="#EC7063", fg="#FFF",font=('Helvetica', 12, 'bold')).grid(row=2,column=2, sticky="nswe")
  
    e.grid(row=2,column=1)   

    root.title("Chatbot Artesan??as Mexicanas")
    root.mainloop()
  
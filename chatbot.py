# Proyecto 1. ChatBot (Artesanias Mexicanas)
# Asigantura: Inteligencia Artificial
# Docente: Galindo Durán Cristal Karina
# Fecha: 08/Nov/2022
# Equipo 5: Machuca Dominguez Carlos Ivan,
#           Pasten Juarez Joshua Michel,
#           Rodriguez Palacios Osvaldo Leonel,
#           Colín Ramiro Joel

import random
import re

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

def revisarMsjs(mensaje):
    highest_prob = {}

    def respuesta(respuestaBot, listaPalabras, respuestaSimple=False, palRequeridas=[]):
        nonlocal highest_prob
        highest_prob[respuestaBot] = probMensaje(mensaje, listaPalabras, respuestaSimple, palRequeridas)

    # Saludos y Despedida
    # 1
    respuesta(saludo(), ['hola','alo','saludos','wenas','buen','dia','ola'], respuestaSimple=True)

    # 2
    respuesta('Mi nombre es ' + nombreBot + ' y soy su asistente virtual dedicado a las artesanías, más concretamente en las mexicanas. Puede hacerme cualquier pregunta sobre ellas.',['quien','eres','haces'], respuestaSimple=True)

    #3
    todoBien = ['Me encuentro bien y usted?','Hoy estoy bien','Podria estar mejor pero no me quejo','Todo bien por acá'][random.randrange(4)]
    respuesta(todoBien, ['como','estas','te','va','vas','encuentras','sientes','todo','bien'], respuestaSimple=True)

    #4
    alegroBien = ['Me alegro que se encuentre bien','Que bueno!','Es bueno de escucharlo','Estupendo!'][random.randrange(4)]
    respuesta(alegroBien,['bien','me','gracias','siento'],respuestaSimple=True)

    #5
    alegroMal = ['Oh lamento escucharlo','Vendrán mejores tiempos','Comase un snickers'][random.randrange(3)]
    respuesta(alegroMal,['siento','mal','me'],respuestaSimple=True)  

    #6
    respuesta('Me llamo '+ nombreBot , ['como','te','llamas','cual','es','tu','nombre'],palRequeridas=['llamas'])
   
    #7
    ayudaUsuario = ['Claro estoy a la orden','En que puedo ayudarle?','En que puedo servirle?','Hoy no, AAAAAAAh se crea, claro que si, en que lo apoyo'][random.randrange(4)]
    respuesta(ayudaUsuario, ['me','puedes','ayudar','ayudarme','apoyar','apoyarme'], respuestaSimple=True)

    # Preguntas De las Artesanías
    #1. ¿Que son las artesanias?
    respuesta('Las artesanías mexicanas son resultado del trabajo de un artesano. Cada una es característica de cada región',['que','es'], palRequeridas=['artesania'])

    #2. ¿De que estan hechas las artesanias? 
    respuesta('Son elaboradas, regularmente, con materiales de origen natural como la madera, el barro, las telas, las semillas, piedras y metales',['de','que','estan','hechas','compuestas','elaborar'],palRequeridas=['hechas','artesanias'])

    #3. ¿Que es un artesano?
    respuesta('Estas personas crean lo que son las artesanias, realizan su trabajo a mano o con distintos instrumentos.',['que','es','hace','artesano'],palRequeridas=['artesano'])

    #4. ¿Me puedes dar un ejemplo de artesania?  
    respuesta('Claro, algunos ejemplos de artesanias pueden ser los sarapes, talaberas, alegrías, rebozos, platería, juguetes entre otros',['ejemplo','artesania'],respuestaSimple=True)

    #5. ¿Qué es una Talavera?
    respuesta('La talavera es un tipo de mayólica proveniente de los estados de Puebla y Tlaxcala',['que','es','talavera'], palRequeridas=['talavera'])

    #6. ¿Que es mayólica?
    respuesta('Es el nombre que se la da desde la epoca del renacimiento a un tipo de decoración cerámica con un esmalte de plomo con estaño en el cual se decoran',['que','es','mayolica'],palRequeridas=['mayolica'])

    #7.¿De donde proviene la talavera?
    respuesta('La talavera proviene de los estados de Tlaxcala y Puebla',['de','donde','es','proviene','viene','talavera'],respuestaSimple=True)

    #8. ¿Que es la platería?
    respuesta('Es el oficio donde se realizan todas las actividades relacionadas con el arte de trabajar la plata. Un dato interesante es que la platería mexicana es reconocida en todo el mundo!',['que','es','plateria'],palRequeridas=['plateria'])

    #9. ¿De donde proviene la plateria?
    respuesta('La plateria se lleva a cabo en el estado de Guerrero, más en concreto en el municipio de Taxco',['de','donde','es','proviene','viene','plateria'],respuestaSimple=True)

    #10. ¿Qué es un rebozo?
    respuesta('Un rebozo es una prenda de vestir, muy similar a un chal, usada en México, Centroamérica y algunas zonas de América del Sur.',['que','es','rebozo','reboso','rebozos','rebosos'], palRequeridas=['rebozo'])

    #11. ¿De donde proviene el rebozo?
    respuesta('Los reobozos provienen de los municipios de Tenancingo en el Estado de México y del municipio de Santa María del Río en San Luis Potosí',['de','donde','es','proviene','provienen','viene','vienen','rebozo','reboso','rebozos','rebosos'], respuestaSimple=True)

    #12. ¿Qué es un sarape?
    respuesta('El sarape o jorongo es una prenda única, llena de pasión y cultura que ha acompañado a los mexicanos desde tiempos coloniales y ha sido utilizada por campesinos, hacendados, artesanos, charros, revolucionarios, generales e incluso artistas a lo largo de la historia.',['que','es','jorongo','zarape','sarape'], respuestaSimple=True)

    #13. ¿De donde proviene el sarape?
    respuesta('El sarape proviene de Saltillo, Coahuila, aunque cada estado tiene su propio estilo, a veces cambiando la forma de elaboración, el diseño, etc.', ['de','donde','es','proviene','provienen','viene','vienen','sarape','zarape','jorongo'], respuestaSimple=True)
    
    #14. ¿Qué es un árbol de la vida?
    respuesta('Son coloridas esculturas de barro que se elaboran tradicionalmente en las regiones montañosas del centro de México',['que','es','arbol','vida'], palRequeridas=['arbol','vida'])

    #15. ¿De donde proviene el arbol de la vida?
    respuesta('El arbol de la vida proviene de Metepec, Estado de México',['de','donde','es','proviene','provienen','viene','vienen','arbol','vida'], palRequeridas=['arbol','vida','donde'])

    #16. ¿Qué es un alebrije?
    respuesta('Los alebrijes son seres imaginarios conformados por elementos fisonómicos de animales diferentes, una combinación de varios animales, no solo fantásticos sino también reales que forman un ser fantástico. Estos seres se representan como artesanías fabricadas con cartón o papel, y estructura de alambre, o con madera, que se pintan con colores mayormente alegres y vibrantes',['que','es','alebrije'],palRequeridas=['alebrije'])

    #17. ¿De donde provienen los alebrijes?
    respuesta('Los alebrijes son originarios de la Ciudad de México más concretamente del barrio de la Merced. Sin embargo, actualmente su elaboración es más popular en el estado de Oaxaca',['de','donde','es','proviene','provienen','viene','vienen'],palRequeridas=['alebrije','donde'])

    #18. ¿La guayabera es una artesanía mexicana?
    respuesta('Por supuesto ya que son originarias de los estados de Veracruz y Yucatán, esta prenda además de cómoda, es un ejemplo de la dedicación en la confección de los artesanos de esas regiones',['la','es','artesania'],palRequeridas=['guayabera'])
    
    #19. ¿Cuáles son los juguetes que se fabrican de forma artesanal?
    respuesta('Son varios, algunos ejemplos son el trompo, la pirinola, la matraca, el balero o la divertida lotería, además de coches y camiones de madera o un sinfín de muñecas entre las que destacan las típicas de trenzas y colores vivos',['cuales','son','juguetes','artesanal'],palRequeridas=['juguetes','fabrican'])

    #20 ¿De que están hechos los sombreros de charro?
    respuesta('Los sombreros de charro son elaborados con piel de conejo, es necesaria una técnica de planchado precisa para lograr esa textura resistente. Posteriormente se borda a mano con uno o varios colores.',['de','que','estan','hechos','sombreros','sombreros'], palRequeridas=['sombrero'])

    #21 ¿Que son las piñatas?
    respuesta('Una piñata  es una olla de barro o de cartón cubierta de papel maché, adornada de papel de colores y usualmente con 7 picos, que en su interior contiene frutas, dulces u otros premios, dependiendo de la celebración',['que','es','piñata','piñatas'], palRequeridas=['piñatas'])

    #22 ¿Las piñatas son artesanías?
    respuesta('Claro, estas creaciones han sido elaboradas por artesanos desde tiempos de su abuelo o visabuelo. Su elaboración es considerada artesanal ya que los maestros piñateros se han podido adaptar a los cambios en la cultura popular y ahora se pueden encontrar piñatas con forma dibujos animados, de tendencias o incluso algunas satíricas',['piñatas','son'], respuestaSimple=True)

    #23 ¿Tu has estado en Oaxaca?
    respuesta('Claro que si, he visitado el centro de Oaxaca, incluso he ido al árbol del Tule. Es uno de los estados más ricos en cuanto a las artesanías se refieren, además de que la comida es exquisita.',['has','vistado','dices','oaxaca','estado','en','me'], respuestaSimple=True)

    #24 ¿Que me dices de Puebla?
    respuesta('Claro, el centro de la ciudad de Puebla es uno de los más bonitos a lo largo de la república, además de que ahi también se puede comer muy bien, solo que cuidado si lo visitas, dicen que la gente se tropieza con ciclovias xD',['has','vistado','dices','puebla','estado','en','me'], respuestaSimple=True)

    #25 ¿Que son las hamacas?
    respuesta('Una hamaca es una lona o red constituida por bramante o cuerda fina que se fija a dos puntos firmes. Estos por lo regular se tratan de troncos de árboles. Es utilizada para dormir o descansar',['que','es'], palRequeridas=['hamaca'])

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    if highest_prob[best_match] < 1:
        return unknown(mensaje)
    else:
        return best_match

def unknown(message_db):
    respuesta = ['Puedes decirlo de nuevo?','No estoy seguro de lo que quieres', 'No tengo ese conocimiento aún, lo siento :c','No te he entendido','Solo entiendo el español','Me lo puedes repetir porfavor?'][random.randrange(6)]

    with open('question_bank.txt', 'a') as file:
        file.write('B'+' '.join(message_db) + '\n')

    return respuesta

def saludo():
    respuesta = ['Hola','Buen dia','En que puedo ayudarlo','Bienvenido','Que bonito está el clima','¿Que hay de nuevo?'][random.randrange(5)]
    return respuesta


if __name__ == '__main__':
    nombreBot = 'Bot'
    nombreUsuario = 'Usuario'
    inicio = 'Bienvenido a su asistente de Artesanías Mexicanas'
    siQuiero = ["s","y","si"]
    
    print("**** " + inicio + " ****")
    opcion = input(nombreBot + ": " +'Mi nombre es ' + nombreBot + ', le gustaría decirme el suyo?').lower()

    if(opcion in siQuiero):
            nombreUsuario = input('Escriba su nombre: ')
            print(nombreBot + ': Bienvenido ' + nombreUsuario + "!!!")             
    else:
        print(nombreBot + ': Bien lo llamaré ' + nombreUsuario)        
                   
    while True:
        print(nombreBot + ": " + getResponse(input("\n" + nombreUsuario + ': ')))
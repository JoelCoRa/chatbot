
import random
import re

def getResponse(user_input):
    split_message = re.split(r'\s|[,:;.?!-_*+]\s*',user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty / float(len(recognized_words)))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Saludos y Despedida
    # 1
    response(saludo(), ['hola','alo','saludos','wenas','buen','dia'], single_response=True)

    # 2
    response('Mi nombre es ' + nombreBot + ' y soy su asistente virtual dedicado a las artesanías, más concretamente en las mexicanas. Puede hacerme cualquier pregunta sobre ellas.',['quien','eres','haces'], single_response=True)

    #3
    response('Me encuentro bien y usted?', ['como','estas','te','va','vas','encuentras','sientes'], single_response=True)

    #4
    response('Me alegro que se encuentre bien',['bien','me','gracias','siento'],required_words=['bien'])

    #5
    response('Oh lamento escucharlo, hay algo en lo que pueda apoyarle?',['siento','mal','me'],required_words=['mal'])  

    #6
    response('Me llamo '+ nombreBot , ['como','te','llamas','cual','es','tu','nombre'],required_words=['llamas'])
   
    #7
    response('Claro estoy a la orden', ['me','puedes','ayudar','ayudarme','apoyar','ayudarme'], single_response=True)

    #8
    response('Siempre a la orden. Si desea terminar la conversación presione Ctrl + C', ['gracias','te lo agradezco','tenkiu','thx','salir'], single_response=True)

    # Preguntas De las Artesanías
    #1. ¿Que son las artesanias?
    response('Las artesanías mexicanas son resultado del trabajo de un artesano. Cada una es característica de cada región',['que','es'], required_words=['artesania'])

    #2. ¿De que estan hechas las artesanias? 
    response('Son elaboradas, regularmente, con materiales de origen natural como la madera, el barro, las telas, las semillas, piedras y metales',['de','que','estan','hechas','compuestas','elaborar'],required_words=['hechas'])

    #3. ¿Que es un artesano?
    response('Estas personas crean lo que son las artesanias, realizan su trabajo a mano o con distintos instrumentos.',['que','es','hace'],required_words=['artesano'])

    #4. ¿Me puedes dar un ejemplo de artesania?  
    response('Claro, algunos ejemplos de artesanias pueden ser los sarapes, talaberas, alegrías, rebozos, platería, juguetes entre otros',['ejemplo','artesania'],required_words=['ejemplo'])

    #5. ¿Qué es una Talavera?
    response('La talavera es un tipo de mayólica proveniente de los estados de Puebla y Tlaxcala',['que','es'],required_words=['talavera'])

    #6. ¿Que es mayólica?
    response('Es el nombre que se la da desde la epoca del renacimiento a un tipo de decoración cerámica con un esmalte de plomo con estaño en el cual se decoran',['que','es'],required_words=['mayolica'])

    #7.¿De donde proviene la talavera?
    response('La talavera proviene de los estados de Tlaxcala y Puebla',['de','donde','es','proviene','viene'],required_words=['talavera'])

    #8. ¿Que es la platería?
    response('Es el oficio donde se realizan todas las actividades relacionadas con el arte de trabajar la plata. Un dato interesante es que la platería mexicana es reconocida en todo el mundo!',['que','es'],required_words=['plateria'])

    #9. ¿De donde proviene la plateria?
    response('La plateria se lleva a cabo en el estado de Guerrero, más en concreto en el municipio de Taxco',['de','donde','es','proviene','viene'],required_words=['plateria'])

    #10. ¿Qué es un rebozo?
    response('Un rebozo es una prenda de vestir, muy similar a un chal, usada en México, Centroamérica y algunas zonas de América del Sur.',['que','es','rebozo','reboso','rebozos','rebosos'], single_response=True)

    #11. ¿De donde proviene el rebozo?
    response('Los reobozos provienen de los municipios de Tenancingo en el Estado de México y del municipio de Santa María del Río en San Luis Potosí',['de','donde','es','proviene','provienen','viene','vienen','rebozo','reboso','rebozos','rebosos'], single_response=True)

    #12. ¿Qué es un sarape?
    response('El sarape o jorongo es una prenda única, llena de pasión y cultura que ha acompañado a los mexicanos desde tiempos coloniales y ha sido utilizada por campesinos, hacendados, artesanos, charros, revolucionarios, generales e incluso artistas a lo largo de la historia.',['que','es','jorongo','zarape','sarape'], single_response=True)

    #13. ¿De donde proviene el sarape?
    response('El sarape proviene de Saltillo, Coahuila, aunque cada estado tiene su propio estilo, a veces cambiando la forma de elaboración, el diseño, etc.', ['de','donde','es','proviene','provienen','viene','vienen'], required_words=['sarape','zarape','jorongo'])
    
    #14. ¿Qué es un árbol de la vida?
    response('Son coloridas esculturas de barro que se elaboran tradicionalmente en las regiones montañosas del centro de México',['que','es'],required_words=['arbol','vida'])

    #15. ¿De donde proviene el arbol de la vida?
    response('El arbol de la vida proviene de Metepec, Estado de México',['de','donde','es','proviene','provienen','viene','vienen'], required_words=['arbol','vida'])

    #16. ¿Qué es un alebrije?
    response('Los alebrijes son seres imaginarios conformados por elementos fisonómicos de animales diferentes, una combinación de varios animales, no solo fantásticos sino también reales que forman un ser fantástico. Estos seres se representan como artesanías fabricadas con cartón o papel, y estructura de alambre, o con madera, que se pintan con colores mayormente alegres y vibrantes',['que','es'],required_words=['alebrije'])

    #17. ¿De donde provienen los alebrijes?
    response('Los alebrijes son originarios de la Ciudad de México más concretamente del barrio de la Merced. Sin embargo, actualmente su elaboración es más popular en el estado de Oaxaca',['de','donde','es','proviene','provienen','viene','vienen'],required_words=['alebrije'])

    #18. ¿La guayabera es una artesanía mexicana?
    response('Por supuesto ya que son originarias de los estados de Veracruz y Yucatán, esta prenda además de cómoda, es un ejemplo de la dedicación en la confección de los artesanos de esas regiones',['la','es','artesania'],required_words=['guayabera'])
    
    #19. ¿Cuáles son los juguetes que se fabrican de forma artesanal?
    response('Son varios, algunos ejemplos son el trompo, la pirinola, la matraca, el balero o la divertida lotería, además de coches y camiones de madera o un sinfín de muñecas entre las que destacan las típicas de trenzas y colores vivos',['cuales','son','juguetes','artesanal'],required_words=['juguetes','fabrican'])

    #20 ¿De que están hechos los sombreros de charro?
    response('Los sombreros de charro son elaborados con piel de conejo, es necesaria una técnica de planchado precisa para lograr esa textura resistente. Posteriormente se borda a mano con uno o varios colores.',['de','que','estan','hechos','sombreros','sombreros'], single_response=True)

    #21 ¿Que son las piñatas?
    response('Una piñata  es una olla de barro o de cartón cubierta de papel maché, adornada de papel de colores y usualmente con 7 picos, que en su interior contiene frutas, dulces u otros premios, dependiendo de la celebración',['que','es','piñata','piñatas'], single_response=True)

    #22 ¿Las piñatas son artesanías?
    response('Claro, estas creaciones han sido elaboradas por artesanos desde tiempos de su abuelo o visabuelo. Su elaboración es considerada artesanal ya que los maestros piñateros se han podido adaptar a los cambios en la cultura popular y ahora se pueden encontrar piñatas con forma dibujos animados, de tendencias o incluso algunas satíricas',['piñatas','son'], single_response=True)

    #23 ¿Tu has estado en Oaxaca?
    response('Claro que si, he visitado el centro de Oaxaca, incluso he ido al árbol del Tule. Es uno de los estados más ricos en cuanto a las artesanías se refieren, además de que la comida es exquisita.',['has','vistado','dices','oaxaca','estado','en','me'], single_response=True)

    #24 ¿Que me dices de Puebla?
    response('Claro, el centro de la ciudad de Puebla es uno de los más bonitos a lo largo de la república, además de que ahi también se puede comer muy bien, solo que cuidado si lo visitas, dicen que la gente se tropieza con ciclovias xD',['has','vistado','dices','puebla','estado','en','me'], single_response=True)

    #25 ¿Que son las hamacas?
    response('Una hamaca es una lona o red constituida por bramante o cuerda fina que se fija a dos puntos firmes. Estos por lo regular se tratan de troncos de árboles. Es utilizada para dormir o descansar',['que','es'], required_words=['hamaca'])

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    if highest_prob[best_match] < 1:
        return unknown(message)
    else:
        return best_match

def unknown(message_db):
    response = ['Puedes decirlo de nuevo?','No estoy seguro de lo que quieres', 'No tengo ese conocimiento aún, lo siento :c','No te he entendido','Solo entiendo el español','Me lo puedes repetir porfavor?'][random.randrange(6)]

    with open('question_bank.txt', 'a') as file:
        file.write('B'+' '.join(message_db) + '\n')

    return response

def saludo():
    response = ['Hola','Buen dia','En que puedo ayudarlo','Bienvenido','Que bonito está el clima','¿Que hay de nuevo?'][random.randrange(5)]
    return response


if __name__ == '__main__':
    nombreBot = 'Bot'
    nombreUsuario = 'Usuario'
    inicio = 'Bienvenido a su asistente de Artesanías   Mexicanas'
    siQuiero = ["s","y","si"]
    
    print(nombreBot + ": " + inicio)
    opcion = input(nombreBot + ": " +'Mi nombre es ' + nombreBot + ', le gustaría decirme el suyo?').lower()

    if(opcion in siQuiero):
        nombreUsuario = input('Escriba su nombre: ')
        print(nombreBot + ': Bienvenido ' + nombreUsuario + "!!!")
    else:
        print(nombreBot + ': Bien lo llamaré ' + nombreUsuario)
               
    while True:
        print(nombreBot + ": " + getResponse(input("\n" + nombreUsuario + ': ')))
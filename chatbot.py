
import random
import re

def getResponse(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*',user_input.lower())
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
    response('Hola', ['hola','alo','saludos','wenas'], single_response=True)
    response('Estoy bien y tu?', ['como','estas','te','va','vas','encuentras','sientes'], required_words=['como'])
    # response('Estamos ubicados en la calle 23 no.123', ['ubicados','direccion','donde','ubicacion'], single_response=True)
    response('Siempre a la orden', ['gracias','te lo agradezco','tenkiu','thx'], single_response=True)


    #1. ¿Que son las artesanias?
    response('Las artesanías mexicanas son resultado del trabajo de un artesano. Cada una es característica de cada región','Que es una artesania mexicana',['que','es','una','artesania','mexicana'], required_words=['que','es','artesania'])

    #2. ¿De que estan hechas las artesanias? 
    response('Son elaboradas, regularmente, con materiales de origen natural como la madera, el barro, las telas, las semillas, piedras y metales',['de','que','estan','hechas','compuestas','elaborar'],required_words=['hechas'])

    #3. ¿Que es un artesano?
    response('Estas personas crean lo que son las artesnias, realizan su trabajo a mano o con distintos instrumentos.',['que','es','hace'],required_words=['artesano'])

    #4. ¿Me puedes dar un ejemplo de artesania?  
    response('Claro, algunos ejemplos de artesanias pueden ser los sarapes, talaberas, alegrías, rebozos, platería, juguetes entre otros',['ejemplo','artesania'],required_words=['ejemplo'])

    #5. ¿Qué es una Talavera?
    response('La talavera es un tipo de mayólica proveniente de los estados de Puebla y Tlaxcala',['que','es'],required_words=['talavera'])
    # 5.1 ¿Que es mayólica?
    response('Es el nombre que se la da desde la epoca del renacimiento a un tipo de decoración cerámica con un esmalte de plomo con estaño en el cual se decoran',['que','es'],required_words=['mayolica'])
    #5.2 ¿De donde proviene la talavera?
    response('La talavera proviene de los estados de Tlaxcala y Puebla',['de','donde','es','proviene','viene'],required_words=['talavera'])

    #6. ¿Que es la platería?
    response('Es el oficio donde se realizan todas las actividades relacionadas con el arte de trabajar la plata. Un dato interesante es que la platería mexicana es reconocida en todo el mundo!',['que','es'],required_words=['plateria'])
    #6.2 ¿De donde proviene la plateria?
    response('La plateria se lleva a cabo en el estado de Guerrero, más en concreto en el municipio de Taxco',['de','donde','es','proviene','viene'],required_words=['plateria'])

    #7. ¿Qué es un rebozo?
    response('Un rebozo es una prenda de vestir, muy similar a un chal, usada en México, Centroamérica y algunas zonas de América del Sur.',['que','es'],required_words=['rebozo'])
    #7.2 ¿De donde proviene el rebozo?
    response('Los reobozos provienen de los municipios de Tenancingo en el Estado de México y del municipio de Santa María del Río en San Luis Potosí',['de','donde','es','proviene','provienen','viene','vienen'], required_words= ['rebozo','reboso','rebozos','rebosos'])


    #8. ¿Qué es un sarape?
    response('El sarape o jorongo es una prenda única, llena de pasión y cultura que ha acompañado a los mexicanos desde tiempos coloniales y ha sido utilizada por campesinos, hacendados, artesanos, charros, revolucionarios, generales e incluso artistas a lo largo de la historia.',['que','es'],required_words=['sarape','zarape','jorongo'])
    #8.2 ¿De donde proviene el sarape?
    response('El sarape proviene de Saltillo, Coahuila, aunque cada estado tiene su propio estilo, a veces cambiando la forma de elaboración, el diseño, etc.', ['de','donde','es','proviene','provienen','viene','vienen'], required_words=['sarape','zarape','jorongo'])
    
    #9. ¿Qué es un árbol de la vida?
    response('Son coloridas esculturas de barro que se elaboran tradicionalmente en las regiones montañosas del centro de México',['que','es'],required_words=['arbol','vida'])
    #9.2 ¿De donde proviene el arbol de la vida?
    response('El arbol de la vida proviene de Metepec, Estado de México',['de','donde','es','proviene','provienen','viene','vienen'], required_words=['arbol','vida'])

    #10. ¿Qué es un alebrije?
    response('Los alebrijes son seres imaginarios conformados por elementos fisonómicos de animales diferentes, una combinación de varios animales, no solo fantásticos sino también reales que forman un ser fantástico. Estos seres se representan como artesanías fabricadas con cartón o papel, y estructura de alambre, o con madera, que se pintan con colores mayormente alegres y vibrantes',['que','es'],required_words=['alebrije'])
    #8.2 ¿De donde provienen los alebrijes?
    response('Los alebrijes son originarios de la Ciudad de México más concretamente del barrio de la Merced. Sin embargo, actualmente su elaboración es más popular en el estado de Oaxaca',['de','donde','es','proviene','provienen','viene','vienen'],required_words=['alebrije'])

    #11. ¿La guayabera es una artesanía mexicana?
    response('Por supuesto ya que son originarias de los estados de Veracruz y Yucatán, esta prenda además de cómoda, es un ejemplo de la dedicación en la confección de los artesanos de esas regiones',['la','es','artesania'],required_words=['guayabera'])
    
    #12. ¿Cuáles son los juguetes que se fabrican de forma artesanal?
    response('Son varios, algunos ejemplos son el trompo, la pirinola, la matraca, el balero o la divertida lotería, además de coches y camiones de madera o un sinfín de muñecas entre las que destacan las típicas de trenzas y colores vivos',['cuales','son','juguetes','artesanal'],required_words=['juguetes','fabrican'])
    #13. ¿Que regiones de México, realizan estas obras?




    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    if highest_prob[best_match] < 1:
        return unknown()
    else:
        return best_match

def unknown():
    response = ['puedes decirlo de nuevo?','No estoy seguro de lo que quieres', 'buscalo en google a ver que tal xd'][random.randrange(3)]
    return response



if __name__ == '__main__':
    while True:
        print("Bot: " + getResponse(input('You: ')))
from nltk.corpus import stopwords
import numpy as np
import nltk
import random
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')

palabras_stop = stopwords.words('spanish');

puntuaciones = [',', '.', '!', '?', ';', '-', '..', '...', '....']

palabras_negativas = [
'Abanto', 'Abrazafarolas', 'Adufe', 'Alcornoque', 'Alfeñique', 'Andurriasmo', 'Arrastracueros', 'Artabán',
'Artaban', 'Atarbán', 'Atarban', 'Atarre', 'Baboso', 'Barrabás', 'Barriobajero', 'Bebecharcos', 'Bellaco',
'Belloto', 'Berzotas', 'Besugo', 'Bobalicón', 'Bocabuzón', 'Bocachancla', 'Bocallanta', 'Boquimuelle',
'Borrico', 'Botarate', 'Brasas', 'Cabestro', 'Cabezaalberca', 'Cabezabuque', 'Cachibache', 
'Cafre', 'Cagalindes', 'Cagarruta', 'Calambuco', 'Calamidad', 'Caldúo', 'Calientahielos', 'Calzamonas', 'Cansalmas', 
'Cantamañanas', 'Capullo', 'Caracaballo', 'Caracartón', 'Caraculo', 'Caraflema', 'Carajaula', 'Carajote', 'Carapapa', 'Carapijo', 
'Cazurro', 'Cebollino', 'Cenizo', 'Cenutrio', 'Ceporro', 'Cernícalo', 'Charrán', 'Chiquilicuatre', 'Chirimbaina', 'Chupacables', 'Chupasangre', 
'Chupóptero', 'Cierrabares', 'Cipote', 'Comebolsas', 'Comechapas', 'Comeflores', 'Comestacas', 'Cretino', 'Cuerpoescombro', 'Culopollo', 
'Descerebrado', 'Desgarracalzas', 'Dondiego', 'Donnadie', 'Echacantos', 'Ejarramantas', 'Energúmeno', 'Esbaratabailes', 'Escolimoso', 
'Escornacabras', 'Estulto', 'Fanfosquero', 'Fantoche', 'Fariseo', 'Filimincias', 'Foligoso', 'Fulastre', 'Ganapán', 'Ganapio', 'Gandúl', 
'Gañán', 'Gaznápiro', 'Gilipuertas', 'Giraesquinas', 'Gorrino', 'Gorrumino', 'Guitarro', 'Gurriato', 'Habahelá', 'Huelegateras', 'Huevón', 
'Lamecharcos', 'Lameculos', 'Lameplatos', 'Lechuguino', 'Lerdo', 'Letrín', 'Lloramigas', 'Longanizas', 'Lumbreras', 'Maganto', 'Majadero', 
'Malasangre', 'Malasombra', 'Malparido', 'Mameluco', 'Mamporrero', 'Manegueta', 'Mangarrán', 'Mangurrián', 'Mastuerzo', 'Matacandiles', 
'Meapilas', 'Melón', 'Mendrugo', 'Mentecato', 'Mequetrefe', 'Merluzo', 'Metemuertos', 'Metijaco', 'Mindundi', 'Morlaco', 'Morroestufa', 
'Muerdesartenes', 'Orate', 'Ovejo', 'Pagafantas', 'Palurdo', 'Pamplinas', 'Panarra', 'Panoli', 'Papafrita', 'Papanatas', 'Papirote', 'Paquete', 
'Pardillo', 'Parguela', 'Pasmarote', 'Pasmasuegras', 'Pataliebre', 'Patán', 'Pavitonto', 'Pazguato', 'Pecholata', 'Pedorro', 'Peinabombillas', 
'Peinaovejas', 'Pelagallos', 'Pelagambas', 'Pelagatos', 'Pelatigres', 'Pelazarzas', 'Pelmazo', 'Pelele', 'Pelma', 'Percebe', 'Perrocostra', 
'Perroflauta', 'Peterete', 'Petimetre', 'Picapleitos', 'Pichabrava', 'Pillavispas', 'Piltrafa', 'Pinchauvas', 'Pintamonas', 'Piojoso', 
'Pitañoso', 'Pitofloro', 'Plomo', 'Pocasluces', 'Pollopera', 'Quitahipos', 'Rastrapajo', 'Rebañasandías', 'Revientabaules', 'Ríeleches', 
'Robaperas', 'Sabandija', 'Sacamuelas', 'Sanguijuela', 'Sinentraero', 'Sinsustancia', 'Sonajas', 'Sonso', 'Soplagaitas', 'Soplaguindas', 
'Sosco', 'Tagarote', 'Tarado', 'Tarugo', 'Tiralevitas', 'Tocapelotas', 'Tocho', 'Tolai', 'Tontaco', 'Tontucio', 'Tordo', 'Tragaldabas', 
'Tuercebotas', 'Tunante', 'Zamacuco', 'Zambombo', 'Zampabollos', 'Zamugo', 'Zángano', 'Zarrapastroso', 'Zascandil', 'Zopenco', 'Zoquete',
'Zote', 'Zullenco', 'Zurcefrenillos', 'No', 'cobarde', 'tibio', 'mk', 'wuevon', 'wvon', 'hvon', 'marica', 'maricon', 'estupido', 'estupida',
'culebrero', 'jibaro', 'quitarnosla', 'quitar', 'amenaza', 'terrorista', 'guerrillas', 'disparate', 'hampon', 'narcoterrorista',
'siniestra', 'grotesca', 'malvada', 'malvado', 'pobreza', 'tirania', 'ruina', 'oscuridad', 'sapos', 'monopolio', 'dañar',
'grave', 'mal', 'conflicto', 'revictimizante', 'agredidas', 'hp', 'envidia', 'hpta', 'nervioso', 'preocupado', 'derrota', 'falsos',
'malo', 'tonta', 'tonto', 'hijueputa', 'bufón', 'bufon', 'chatarra', 'matar', 'malos', 'vicioso', 'narcotraficante', 'violencia', 'mentir',
'titere', 'caga', 'narco', 'payasín', 'susto', 'robar', 'criminales', 'mentira', 'corrupto', 'paramilitar', 'culo', 'prepago', 'uribestia',
'resentida', 'rogados', 'inhabilitado', 'golpes', 'traquetos', 'ilegal', 'panico', 'mafias', 'violando', 'violación', 'violacion', 'ignorante',
'chismoso', 'complice', 'chimbo', 'pendejadas', 'fracasado', 'fracasada', 'enfermedad', 'muerte', 'narcotráfico', 'asesinos', 'destrucción',
'hambre', 'mierda', 'mrd', 'bobo', 'pobres', 'felices', 'secuestros', 'secuestro', 'desaparecidos', 'insoportables', 'insoportable', 'pésimo', 'pesimo',
'populista', 'payaso', 'enemigo', 'hipocrita', 'hipócrita', 'bruto', 'bobos', 'paraco', 'paracos', 'bandido', 'perdedor', 'desafortunadamente',
'contaminaron', 'lastima', 'insultar', 'incongruente', 'maltrato', 'terror', 'delincuencia', 'delincuente', 'loco', 'loca', 'descaro', 'descarada',
'descarado', 'empeoro', 'empeorar', 'empeorando', 'subdito', 'subditos', 'mala', 'nada', 'putas', 'puta', 'estupidos', 'estúpidos',
'lagarto', 'lagartear'
]

palabras_positivas = [
'abrazo', 'admirable', 'agraciado', 'agradable', 'agradecido', 'amigo', 'amistad', 'amor', 'apasionado', 
'aprecio', 'aprobacion', 'aprobación', 'apropiado', 'bella', 'bello', 'bendecido', 'beso', 'bien', 'bonita', 'bonito', 
'calificado', 'calma', 'capacitado', 'cariñoso', 'carisma', 'celebracion', 'celebración', 'compasion', 'compasión', 
'comprensivo', 'confiable', 'conveniente', 'curioso', 'decente', 'delicada', 'delicado', 'destreza', 'dichoso', 'digno', 
'dios', 'disciplina', 'divina', 'divino', 'dulce', 'dulzura', 'educada', 'educado', 'efectiva', 'efectivo', 'eficaz', 'eficiente', 
'efusiva', 'efusivo', 'ejemplar', 'elegancia', 'elegante', 'elocuente', 'emocionada', 'emocionado', 'empatia', 'empatico', 'empatico', 
'empatizar', 'enamorada', 'enamorado', 'encantada', 'encantado', 'energetica', 'energetico', 'equitativa', 'equitativo', 'especial', 
'espectacular', 'esperanza', 'espiritu', 'estelar', 'estimulante', 'excelente', 'excelentes', 'excepcional', 'exito', 'exitosa', 'exitoso', 'fabuloso', 
'facil', 'facilidad', 'factible', 'familia', 'fantastico', 'fascinante', 'felicitar', 'felicito', 'feliz', 'fortaleza', 'futuro', 'ganador', 'generosa', 
'generoso', 'genial', 'gracia', 'gracias', 'gratitud', 'hermosa', 'hermoso', 'ideal', 'idolatrar', 'imparcial', 'impresionante', 
'incondicional', 'inolvidable', 'integral', 'inteligencia', 'inteligente', 'intrigante', 'joven', 'juicioso', 'justa', 'justo', 
'juventud', 'leal', 'lealtad', 'legal', 'legendario', 'lider', 'madurez', 'magico', 'magnifica', 'magnifico', 'maravilloso', 
'memorable', 'merecedor', 'meticuloso', 'milagro', 'modesta', 'modesto', 'monumental', 'notable', 'oportunidad', 'optima', 
'optimismo', 'optimista', 'optimo', 'orden', 'ordenada', 'ordenado', 'orgullo', 'orgulloso', 'ostentoso', 'placer', 'positivo', 
'querido', 'querida', 'sabiduria', 'sabio', 'sabroso', 'salud', 'saludable', 'salvacion', 'salvación', 'santa', 'santo', 'satisfecha', 
'satisfecho', 'sencilla', 'sencillo', 'sensacional', 'serena', 'serenidad', 'sereno', 'si', 'sí', 'sinceramente', 'sincero', 
'sincero', 'solidaria', 'solidario', 'solucion', 'solución', 'sonrisa', 'sorprendente', 'sostenible', 'super', 'talento', 'talentosa', 
'talentoso', 'tesoro', 'tolerancia', 'tolerante', 'trabajador', 'trabajadora', 'triunfal', 'triunfo', 'trofeo', 'unidad', 'util', 'útil', 
'valentia', 'valentía', 'valiente', 'valioso', 'valor', 'ventaja', 'vigor', 'visionario', 'virtuoso', 'virtud', 'vigorizante', 'victorioso', 
'vivaz', 'afinidad', 'vida', 'amo', 'fuerza', 'fortaleza', 'dignidad', 'bendición', 'unidos', 'apoyo', 'sueño', 'anhelado', 'mejor', 'inclusión',
'inclusion', 'sana', 'salud', 'salva', 'correctos', 'correcto', 'animo', 'bueno', 'conviccion', 'convicción', 'merecemos', 'transparente', 'quiero',
'humildad', 'inteligencia', 'amas', 'honestidad', 'sensata', 'encanta', 'buena', 'buenas', 'gran', 'dedicacion', 'dedicación'
]

def get_tweet_with_sentiment_pos(input):
    tweetTokens = nltk.word_tokenize(input, "spanish");
    cleanedTweet = [];
    for word in tweetTokens:
        if len(word) == 1:
            continue;
        if word.lower() in palabras_stop:
            continue;
        if word.lower() in puntuaciones:
            continue;
        if word.lower() in (string.lower() for string in palabras_positivas):
            cleanedTweet.append(word);
            cleanedTweet.append('POS');
            continue;
        if word.lower() in (string.lower() for string in palabras_negativas):
            cleanedTweet.append(word);
            cleanedTweet.append('NEG');
            continue;
        cleanedTweet.append(word);
        cleanedTweet.append('NET')
    return cleanedTweet;


def create_word_embedding( phrases, add_pos_tags = False ):
    count = 0
    word_embedding = {} 
    encoded_phrases = []

    for phrase in phrases:
        cleanPhrase = [phrase]

        if add_pos_tags:
            cleanPhrase = get_tweet_with_sentiment_pos(phrase);

        encoded_phrase = []
        for word in cleanPhrase:
            if word not in word_embedding:
                word_embedding[word] = count
                count += 1
            encoded_phrase.append(word_embedding[word])
        encoded_phrases.append(encoded_phrase)
    return encoded_phrases


def load_encoded_data( data_split = 0.8 ):
    data = pd.read_csv('./training.csv')
    classified_tweets = data.values.tolist()
    random.shuffle(classified_tweets)

    tweets, categories = [], []
    for tweet, category in classified_tweets:
        tweets.append(tweet)
        categories.append(category)
        print(tweet)
        print(category)
    
    # Word + Punctuation + POS Tags embedding
    encoded_comments = create_word_embedding(tweets, add_pos_tags = True)

    # Word embedding, ensure you don't add the POS tags
    encoded_categories = create_word_embedding(categories, add_pos_tags = False)

    # Determine the training sample split point
    training_sample = int(len(encoded_comments) * data_split)

    # Split the dataset into training vs testing datasets
    x_train = np.array(encoded_comments[:training_sample], dtype=object)
    x_test = np.array(encoded_comments[training_sample:], dtype=object)
    y_train = np.array(encoded_categories[:training_sample], dtype=object)
    y_test = np.array(encoded_categories[training_sample:], dtype=object)
    return x_train, x_test, y_train, y_test

def parseInputs(inputs):
    encoded_input = create_word_embedding(inputs, add_pos_tags = True)
    return np.array(encoded_input, dtype=object)
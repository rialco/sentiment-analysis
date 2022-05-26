import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

palabras_stop = stopwords.words('spanish')

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
    'hambre', 'mierda', 'mrd', 'bobo', 'pobres', 'secuestros', 'secuestro', 'desaparecidos', 'insoportables', 'insoportable', 'pésimo', 'pesimo',
    'populista', 'payaso', 'enemigo', 'hipocrita', 'hipócrita', 'bruto', 'bobos', 'paraco', 'paracos', 'bandido', 'perdedor', 'desafortunadamente',
    'contaminaron', 'lastima', 'insultar', 'incongruente', 'maltrato', 'terror', 'delincuencia', 'delincuente', 'loco', 'loca', 'descaro', 'descarada',
    'descarado', 'empeoro', 'empeorar', 'empeorando', 'subdito', 'subditos', 'mala', 'nada', 'putas', 'puta', 'estupidos', 'estúpidos',
    'lagarto', 'lagartear', 'bandidos', 'obsesión', 'obsesion', 'narcotraficantes', 'destruido', 'destruir', 'charlatanes', 'ratas',
    'undir', 'daño', 'dano', 'pesimas', 'pesimos', 'costosa', 'estafa', 'prepagos', 'golpe', 'atarbanes', 'arcaico', 'monda', 'verga', 'huevo', 'huevon',
    'gonorrea', 'chimba', 'perra', 'peor', 'desgraciado', 'desgraciada', 'desgracia', 'desagradable', 'basura', 'pirobo', 'piroba',
    'torcido', 'ladrones', 'ladron', 'vulgar', 'patan', 'hipócrita', 'falso', 'desleal', 'farsa', 'engañar', 'engaño', 'guerrillera', 'guerrilleras',
    'hjpta', 'qlo', 'descabezado', 'curtido', 'deslealtad', 'demencia', 'demente', 'vergüenza', 'miedo', 'desesperados', 'desesperado', 'sinvergüenza',
    'matarife', 'insultando', 'insulto', 'desprecio', 'desprecia', 'irresponsable', 'violento', 'diablo', 'derrotar', 'berrinche', 'ni',
    'error', 'marik', 'nefasto', 'guatepeor', 'peligroso', 'peligrosa', 'quemado', 'quemada', 'cacas', 'desempleo', 'desempleado', 'desempleada',
    'guerra', 'sucia', 'sarnoso', 'sarnosa', 'sucio', 'ofenden', 'ofender', 'secta', 'espantosa', 'espantoso', 'ñero', 'ñera',
    'cizaña', 'bruta', 'mafia', 'mafioso', 'mafiosa', 'perdedora', 'castigó', 'castigo', 'destruyó', 'destruyo', 'parapolitica', 'desmadre', 'desmedro',
    'joden', 'patetico', 'problema', 'mentiras', 'persecución', 'atracadores', 'atracador', 'politiquera', 'cinismo', 'cinico', 'cinica',
    'horrible', 'odio', 'armas', 'dictadores', 'fantasma', 'desinformación', 'babosa', 'falsa', 'fake', 'picardías', 'vándalos', 'vandalos', 'misera',
    'misero', 'miserable', 'miseria', 'saqueo', 'sandeces', 'crisis', 'inaceptable', 'inaudito', 'deplorables', 'atropellos', 'asustados',
    'porquerías', 'porquerias', 'adoctrinamiento', 'sangre', 'cagarse', 'chamfle', 'calaña', 'caros', 'culebreros', 'ignorantes',
    'flojo', 'verguenza', 'expropiar', 'fiasco', 'dictadura', 'matado', 'emputada'
]

palabras_positivas = [
    'abrazo', 'admirable', 'agraciado', 'agradable', 'agradecido', 'amigo', 'amistad', 'amor', 'apasionado',
    'aprecio', 'aprobacion', 'aprobación', 'apropiado', 'bella', 'bello', 'bendecido', 'beso', 'bien', 'bonita', 'bonito',
    'calificado', 'calma', 'capacitado', 'cariñoso', 'carisma', 'celebracion', 'celebración', 'compasion', 'compasión',
    'comprensivo', 'confiable', 'conveniente', 'curioso', 'decente', 'delicada', 'delicado', 'destreza', 'dichoso', 'digno',
    'dios', 'disciplina', 'divina', 'divino', 'dulce', 'dulzura', 'educada', 'educado', 'efectiva', 'efectivo', 'eficaz', 'eficiente',
    'efusiva', 'efusivo', 'ejemplar', 'elegancia', 'elegante', 'elocuente', 'emocionada', 'emocionado', 'empatia', 'empatico', 'empatica',
    'empatizar', 'enamorada', 'enamorado', 'encantada', 'encantado', 'energetica', 'energetico', 'equitativa', 'equitativo', 'especial',
    'espectacular', 'esperanza', 'espiritu', 'estelar', 'estimulante', 'excelente', 'excelentes', 'excepcional', 'exito', 'exitosa', 'exitoso', 'fabuloso',
    'facil', 'facilidad', 'factible', 'familia', 'fantastico', 'fascinante', 'felicitar', 'felicito', 'feliz', 'fortaleza', 'futuro', 'ganador', 'generosa',
    'generoso', 'genial', 'gracia', 'gracias', 'gratitud', 'hermosa', 'hermoso', 'ideal', 'idolatrar', 'imparcial', 'impresionante',
    'incondicional', 'inolvidable', 'integral', 'inteligencia', 'inteligente', 'intrigante', 'joven', 'juicioso', 'justa', 'justo',
    'juventud', 'leal', 'lealtad', 'legal', 'legendario', 'lider', 'madurez', 'magico', 'magnifica', 'magnifico', 'maravilloso',
    'memorable', 'merecedor', 'meticuloso', 'milagro', 'modesta', 'modesto', 'monumental', 'notable', 'oportunidad', 'optima',
    'optimismo', 'optimista', 'optimo', 'orden', 'ordenada', 'ordenado', 'orgullo', 'orgulloso', 'ostentoso', 'placer', 'positivo',
    'querido', 'querida', 'sabiduria', 'sabio', 'sabroso', 'saludable', 'salvacion', 'salvación', 'santa', 'santo', 'satisfecha',
    'satisfecho', 'sencilla', 'sencillo', 'sensacional', 'serena', 'serenidad', 'sereno', 'si', 'sí', 'sinceramente', 'sincero',
    'sincero', 'solidaria', 'solidario', 'solucion', 'solución', 'sonrisa', 'sorprendente', 'sostenible', 'super', 'talento', 'talentosa',
    'talentoso', 'tesoro', 'tolerancia', 'tolerante', 'trabajador', 'trabajadora', 'triunfal', 'triunfo', 'trofeo', 'unidad', 'util', 'útil',
    'valentia', 'valentía', 'valiente', 'valioso', 'valor', 'ventaja', 'vigor', 'visionario', 'virtuoso', 'virtud', 'vigorizante', 'victorioso',
    'vivaz', 'afinidad', 'vida', 'amo', 'fuerza', 'fortaleza', 'dignidad', 'bendición', 'unidos', 'apoyo', 'sueño', 'anhelado', 'mejor', 'inclusión',
    'inclusion', 'sana', 'salud', 'salva', 'correctos', 'correcto', 'animo', 'bueno', 'conviccion', 'convicción', 'merecemos', 'transparente', 'quiero',
    'humildad', 'inteligencia', 'amas', 'honestidad', 'sensata', 'encanta', 'buena', 'buenas', 'gran', 'dedicacion', 'dedicación',
    'divinos', 'divinas', 'belleza', 'perfectas', 'perfectos', 'resistente', 'gusta', 'preparado', 'sensatez', 'sensato', 'honesto', 'honesta',
    'coraje', 'respeto', 'decencia', 'orgullosamente', 'alegria', 'alegría', 'disfrutamos', 'garantizo', 'garantizar',
    'construyendo', 'uniendo', 'libertad', 'real', 'felices', 'amando', 'inigualables', 'claro', 'rica', 'lindo', 'linda', 'lindura',
    'preciosa', 'precioso', 'preciosos', 'preciosas', 'encanto', 'encantador', 'amable', 'parcero', 'bro', 'hermano', 'hermana',
    'valeroso', 'beneficio', 'beneficiario', 'paz', 'admiración', 'admiracion', 'respetuoso', 'respetuosa', 'oportunidades',
    'agradecimiento', 'progresas', 'progresar', 'progreso', 'posible', 'mejores', 'éxitos', 'equidad', 'igualdad', 'activismo',
    'productiva', 'productivo', 'resiliencia', 'celebrar', 'épicos', 'estelar', 'amada', 'amado', 'orgullosos', 'orgullosas', 'celebramos',
    'futuro', 'voluntarios', 'estimado'
]

# print ('Palabras negativas:', len(palabras_negativas))
# print ('Palabras positivas:', len(palabras_positivas))

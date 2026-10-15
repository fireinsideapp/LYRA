"""Catálogo base: 28 recetas mexicanas tradicionales adaptadas para adultos mayores."""

RECETAS: list[dict] = [   {   'descripcion': 'Albóndigas suaves de pollo molido con avena, cocidas en un caldillo casero de jitomate, sin '
                       'necesidad de agregar mucha sal.',
        'dificultad': 'media',
        'ingredientes': {   'base': [('Pollo molido', '400 g'), ('Avena molida', '30 g')],
                            'salsa': [   ('Jitomate', '300 g'),
                                         ('Cebolla', '60 g'),
                                         ('Ajo', '1 diente'),
                                         ('Agua', '500 ml')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a hacer esta receta con calma. Primero, lávate bien las manos y pon '
                                            'todos tus ingredientes a la mano sobre la mesa.',
                         'imagen': 'albondigas-pollo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté seco para evitar resbalones.',
                         'resumen_visual': 'Vamos a hacer esta receta con calma.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'En un recipiente o tazón hondo, pon el pollo molido y la avena molida. '
                                            'Mezcla todo muy bien con una cuchara o con tus manos limpias.',
                         'imagen': 'albondigas-pollo-paso2.jpeg',
                         'nota_seguridad': 'Si usaste tus manos, lávatelas muy bien con jabón inmediatamente después '
                                           'de tocar el pollo crudo.',
                         'resumen_visual': 'En un recipiente o tazón hondo, pon el pollo molido y la avena molida.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Ahora, forma bolitas con la mezcla de pollo, como del tamaño de una nuez '
                                            'grande. Hazlas pequeñitas para que sean fáciles de masticar. Ponlas en un '
                                            'plato y apártalas.',
                         'imagen': 'albondigas-pollo-paso3.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ahora, forma bolitas con la mezcla de pollo, como del tamaño de una nuez '
                                           'grande.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'licuadora'],
                         'detalle_hablado': 'Lava muy bien los jitomates, quítales el rabito y pártelos en cuartos '
                                            'para ayudar a tu licuadora.',
                         'imagen': 'albondigas-pollo-paso4.jpeg',
                         'nota_seguridad': 'Usa una tabla para picar bien apoyada, así evitamos accidentes con el '
                                           'cuchillo.',
                         'resumen_visual': 'Lava muy bien los jitomates, quítales el rabito y pártelos en cuartos para '
                                           'ayudar a tu licuadora.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Pon en la licuadora los jitomates partidos, el trozo de cebolla, el '
                                            'diente de ajo pelado y la mitad del agua (una taza o 250 ml). Licúa hasta '
                                            'que quede un caldito parejo.',
                         'imagen': 'albondigas-pollo-paso5.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa de la licuadora antes de encenderla.',
                         'resumen_visual': 'Pon en la licuadora los jitomates partidos, el trozo de cebolla, el diente '
                                           'de ajo pelado y la mit...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'licuadora'],
                         'detalle_hablado': 'Enciende la estufa a fuego medio. Pon una olla y vacía ahí el caldillo '
                                            'que acabas de licuar, luego agrega el resto del agua.',
                         'imagen': 'albondigas-pollo-paso6.jpeg',
                         'nota_seguridad': 'Acostumbra dejar el mango de la olla volteado hacia el centro de la estufa '
                                           'para que no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende la estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vamos a esperar a que el caldillo suelte el hervor. Te pondré un '
                                            'temporizador de 10 minutos para que lo vengas a revisar.',
                         'imagen': 'albondigas-pollo-paso7.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la lumbre esté prendida.',
                         'resumen_visual': 'Vamos a esperar a que el caldillo suelte el hervor.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': '¡Ya pasaron los 10 minutos! El caldillo ya debe estar hirviendo. Bájale '
                                            'al fuego para que quede suavecito.',
                         'imagen': 'albondigas-pollo-paso8.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': '¡Ya pasaron los 10 minutos!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Con mucho cuidado, ve echando las albóndigas de pollo una por una adentro '
                                            'del caldillo caliente. Procura que no queden todas amontonadas.',
                         'imagen': 'albondigas-pollo-paso9.jpeg',
                         'nota_seguridad': 'Pon las bolitas suavemente desde abajito para que no te vaya a salpicar '
                                           'agua caliente.',
                         'resumen_visual': 'Con mucho cuidado, ve echando las albóndigas de pollo una por una adentro '
                                           'del caldillo caliente.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Tapa la olla de ladito, dejando una pequeña abertura. Te aviso en 20 '
                                            'minutos para que el pollo se cueza muy bien por dentro.',
                         'imagen': 'albondigas-pollo-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Tapa la olla de ladito, dejando una pequeña abertura.',
                         'temporizador_segundos': 1200},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo el tiempo! Saca una albóndiga grande, pártela a la mitad y revisa '
                                            'que ya no esté rosita por dentro. Si aún se ve cruda, déjalas otros 5 '
                                            'minutitos.',
                         'imagen': 'albondigas-pollo-paso11.jpeg',
                         'nota_seguridad': 'Sopla un poco antes de revisarla, va a estar muy caliente.',
                         'resumen_visual': '¡Listo el tiempo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Si ya están bien cocidas, apaga la estufa en este momento para que no se '
                                            'consuma el caldillo.',
                         'imagen': 'albondigas-pollo-paso12.jpeg',
                         'nota_seguridad': 'Verifica con tus ojos que la perilla de la estufa sí quedó bien cerrada y '
                                           'no se escucha salir gas.',
                         'resumen_visual': 'Si ya están bien cocidas, apaga la estufa en este momento para que no se '
                                           'consuma el caldillo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Deja reposar la olla unos 2 minutitos. Te pongo el tiempo rápido para que '
                                            'se asienten los sabores.',
                         'imagen': 'albondigas-pollo-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar la olla unos 2 minutitos.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tus albóndigas calientitas con bastante caldito. Si te acomoda '
                                            'mejor, córtalas en pedacitos más chiquitos en tu plato para comerlas a '
                                            'gusto. ¡Que lo disfrutes!',
                         'imagen': 'albondigas-pollo-paso14.jpeg',
                         'nota_seguridad': 'Tócala primero con los labios para asegurar que la comida no esté '
                                           'demasiado caliente.',
                         'resumen_visual': 'Sirve tus albóndigas calientitas con bastante caldito.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'albondigas-pollo-caldillo',
        'tiempo_total_min': 44,
        'titulo': 'Albóndigas de pollo en caldillo de jitomate'},
    {   'descripcion': 'Albóndigas suaves de carne molida con arroz, cocidas en un caldo casero de jitomate, zanahoria '
                       'y calabacita, con verduras tiernas y poca sal añadida.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Carne molida de res', '400 g'),
                                        ('Arroz crudo', '40 g'),
                                        ('Zanahoria', '150 g'),
                                        ('Calabacita', '200 g')],
                            'salsa': [('Jitomate', '250 g'), ('Cebolla', '50 g'), ('Agua', '1.5 litros')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar este caldito reconfortante paso a paso. Primero, lávate '
                                            'bien las manos y pon todos tus ingredientes a la mano sobre la mesa.',
                         'imagen': 'albondigas-res-caldo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar cualquier '
                                           'resbalón.',
                         'resumen_visual': 'Vamos a preparar este caldito reconfortante paso a paso.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pon el arroz crudo en un colador pequeño, enjuágalo bajo el chorro de '
                                            'agua limpia y déjalo escurrir un ratito.',
                         'imagen': 'albondigas-res-caldo-paso2.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pon el arroz crudo en un colador pequeño, enjuágalo bajo el chorro de agua '
                                           'limpia y déjalo escurr...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'En un tazón hondo, pon la carne molida de res y el arroz escurrido. Amasa '
                                            'todo con tus manos limpias hasta que se mezcle bien.',
                         'imagen': 'albondigas-res-caldo-paso3.jpeg',
                         'nota_seguridad': 'En cuanto termines de mezclar la carne cruda, lávate muy bien las manos '
                                           'con agua y jabón.',
                         'resumen_visual': 'En un tazón hondo, pon la carne molida de res y el arroz escurrido.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Forma bolitas con la carne, más o menos del tamaño de una nuez grande, '
                                            'para que queden de buen bocado. Ponlas en un plato y apártalas.',
                         'imagen': 'albondigas-res-caldo-paso4.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Forma bolitas con la carne, más o menos del tamaño de una nuez grande, '
                                           'para que queden de buen bo...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'licuadora'],
                         'detalle_hablado': 'Lava muy bien los jitomates, quítales el rabito y pártelos en cuartos. '
                                            'Ponlos en la licuadora junto con el trozo de cebolla y una tacita de '
                                            'agua.',
                         'imagen': 'albondigas-res-caldo-paso5.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate en la mesa con una tabla firme para '
                                           'picar los jitomates.',
                         'resumen_visual': 'Lava muy bien los jitomates, quítales el rabito y pártelos en cuartos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa muy bien los jitomates con la cebolla hasta que quede un caldito '
                                            'rojo y parejito.',
                         'imagen': 'albondigas-res-caldo-paso6.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa de la licuadora antes de prenderla.',
                         'resumen_visual': 'Licúa muy bien los jitomates con la cebolla hasta que quede un caldito '
                                           'rojo y parejito.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende la estufa a fuego medio. Pon una olla grande y vacía el caldillo '
                                            'de jitomate, luego agrégale el resto del agua.',
                         'imagen': 'albondigas-res-caldo-paso7.jpeg',
                         'nota_seguridad': 'Voltea el mango de la olla hacia el centro de la estufa para que no lo '
                                           'vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende la estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Vamos a esperar a que el caldo empiece a hervir. Te pondré un tiempo de '
                                            '10 minutos para que lo vengas a revisar.',
                         'imagen': 'albondigas-res-caldo-paso8.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la lumbre esté prendida.',
                         'resumen_visual': 'Vamos a esperar a que el caldo empiece a hervir.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Cuando veas que el caldito ya está hirviendo, bájale a la flama. Con '
                                            'mucho cuidado, ve echando las albóndigas una por una para que no te '
                                            'salpique el agua caliente.',
                         'imagen': 'albondigas-res-caldo-paso9.jpeg',
                         'nota_seguridad': 'Si te da miedo quemarte, ayúdate con una cuchara grande para bajar las '
                                           'bolitas al caldo.',
                         'resumen_visual': 'Cuando veas que el caldito ya está hirviendo, bájale a la flama.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Tapa tu olla de ladito, dejando que salga un poquito de vapor. Te aviso '
                                            'en 20 minutos para que la carne se vaya cociendo suavemente.',
                         'imagen': 'albondigas-res-caldo-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Tapa tu olla de ladito, dejando que salga un poquito de vapor.',
                         'temporizador_segundos': 1200},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Mientras se cuecen las albóndigas, pela tu zanahoria, lávala y pícala en '
                                            'cuadritos chiquitos para que esté suave al masticar.',
                         'imagen': 'albondigas-res-caldo-paso11.jpeg',
                         'nota_seguridad': 'Hazlo con calma y usa un cuchillo que no esté muy pesado para ti.',
                         'resumen_visual': 'Mientras se cuecen las albóndigas, pela tu zanahoria, lávala y pícala en '
                                           'cuadritos chiquitos para...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Lava también la calabacita, quítale las puntas y pícala en cuadritos del '
                                            'mismo tamaño. Sepárala en otro platito.',
                         'imagen': 'albondigas-res-caldo-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Lava también la calabacita, quítale las puntas y pícala en cuadritos del '
                                           'mismo tamaño.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Ya pasaron los 20 minutos! Destapa la olla y agrega la zanahoria picada. '
                                            'Te pondré 10 minutitos más porque la zanahoria tarda un poquito más en '
                                            'ablandarse.',
                         'imagen': 'albondigas-res-caldo-paso13.jpeg',
                         'nota_seguridad': 'Ten cuidado con el vapor al destapar la olla, hazlo con la tapa apuntando '
                                           'hacia otro lado.',
                         'resumen_visual': '¡Ya pasaron los 20 minutos!',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ahora sí, echa la calabacita a la olla. Vamos a darle unos 8 a 10 minutos '
                                            'para que todas las verduras queden bien tiernitas.',
                         'imagen': 'albondigas-res-caldo-paso14.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ahora sí, echa la calabacita a la olla.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca la albóndiga más gordita, pártela a la mitad y revisa que ya no se '
                                            'vea roja por dentro y que el arrocito esté suave. Si aún le falta, '
                                            'déjalas 5 minutitos más.',
                         'imagen': 'albondigas-res-caldo-paso15.jpeg',
                         'nota_seguridad': 'Sopla un poco antes de revisarla de cerca, porque guarda mucho calor por '
                                           'dentro.',
                         'resumen_visual': 'Saca la albóndiga más gordita, pártela a la mitad y revisa que ya no se '
                                           'vea roja por dentro y que...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Ya quedó todo bien cocidito y tierno! Apaga la estufa en este momento '
                                            'para que no se evapore tu caldo.',
                         'imagen': 'albondigas-res-caldo-paso16.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que la perilla de la estufa sí '
                                           'quedó bien cerrada.',
                         'resumen_visual': '¡Ya quedó todo bien cocidito y tierno!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar tu olla unos 2 minutitos con la estufa apagada. Te pongo el '
                                            'tiempo rápido para que se enfríe un poco.',
                         'imagen': 'albondigas-res-caldo-paso17.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar tu olla unos 2 minutitos con la estufa apagada.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': '¡A comer! Sirve tus albóndigas en un plato hondo con bastante caldito y '
                                            'verduritas. Si lo prefieres, parte las bolitas en trozos pequeños ahí '
                                            'mismo en tu plato para comer más a gusto. ¡Buen provecho!',
                         'imagen': 'albondigas-res-caldo-paso18.jpeg',
                         'nota_seguridad': 'Toca la comida con los labios primero para asegurar que no esté demasiado '
                                           'caliente al tragar.',
                         'resumen_visual': '¡A comer!',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'albondigas-res-caldo-verduras',
        'tiempo_total_min': 64,
        'titulo': 'Albóndigas de res en caldo de verduras'},
    {   'descripcion': 'Arroz suelto cocido con salsa de jitomate. Un acompañamiento clásico de la comida mexicana.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Arroz', '1 taza'),
                                        ('Aceite', '3 cucharadas'),
                                        ('Caldo o agua caliente', '2 tazas'),
                                        ('Sal', '1/2 cucharadita')],
                            'salsa': [('Jitomates', '2 medianos'), ('Cebolla', '1/4 de pieza'), ('Ajo', '1 diente')],
                            'servicio': [('Zanahoria y chícharos (opcional)', 'Al gusto')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un arrocito rojo muy sabroso. Primero, lávate bien las '
                                            'manos y pon todos tus ingredientes en la mesa para no dar tantas vueltas.',
                         'imagen': 'arroz-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones.',
                         'resumen_visual': 'Vamos a preparar un arrocito rojo muy sabroso.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pon la taza de arroz en un colador de malla fina. Enjuágalo bajo el '
                                            'chorro de agua fría moviéndolo con tu mano, hasta que el agua salga '
                                            'clarita.',
                         'imagen': 'arroz-paso2.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pon la taza de arroz en un colador de malla fina.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite'],
                         'detalle_hablado': 'Deja escurriendo el arroz un buen rato. Debe estar bien seco para que no '
                                            'brinque el aceite caliente más adelante.',
                         'imagen': 'arroz-paso3.jpeg',
                         'nota_seguridad': 'Puedes apoyar el colador sobre un plato hondo para que no gotee el piso.',
                         'resumen_visual': 'Deja escurriendo el arroz un buen rato.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'licuadora'],
                         'detalle_hablado': 'Lava los jitomates, quítales el ombliguito y pártelos en cuartos. Ponlos '
                                            'en la licuadora con el pedazo de cebolla, el diente de ajo pelado y media '
                                            'taza de agua.',
                         'imagen': 'arroz-paso4.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar los jitomates.',
                         'resumen_visual': 'Lava los jitomates, quítales el ombliguito y pártelos en cuartos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa todo muy bien hasta que quede una salsa suavecita y sin grumos '
                                            'grandes. Déjala ahí un ladito.',
                         'imagen': 'arroz-paso5.jpeg',
                         'nota_seguridad': 'Verifica que la tapa de la licuadora esté bien puesta antes de prenderla.',
                         'resumen_visual': 'Licúa todo muy bien hasta que quede una salsa suavecita y sin grumos '
                                           'grandes.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Ahora sí, enciende la estufa a fuego medio. Pon una cazuela o una olla '
                                            'extendida y agrega las tres cucharadas de aceite para que se calienten.',
                         'imagen': 'arroz-paso6.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la cazuela hacia adentro de la estufa para no tropezar '
                                           'con él.',
                         'resumen_visual': 'Ahora sí, enciende la estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Con mucho cuidado, vacía el arroz ya seco en el aceite caliente. Muévelo '
                                            'suavemente con una cuchara de madera o plástico especial.',
                         'imagen': 'arroz-paso7.jpeg',
                         'nota_seguridad': 'El aceite puede chisporrotear un poco, usa una cuchara de mango largo.',
                         'resumen_visual': 'Con mucho cuidado, vacía el arroz ya seco en el aceite caliente.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Sigue moviendo el arroz constantemente para que no se queme. Te pongo 3 '
                                            'minutos; debe agarrar un color doradito claro, color paja, y sonar como '
                                            'arenita suelta.',
                         'imagen': 'arroz-paso8.jpeg',
                         'nota_seguridad': 'No dejes de moverlo porque el arroz se quema muy rápido.',
                         'resumen_visual': 'Sigue moviendo el arroz constantemente para que no se queme.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['aceite', 'cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Ahora agrégale la salsa de jitomate. Hazlo despacito, desde '
                                            'bajito, porque la cazuela va a chillar.',
                         'imagen': 'arroz-paso9.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si salpica el '
                                           'aceite.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ponle su media cucharadita de sal. Mezcla todo y deja que la salsa hierva '
                                            'para que cambie a un color rojo más oscuro. Te aviso en 2 minutitos.',
                         'imagen': 'arroz-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ponle su media cucharadita de sal.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega con cuidado las dos tazas de caldo o agua caliente. Si tienes '
                                            'zanahoria picadita o chícharos, échaselos de una vez. Mezcla todo '
                                            'suavemente por última vez.',
                         'imagen': 'arroz-paso11.jpeg',
                         'nota_seguridad': 'Si el caldo está muy caliente, usa un trapito grueso para sostener la olla '
                                           'y no quemarte.',
                         'resumen_visual': 'Agrega con cuidado las dos tazas de caldo o agua caliente.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Espera a que veas que todo el caldito empieza a hervir parejo. En ese '
                                            'momento, bájale al fuego a lo más, más bajito que se pueda y tapa muy '
                                            'bien tu olla.',
                         'imagen': 'arroz-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Espera a que veas que todo el caldito empieza a hervir parejo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'A partir de ahora no debes destapar la olla ni mover el arroz. Te pongo '
                                            '15 minutos de tiempo para que se cueza despacito y absorba el agua.',
                         'imagen': 'arroz-paso13.jpeg',
                         'nota_seguridad': 'Quédate cerca, tal vez sentada en la cocina, para escuchar cuando suene la '
                                           'alarma.',
                         'resumen_visual': 'A partir de ahora no debes destapar la olla ni mover el arroz.',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Sonó la alarma! Apaga la estufa de inmediato para que el arrocito no se '
                                            'te vaya a pegar o quemar del fondo.',
                         'imagen': 'arroz-paso14.jpeg',
                         'nota_seguridad': 'Revisa muy bien con tus ojitos que la perilla del gas quedó completamente '
                                           'cerrada.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Deja tu olla en la estufa, así apagada y sin destapar, por 5 minutos más. '
                                            'Este es el secreto para que el arroz esponje bonito con su propio vapor.',
                         'imagen': 'arroz-paso15.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja tu olla en la estufa, así apagada y sin destapar, por 5 minutos más.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['vapor'],
                         'detalle_hablado': '¡Ya está! Destapa tu olla con cuidado. Mete un tenedor y mueve el '
                                            'arrocito muy suavemente para separarlo. Sírvelo calientito para acompañar '
                                            'tu comida. ¡Buen provecho!',
                         'imagen': 'arroz-paso16.jpeg',
                         'nota_seguridad': 'Al destapar la olla, hazlo con la tapa apuntando hacia otro lado para que '
                                           'el vapor caliente no te dé en la cara.',
                         'resumen_visual': '¡Ya está!',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'arroz-rojo',
        'tiempo_total_min': 37,
        'titulo': 'Arroz rojo'},
    {   'descripcion': 'Desayuno caliente de avena con leche y manzana cocida, de consistencia cremosa y sabor suave.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Avena en hojuelas', '80 g'),
                                        ('Leche', '400 ml'),
                                        ('Manzana pelada y picada', '150 g'),
                                        ('Agua', '100 ml')],
                            'salsa': [('Canela molida', '1 g')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a prepararte una avenita calientita y suave para reconfortar la '
                                            'mañana. Primero, lávate bien las manos y pon tus ingredientes sobre la '
                                            'mesa.',
                         'imagen': 'avena-manzana-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de tu cocina esté bien seco para que no haya '
                                           'peligro de resbalones.',
                         'resumen_visual': 'Vamos a prepararte una avenita calientita y suave para reconfortar la '
                                           'mañana.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien la manzana. Pélala, quítale el corazón y las semillas, y '
                                            'pícala en cuadritos chiquitos para que te sea muy fácil de masticar.',
                         'imagen': 'avena-manzana-paso2.jpeg',
                         'nota_seguridad': 'Si sientes pesadez en las piernas, siéntate a la mesa para picar la fruta '
                                           'sobre una tabla firme. Tómalo con calma.',
                         'resumen_visual': 'Lava muy bien la manzana.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'En una olla pequeña, pon el chorrito de agua y los cuadritos de manzana.',
                         'imagen': 'avena-manzana-paso3.jpeg',
                         'nota_seguridad': 'Recuerda voltear el mango de tu olla hacia adentro de la estufa para que '
                                           'no lo vayas a golpear sin querer al pasar.',
                         'resumen_visual': 'En una olla pequeña, pon el chorrito de agua y los cuadritos de manzana.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Vamos a dejar que la manzana hierva un '
                                            'poco en el agua para que quede bien tiernita. Te pondré un tiempo de 5 '
                                            'minutos.',
                         'imagen': 'avena-manzana-paso4.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la cocina mientras la lumbre esté prendida, no te '
                                           'vayas a ir muy lejos.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Ya pasaron los 5 minutos! Con un tenedor, aplasta suavecito un cuadrito '
                                            'de manzana. Si ya se siente suave, vamos a lo que sigue.',
                         'imagen': 'avena-manzana-paso5.jpeg',
                         'nota_seguridad': 'Acerca tu cara de ladito, no directo arriba de la olla para que el vapor '
                                           'calientito no te dé en los ojos.',
                         'resumen_visual': '¡Ya pasaron los 5 minutos!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Ahora, con cuidado, vacía toda la leche en la olla. Agrega de una vez las '
                                            'hojuelas de avena y la pizca de canela molida para que vaya soltando su '
                                            'aroma.',
                         'imagen': 'avena-manzana-paso6.jpeg',
                         'nota_seguridad': 'Echa la leche despacito desde abajito para que no vaya a salpicar.',
                         'resumen_visual': 'Ahora, con cuidado, vacía toda la leche en la olla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Bájale a la flama de tu estufa; déjala a fuego muy suavecito. Empieza a '
                                            'mover despacio con una cuchara grande. Te aviso en 5 minutos para que '
                                            'espese.',
                         'imagen': 'avena-manzana-paso7.jpeg',
                         'nota_seguridad': 'No dejes de mover la olla de vez en cuando y no le subas al fuego, porque '
                                           'la leche hierve muy rápido, sube y se derrama.',
                         'resumen_visual': 'Bájale a la flama de tu estufa; déjala a fuego muy suavecito.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo el tiempo! Revisa cómo se ve tu avenita. Si ya está cremosita y a '
                                            'tu gusto, ya quedó lista. (Si sientes que está muy espesa, ponle otro '
                                            'chorrito de leche caliente).',
                         'imagen': 'avena-manzana-paso8.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': '¡Listo el tiempo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Apaga la estufa de inmediato para que tu avena no se seque de más.',
                         'imagen': 'avena-manzana-paso9.jpeg',
                         'nota_seguridad': 'Por favor, fíjate muy bien y asegúrate de que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': 'Apaga la estufa de inmediato para que tu avena no se seque de más.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja tu olla reposando ahí mismo en la estufa unos 3 minutitos. Así '
                                            'terminará de espesar rico y evitarás quemarte la boca. Te marco el '
                                            'tiempo.',
                         'imagen': 'avena-manzana-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja tu olla reposando ahí mismo en la estufa unos 3 minutitos.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': '¡A desayunar rico! Sirve tu avenita en dos tazones hondos. Tócala tantito '
                                            'con los labios antes de dar el primer bocado grande. ¡Buen provecho y '
                                            'bonito día!',
                         'imagen': 'avena-manzana-paso11.jpeg',
                         'nota_seguridad': 'Procura usar un platito abajo de tu tazón al llevarlo a la mesa por si '
                                           'está muy caliente de la base.',
                         'resumen_visual': '¡A desayunar rico!',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'avena-cremosa-manzana',
        'tiempo_total_min': 25,
        'titulo': 'Avena cremosa con manzana'},
    {   'descripcion': 'Guiso casero de calabacita, elote y jitomate con queso fresco, de sabor suave.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Calabacitas', '300 g'),
                                        ('Granos de elote cocidos', '100 g'),
                                        ('Jitomate', '150 g'),
                                        ('Cebolla', '40 g'),
                                        ('Aceite vegetal', '5 ml'),
                                        ('Agua', '100 ml')],
                            'salsa': [],
                            'servicio': [('Queso fresco', '60 g')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a hacer un guiso de calabacitas muy rico y suave. Primero, lávate '
                                            'bien las manos y pon todos tus ingredientes a la mano sobre la mesa.',
                         'imagen': 'calabacitas-elote-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a hacer un guiso de calabacitas muy rico y suave.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien las calabacitas, quítales las puntitas y córtalas en '
                                            'cuadritos chiquitos. Así serán mucho más fáciles y suaves de masticar.',
                         'imagen': 'calabacitas-elote-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa y pica las verduras sobre '
                                           'una tabla bien firme.',
                         'resumen_visual': 'Lava muy bien las calabacitas, quítales las puntitas y córtalas en '
                                           'cuadritos chiquitos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava el jitomate y córtalo en cuadritos pequeños. Haz lo mismo con la '
                                            'cebolla, picándola muy finita para que casi no se sienta al comer.',
                         'imagen': 'calabacitas-elote-paso3.jpeg',
                         'nota_seguridad': 'Hazlo con calma y procura usar un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Lava el jitomate y córtalo en cuadritos pequeños.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una olla pequeña o cazuelita y '
                                            'agrégale el chorrito de aceite (como una cucharadita) para que se vaya '
                                            'calentando.',
                         'imagen': 'calabacitas-elote-paso4.jpeg',
                         'nota_seguridad': 'Acostumbra dejar el mango de la cazuela volteado hacia el centro de la '
                                           'estufa para que no vayas a tropezar con él al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega la cebolla picadita a la olla. Muévela suavecito con una cuchara '
                                            'de madera hasta que se vea transparente. Te pondré un tiempo de 3 minutos '
                                            'para revisarla.',
                         'imagen': 'calabacitas-elote-paso5.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la estufa para que la cebolla no se te vaya a quemar.',
                         'resumen_visual': 'Agrega la cebolla picadita a la olla.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['aceite', 'cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Ahora agrega el jitomate picado. Revuelve bien y deja cocinar '
                                            'para que el jitomate suelte su juguito y se deshaga un poco. Te aviso en '
                                            '5 minutos.',
                         'imagen': 'calabacitas-elote-paso6.jpeg',
                         'nota_seguridad': 'Echa el jitomate despacito, bajando tu mano, para que el aceite caliente '
                                           'no te salpique.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Con mucho cuidado, vacía las calabacitas picadas y los granitos de elote '
                                            'a la olla. Mezcla todo suavemente para que los sabores se vayan juntando.',
                         'imagen': 'calabacitas-elote-paso7.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Con mucho cuidado, vacía las calabacitas picadas y los granitos de elote a '
                                           'la olla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega media tacita de agua y una pizca de sal a tu gusto. Bájale a la '
                                            'flama de la estufa para que sea un fuego suavecito y tapa tu olla. Te '
                                            'pondré un aviso en 10 minutos.',
                         'imagen': 'calabacitas-elote-paso8.jpeg',
                         'nota_seguridad': 'No te vayas lejos de la cocina mientras la lumbre siga prendida.',
                         'resumen_visual': 'Agrega media tacita de agua y una pizca de sal a tu gusto.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado y pica un cuadrito de '
                                            'calabacita con un tenedor. Si ya está bien tiernita, ya quedó. Si todavía '
                                            'la sientes algo durita, déjala otros 3 minutitos tapada.',
                         'imagen': 'calabacitas-elote-paso9.jpeg',
                         'nota_seguridad': 'Destapa la olla levantando la tapa hacia otro lado, para que el vapor '
                                           'caliente no te dé directo en la cara.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedaron suavecitas! Apaga la estufa de inmediato para que la verdura '
                                            'no se te bata ni se reseque tu guisado.',
                         'imagen': 'calabacitas-elote-paso10.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': '¡Ya quedaron suavecitas!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tus calabacitas en un plato hondo para que las disfrutes '
                                            'calientitas con su juguito. Por último, desmorona el queso fresco encima '
                                            'de tu plato. ¡Que tengas buen provecho!',
                         'imagen': 'calabacitas-elote-paso11.jpeg',
                         'nota_seguridad': 'Tócalas un poquito con los labios antes de llevarlas a la boca para '
                                           'asegurar que no estén demasiado calientes.',
                         'resumen_visual': 'Sirve tus calabacitas en un plato hondo para que las disfrutes calientitas '
                                           'con su juguito.',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'calabacitas-elote-queso',
        'tiempo_total_min': 30,
        'titulo': 'Calabacitas con elote y queso'},
    {   'descripcion': 'Caldo casero de pollo con arroz, zanahoria y calabacita cocidos hasta quedar suaves.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Pechuga de pollo sin hueso', '400 g'),
                                        ('Arroz blanco crudo', '100 g'),
                                        ('Zanahoria', '150 g'),
                                        ('Calabacita', '150 g')],
                            'salsa': [('Cebolla', '40 g'), ('Agua', '1.8 litros')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un caldito de pollo muy reconfortante. Primero, lávate '
                                            'bien las manos y pon todos tus ingredientes a la mano sobre la mesa.',
                         'imagen': 'caldo-pollo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar un caldito de pollo muy reconfortante.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'En una olla grande, pon la pechuga de pollo, el pedacito de cebolla y '
                                            'vacía casi toda el agua. Deja solo un vasito de agua reservado por si se '
                                            'ocupa después.',
                         'imagen': 'caldo-pollo-paso2.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no vayas a tropezar con él al pasar.',
                         'resumen_visual': 'En una olla grande, pon la pechuga de pollo, el pedacito de cebolla y '
                                           'vacía casi toda el agua.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio-alto. Vamos a esperar a que el agua '
                                            'empiece a hervir. Te pondré un tiempo de 15 minutos para venir a '
                                            'revisarlo.',
                         'imagen': 'caldo-pollo-paso3.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la lumbre esté prendida.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio-alto.',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa', 'vapor'],
                         'detalle_hablado': 'Cuando el caldo empiece a hervir, vas a ver que se le hace una espumita '
                                            'en la parte de arriba. Retírala poco a poco con una cuchara y tírala.',
                         'imagen': 'caldo-pollo-paso4.jpeg',
                         'nota_seguridad': 'Acerca tu cara de ladito, no directamente arriba de la olla para que el '
                                           'vapor caliente no te dé en los ojos.',
                         'resumen_visual': 'Cuando el caldo empiece a hervir, vas a ver que se le hace una espumita en '
                                           'la parte de arriba.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ahora bájale a la flama de tu estufa para que hierva muy suavecito, y '
                                            'tapa tu olla de ladito. Te pondré 20 minutos para que el pollo se cueza '
                                            'bien por dentro.',
                         'imagen': 'caldo-pollo-paso5.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ahora bájale a la flama de tu estufa para que hierva muy suavecito, y tapa '
                                           'tu olla de ladito.',
                         'temporizador_segundos': 1200},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras el pollo está en la lumbre, pon tu arroz en un colador chiquito '
                                            'y enjuágalo bajo el chorro de agua fría hasta que el agua salga '
                                            'limpiecita. Déjalo escurriendo.',
                         'imagen': 'caldo-pollo-paso6.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Mientras el pollo está en la lumbre, pon tu arroz en un colador chiquito y '
                                           'enjuágalo bajo el chor...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Pela la zanahoria, córtale las puntas y pícala en cuadritos chiquitos '
                                            'para que te sea muy fácil de masticar.',
                         'imagen': 'caldo-pollo-paso7.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar la verdura con '
                                           'calma sobre una tabla firme.',
                         'resumen_visual': 'Pela la zanahoria, córtale las puntas y pícala en cuadritos chiquitos para '
                                           'que te sea muy fácil d...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Lava la calabacita, quítale las puntitas y pícala también en cuadritos '
                                            'del mismo tamaño. Sepárala en otro platito.',
                         'imagen': 'caldo-pollo-paso8.jpeg',
                         'nota_seguridad': 'Usa un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Lava la calabacita, quítale las puntitas y pícala también en cuadritos del '
                                           'mismo tamaño.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': '¡Ya sonó el tiempo del pollo! Saca la pechuga de la olla, ponla en un '
                                            'plato y déjala enfriar un buen rato.',
                         'imagen': 'caldo-pollo-paso9.jpeg',
                         'nota_seguridad': 'Usa unas pinzas largas o dos cucharas para sacar el pollo, no vayas a '
                                           'meter la mano ni te expongas a salpicaduras.',
                         'resumen_visual': '¡Ya sonó el tiempo del pollo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Ahí mismo en tu olla con el caldo hirviendo, echa con cuidado el arroz '
                                            'escurrido y la zanahoria picada. Te pondré 15 minutos para que se vayan '
                                            'ablandando.',
                         'imagen': 'caldo-pollo-paso10.jpeg',
                         'nota_seguridad': 'Echa las cosas despacito, pegado a la orilla del caldo, para que el agua '
                                           'caliente no te brinque.',
                         'resumen_visual': 'Ahí mismo en tu olla con el caldo hirviendo, echa con cuidado el arroz '
                                           'escurrido y la zanahoria p...',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras pasan esos 15 minutos, revisa si el pollo ya no quema. Con tus '
                                            'manos bien limpias, deshébralo en tiritas delgaditas para que sea suave '
                                            'al comer.',
                         'imagen': 'caldo-pollo-paso11.jpeg',
                         'nota_seguridad': 'Si todavía se siente muy caliente, no te apresures, ayúdate con dos '
                                           'tenedores para separarlo.',
                         'resumen_visual': 'Mientras pasan esos 15 minutos, revisa si el pollo ya no quema.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': '¡Pasaron los 15 minutos! Ahora echa la calabacita picada a la olla, el '
                                            'pollo deshebrado y ponle sal a tu gusto. Te pongo 10 minutitos más para '
                                            'que todo quede bien tierno y calientito.',
                         'imagen': 'caldo-pollo-paso12.jpeg',
                         'nota_seguridad': 'Prueba el caldito con una cuchara soplando antes, para ver si le falta sal '
                                           'o agua.',
                         'resumen_visual': '¡Pasaron los 15 minutos!',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca un granito de arroz y un cuadrito de zanahoria para revisarlos. Si '
                                            'ya están bien suavecitos y se deshacen fácil, ¡ya quedó listo nuestro '
                                            'caldo!',
                         'imagen': 'caldo-pollo-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Saca un granito de arroz y un cuadrito de zanahoria para revisarlos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Apaga la estufa de inmediato para que tu caldito no se vaya a consumir y '
                                            'la verdura no se desbarate.',
                         'imagen': 'caldo-pollo-paso14.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada hacia arriba.',
                         'resumen_visual': 'Apaga la estufa de inmediato para que tu caldito no se vaya a consumir y '
                                           'la verdura no se desbarate.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja tu olla reposando ahí mismo en la estufa unos 5 minutitos para que '
                                            'se asienten los sabores.',
                         'imagen': 'caldo-pollo-paso15.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja tu olla reposando ahí mismo en la estufa unos 5 minutitos para que se '
                                           'asienten los sabores.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': '¡A comer rico! Sirve tu caldito en un plato hondo. Ponle unas gotitas de '
                                            'limón si te gusta. Tócalo tantito con los labios antes de dar el primer '
                                            'bocado grande. ¡Buen provecho y que te caiga muy bien!',
                         'imagen': 'caldo-pollo-paso16.jpeg',
                         'nota_seguridad': 'Procura ponerle un plato extendido abajo a tu plato hondo para que no te '
                                           'queme las manos al llevarlo a la mesa.',
                         'resumen_visual': '¡A comer rico!',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'caldo-pollo-arroz-verduras',
        'tiempo_total_min': 77,
        'titulo': 'Caldo de pollo con arroz y verduras'},
    {   'descripcion': 'Caldo casero de res con papa, zanahoria, calabacita y elote, preparado con verduras bien '
                       'cocidas para ser suave y reconfortante.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Carne de res para caldo sin exceso de grasa', '500 g'),
                                        ('Papa', '250 g'),
                                        ('Zanahoria', '150 g'),
                                        ('Calabacita', '200 g'),
                                        ('Elote', '1 pieza de 200 g')],
                            'salsa': [('Jitomate', '150 g'), ('Cebolla', '50 g'), ('Agua', '2 litros'), ('Sal', '2 g')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un caldo de res muy nutritivo y suave. Primero, lávate '
                                            'muy bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'caldo-res-paso1.jpeg',
                         'nota_seguridad': 'Verifica que el piso de la cocina esté bien seco para no resbalar.',
                         'resumen_visual': 'Vamos a preparar un caldo de res muy nutritivo y suave.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pide en la carnicería que te den la carne ya cortada en trozos medianos y '
                                            'sin tanta grasa. Si tienes que cortarla tú, hazlo sobre una tabla firme y '
                                            'limpia.',
                         'imagen': 'caldo-res-paso2.jpeg',
                         'nota_seguridad': 'Después de tocar la carne cruda, lávate las manos con agua y jabón.',
                         'resumen_visual': 'Pide en la carnicería que te den la carne ya cortada en trozos medianos y '
                                           'sin tanta grasa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'En una olla grande, pon los trozos de carne y vacía los 2 litros de agua '
                                            'limpia. Asegúrate de que la olla quede bien asentada en la parrilla.',
                         'imagen': 'caldo-res-paso3.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa.',
                         'resumen_visual': 'En una olla grande, pon los trozos de carne y vacía los 2 litros de agua '
                                           'limpia.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego alto para que el agua hierva. Cuando veas que '
                                            'suelta el hervor, bájale al fuego a lo más mínimo para que hierva '
                                            'suavecito.',
                         'imagen': 'caldo-res-paso4.jpeg',
                         'nota_seguridad': 'Si sale espumita café en el agua, sácala con una cuchara con mucho cuidado '
                                           'y tírala.',
                         'resumen_visual': 'Enciende tu estufa a fuego alto para que el agua hierva.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Tapa tu olla dejando una pequeña rendija para que salga el vapor. Vamos a '
                                            'dejar que la carne se cueza lentamente por 1 hora. Te pondré el aviso.',
                         'imagen': 'caldo-res-paso5.jpeg',
                         'nota_seguridad': 'No acerques la cara a la olla al destaparla para evitar que el vapor te '
                                           'queme.',
                         'resumen_visual': 'Tapa tu olla dejando una pequeña rendija para que salga el vapor.',
                         'temporizador_segundos': 3600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras la carne se cuece, siéntate a la mesa a preparar las verduras. '
                                            'Lava muy bien la papa, la zanahoria, el elote, la calabacita, el jitomate '
                                            'y la cebolla.',
                         'imagen': 'caldo-res-paso6.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Mientras la carne se cuece, siéntate a la mesa a preparar las verduras.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Pela la papa y la zanahoria. Pícalas en cuadritos pequeños para que se '
                                            'ablanden rápido y te sean muy fáciles de masticar.',
                         'imagen': 'caldo-res-paso7.jpeg',
                         'nota_seguridad': 'Usa un cuchillo ligero y tómate tu tiempo, no hay prisa.',
                         'resumen_visual': 'Pela la papa y la zanahoria.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Corta el elote en 4 o 5 pedazos cortos. Si sientes que está muy duro, '
                                            'puedes desgranarlo con cuidado apoyando el elote en la tabla.',
                         'imagen': 'caldo-res-paso8.jpeg',
                         'nota_seguridad': 'Pide ayuda para cortar el elote si sientes que el cuchillo se resbala.',
                         'resumen_visual': 'Corta el elote en 4 o 5 pedazos cortos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Pica finamente el jitomate y la cebolla. Córtale las puntas a la '
                                            'calabacita y pícala también en cuadritos. Separa todo en platitos.',
                         'imagen': 'caldo-res-paso9.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pica finamente el jitomate y la cebolla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya pasó 1 hora! Destapa la olla con cuidado y saca un pedacito de carne. '
                                            'Pícalo con un tenedor; si ya está un poco suave, vamos a agregar lo '
                                            'demás.',
                         'imagen': 'caldo-res-paso10.jpeg',
                         'nota_seguridad': 'Sopla el pedacito de carne antes de tocarlo, estará muy caliente.',
                         'resumen_visual': '¡Ya pasó 1 hora!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega a la olla, con mucho cuidado, la papa, la zanahoria, el elote, el '
                                            'jitomate y la cebolla picados. Vuelve a tapar dejando la rendija. Te '
                                            'aviso en 25 minutos.',
                         'imagen': 'caldo-res-paso11.jpeg',
                         'nota_seguridad': 'Echa la verdura casi pegadita al caldo, desde abajo, para que no te '
                                           'salpique el agua caliente.',
                         'resumen_visual': 'Agrega a la olla, con mucho cuidado, la papa, la zanahoria, el elote, el '
                                           'jitomate y la cebolla pi...',
                         'temporizador_segundos': 1500},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo el tiempo! Ahora agrega la calabacita picada y la pizca de sal. '
                                            'Revuelve todo suavecito con un cucharón largo. Te pondré los últimos 10 '
                                            'minutos.',
                         'imagen': 'caldo-res-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': '¡Listo el tiempo!',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca un pedacito de papa y uno de carne. Si ya todo se siente muy suave y '
                                            'tierno al pincharlo, ¡nuestro caldo ya está listo!',
                         'imagen': 'caldo-res-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Saca un pedacito de papa y uno de carne.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Apaga la estufa de inmediato para que tu caldo no se vaya a consumir y la '
                                            'verdura no se deshaga.',
                         'imagen': 'caldo-res-paso14.jpeg',
                         'nota_seguridad': 'Verifica muy bien con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': 'Apaga la estufa de inmediato para que tu caldo no se vaya a consumir y la '
                                           'verdura no se deshaga.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar la olla unos 5 minutitos en la estufa apagada para que el '
                                            'caldo se enfríe un poco y no te vayas a quemar la boca.',
                         'imagen': 'caldo-res-paso15.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar la olla unos 5 minutitos en la estufa apagada para que el '
                                           'caldo se enfríe un poco y...',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': '¡A comer rico! Sirve tu caldo en un plato hondo grande con bastante '
                                            'verdurita y carne. Tócalo tantito con los labios antes de dar el primer '
                                            'bocado. ¡Buen provecho!',
                         'imagen': 'caldo-res-paso16.jpeg',
                         'nota_seguridad': 'Al momento de servir o comer la carne, fíjate bien que no se haya ido '
                                           'algún huesito duro.',
                         'resumen_visual': '¡A comer rico!',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'caldo-res-verduras',
        'tiempo_total_min': 112,
        'titulo': 'Caldo de res con verduras'},
    {   'descripcion': 'Desayuno tradicional mexicano: totopos de maíz bañados en una rica salsa roja, con queso, '
                       'crema, cebolla y cilantro.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Tortillas de maíz', '10 a 12 (mejor si son de un día anterior)'),
                                        ('Aceite para freír', 'Suficiente')],
                            'salsa': [   ('Tomates rojos (jitomates)', '4 medianos'),
                                         ('Chile guajillo', '2 piezas'),
                                         ('Chile de árbol', '1 o 2 piezas (según lo picoso que lo quiera)'),
                                         ('Cebolla', 'Un cuarto de pieza'),
                                         ('Ajo', '1 diente'),
                                         ('Sal', 'Al gusto')],
                            'servicio': [   ('Queso fresco desmenuzado (o cotija)', 'Al gusto'),
                                            ('Crema', 'Al gusto'),
                                            ('Cebolla picada', 'Al gusto'),
                                            ('Cilantro fresco picado', 'Al gusto'),
                                            ('Huevo frito o pollo deshebrado', 'Opcional, para acompañar')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unos ricos chilaquiles rojos paso a pasito. Primero, '
                                            'lávate bien las manos y pon todos tus ingredientes sobre la mesa para no '
                                            'dar muchas vueltas.',
                         'imagen': 'rojos-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones.',
                         'resumen_visual': 'Vamos a preparar unos ricos chilaquiles rojos paso a pasito.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Toma las tortillas de maíz y córtalas en forma de triángulos. Hazlo sobre '
                                            'una tabla de picar limpia con un cuchillo o unas tijeras de cocina.',
                         'imagen': 'rojos-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para cortar las tortillas '
                                           'con calma.',
                         'resumen_visual': 'Toma las tortillas de maíz y córtalas en forma de triángulos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Limpia los chiles guajillos: ábrelos con cuidado y quítales las semillas '
                                            'y las venitas para que la salsa no quede amarga ni caiga pesada al '
                                            'estómago.',
                         'imagen': 'rojos-paso3.jpeg',
                         'nota_seguridad': 'Lávate bien las manos después de tocar los chiles para que no te vayas a '
                                           'tallar los ojos.',
                         'resumen_visual': 'Limpia los chiles guajillos: ábrelos con cuidado y quítales las semillas y '
                                           'las venitas para que l...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Pon los jitomates lavados, los chiles guajillos y los chiles de árbol en '
                                            'una olla pequeña. Cúbrelos con agua limpia.',
                         'imagen': 'rojos-paso4.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa.',
                         'resumen_visual': 'Pon los jitomates lavados, los chiles guajillos y los chiles de árbol en '
                                           'una olla pequeña.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende la estufa a fuego medio. Vamos a dejar que hiervan hasta que los '
                                            'jitomates se vean suavecitos y se les despegue la piel. Te pondré un '
                                            'aviso en 10 minutos.',
                         'imagen': 'rojos-paso5.jpeg',
                         'nota_seguridad': 'No te vayas muy lejos de la cocina mientras la lumbre esté prendida.',
                         'resumen_visual': 'Enciende la estufa a fuego medio.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': '¡Ya pasaron los 10 minutos! Apaga la estufa. Retira la olla del fuego con '
                                            'mucho cuidado, escúrreles el agua caliente y déjalos enfriar un ratito.',
                         'imagen': 'rojos-paso6.jpeg',
                         'nota_seguridad': 'Usa un trapo grueso o guante de cocina para agarrar la olla caliente.',
                         'resumen_visual': '¡Ya pasaron los 10 minutos!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Pon en el vaso de la licuadora los jitomates, los chiles ya suaves, el '
                                            'trozo de cebolla, el diente de ajo y una pizca de sal. Licúa muy bien '
                                            'hasta que quede una salsita parejita.',
                         'imagen': 'rojos-paso7.jpeg',
                         'nota_seguridad': 'Ponle un trapo limpio encima a la tapa de la licuadora y sujétala bien con '
                                           'la mano. Los ingredientes calientes pueden saltar por la presión.',
                         'resumen_visual': 'Pon en el vaso de la licuadora los jitomates, los chiles ya suaves, el '
                                           'trozo de cebolla, el dient...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Ahora vamos a hacer los totopos. Enciende la estufa a fuego medio y '
                                            'calienta el aceite en una sartén amplia.',
                         'imagen': 'rojos-paso8.jpeg',
                         'nota_seguridad': 'Verifica que las mangas de tu ropa no queden colgando cerca de la lumbre.',
                         'resumen_visual': 'Ahora vamos a hacer los totopos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega los triángulos de tortilla al aceite para freírlos. Te aviso en 5 '
                                            'minutos para que los voltees con unas pinzas y revises si ya están '
                                            'doraditos.',
                         'imagen': 'rojos-paso9.jpeg',
                         'nota_seguridad': 'Ten cuidado al echar las tortillas, el aceite caliente puede salpicar.',
                         'resumen_visual': 'Agrega los triángulos de tortilla al aceite para freírlos.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca los totopos bien doraditos y ponlos sobre servilletas de papel para '
                                            'quitarles el exceso de grasa. ¡Apaga la estufa por un momento para evitar '
                                            'accidentes!',
                         'imagen': 'rojos-paso10.jpeg',
                         'nota_seguridad': 'Apoya la sartén en la parrilla para que no te pese mientras sacas los '
                                           'totopos.',
                         'resumen_visual': 'Saca los totopos bien doraditos y ponlos sobre servilletas de papel para '
                                           'quitarles el exceso de g...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Enciende de nuevo la estufa. En otra cazuela con solo un hilito de aceite '
                                            'caliente, vierte despacito la salsa roja que licuaste.',
                         'imagen': 'rojos-paso11.jpeg',
                         'nota_seguridad': 'Al echar la salsa al aceite caliente va a chillar y brincar un poquito, '
                                           'hazlo con la mano bajita y retira la cara.',
                         'resumen_visual': 'Enciende de nuevo la estufa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja que la salsa hierva a fuego suave. Te aviso en 5 minutos para que el '
                                            'jitomate y los chiles se guisen bien. Pruébala de sal y ajústala a tu '
                                            'gusto.',
                         'imagen': 'rojos-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja que la salsa hierva a fuego suave.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Es hora de agregar los totopos doraditos a la salsa caliente. Muévelos '
                                            'muy suavecito, de abajo hacia arriba, para que todos se bañen de salsa. '
                                            'Te pongo 2 minutos para que se ablanden a tu gusto.',
                         'imagen': 'rojos-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Es hora de agregar los totopos doraditos a la salsa caliente.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo el tiempo! Apaga la estufa de inmediato para que los chilaquiles '
                                            'queden en su punto y no se te deshagan por completo.',
                         'imagen': 'rojos-paso14.jpeg',
                         'nota_seguridad': 'Verifica muy bien con tu vista que la perilla de la estufa quedó '
                                           'completamente cerrada.',
                         'resumen_visual': '¡Listo el tiempo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tus chilaquiles rojos calientitos en un plato. Ponles encima un '
                                            'poco de crema, su queso fresco desmoronado, cebollita y cilantro. Si te '
                                            'apetece, acompáñalos con pollito o un huevo. ¡A disfrutar este delicioso '
                                            'almuerzo!',
                         'imagen': 'rojos-paso15.jpeg',
                         'nota_seguridad': 'Tócalos un poco con los labios antes de dar el primer bocado grande para '
                                           'no quemarte la boca.',
                         'resumen_visual': 'Sirve tus chilaquiles rojos calientitos en un plato.',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'chilaquiles-rojos',
        'tiempo_total_min': 34,
        'titulo': 'Chilaquiles rojos'},
    {   'descripcion': 'Desayuno tradicional mexicano: totopos de maíz bañados en salsa verde, con queso, crema, '
                       'cebolla y cilantro.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Tortillas de maíz cortadas en triángulos', '8 a 12 aproximadamente'),
                                        ('Aceite para freír', 'Suficiente')],
                            'salsa': [   ('Tomatillos verdes', 'Medio kilo'),
                                         ('Chiles serranos o jalapeños', 'Al gusto (1 o 2 piezas)'),
                                         ('Cebolla', 'Un cuarto'),
                                         ('Ajo', '1 diente'),
                                         ('Sal', 'Al gusto')],
                            'servicio': [   ('Queso fresco desmenuzado (o cotija)', 'Al gusto'),
                                            ('Crema', 'Al gusto'),
                                            ('Cebolla picada', 'Al gusto'),
                                            ('Cilantro fresco picado', 'Al gusto'),
                                            ('Huevo frito o pollo deshebrado', 'Opcional')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unos deliciosos chilaquiles verdes paso a paso, sin '
                                            'prisa. Primero, reúne todos tus ingredientes sobre la mesa para tenerlos '
                                            'a la mano.',
                         'imagen': 'verdes-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté completamente seco para evitar '
                                           'resbalones.',
                         'resumen_visual': 'Vamos a preparar unos deliciosos chilaquiles verdes paso a paso, sin '
                                           'prisa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Toma las tortillas de maíz y córtalas en forma de triángulos con un '
                                            'cuchillo o unas tijeras de cocina limpias.',
                         'imagen': 'verdes-paso2.jpeg',
                         'nota_seguridad': 'Hazlo sobre una tabla de picar y, si te cansas, siéntate a la mesa para '
                                           'hacerlo con más comodidad.',
                         'resumen_visual': 'Toma las tortillas de maíz y córtalas en forma de triángulos con un '
                                           'cuchillo o unas tijeras de co...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Pon los tomatillos verdes sin cáscara y los chiles en una olla pequeña. '
                                            'Cúbrelos con agua limpia.',
                         'imagen': 'verdes-paso3.jpeg',
                         'nota_seguridad': 'Coloca la olla asegurándote de que el mango quede volteado hacia el centro '
                                           'de la estufa.',
                         'resumen_visual': 'Pon los tomatillos verdes sin cáscara y los chiles en una olla pequeña.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Enciende la estufa a fuego medio y pon a hervir la olla con los '
                                            'tomatillos. Te pondré un temporizador de 10 minutos para revisarlos; '
                                            'deben cambiar a un color verde pálido.',
                         'imagen': 'verdes-paso4.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la estufa esté prendida.',
                         'resumen_visual': 'Enciende la estufa a fuego medio y pon a hervir la olla con los '
                                           'tomatillos.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Es hora! Apaga la estufa. Retira la olla del fuego con mucho cuidado y '
                                            'escurre los tomatillos y chiles. Déjalos enfriar un par de minutitos.',
                         'imagen': 'verdes-paso5.jpeg',
                         'nota_seguridad': 'Usa un trapo grueso o guantes para cocina al agarrar la olla caliente para '
                                           'no quemarte.',
                         'resumen_visual': '¡Es hora!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora', 'vapor'],
                         'detalle_hablado': 'Pon en el vaso de la licuadora los tomatillos, los chiles, el trozo de '
                                            'cebolla, el diente de ajo y una pizca de sal. Licúa muy bien.',
                         'imagen': 'verdes-paso6.jpeg',
                         'nota_seguridad': 'Ponle un trapo limpio encima a la tapa de la licuadora y sujétala bien. '
                                           'Los ingredientes calientes pueden saltar por el vapor.',
                         'resumen_visual': 'Pon en el vaso de la licuadora los tomatillos, los chiles, el trozo de '
                                           'cebolla, el diente de ajo...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Ahora vamos a hacer los totopos. Enciende la estufa a fuego medio y '
                                            'calienta un poco de aceite en una sartén amplia.',
                         'imagen': 'verdes-paso7.jpeg',
                         'nota_seguridad': 'Revisa que las mangas de tu ropa no queden cerca de la llama.',
                         'resumen_visual': 'Ahora vamos a hacer los totopos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega los triángulos de tortilla al aceite para freírlos. Te aviso en 5 '
                                            'minutos para que los voltees con unas pinzas y veas si ya están doraditos '
                                            'y crujientes.',
                         'imagen': 'verdes-paso8.jpeg',
                         'nota_seguridad': 'Ten cuidado, ponlos suavecito porque el aceite caliente puede salpicar.',
                         'resumen_visual': 'Agrega los triángulos de tortilla al aceite para freírlos.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Saca los totopos doraditos y ponlos sobre unas servilletas de papel para '
                                            'quitarles el exceso de grasa. ¡Apaga la estufa por un momento para evitar '
                                            'accidentes!',
                         'imagen': 'verdes-paso9.jpeg',
                         'nota_seguridad': 'Usa unas pinzas largas para no acercar mucho las manos al aceite caliente.',
                         'resumen_visual': 'Saca los totopos doraditos y ponlos sobre unas servilletas de papel para '
                                           'quitarles el exceso de g...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'agua_caliente', 'cuchillo', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Enciende de nuevo la estufa. En otra olla o cazuela con solo un hilito de '
                                            'aceite caliente, vierte con cuidado la salsa verde que licuaste.',
                         'imagen': 'verdes-paso10.jpeg',
                         'nota_seguridad': 'Al echar la salsa al aceite caliente va a chillar y salpicar un poco, '
                                           'hazlo con cuidado, bajando la mano.',
                         'resumen_visual': 'Enciende de nuevo la estufa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja que la salsa hierva a fuego suave. Te aviso en 5 minutos para que '
                                            'los sabores se mezclen bien. Pruébala de sal y si le falta, ponle otro '
                                            'poquito.',
                         'imagen': 'verdes-paso11.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja que la salsa hierva a fuego suave.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega los totopos a la salsa caliente. Muévelos suavecito con una '
                                            'cuchara, de abajo hacia arriba, para que se bañen todos sin romperse. Te '
                                            'pongo 2 minutos para que se ablanden un poquito.',
                         'imagen': 'verdes-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Agrega los totopos a la salsa caliente.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo el tiempo! Apaga la estufa de inmediato para que los chilaquiles '
                                            'queden en su punto y no se te batan.',
                         'imagen': 'verdes-paso13.jpeg',
                         'nota_seguridad': 'Verifica visualmente que la perilla de la estufa esté bien cerrada.',
                         'resumen_visual': '¡Listo el tiempo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sírvelos calientitos en tu plato. Ponles encima su cremita, queso fresco '
                                            'desmoronado, cebolla y cilantro al gusto. Si quieres, acompáñalos con un '
                                            'huevito o pollo deshebrado. ¡A disfrutar de este rico almuerzo!',
                         'imagen': 'verdes-paso14.jpeg',
                         'nota_seguridad': 'Tócalos un poquito con los labios antes de comer para asegurarte de que no '
                                           'estén muy calientes.',
                         'resumen_visual': 'Sírvelos calientitos en tu plato.',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'chilaquiles-verdes',
        'tiempo_total_min': 34,
        'titulo': 'Chilaquiles verdes'},
    {   'descripcion': 'Crema suave de calabacita con papa y leche, ideal como entrada o cena ligera y muy amigable '
                       'con el estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Calabacitas', '400 g'),
                                        ('Papa', '100 g (una papa chica)'),
                                        ('Leche', '250 ml (una taza)'),
                                        ('Agua', '400 ml'),
                                        ('Aceite de oliva o aceite vegetal', '5 ml (una cucharadita)')],
                            'salsa': [('Cebolla', '30 g (un pedacito)')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar una deliciosa y calientita crema de calabacita. Primero, '
                                            'lávate bien las manos y pon todos tus ingredientes a la mano sobre la '
                                            'mesa.',
                         'imagen': 'crema-calabacita-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar una deliciosa y calientita crema de calabacita.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien las calabacitas, quítales las puntitas y córtalas en '
                                            'cuadritos. Pela tu papa, lávala y córtala también en cuadritos chiquitos.',
                         'imagen': 'crema-calabacita-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar las verduras '
                                           'con calma sobre una tabla firme.',
                         'resumen_visual': 'Lava muy bien las calabacitas, quítales las puntitas y córtalas en '
                                           'cuadritos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pica finamente el pedacito de cebolla. Separa todas tus verduras en '
                                            'platitos para tenerlas listas y no andar a las prisas.',
                         'imagen': 'crema-calabacita-paso3.jpeg',
                         'nota_seguridad': 'Hazlo despacio y usa un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Pica finamente el pedacito de cebolla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una olla mediana y agrégale la '
                                            'cucharadita de aceite para que se vaya calentando.',
                         'imagen': 'crema-calabacita-paso4.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no vayas a tropezar con él al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega la cebolla picadita a la olla. Muévela suavecito con una cuchara '
                                            'de madera. Te pondré un tiempo de 3 minutos para que se acitrone y se '
                                            'ponga transparente.',
                         'imagen': 'crema-calabacita-paso5.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la estufa para que la cebolla no se te vaya a quemar.',
                         'resumen_visual': 'Agrega la cebolla picadita a la olla.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['aceite', 'agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Ahora agrega los cuadritos de calabacita y papa, y vacía los 400 '
                                            'ml de agua y una pizquita de sal. Mezcla todo un poquito.',
                         'imagen': 'crema-calabacita-paso6.jpeg',
                         'nota_seguridad': 'Vacía el agua despacito y desde abajo para que no te vaya a salpicar el '
                                           'aceite caliente.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Tapa tu olla y déjala a fuego suave. Vamos a dejar que las verduras '
                                            'hiervan hasta que estén bien tiernitas. Te pondré un aviso en 15 minutos.',
                         'imagen': 'crema-calabacita-paso7.jpeg',
                         'nota_seguridad': 'No te vayas muy lejos de la cocina mientras la lumbre siga prendida.',
                         'resumen_visual': 'Tapa tu olla y déjala a fuego suave.',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado y pica un cuadrito de papa '
                                            'con un tenedor. Si ya está bien suavecito y se deshace fácil, ¡ya están '
                                            'listas las verduras!',
                         'imagen': 'crema-calabacita-paso8.jpeg',
                         'nota_seguridad': 'Destapa la olla levantando la tapa hacia otro lado, para que el vapor '
                                           'caliente no te dé directo en la cara.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'licuadora'],
                         'detalle_hablado': 'Apaga la estufa en este momento. Deja la olla reposar ahí mismo unos 10 '
                                            'minutitos para que las verduras y el caldo se enfríen un poco antes de '
                                            'licuarlas.',
                         'imagen': 'crema-calabacita-paso9.jpeg',
                         'nota_seguridad': 'Verifica con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': 'Apaga la estufa en este momento.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Con ayuda de un cucharón, pasa las verduras y su caldito a la licuadora. '
                                            'Licúa muy bien, por un par de minutos, hasta que te quede una cremita '
                                            'suave, sin grumos.',
                         'imagen': 'crema-calabacita-paso10.jpeg',
                         'nota_seguridad': 'No llenes la licuadora hasta el tope. Ponle un trapo limpio encima a la '
                                           'tapa y sujétala bien con tu mano, porque los líquidos calientes generan '
                                           'presión y pueden botar la tapa.',
                         'resumen_visual': 'Con ayuda de un cucharón, pasa las verduras y su caldito a la licuadora.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Regresa la crema ya licuada a la misma olla. Agrega la taza de leche, una '
                                            'pizca más de sal si hace falta, y enciende la estufa a fuego muy bajito.',
                         'imagen': 'crema-calabacita-paso11.jpeg',
                         'nota_seguridad': 'Vacía la crema despacito para no salpicar.',
                         'resumen_visual': 'Regresa la crema ya licuada a la misma olla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mueve la crema suavecito y constante con tu cuchara. Te pondré 5 '
                                            'minutitos de tiempo para que se caliente muy bien junto con la leche y '
                                            'espese un poquito más.',
                         'imagen': 'crema-calabacita-paso12.jpeg',
                         'nota_seguridad': 'No dejes de mover la olla y no dejes que hierva fuerte, porque la leche '
                                           'sube muy rápido y se te puede derramar.',
                         'resumen_visual': 'Mueve la crema suavecito y constante con tu cuchara.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedó calientita, tersa y deliciosa! Apaga la estufa de inmediato '
                                            'para que no se seque.',
                         'imagen': 'crema-calabacita-paso13.jpeg',
                         'nota_seguridad': 'Revisa otra vez que la perilla de la estufa esté bien apagada.',
                         'resumen_visual': '¡Ya quedó calientita, tersa y deliciosa!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu cremita en un plato hondo o tazón. Tócala tantito con los labios '
                                            'antes de comer para asegurarte de que no esté muy caliente. ¡Que te '
                                            'aproveche mucho!',
                         'imagen': 'crema-calabacita-paso14.jpeg',
                         'nota_seguridad': 'Procura poner un plato extendido debajo de tu tazón para que no te queme '
                                           'las manos al llevarlo a la mesa.',
                         'resumen_visual': 'Sirve tu cremita en un plato hondo o tazón.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'crema-calabacita',
        'tiempo_total_min': 45,
        'titulo': 'Crema de calabacita'},
    {   'descripcion': 'Crema casera de zanahoria y leche, de consistencia muy suave, sabor ligeramente dulce y fácil '
                       'de digerir.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Zanahoria', '400 g'),
                                        ('Papa', '100 g (una papa chica)'),
                                        ('Leche', '250 ml (una taza)'),
                                        ('Agua', '500 ml (dos tazas)'),
                                        ('Aceite de oliva o vegetal', '5 ml (una cucharadita)')],
                            'salsa': [('Cebolla', '30 g (un pedacito)')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a prepararte una cremita de zanahoria muy suavecita y nutritiva. '
                                            'Primero, lávate bien las manos y pon todos tus ingredientes sobre la '
                                            'mesa.',
                         'imagen': 'crema-zanahoria-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar cualquier '
                                           'resbalón al caminar.',
                         'resumen_visual': 'Vamos a prepararte una cremita de zanahoria muy suavecita y nutritiva.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien las zanahorias y la papa. Pélalas con cuidado y córtalas en '
                                            'cuadritos chiquitos o rueditas delgaditas para que se ablanden más '
                                            'rápido.',
                         'imagen': 'crema-zanahoria-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para pelar y picar las '
                                           'verduras sobre una tabla firme.',
                         'resumen_visual': 'Lava muy bien las zanahorias y la papa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pica finamente el pedacito de cebolla. Separa tus verduras en platitos '
                                            'para tenerlas listas y no andar a las prisas.',
                         'imagen': 'crema-zanahoria-paso3.jpeg',
                         'nota_seguridad': 'Hazlo despacito y usa un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Pica finamente el pedacito de cebolla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una olla mediana y agrégale la '
                                            'cucharadita de aceite para que se vaya calentando.',
                         'imagen': 'crema-zanahoria-paso4.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no vayas a tropezar con él al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega la cebolla picadita a la olla. Muévela suavecito con una cuchara '
                                            'de madera. Te pondré un tiempo de 3 minutos para que se fría y quede '
                                            'transparente.',
                         'imagen': 'crema-zanahoria-paso5.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la estufa para que la cebolla no se te vaya a quemar.',
                         'resumen_visual': 'Agrega la cebolla picadita a la olla.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Ahora agrega la zanahoria y la papa, y vacía las dos tazas de '
                                            'agua con una pizquita de sal. Mezcla todo un poquito.',
                         'imagen': 'crema-zanahoria-paso6.jpeg',
                         'nota_seguridad': 'Vacía el agua despacito, desde abajito, para que no te vaya a salpicar la '
                                           'olla caliente.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Tapa tu olla y bájale a la lumbre a un fuego suave. Vamos a dejar que las '
                                            'verduras hiervan hasta que estén muy tiernitas. Te pondré un aviso en 20 '
                                            'minutos.',
                         'imagen': 'crema-zanahoria-paso7.jpeg',
                         'nota_seguridad': 'No te vayas muy lejos de la cocina mientras la lumbre siga prendida.',
                         'resumen_visual': 'Tapa tu olla y bájale a la lumbre a un fuego suave.',
                         'temporizador_segundos': 1200},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado y pica un pedacito de '
                                            'zanahoria con un tenedor. Si ya está bien suavecito y se deshace fácil, '
                                            '¡ya están listas!',
                         'imagen': 'crema-zanahoria-paso8.jpeg',
                         'nota_seguridad': 'Destapa la olla levantando la tapa hacia el otro lado, para que el vapor '
                                           'caliente no te dé directo en la cara.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'licuadora'],
                         'detalle_hablado': 'Apaga la estufa en este momento. Deja la olla reposando ahí mismo unos 10 '
                                            'minutitos para que las verduras y el caldito se enfríen un poco antes de '
                                            'pasarlas a la licuadora.',
                         'imagen': 'crema-zanahoria-paso9.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': 'Apaga la estufa en este momento.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Con ayuda de un cucharón, pasa las verduras y su caldito a la licuadora. '
                                            'Licúa muy bien por un par de minutos, hasta que te quede una cremita muy '
                                            'suave y sin grumos.',
                         'imagen': 'crema-zanahoria-paso10.jpeg',
                         'nota_seguridad': 'No llenes la licuadora hasta el tope. Ponle un trapo limpio encima a la '
                                           'tapa y sujétala bien con tu mano para evitar que brinque por lo caliente.',
                         'resumen_visual': 'Con ayuda de un cucharón, pasa las verduras y su caldito a la licuadora.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'licuadora'],
                         'detalle_hablado': 'Regresa la crema ya licuada a la misma olla. Agrega la taza de leche, '
                                            'prueba de sal, y enciende la estufa a fuego muy bajito.',
                         'imagen': 'crema-zanahoria-paso11.jpeg',
                         'nota_seguridad': 'Vacía la crema despacito para no manchar ni quemarte.',
                         'resumen_visual': 'Regresa la crema ya licuada a la misma olla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mueve la crema suavecito y constante con tu cuchara. Te pondré 5 '
                                            'minutitos de tiempo para que se caliente muy bien y se integre todo.',
                         'imagen': 'crema-zanahoria-paso12.jpeg',
                         'nota_seguridad': 'No dejes de mover la olla y no dejes que hierva fuerte, porque la leche '
                                           'sube muy rápido y se puede derramar.',
                         'resumen_visual': 'Mueve la crema suavecito y constante con tu cuchara.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedó tu cremita, lista y deliciosa! Apaga la estufa de inmediato '
                                            'para que no se seque o se pegue en el fondo.',
                         'imagen': 'crema-zanahoria-paso13.jpeg',
                         'nota_seguridad': 'Revisa otra vez que la perilla de la estufa esté bien apagada.',
                         'resumen_visual': '¡Ya quedó tu cremita, lista y deliciosa!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu crema en un plato hondo o tazón. Tócala tantito con los labios '
                                            'antes de dar la primera cucharada para asegurarte de que no esté muy '
                                            'caliente. ¡Que te aproveche mucho!',
                         'imagen': 'crema-zanahoria-paso14.jpeg',
                         'nota_seguridad': 'Procura poner un plato extendido debajo de tu tazón para que no te queme '
                                           'las manos al llevarlo a la mesa.',
                         'resumen_visual': 'Sirve tu crema en un plato hondo o tazón.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'crema-zanahoria',
        'tiempo_total_min': 50,
        'titulo': 'Crema de zanahoria'},
    {   'descripcion': 'Tortillas suaves bañadas en una rica salsita de frijoles y rellenas de queso fresco. Un '
                       'almuerzo tradicional muy amigable con el estómago.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Tortillas de maíz', '6 piezas'),
                                        ('Queso fresco (panela, canasto o cotija)', '100 g'),
                                        ('Aceite vegetal o manteca', '5 ml (una cucharadita)')],
                            'salsa': [   ('Frijoles cocidos', '300 g (aprox. 1 taza y media)'),
                                         ('Caldo de los frijoles o agua limpia', '200 ml')],
                            'servicio': [('Cebolla picada', '30 g')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unas ricas enfrijoladas, suavecitas y calientitas. '
                                            'Primero, lávate bien las manos y pon tus ingredientes en la mesa.',
                         'imagen': 'enfrijoladas-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar unas ricas enfrijoladas, suavecitas y calientitas.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Desmorona el queso fresco con tus manos bien limpias y pica finamente la '
                                            'cebolla para que sea muy suave de masticar. Sepáralos en platitos.',
                         'imagen': 'enfrijoladas-paso2.jpeg',
                         'nota_seguridad': 'Si sientes las piernas cansadas, siéntate a la mesa para picar la cebolla '
                                           'con calma y sin prisas.',
                         'resumen_visual': 'Desmorona el queso fresco con tus manos bien limpias y pica finamente la '
                                           'cebolla para que sea muy...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Pon los frijoles cocidos y el caldito (o agua) en el vaso de la '
                                            'licuadora. Si los frijoles estaban calientes, déjalos entibiar un poquito '
                                            'antes.',
                         'imagen': 'enfrijoladas-paso3.jpeg',
                         'nota_seguridad': 'Nunca llenes la licuadora hasta el tope, sobre todo si los frijoles están '
                                           'calientes.',
                         'resumen_visual': 'Pon los frijoles cocidos y el caldito (o agua) en el vaso de la licuadora.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa muy bien los frijoles por un par de minutos. Debe quedarte una '
                                            'salsita espesa pero que fluya bien. Si está muy dura, ponle un chorrito '
                                            'más de agua.',
                         'imagen': 'enfrijoladas-paso4.jpeg',
                         'nota_seguridad': 'Ponle un trapo limpio encima a la tapa de la licuadora y sujétala bien con '
                                           'la mano antes de prenderla.',
                         'resumen_visual': 'Licúa muy bien los frijoles por un par de minutos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Si quieres que tus enfrijoladas queden súper lisitas y más fáciles de '
                                            'digerir, puedes pasar la mezcla de la licuadora por un colador.',
                         'imagen': 'enfrijoladas-paso5.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Si quieres que tus enfrijoladas queden súper lisitas y más fáciles de '
                                           'digerir, puedes pasar la me...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una cazuela o olla pequeña y '
                                            'agrégale el poquito de aceite para que se vaya calentando.',
                         'imagen': 'enfrijoladas-paso6.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la cazuela volteado hacia el centro de la estufa para '
                                           'no tropezar con él.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Vacía la salsa de frijoles en la cazuela. Hazlo despacito y con la mano '
                                            'bajita, porque el aceite calientito puede hacer que chille y brinque.',
                         'imagen': 'enfrijoladas-paso7.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si brinca alguna '
                                           'gotita.',
                         'resumen_visual': 'Vacía la salsa de frijoles en la cazuela.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Bájale a la flama de tu estufa para que hierva muy suavecito y mueve los '
                                            'frijoles con una cuchara de madera. Te pongo 5 minutitos para que el '
                                            'sabor se sazone bien.',
                         'imagen': 'enfrijoladas-paso8.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la estufa, la salsa de frijol espesa rápido y puede '
                                           'salpicar o pegarse.',
                         'resumen_visual': 'Bájale a la flama de tu estufa para que hierva muy suavecito y mueve los '
                                           'frijoles con una cuchara...',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras los frijoles están a fuego bajito, enciende otro quemador '
                                            'también a fuego bajo y pon a calentar tu comal.',
                         'imagen': 'enfrijoladas-paso9.jpeg',
                         'nota_seguridad': 'Asegúrate de no traer mangas anchas que puedan rozar con las llamas de la '
                                           'estufa.',
                         'resumen_visual': 'Mientras los frijoles están a fuego bajito, enciende otro quemador también '
                                           'a fuego bajo y pon a c...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Calienta las tortillas de maíz en el comal. Solo queremos que se pongan '
                                            'bien suavecitas y flexibles para que no se rompan al doblarlas.',
                         'imagen': 'enfrijoladas-paso10.jpeg',
                         'nota_seguridad': 'Usa unas pinzas largas para voltear las tortillas en el comal y así evitas '
                                           'quemarte los deditos.',
                         'resumen_visual': 'Calienta las tortillas de maíz en el comal.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Toma una tortilla suavecita con las pinzas y métela a la olla de los '
                                            'frijoles para bañarla muy bien por los dos lados.',
                         'imagen': 'enfrijoladas-paso11.jpeg',
                         'nota_seguridad': 'Haz este paso con mucha calma, escurriendo un poco la tortilla en el borde '
                                           'de la cazuela.',
                         'resumen_visual': 'Toma una tortilla suavecita con las pinzas y métela a la olla de los '
                                           'frijoles para bañarla muy bi...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Pasa la tortilla bañada a tu plato. Ponle un poquito del queso '
                                            'desmoronado en medio y dóblala a la mitad. Repite esto con las demás '
                                            'tortillas.',
                         'imagen': 'enfrijoladas-paso12.jpeg',
                         'nota_seguridad': 'El plato se irá calentando, procura no sostenerlo desde abajo por mucho '
                                           'rato.',
                         'resumen_visual': 'Pasa la tortilla bañada a tu plato.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya armaste tus enfrijoladas! Es momento de apagar la estufa, tanto de '
                                            'los frijoles como del comal.',
                         'imagen': 'enfrijoladas-paso13.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que las dos perillas del gas sí '
                                           'quedaron completamente cerradas.',
                         'resumen_visual': '¡Ya armaste tus enfrijoladas!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Baña las enfrijoladas por encima con un poco más de salsa caliente de la '
                                            'cazuela. Échales arriba el resto del quesito fresco y la cebolla picada.',
                         'imagen': 'enfrijoladas-paso14.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Baña las enfrijoladas por encima con un poco más de salsa caliente de la '
                                           'cazuela.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Deja reposar tu plato unos 2 minutitos para que se enfríen un poco y no '
                                            'te quemes la boca. Te marco el tiempo.',
                         'imagen': 'enfrijoladas-paso15.jpeg',
                         'nota_seguridad': 'Toca la tortilla tantito con los labios antes de dar el primer bocado. '
                                           '¡Buen provecho y que lo disfrutes!',
                         'resumen_visual': 'Deja reposar tu plato unos 2 minutitos para que se enfríen un poco y no te '
                                           'quemes la boca.',
                         'temporizador_segundos': 120}],
        'porciones': 2,
        'slug': 'enfrijoladas-queso',
        'tiempo_total_min': 19,
        'titulo': 'Enfrijoladas con queso'},
    {   'descripcion': 'Frijoles cocidos lentamente con cebolla y ajo, en su caldito. Ideales para acompañar cualquier '
                       'comida o comerlos solitos de la olla.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Frijol seco (pinto, bayo o negro)', '2 tazas (aprox. medio kilo)'),
                                        ('Agua', '8 tazas (o la necesaria)'),
                                        ('Cebolla', 'Un cuarto de pieza'),
                                        ('Ajo', '2 dientes'),
                                        ('Sal', '1 cucharadita (o al gusto)'),
                                        ('Epazote fresco (opcional)', '1 ramita')],
                            'salsa': [],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unos deliciosos frijolitos de la olla. Primero, lávate '
                                            'muy bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'frijoles-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar unos deliciosos frijolitos de la olla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Siéntate a la mesa donde tengas buena luz. Extiende los frijoles crudos '
                                            'en un plato grande o sobre la mesa limpia. Revísalos poco a poco, '
                                            'quitando las piedritas, basuritas o los frijoles que estén picados.',
                         'imagen': 'frijoles-paso2.jpeg',
                         'nota_seguridad': 'Tómate tu tiempo, limpiar los frijoles sentada evita que te canses de la '
                                           'espalda o las piernas.',
                         'resumen_visual': 'Siéntate a la mesa donde tengas buena luz.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pon los frijoles ya limpiecitos en un colador. Enjuágalos bajo el chorro '
                                            'de agua fría, moviéndolos con tu mano hasta que el agua salga clarita y '
                                            'sin polvo.',
                         'imagen': 'frijoles-paso3.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pon los frijoles ya limpiecitos en un colador.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'En una olla grande y honda (si tienes una de barro curada o peltre, '
                                            '¡mucho mejor!), pon los frijoles lavados, el pedazo de cebolla y los dos '
                                            'dientes de ajo pelados.',
                         'imagen': 'frijoles-paso4.jpeg',
                         'nota_seguridad': 'Si usas olla de barro, manéjala con cuidado porque es pesada.',
                         'resumen_visual': 'En una olla grande y honda (si tienes una de barro curada o peltre, ¡mucho '
                                           'mejor!), pon los frijo...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrégale las 8 tazas de agua limpia. El agua debe cubrir los frijoles por '
                                            'al menos cuatro dedos por encima, porque van a esponjar.',
                         'imagen': 'frijoles-paso5.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Agrégale las 8 tazas de agua limpia.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego alto. Vamos a esperar a que el agua empiece a '
                                            'hervir fuerte. Te pondré un aviso de 20 minutos para que vengas a '
                                            'revisar.',
                         'imagen': 'frijoles-paso6.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la lumbre esté prendida a fuego '
                                           'alto.',
                         'resumen_visual': 'Enciende tu estufa a fuego alto.',
                         'temporizador_segundos': 1200},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Cuando veas que el agua ya está hirviendo, bájale a la flama de tu estufa '
                                            'a lo más bajito que se pueda. Tapa tu olla dejando solo una pequeña '
                                            'rendija.',
                         'imagen': 'frijoles-paso7.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Cuando veas que el agua ya está hirviendo, bájale a la flama de tu estufa '
                                           'a lo más bajito que se...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vamos a dejar que los frijolitos se cuezan lentamente. Te pondré un '
                                            'tiempo de 1 hora para que vengas a revisarlos y no tengas que estar '
                                            'parada en la estufa.',
                         'imagen': 'frijoles-paso8.jpeg',
                         'nota_seguridad': 'Siéntate a descansar, yo te aviso cuando pase la hora.',
                         'resumen_visual': 'Vamos a dejar que los frijolitos se cuezan lentamente.',
                         'temporizador_segundos': 3600},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con mucho cuidado. Revisa cómo van de '
                                            'agua. Si ves que el agua bajó mucho, ponle más, pero OJO: el agua que le '
                                            'agregues DEBE estar bien caliente.',
                         'imagen': 'frijoles-paso9.jpeg',
                         'nota_seguridad': 'Levanta la tapa hacia el lado contrario de tu cara para que el vapor no te '
                                           'queme. Y recuerda, no les pongas agua fría porque se pasman y ya no se '
                                           'ablandan.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vuelve a tapar la olla. Te pondré otros 30 minutos para que sigan '
                                            'cociéndose. El tiempo total depende mucho del tipo de frijol, pero con '
                                            'calma quedan muy suaves.',
                         'imagen': 'frijoles-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Vuelve a tapar la olla.',
                         'temporizador_segundos': 1800},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': '¡Pasó el tiempo! Saca un frijolito con una cuchara, sóplale muy bien para '
                                            'no quemarte, y apachúrralo con tus dedos. Si ya está bien suavecito, ¡ya '
                                            'casi terminamos!',
                         'imagen': 'frijoles-paso11.jpeg',
                         'nota_seguridad': 'Si lo sientes duro de en medio, ponle un poco más de agua caliente y '
                                           'déjalos otros 20 minutitos.',
                         'resumen_visual': '¡Pasó el tiempo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Una vez que los frijoles ya están suavecitos, es el momento de agregar la '
                                            'cucharadita de sal y la ramita de epazote bien lavada.',
                         'imagen': 'frijoles-paso12.jpeg',
                         'nota_seguridad': 'La sal siempre se pone hasta que el frijol ya está suave, si se la pones '
                                           'al principio se quedan duros.',
                         'resumen_visual': 'Una vez que los frijoles ya están suavecitos, es el momento de agregar la '
                                           'cucharadita de sal y la...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mueve suavecito con un cucharón. Te pondré los últimos 10 minutos de '
                                            'tiempo para que la sal y el epazote suelten todo su sabor en el caldo.',
                         'imagen': 'frijoles-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Mueve suavecito con un cucharón.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo! Ya quedaron nuestros frijoles de la olla, calientitos y sabrosos. '
                                            'Apaga la estufa de inmediato para que no se siga consumiendo el caldito.',
                         'imagen': 'frijoles-paso14.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada hacia arriba.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Deja tu olla reposando ahí mismo en la estufa unos 10 minutitos para que '
                                            'el caldo agarre más cuerpo y no te vayas a quemar la boca.',
                         'imagen': 'frijoles-paso15.jpeg',
                         'nota_seguridad': 'Si vas a mover la olla, usa siempre unos trapos gruesos, estará hirviendo.',
                         'resumen_visual': 'Deja tu olla reposando ahí mismo en la estufa unos 10 minutitos para que '
                                           'el caldo agarre más cuer...',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tus frijolitos en un plato hondo o taza, con bastante caldito. '
                                            'Tócalos tantito con los labios antes de dar el primer bocado grande. '
                                            '¡Buen provecho y que los disfrutes mucho!',
                         'imagen': 'frijoles-paso16.jpeg',
                         'nota_seguridad': 'Procura poner un platito extendido debajo de tu plato hondo para que no te '
                                           'queme las manos al llevarlo a la mesa.',
                         'resumen_visual': 'Sirve tus frijolitos en un plato hondo o taza, con bastante caldito.',
                         'temporizador_segundos': None}],
        'porciones': 6,
        'slug': 'frijoles-de-la-olla',
        'tiempo_total_min': 142,
        'titulo': 'Frijoles de la olla'},
    {   'descripcion': 'Hotcakes caseros suaves elaborados con avena, plátano y leche, ideales para un desayuno '
                       'sencillo y muy amigable con el estómago.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Avena molida', '100 g'),
                                        ('Plátano maduro', '120 g (un plátano mediano)'),
                                        ('Leche', '120 ml (media taza)'),
                                        ('Polvo para hornear', '4 g (una cucharadita)'),
                                        ('Aceite vegetal o mantequilla', '5 ml (una embarradita)')],
                            'salsa': [],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a prepararte unos hotcakes muy ricos y nutritivos. Primero, lávate '
                                            'bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'hotcakes-avena-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a prepararte unos hotcakes muy ricos y nutritivos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Toma el plátano maduro, pélalo y ponlo en un plato hondo. Con un tenedor, '
                                            'apachúrralo muy bien hasta que quede como una papilla suave, sin pedazos '
                                            'grandes.',
                         'imagen': 'hotcakes-avena-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para apachurrar el '
                                           'plátano con más comodidad.',
                         'resumen_visual': 'Toma el plátano maduro, pélalo y ponlo en un plato hondo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'En un tazón mediano, pon la avena molida y el polvito para hornear. '
                                            'Revuelve un poquito con una cuchara para que se mezclen los polvos.',
                         'imagen': 'hotcakes-avena-paso3.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'En un tazón mediano, pon la avena molida y el polvito para hornear.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Ahí mismo en el tazón, agrega el plátano apachurrado y la media taza de '
                                            'leche. Mezcla todo suavecito hasta que te quede una masita espesa y '
                                            'pareja.',
                         'imagen': 'hotcakes-avena-paso4.jpeg',
                         'nota_seguridad': 'Hazlo con calma, la mezcla no necesita batirse fuerte, solo que se integre '
                                           'todo.',
                         'resumen_visual': 'Ahí mismo en el tazón, agrega el plátano apachurrado y la media taza de '
                                           'leche.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Deja reposar tu masita por 2 minutitos. Esto sirve para que la avena '
                                            'absorba la leche y tus hotcakes queden bien esponjocitos. Te marco el '
                                            'tiempo.',
                         'imagen': 'hotcakes-avena-paso5.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar tu masita por 2 minutitos.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego muy bajito. Pon un sartén de teflón o que no '
                                            'se pegue, y úntale apenas un poquito de aceite o mantequilla con una '
                                            'servilleta limpia.',
                         'imagen': 'hotcakes-avena-paso6.jpeg',
                         'nota_seguridad': 'Acomoda el mango del sartén hacia el centro de la estufa para que no lo '
                                           'vayas a golpear sin querer al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego muy bajito.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Con una cuchara grande, vacía un poquito de masa en el centro del sartén. '
                                            'Haz tus hotcakes más chiquitos de lo normal para que te sea muy fácil '
                                            'voltearlos.',
                         'imagen': 'hotcakes-avena-paso7.jpeg',
                         'nota_seguridad': 'No acerques mucho la mano al sartén caliente al poner la masa.',
                         'resumen_visual': 'Con una cuchara grande, vacía un poquito de masa en el centro del sartén.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Déjalo cocer a fuego muy lento para que no se queme por fuera y quede '
                                            'crudo por dentro. Te pondré 3 minutos de tiempo. Tienes que ver que las '
                                            'orillas se vean secas.',
                         'imagen': 'hotcakes-avena-paso8.jpeg',
                         'nota_seguridad': 'Quédate en la cocina, los hotcakes se pueden quemar muy rápido si te '
                                           'distraes.',
                         'resumen_visual': 'Déjalo cocer a fuego muy lento para que no se queme por fuera y quede '
                                           'crudo por dentro.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Es hora de voltearlo! Mete una espátula ancha por debajo con mucho '
                                            'cuidado y dale la vuelta en un solo movimiento.',
                         'imagen': 'hotcakes-avena-paso9.jpeg',
                         'nota_seguridad': 'Si te tiembla un poquito la mano, ayúdate con una cuchara en la otra mano '
                                           'para sostenerlo por arriba mientras lo volteas.',
                         'resumen_visual': '¡Es hora de voltearlo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vamos a dejarlo que se cueza bien por el otro lado. Te pongo 2 minutitos '
                                            'más para asegurar que el centro quede bien cocido y suavecito.',
                         'imagen': 'hotcakes-avena-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Vamos a dejarlo que se cueza bien por el otro lado.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca tu hotcake y ponlo en un plato. Si tienes más masa, repite los pasos '
                                            'para hacer otro. Cuando termines, apaga tu estufa de inmediato.',
                         'imagen': 'hotcakes-avena-paso11.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': 'Saca tu hotcake y ponlo en un plato.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tus hotcakes de avena calientitos. Córtalos en pedacitos pequeños '
                                            'en tu plato para que no pases trabajo al masticar. ¡Que tengas un muy '
                                            'buen provecho!',
                         'imagen': 'hotcakes-avena-paso12.jpeg',
                         'nota_seguridad': 'Tócalos un poquito con los labios para asegurar que no estén muy calientes '
                                           'antes de dar el primer bocado.',
                         'resumen_visual': 'Sirve tus hotcakes de avena calientitos.',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'hotcakes-avena-platano',
        'tiempo_total_min': 19,
        'titulo': 'Hotcakes de avena y plátano'},
    {   'descripcion': 'Un desayuno tradicional, rápido y muy nutritivo. Huevos revueltitos con jitomate, cebolla y '
                       'chile, suavecitos y fáciles de masticar.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Huevos', '4 piezas'),
                                        ('Jitomate', '1 mediano'),
                                        ('Cebolla', 'Un cuarto de pieza'),
                                        ('Chile serrano o jalapeño', '1 pieza (opcional, al gusto)'),
                                        ('Aceite vegetal o manteca', '1 cucharada')],
                            'salsa': [('Sal', 'Una pizca')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un almuerzo muy tradicional. Primero, lávate bien las '
                                            'manos y pon todos tus ingredientes a la mano sobre la mesa.',
                         'imagen': 'mexicana-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar cualquier '
                                           'resbalón.',
                         'resumen_visual': 'Vamos a preparar un almuerzo muy tradicional.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Lava muy bien el jitomate, el chile y el pedacito de cebolla. Escúrrelos '
                                            'un poco.',
                         'imagen': 'mexicana-paso2.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Lava muy bien el jitomate, el chile y el pedacito de cebolla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pica el jitomate y la cebolla en cuadritos muy finitos para que casi no '
                                            'se sientan al masticar. Ponlos en un platito.',
                         'imagen': 'mexicana-paso3.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar todo con calma '
                                           'sobre una tabla firme.',
                         'resumen_visual': 'Pica el jitomate y la cebolla en cuadritos muy finitos para que casi no se '
                                           'sientan al masticar.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Si vas a usar el chile, quítale las semillas y las venitas para que no '
                                            'pique tanto, y córtalo en pedacitos muy chiquitos.',
                         'imagen': 'mexicana-paso4.jpeg',
                         'nota_seguridad': 'Lávate muy bien las manos con agua y jabón después de picar el chile para '
                                           'no enchilarte los ojos.',
                         'resumen_visual': 'Si vas a usar el chile, quítale las semillas y las venitas para que no '
                                           'pique tanto, y córtalo en...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Rompe los 4 huevos en un plato hondo. Agrégales la pizca de sal y bátelos '
                                            'suavemente con un tenedor hasta que la yema y la clara se junten. Hacer '
                                            'esto antes de prender la estufa evita que andes a las prisas.',
                         'imagen': 'mexicana-paso5.jpeg',
                         'nota_seguridad': 'Si cae un pedacito de cascarón, sácalo con ayuda de una de las mitades de '
                                           'la misma cáscara.',
                         'resumen_visual': 'Rompe los 4 huevos en un plato hondo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Ahora sí, enciende tu estufa a fuego medio. Pon una sartén y agrégale la '
                                            'cucharada de aceite para que se vaya calentando.',
                         'imagen': 'mexicana-paso6.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la sartén volteado hacia el centro de la estufa para '
                                           'que no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Ahora sí, enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega con cuidado la cebolla y el chile picados a la sartén. Muévelos '
                                            'con una cuchara de madera. Te pondré un tiempo de 2 minutos para que se '
                                            'acitronen.',
                         'imagen': 'mexicana-paso7.jpeg',
                         'nota_seguridad': 'No te alejes de la estufa y mantén tu cara un poco alejada por si el '
                                           'aceite salpica.',
                         'resumen_visual': 'Agrega con cuidado la cebolla y el chile picados a la sartén.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['aceite', 'cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Ahora vacía el jitomate picado a la sartén. Revuelve todo junto '
                                            'para que el jitomate suelte su juguito. Te pondré 3 minutos más.',
                         'imagen': 'mexicana-paso8.jpeg',
                         'nota_seguridad': 'Al echar el jitomate va a chillar la sartén, hazlo desde abajito para '
                                           'evitar brincos de aceite.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Cuando el jitomate ya se vea suavecito y como un puré, bájale un poco al '
                                            'fuego. Vacía los huevos batidos sobre toda la verdura.',
                         'imagen': 'mexicana-paso9.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Cuando el jitomate ya se vea suavecito y como un puré, bájale un poco al '
                                           'fuego.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mueve los huevos despacio desde las orillas hacia el centro, para que te '
                                            'queden esponjositos y no se resequen. Te aviso en 2 minutos para que veas '
                                            'si ya están a tu gusto.',
                         'imagen': 'mexicana-paso10.jpeg',
                         'nota_seguridad': 'Raspa suavemente el fondo de la sartén para que el huevo no se pegue.',
                         'resumen_visual': 'Mueve los huevos despacio desde las orillas hacia el centro, para que te '
                                           'queden esponjositos y no...',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedaron listos! Apaga la estufa de inmediato para que el huevo no se '
                                            'te ponga duro ni seco.',
                         'imagen': 'mexicana-paso11.jpeg',
                         'nota_seguridad': 'Por favor, verifica con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': '¡Ya quedaron listos!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tus huevitos a la mexicana calientitos en un plato. Los puedes '
                                            'acompañar con unos frijolitos de la olla o unas tortillas. ¡Que tengas un '
                                            'excelente almuerzo!',
                         'imagen': 'mexicana-paso12.jpeg',
                         'nota_seguridad': 'Toca la comida un poquito con los labios antes de dar el primer bocado '
                                           'para asegurar que no te queme.',
                         'resumen_visual': 'Sirve tus huevitos a la mexicana calientitos en un plato.',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'huevos-a-la-mexicana',
        'tiempo_total_min': 19,
        'titulo': 'Huevos a la mexicana'},
    {   'descripcion': 'Un guisito de lentejas con zanahoria y jitomate muy casero, nutritivo y suavecito para el '
                       'estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Lentejas secas', '250 g (aprox. 1 taza y media)'),
                                        ('Zanahoria', '150 g (1 grande o 2 chicas)'),
                                        ('Agua', '1.5 litros'),
                                        ('Aceite vegetal o de oliva', '5 ml (una cucharadita)')],
                            'salsa': [   ('Jitomate', '200 g (2 medianos)'),
                                         ('Cebolla', '50 g (un pedazo pequeño)'),
                                         ('Ajo', '1 diente'),
                                         ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unas lentejas muy sabrosas y fáciles de masticar. '
                                            'Primero, lávate bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'lentejas-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar unas lentejas muy sabrosas y fáciles de masticar.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Siéntate a la mesa donde tengas buena luz. Extiende las lentejas crudas '
                                            'en un plato y revísalas poco a poco, quitando las piedritas o basuritas '
                                            'que lleguen a traer.',
                         'imagen': 'lentejas-paso2.jpeg',
                         'nota_seguridad': 'Hacer esto sentada evita que te canses de las piernas o la espalda.',
                         'resumen_visual': 'Siéntate a la mesa donde tengas buena luz.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pon las lentejas ya limpiecitas en un colador. Enjuágalas bajo el chorro '
                                            'de agua fría, frotándolas suavemente hasta que el agua salga clara y sin '
                                            'polvo.',
                         'imagen': 'lentejas-paso3.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pon las lentejas ya limpiecitas en un colador.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Ahí mismo sentada en la mesa, pela tu zanahoria, lávala y córtala en '
                                            'cuadritos muy chiquitos. Así se cocerán rápido y serán muy suaves de '
                                            'comer.',
                         'imagen': 'lentejas-paso4.jpeg',
                         'nota_seguridad': 'Usa una tabla firme y un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Ahí mismo sentada en la mesa, pela tu zanahoria, lávala y córtala en '
                                           'cuadritos muy chiquitos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Lava muy bien los jitomates, quítales el ombliguito y pártelos en '
                                            'cuartos. Ponlos en el vaso de la licuadora junto con la cebolla, el ajo '
                                            'pelado y media tacita de agua.',
                         'imagen': 'lentejas-paso5.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Lava muy bien los jitomates, quítales el ombliguito y pártelos en cuartos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa todo muy bien hasta que te quede una salsita de jitomate suave, sin '
                                            'grumos grandes. Déjala ahí lista en el vaso.',
                         'imagen': 'lentejas-paso6.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa a la licuadora antes de encenderla.',
                         'resumen_visual': 'Licúa todo muy bien hasta que te quede una salsita de jitomate suave, sin '
                                           'grumos grandes.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Ahora sí, enciende tu estufa a fuego medio. Pon una olla mediana o '
                                            'cazuela y agrégale la cucharadita de aceite para que se caliente.',
                         'imagen': 'lentejas-paso7.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Ahora sí, enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Vacía con mucho cuidado la salsa de la licuadora en la olla. Hazlo '
                                            'despacito y desde abajito, porque el aceite caliente puede hacer que '
                                            'chille y brinque.',
                         'imagen': 'lentejas-paso8.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa para que no te '
                                           'salpique.',
                         'resumen_visual': 'Vacía con mucho cuidado la salsa de la licuadora en la olla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mueve la salsita con una cuchara de madera. Te pondré 5 minutitos para '
                                            'que hierva, el jitomate cambie a un rojo más oscuro y agarre buen sabor.',
                         'imagen': 'lentejas-paso9.jpeg',
                         'nota_seguridad': 'No te alejes de la estufa mientras el jitomate se fríe.',
                         'resumen_visual': 'Mueve la salsita con una cuchara de madera.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Agrega a la olla las lentejas escurridas, la zanahoria picadita y '
                                            'vacía el litro y medio de agua limpia. Revuelve todo suavecito.',
                         'imagen': 'lentejas-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Espera a que el agua empiece a hervir fuerte. Cuando veas las burbujas '
                                            'grandes, bájale a la flama a un fuego muy suavecito y tapa tu olla '
                                            'dejando una pequeña rendija.',
                         'imagen': 'lentejas-paso11.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Espera a que el agua empiece a hervir fuerte.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vamos a dejar que las lentejas se cuezan lentamente. Te pondré un aviso '
                                            'de 30 minutos para que vengas a revisarlas.',
                         'imagen': 'lentejas-paso12.jpeg',
                         'nota_seguridad': 'Ve a sentarte y descansar, no te quedes de pie junto a la estufa '
                                           'esperando.',
                         'resumen_visual': 'Vamos a dejar que las lentejas se cuezan lentamente.',
                         'temporizador_segundos': 1800},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado. Revisa si les falta agua; '
                                            'si es así, agrégales media tacita de agua caliente. Ponles la sal a tu '
                                            'gusto, revuelve y te pongo otros 15 minutitos.',
                         'imagen': 'lentejas-paso13.jpeg',
                         'nota_seguridad': 'Al destapar la olla, hazlo con la tapa apuntando hacia otro lado para que '
                                           'el vapor caliente no te dé en la cara.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca unas cuantas lentejas con una cuchara, sóplales muy bien y '
                                            'apachúrralas con tus dedos. Si ya están bien suavecitas, ¡ya quedó '
                                            'nuestro guisado!',
                         'imagen': 'lentejas-paso14.jpeg',
                         'nota_seguridad': 'Si aún las sientes duritas del centro, déjalas otros 10 minutos tapadas a '
                                           'fuego suave.',
                         'resumen_visual': 'Saca unas cuantas lentejas con una cuchara, sóplales muy bien y '
                                           'apachúrralas con tus dedos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Apaga la estufa de inmediato para que tu caldito no se vaya a consumir y '
                                            'las lentejas no se sequen.',
                         'imagen': 'lentejas-paso15.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': 'Apaga la estufa de inmediato para que tu caldito no se vaya a consumir y '
                                           'las lentejas no se sequen.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar la olla unos 5 minutitos en la estufa apagada para que el '
                                            'caldo espese un poquito más y no te vayas a quemar la boca.',
                         'imagen': 'lentejas-paso16.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar la olla unos 5 minutitos en la estufa apagada para que el '
                                           'caldo espese un poquito má...',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': '¡A comer rico! Sirve tus lentejitas calientitas en un plato hondo. Si te '
                                            'cuesta un poquito masticar, puedes aplastar algunas en tu mismo plato con '
                                            'un tenedor. ¡Buen provecho!',
                         'imagen': 'lentejas-paso17.jpeg',
                         'nota_seguridad': 'Toca el caldito con los labios antes de dar la primera cucharada grande '
                                           'para asegurarte de que ya no quema.',
                         'resumen_visual': '¡A comer rico!',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'lentejas-guisadas-zanahoria',
        'tiempo_total_min': 67,
        'titulo': 'Lentejas guisadas con zanahoria'},
    {   'descripcion': 'Pan con frijoles refritos y quesito Oaxaca derretido, preparados con una textura suave y muy '
                       'fáciles de comer.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Bolillos pequeños', '2 piezas'),
                                        ('Frijoles cocidos y escurridos', '160 g (como una taza chiquita)'),
                                        ('Queso Oaxaca deshebrado', '80 g'),
                                        ('Agua o caldito de frijol', '30 ml (unas dos cucharadas)')],
                            'salsa': [],
                            'servicio': [('Jitomate picado', '60 g (un jitomate chico)')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a prepararte unos ricos molletes. Primero, lávate bien las manos y '
                                            'pon todos tus ingredientes en la mesa para que no des muchas vueltas.',
                         'imagen': 'molletes-paso1.jpeg',
                         'nota_seguridad': 'Revisa que el piso de la cocina esté bien seco para evitar resbalones.',
                         'resumen_visual': 'Vamos a prepararte unos ricos molletes.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Toma los bolillos y córtalos por la mitad a lo largo con un cuchillo de '
                                            'sierra. Si sientes que la costra de arriba está muy dura, puedes '
                                            'quitársela un poquito con la mano para que no te cueste trabajo masticar.',
                         'imagen': 'molletes-paso2.jpeg',
                         'nota_seguridad': 'Apoya bien el pan en una tabla firme sobre la mesa para cortarlo sin '
                                           'peligro.',
                         'resumen_visual': 'Toma los bolillos y córtalos por la mitad a lo largo con un cuchillo de '
                                           'sierra.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien el jitomate y pícalo en cuadritos chiquitos. Deshebra el '
                                            'queso Oaxaca con tus manos limpias y pon todo separadito en platitos.',
                         'imagen': 'molletes-paso3.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar y deshebrar '
                                           'con toda la calma.',
                         'resumen_visual': 'Lava muy bien el jitomate y pícalo en cuadritos chiquitos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego bajo. Pon un sartén chiquito u ollita y agrega '
                                            'los frijoles cocidos junto con las dos cucharadas de agua (o caldito de '
                                            'frijol).',
                         'imagen': 'molletes-paso4.jpeg',
                         'nota_seguridad': 'Voltea el mango del sartén hacia el centro de la estufa para que no vayas '
                                           'a chocar con él.',
                         'resumen_visual': 'Enciende tu estufa a fuego bajo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Con un machacador de frijoles o un tenedor fuerte, aplasta los frijoles '
                                            'ahí mismo en el sartén hasta que te quede una pastita muy suave, como un '
                                            'puré. Te pongo 3 minutos para que se calienten bien.',
                         'imagen': 'molletes-paso5.jpeg',
                         'nota_seguridad': 'Mueve el sartén con cuidado para evitar que los frijoles brinque o se '
                                           'peguen al fondo.',
                         'resumen_visual': 'Con un machacador de frijoles o un tenedor fuerte, aplasta los frijoles '
                                           'ahí mismo en el sartén ha...',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo! Ya quedaron bien suavecitos. Apaga la estufa en este momento para '
                                            'que los frijoles no se resequen.',
                         'imagen': 'molletes-paso6.jpeg',
                         'nota_seguridad': 'Asegúrate de que la perilla de la estufa sí quedó completamente cerrada.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Con ayuda de una cuchara, úntales una capa generosa de tus frijolitos '
                                            'calientes a las mitades de bolillo.',
                         'imagen': 'molletes-paso7.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Con ayuda de una cuchara, úntales una capa generosa de tus frijolitos '
                                           'calientes a las mitades de...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Ponle encima a cada panecito un buen puño del queso Oaxaca deshebrado, '
                                            'repartiéndolo bien por todo el pan.',
                         'imagen': 'molletes-paso8.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ponle encima a cada panecito un buen puño del queso Oaxaca deshebrado, '
                                           'repartiéndolo bien por tod...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'horno'],
                         'detalle_hablado': 'Para derretir el queso de forma segura, vamos a usar un comal o un sartén '
                                            'grande con tapa. Enciende tu estufa a fuego muy, muy bajito.',
                         'imagen': 'molletes-paso9.jpeg',
                         'nota_seguridad': 'Usar el comal tapado a fuego muy bajo es más seguro y fácil que usar el '
                                           'horno de la estufa.',
                         'resumen_visual': 'Para derretir el queso de forma segura, vamos a usar un comal o un sartén '
                                           'grande con tapa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Acomoda tus molletes en el comal y ponles una tapa grande encima (puede '
                                            'ser la tapa de una olla). Te pondré un tiempo de 5 minutos para que el '
                                            'pan se caliente y el quesito se derrita con el vapor.',
                         'imagen': 'molletes-paso10.jpeg',
                         'nota_seguridad': 'No dejes la cocina sola, quédate cerquita para cuidar que el pan no se '
                                           'vaya a quemar de abajo.',
                         'resumen_visual': 'Acomoda tus molletes en el comal y ponles una tapa grande encima (puede '
                                           'ser la tapa de una olla).',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Revisa que el queso esté bien derretido. Si ya está '
                                            'listo, apaga la estufa de inmediato.',
                         'imagen': 'molletes-paso11.jpeg',
                         'nota_seguridad': 'Destapa el comal con cuidado, levantando la tapa hacia un lado para no '
                                           'quemarte con el vaporcito.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pasa los molletes a tu plato usando una espátula ancha. Déjalos reposar '
                                            'unos 2 minutitos para que el queso y los frijoles no te vayan a quemar la '
                                            'boca. Te marco el tiempo.',
                         'imagen': 'molletes-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pasa los molletes a tu plato usando una espátula ancha.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Ponle encima su jitomatito picado a cada mollete. Córtalos en pedacitos '
                                            'más chicos ahí mismo en tu plato para comerlos muy a gusto. ¡Que tengas '
                                            'un excelente almuerzo!',
                         'imagen': 'molletes-paso13.jpeg',
                         'nota_seguridad': 'Tócalos un poquito con los labios antes de dar el primer bocado para '
                                           'asegurar que la temperatura esté agradable.',
                         'resumen_visual': 'Ponle encima su jitomatito picado a cada mollete.',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'molletes-frijoles-queso',
        'tiempo_total_min': 22,
        'titulo': 'Molletes de frijoles y queso'},
    {   'descripcion': 'Filete de pescado blanco muy blandito, cocido al vapor con zanahoria y calabacita. Muy ligero '
                       'y fácil de digerir.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   (   'Filete de pescado blanco (como tilapia o mojarra)',
                                            '300 g (2 filetes medianos)'),
                                        ('Zanahoria', '100 g (una chica)'),
                                        ('Calabacita', '150 g (una mediana)'),
                                        ('Agua', '500 ml (dos tazas, para la olla)')],
                            'salsa': [   ('Limón', 'El jugo de medio limón'),
                                         ('Aceite de oliva', '5 ml (una cucharadita)'),
                                         ('Sal y pimienta (opcional)', 'Una pizquita')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': ['vapor'],
                         'detalle_hablado': 'Vamos a prepararte un pescadito al vapor, muy sano y suavecito. Primero, '
                                            'lávate bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'pescado-vapor-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a prepararte un pescadito al vapor, muy sano y suavecito.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pela tu zanahoria, lávala y córtala en rueditas muy delgaditas para que '
                                            'se ablanden rápido.',
                         'imagen': 'pescado-vapor-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar las verduras '
                                           'con calma sobre una tabla firme.',
                         'resumen_visual': 'Pela tu zanahoria, lávala y córtala en rueditas muy delgaditas para que se '
                                           'ablanden rápido.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava la calabacita, quítale las puntas y córtala también en rueditas '
                                            'delgadas. Ponlas en un platito junto con la zanahoria.',
                         'imagen': 'pescado-vapor-paso3.jpeg',
                         'nota_seguridad': 'Hazlo despacio y usa un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Lava la calabacita, quítale las puntas y córtala también en rueditas '
                                           'delgadas.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pasa tus deditos limpios por todo el filete de pescado, apachurrando '
                                            'suavemente, para revisar que no traiga ninguna espina escondida.',
                         'imagen': 'pescado-vapor-paso4.jpeg',
                         'nota_seguridad': 'Si encuentras una espina, quítala con cuidado. Lávate las manos '
                                           'inmediatamente después de tocar el pescado crudo.',
                         'resumen_visual': 'Pasa tus deditos limpios por todo el filete de pescado, apachurrando '
                                           'suavemente, para revisar que...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Pon tu olla en la estufa. Vacía las dos tazas de agua en el fondo y '
                                            'coloca tu rejilla vaporera (la canastita de metal) encima. El agua no '
                                            'debe tapar la rejilla.',
                         'imagen': 'pescado-vapor-paso5.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Pon tu olla en la estufa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Acomoda sobre la rejilla los filetes de pescado y las verduras, tratando '
                                            'de que no queden muy amontonados. Ponles su pizquita de sal si te gusta.',
                         'imagen': 'pescado-vapor-paso6.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Acomoda sobre la rejilla los filetes de pescado y las verduras, tratando '
                                           'de que no queden muy amo...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Tapa tu olla y enciende la estufa a fuego medio. Vamos a dejar que el '
                                            'vapor cocine todo. Te pondré un tiempo de 15 minutos para que vengas a '
                                            'revisar.',
                         'imagen': 'pescado-vapor-paso7.jpeg',
                         'nota_seguridad': 'No te alejes de la cocina mientras la lumbre esté prendida.',
                         'resumen_visual': 'Tapa tu olla y enciende la estufa a fuego medio.',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con mucho cuidado. Revisa si el pescado '
                                            'ya se ve todo blanco (que no se vea transparente) y pica una zanahoria '
                                            'con el tenedor para ver si ya está suave.',
                         'imagen': 'pescado-vapor-paso8.jpeg',
                         'nota_seguridad': 'Levanta la tapa hacia el lado contrario de tu cara, para que el vapor '
                                           'caliente no te dé directo en los ojos ni te queme.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Si ya todo está bien suavecito y cocido, apaga la estufa en este momento.',
                         'imagen': 'pescado-vapor-paso9.jpeg',
                         'nota_seguridad': 'Verifica muy bien con tus propios ojos que la perilla del gas sí quedó '
                                           'completamente cerrada.',
                         'resumen_visual': 'Si ya todo está bien suavecito y cocido, apaga la estufa en este momento.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Con ayuda de una espátula ancha, saca tu filete y tus verduras y ponlas '
                                            'en tu plato. Hazlo con mucho cuidado porque está caliente y el pescado se '
                                            'desbarata fácil.',
                         'imagen': 'pescado-vapor-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Con ayuda de una espátula ancha, saca tu filete y tus verduras y ponlas en '
                                           'tu plato.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Ahí en tu plato, desmenuza el filete en pedacitos pequeños con tu '
                                            'tenedor. Esta es una segunda oportunidad para revisar que no se haya ido '
                                            'ninguna espinita.',
                         'imagen': 'pescado-vapor-paso11.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ahí en tu plato, desmenuza el filete en pedacitos pequeños con tu tenedor.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite'],
                         'detalle_hablado': 'Échale unas gotitas de limón al pescado, un chorrito de aceite de oliva '
                                            'por encima y ¡a comer rico! Tócalo con los labios primero para asegurar '
                                            'que ya no quema.',
                         'imagen': 'pescado-vapor-paso12.jpeg',
                         'nota_seguridad': 'Procura poner tu plato hondo sobre uno extendido para que no te quemes las '
                                           'manos al llevarlo a la mesa.',
                         'resumen_visual': 'Échale unas gotitas de limón al pescado, un chorrito de aceite de oliva '
                                           'por encima y ¡a comer rico!',
                         'temporizador_segundos': None}],
        'porciones': 2,
        'slug': 'pescado-vapor-verduras',
        'tiempo_total_min': 27,
        'titulo': 'Pescado al vapor con verduras'},
    {   'descripcion': 'Carne molida de res guisada con papa, zanahoria y jitomate. Preparado jugosito, bien cocido y '
                       'con verduras muy picaditas para que sea suave y fácil de comer.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Carne molida de res magra', '400 g'),
                                        ('Papa', '200 g (una grande o dos chicas)'),
                                        ('Zanahoria', '120 g (una mediana)'),
                                        ('Agua', '300 ml (taza y media)'),
                                        ('Aceite vegetal', '5 ml (una cucharadita)')],
                            'salsa': [   ('Jitomate', '250 g (dos medianos)'),
                                         ('Cebolla', '40 g (un pedacito)'),
                                         ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Vamos a preparar un picadillo de res muy rico, jugosito y seguro para tu '
                                            'estómago. Primero, lávate bien las manos y pon todos tus ingredientes en '
                                            'la mesa.',
                         'imagen': 'picadillo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar un picadillo de res muy rico, jugosito y seguro para tu '
                                           'estómago.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pela tu papa y la zanahoria. Córtalas en cuadritos muy, muy chiquitos '
                                            'para que se cuezan rápido y te sean muy fáciles de masticar.',
                         'imagen': 'picadillo-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar la verdura con '
                                           'calma sobre una tabla firme.',
                         'resumen_visual': 'Pela tu papa y la zanahoria.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Lava muy bien los jitomates, quítales el ombliguito y pártelos en '
                                            'cuartos. Ponlos en el vaso de la licuadora con el pedacito de cebolla y '
                                            'media tacita del agua.',
                         'imagen': 'picadillo-paso3.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Lava muy bien los jitomates, quítales el ombliguito y pártelos en cuartos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa todo muy bien por un minuto hasta que te quede una salsa de '
                                            'jitomate suave y sin grumos grandes. Déjala lista en la licuadora.',
                         'imagen': 'picadillo-paso4.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa de la licuadora antes de prenderla.',
                         'resumen_visual': 'Licúa todo muy bien por un minuto hasta que te quede una salsa de jitomate '
                                           'suave y sin grumos gra...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Ahora sí, enciende tu estufa a fuego medio. Pon una cazuela u olla '
                                            'extendida y agrégale la cucharadita de aceite para que se vaya '
                                            'calentando.',
                         'imagen': 'picadillo-paso5.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no vayas a tropezar con él al pasar.',
                         'resumen_visual': 'Ahora sí, enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega con cuidado la carne molida a la olla. Con una cuchara de madera, '
                                            've desbaratando las bolitas para que quede suelta. Es muy importante '
                                            'cocinarla hasta que no quede ninguna parte rosada o cruda. Te pongo 8 '
                                            'minutos.',
                         'imagen': 'picadillo-paso6.jpeg',
                         'nota_seguridad': 'Lávate las manos inmediatamente después de tocar la carne cruda. Usa una '
                                           'cuchara limpia para probar, nunca la misma con la que moviste la carne '
                                           'cruda.',
                         'resumen_visual': 'Agrega con cuidado la carne molida a la olla.',
                         'temporizador_segundos': 480},
                     {   'alertas_seguridad': ['estufa', 'licuadora'],
                         'detalle_hablado': 'Cuando veas que la carne ya está bien cocida de un color café parejo, '
                                            'vacíale la salsa de jitomate que licuaste. Hazlo despacito y desde '
                                            'abajito.',
                         'imagen': 'picadillo-paso7.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si brinca alguna '
                                           'gotita caliente.',
                         'resumen_visual': 'Cuando veas que la carne ya está bien cocida de un color café parejo, '
                                           'vacíale la salsa de jitomat...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Revuelve bien todo y deja que la salsa hierva un poco para que el '
                                            'jitomate agarre buen sabor y color. Te aviso en 5 minutos.',
                         'imagen': 'picadillo-paso8.jpeg',
                         'nota_seguridad': 'No dejes la cuchara dentro de la olla caliente para que no te quemes al '
                                           'volver a agarrarla.',
                         'resumen_visual': 'Revuelve bien todo y deja que la salsa hierva un poco para que el jitomate '
                                           'agarre buen sabor y co...',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Ahora agrega la papa y la zanahoria picaditas. Vacía el resto del '
                                            'agua y ponle su sal a tu gusto. Revuelve todo muy suavecito.',
                         'imagen': 'picadillo-paso9.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Espera a que veas que el caldito empieza a hervir de nuevo. Entonces, '
                                            'bájale a la flama a un fuego muy suavecito y tapa tu olla dejando solo '
                                            'una pequeña rendija.',
                         'imagen': 'picadillo-paso10.jpeg',
                         'nota_seguridad': 'Evita que el guiso se quede sin líquido, si lo ves muy seco, ponle un '
                                           'chorrito más de agua tibia.',
                         'resumen_visual': 'Espera a que veas que el caldito empieza a hervir de nuevo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Vamos a dejar que el picadillo se cueza lentamente para que quede bien '
                                            'suavecito. Te pondré un aviso de 20 minutos para que vengas a revisarlo.',
                         'imagen': 'picadillo-paso11.jpeg',
                         'nota_seguridad': 'Ve a sentarte y descansar, no te quedes de pie esperando junto a la '
                                           'estufa.',
                         'resumen_visual': 'Vamos a dejar que el picadillo se cueza lentamente para que quede bien '
                                           'suavecito.',
                         'temporizador_segundos': 1200},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado. Saca un cuadrito de papa, '
                                            'sóplale bien y apachúrralo; si ya está muy suavecito y el guiso se ve '
                                            'jugoso, ¡ya quedó!',
                         'imagen': 'picadillo-paso12.jpeg',
                         'nota_seguridad': 'Al destapar la olla, hazlo con la tapa apuntando hacia el otro lado para '
                                           'que el vapor caliente no te dé en la cara.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Apaga la estufa de inmediato para que el picadillo no se seque y te quede '
                                            'con bastante caldito rico.',
                         'imagen': 'picadillo-paso13.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': 'Apaga la estufa de inmediato para que el picadillo no se seque y te quede '
                                           'con bastante caldito rico.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar la olla unos 5 minutitos en la estufa apagada para que el '
                                            'guisado espese tantito y no te vayas a quemar la boca al comer.',
                         'imagen': 'picadillo-paso14.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar la olla unos 5 minutitos en la estufa apagada para que el '
                                           'guisado espese tantito y n...',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': '¡A comer rico! Sirve tu picadillo calientito y jugosito en un plato '
                                            'hondo. Tócalo tantito con los labios antes de dar el primer bocado para '
                                            'asegurar que la temperatura esté agradable. ¡Buen provecho!',
                         'imagen': 'picadillo-paso15.jpeg',
                         'nota_seguridad': 'Procura poner tu plato hondo sobre uno extendido para que no te queme las '
                                           'manos al llevarlo a la mesa.',
                         'resumen_visual': '¡A comer rico!',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'picadillo-res-verduras',
        'tiempo_total_min': 50,
        'titulo': 'Picadillo de res con verduras'},
    {   'descripcion': 'Pollo cocido y deshebrado finamente con una salsita verde de pepitas y tomatillo. Un guisado '
                       'casero, muy nutritivo, sin picante y con una textura muy suave para su estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Pechuga de pollo sin hueso', '450 g (aprox. dos pechugas chicas)'),
                                        ('Agua', '700 ml (unas tres tazas)'),
                                        ('Aceite vegetal o manteca', '5 ml (una cucharadita)')],
                            'salsa': [   ('Tomatillos verdes', '300 g (unos 6 o 7 tomatillos)'),
                                         ('Pepitas de calabaza (sin cáscara)', '60 g (como un puñito)'),
                                         ('Cebolla', '50 g (un pedazo para cocer el pollo y otro para la salsa)'),
                                         ('Cilantro fresco', '15 g (unas cuantas ramitas)'),
                                         ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un rico pipián verde. Primero, lávate muy bien las manos '
                                            'y pon todos tus ingredientes a la mano sobre la mesa.',
                         'imagen': 'pipian-pollo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para que no haya '
                                           'riesgo de resbalones.',
                         'resumen_visual': 'Vamos a preparar un rico pipián verde.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo'],
                         'detalle_hablado': 'En una olla mediana, pon la pechuga de pollo, un pedacito de la cebolla, '
                                            'sal al gusto y vacía casi toda el agua. Deja una taza de agua reservada.',
                         'imagen': 'pipian-pollo-paso2.jpeg',
                         'nota_seguridad': 'Recuerda no lavar el pollo crudo en el fregadero para evitar salpicar. '
                                           'Lávate bien las manos después de ponerlo en la olla.',
                         'resumen_visual': 'En una olla mediana, pon la pechuga de pollo, un pedacito de la cebolla, '
                                           'sal al gusto y vacía cas...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio y pon la olla. Vamos a dejar que el '
                                            'pollo se cueza muy bien por dentro. Te pondré un tiempo de 25 minutos.',
                         'imagen': 'pipian-pollo-paso3.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear sin querer.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio y pon la olla.',
                         'temporizador_segundos': 1500},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras el pollo se cuece, vamos a tostar las pepitas. Pon un sartén en '
                                            'otra hornilla a fuego muy, muy bajito.',
                         'imagen': 'pipian-pollo-paso4.jpeg',
                         'nota_seguridad': 'Asegúrate de no traer mangas anchas que puedan rozar con las llamas.',
                         'resumen_visual': 'Mientras el pollo se cuece, vamos a tostar las pepitas.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Echa las pepitas de calabaza al sartén sin aceite. Muévelas '
                                            'constantemente con una cuchara de madera hasta que se inflen un poquito y '
                                            'huelan a tostado. Tardan como 3 o 4 minutos.',
                         'imagen': 'pipian-pollo-paso5.jpeg',
                         'nota_seguridad': 'No te descuides ni dejes de moverlas, las pepitas se queman muy rápido y '
                                           'pueden amargar tu comida.',
                         'resumen_visual': 'Echa las pepitas de calabaza al sartén sin aceite.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Saca las pepitas tostadas del sartén rápido, ponlas en un platito y apaga '
                                            'esa hornilla.',
                         'imagen': 'pipian-pollo-paso6.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Saca las pepitas tostadas del sartén rápido, ponlas en un platito y apaga '
                                           'esa hornilla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Lava muy bien los tomatillos y las ramitas de cilantro. En una ollita '
                                            'pequeña, pon a hervir los tomatillos con la taza de agua que reservaste. '
                                            'Te aviso en 10 minutos para que los saques, deben estar suaves y de color '
                                            'verde pálido.',
                         'imagen': 'pipian-pollo-paso7.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Lava muy bien los tomatillos y las ramitas de cilantro.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': '¡Sonó la alarma del pollo! Saca la pechuga de la olla, ponla en un plato '
                                            'y déjala enfriar un buen rato. No tires el caldo, lo vamos a ocupar para '
                                            'la salsa.',
                         'imagen': 'pipian-pollo-paso8.jpeg',
                         'nota_seguridad': 'Usa unas pinzas para sacar el pollo del caldo hirviendo, nunca metas las '
                                           'manos ni los tenedores cortos.',
                         'resumen_visual': '¡Sonó la alarma del pollo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora', 'vapor'],
                         'detalle_hablado': 'Pon en la licuadora las pepitas tostadas, los tomatillos hervidos (sin su '
                                            'agua), el cilantro, el otro pedacito de cebolla y dos tazas del caldo de '
                                            'pollo. Licúa muy bien por un buen rato hasta que quede una salsa '
                                            'completamente lisa y homogénea.',
                         'imagen': 'pipian-pollo-paso9.jpeg',
                         'nota_seguridad': 'Como el caldo está caliente, ponle un trapo limpio encima a la tapa de la '
                                           'licuadora y sujétala bien antes de prenderla para que el vapor no bote la '
                                           'tapa.',
                         'resumen_visual': 'Pon en la licuadora las pepitas tostadas, los tomatillos hervidos (sin su '
                                           'agua), el cilantro, el...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende la estufa a fuego bajo. En una cazuela grande, pon a calentar la '
                                            'cucharadita de aceite.',
                         'imagen': 'pipian-pollo-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Enciende la estufa a fuego bajo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Vacía la salsa de la licuadora a la cazuela. Hazlo despacito y desde '
                                            'abajo. Mueve la salsa; verás que la pepita hace que espese muy bonito.',
                         'imagen': 'pipian-pollo-paso11.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si el aceite '
                                           'brinca un poco.',
                         'resumen_visual': 'Vacía la salsa de la licuadora a la cazuela.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras la salsa hierve a fuego muy suavecito, deshebra el pollo que ya '
                                            'se enfrió. Hazlo en tiritas muy finitas y chiquitas para que te sea muy '
                                            'fácil de masticar.',
                         'imagen': 'pipian-pollo-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Mientras la salsa hierve a fuego muy suavecito, deshebra el pollo que ya '
                                           'se enfrió.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega el pollo a la salsa y revuelve. Si sientes que la salsa está muy '
                                            'espesa, ponle un poquito más de caldo. Te pondré los últimos 5 minutitos '
                                            'para que todo se caliente parejo.',
                         'imagen': 'pipian-pollo-paso13.jpeg',
                         'nota_seguridad': 'Mueve frecuentemente la cazuela porque el pipián espeso se pega fácil al '
                                           'fondo.',
                         'resumen_visual': 'Agrega el pollo a la salsa y revuelve.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedó listo tu guisado! Apaga la estufa de inmediato.',
                         'imagen': 'pipian-pollo-paso14.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': '¡Ya quedó listo tu guisado!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar la olla unos minutitos en la estufa apagada. Después, sirve '
                                            'tu pipián calientito en un plato. ¡Que tengas un excelente provecho!',
                         'imagen': 'pipian-pollo-paso15.jpeg',
                         'nota_seguridad': 'Toca la salsita tantito con los labios antes de dar el primer bocado '
                                           'grande para asegurar que no te quema.',
                         'resumen_visual': 'Deja reposar la olla unos minutitos en la estufa apagada.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'pipian-verde-pollo',
        'tiempo_total_min': 52,
        'titulo': 'Pipián verde con pollo'},
    {   'descripcion': 'Pechuga de pollo cocida y deshebrada, guisada en una crema ligerita con rajas de chile poblano '
                       'y elote. Muy suavecita y sin nada de picante para cuidar su estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Pechuga de pollo sin hueso', '450 g (aprox. 2 pechugas chicas)'),
                                        ('Chile poblano', '1 pieza grande'),
                                        ('Granos de elote amarillo', '120 g (como media taza)'),
                                        ('Cebolla', '80 g (un buen pedazo)'),
                                        ('Aceite vegetal o mantequilla', '5 ml (una cucharadita)')],
                            'salsa': [('Leche o media crema', '100 ml (media taza)'), ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un rico pollito con rajas, cuidando que no pique nada. '
                                            'Primero, lávate bien las manos y pon todos tus ingredientes a la mano '
                                            'sobre la mesa.',
                         'imagen': 'pollo-rajas-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar un rico pollito con rajas, cuidando que no pique nada.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'En una olla, pon a cocer el pollo con suficiente agua, un pedacito de '
                                            'cebolla y sal. Te pondré un aviso de 25 minutos para que se cueza muy '
                                            'bien por dentro.',
                         'imagen': 'pollo-rajas-paso2.jpeg',
                         'nota_seguridad': 'No laves el pollo crudo en el fregadero para evitar salpicar bacterias. '
                                           'Ponlo directo en la olla.',
                         'resumen_visual': 'En una olla, pon a cocer el pollo con suficiente agua, un pedacito de '
                                           'cebolla y sal.',
                         'temporizador_segundos': 1500},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras el pollo se cuece, enciende otro quemador de tu estufa a fuego '
                                            'medio. Lava el chile poblano, sécalo bien y ponlo directo en la lumbre '
                                            'para asarlo.',
                         'imagen': 'pollo-rajas-paso3.jpeg',
                         'nota_seguridad': 'Voltéalo con unas pinzas largas para no quemarte los dedos. Aléjate un '
                                           'poco para que no te brinque aceitito de la cáscara.',
                         'resumen_visual': 'Mientras el pollo se cuece, enciende otro quemador de tu estufa a fuego '
                                           'medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Cuando el chile esté quemadito (negrito) de todos lados, sácalo con las '
                                            'pinzas y mételo en una bolsita de plástico limpia. Amárrala y déjalo '
                                            'sudar por 10 minutos.',
                         'imagen': 'pollo-rajas-paso4.jpeg',
                         'nota_seguridad': 'Apaga la hornilla donde asaste el chile de inmediato.',
                         'resumen_visual': 'Cuando el chile esté quemadito (negrito) de todos lados, sácalo con las '
                                           'pinzas y mételo en una bo...',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Sonó la alarma del pollo! Saca la pechuga de la olla, ponla en un plato '
                                            'y apaga esa hornilla. Déjala enfriar un buen rato.',
                         'imagen': 'pollo-rajas-paso5.jpeg',
                         'nota_seguridad': 'No intentes deshebrarlo ahorita porque guarda mucho calor por dentro y te '
                                           'puedes quemar las manos.',
                         'resumen_visual': '¡Sonó la alarma del pollo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Saca el chile poblano de la bolsa. Con un cuchillito raspa la piel negra '
                                            'para pelarlo. Ábrelo y quítale absolutamente todas las semillas y las '
                                            'venitas blancas de adentro.',
                         'imagen': 'pollo-rajas-paso6.jpeg',
                         'nota_seguridad': 'Es muy importante quitar todas las venas para asegurarnos de que no pique '
                                           'nada y caiga muy suave en tu estómago. Lávate las manos al terminar.',
                         'resumen_visual': 'Saca el chile poblano de la bolsa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Siéntate a la mesa y pica el chile poblano limpio en tiritas chiquitas. '
                                            'Pica también la cebolla restante muy finita.',
                         'imagen': 'pollo-rajas-paso7.jpeg',
                         'nota_seguridad': 'Picar las rajitas en tamaño pequeño ayudará a que las puedas masticar y '
                                           'digerir sin esfuerzo.',
                         'resumen_visual': 'Siéntate a la mesa y pica el chile poblano limpio en tiritas chiquitas.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Revisa si el pollo ya no quema. Con tus manos limpias o con ayuda de dos '
                                            'tenedores, deshébralo muy finito para que quede suave.',
                         'imagen': 'pollo-rajas-paso8.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Revisa si el pollo ya no quema.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio-bajo. Pon una cazuela o sartén extendido '
                                            'y calienta el poquito de aceite o mantequilla.',
                         'imagen': 'pollo-rajas-paso9.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la cazuela volteado hacia el centro de la estufa para '
                                           'que no lo golpees al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio-bajo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega la cebolla picada a la cazuela y muévela suavecito. Te pondré un '
                                            'tiempo de 3 minutos para que se acitrone.',
                         'imagen': 'pollo-rajas-paso10.jpeg',
                         'nota_seguridad': 'No dejes la espátula adentro de la cazuela para que no se caliente.',
                         'resumen_visual': 'Agrega la cebolla picada a la cazuela y muévela suavecito.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Añade las rajitas de poblano y los granitos de elote. Revuelve todo junto '
                                            'por otros 3 minutitos para que los sabores se mezclen bien.',
                         'imagen': 'pollo-rajas-paso11.jpeg',
                         'nota_seguridad': 'Si el aceite brinca un poquito por el elote, baja un poco más la flama.',
                         'resumen_visual': 'Añade las rajitas de poblano y los granitos de elote.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega todo el pollo deshebrado a la cazuela y vacía la media taza de '
                                            'leche o crema. Ponle su sal a tu gusto.',
                         'imagen': 'pollo-rajas-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Agrega todo el pollo deshebrado a la cazuela y vacía la media taza de '
                                           'leche o crema.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mezcla todo suavecito y deja que hierva a fuego muy bajito. Te pondré los '
                                            'últimos 5 minutos para que la salsita espese y todo quede bien jugosito.',
                         'imagen': 'pollo-rajas-paso13.jpeg',
                         'nota_seguridad': 'No dejes de mover la olla de vez en cuando, porque la leche se puede subir '
                                           'o pegar en el fondo fácilmente.',
                         'resumen_visual': 'Mezcla todo suavecito y deja que hierva a fuego muy bajito.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedó listo tu guisado! Apaga la estufa de inmediato para que no se '
                                            'reseque la cremita.',
                         'imagen': 'pollo-rajas-paso14.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': '¡Ya quedó listo tu guisado!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu pollito calientito en un plato. Lo puedes acompañar con unas '
                                            'tortillitas de maíz bien calientes. ¡Que tengas muy buen provecho!',
                         'imagen': 'pollo-rajas-paso15.jpeg',
                         'nota_seguridad': 'Toca el guisado un poquito con los labios antes de comer para asegurar que '
                                           'no te queme la boca.',
                         'resumen_visual': 'Sirve tu pollito calientito en un plato.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'pollo-rajas-poblano-elote',
        'tiempo_total_min': 58,
        'titulo': 'Pollo con rajas de poblano y elote'},
    {   'descripcion': 'Pollo cocido y deshebrado muy finito, acompañado de una salsita verde suave, sin picante y '
                       'amigable con su estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Pechuga de pollo sin hueso', '450 g (aprox. 2 pechugas chicas)'),
                                        ('Agua', '800 ml (poco más de tres tazas)'),
                                        ('Aceite vegetal', '5 ml (una cucharadita)')],
                            'salsa': [   ('Tomatillos verdes', '300 g (unos 6 a 8 tomatillos)'),
                                         ('Cebolla', '60 g (un pedacito para cocer el pollo y otro para la salsa)'),
                                         ('Ajo', '1 diente pelado'),
                                         ('Cilantro fresco', '10 g (unas cuantas ramitas)'),
                                         ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un guisadito de pollo verde muy sabroso y jugosito. '
                                            'Primero, lávate bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'pollo-salsa-verde-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar un guisadito de pollo verde muy sabroso y jugosito.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo'],
                         'detalle_hablado': 'En una olla mediana, pon la pechuga de pollo, un pedacito de la cebolla y '
                                            'su sal. Vacía el agua limpia cuidando que cubra bien la carne.',
                         'imagen': 'pollo-salsa-verde-paso2.jpeg',
                         'nota_seguridad': 'Recuerda no lavar el pollo crudo en el fregadero para evitar salpicar '
                                           'bacterias. Ponlo directo del empaque a la olla.',
                         'resumen_visual': 'En una olla mediana, pon la pechuga de pollo, un pedacito de la cebolla y '
                                           'su sal.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Vamos a dejar que el pollo hierva y se '
                                            'cueza muy bien por dentro. Te pondré un tiempo de 25 minutos.',
                         'imagen': 'pollo-salsa-verde-paso3.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': 1500},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Mientras el pollo está en la lumbre, siéntate a la mesa. Lava muy bien '
                                            'los tomatillos, quítales la cáscara pegajosa, y enjuaga las ramitas de '
                                            'cilantro.',
                         'imagen': 'pollo-salsa-verde-paso4.jpeg',
                         'nota_seguridad': 'Sentarte a hacer esto te ayudará a no cansarte de las piernas o la '
                                           'espalda.',
                         'resumen_visual': 'Mientras el pollo está en la lumbre, siéntate a la mesa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Sonó la alarma del pollo! Saca la pechuga de la olla con unas pinzas '
                                            'largas, ponla en un plato y apaga esa hornilla. Deja enfriar la carne un '
                                            'buen rato.',
                         'imagen': 'pollo-salsa-verde-paso5.jpeg',
                         'nota_seguridad': '¡Cuidado! No toques la carne con las manos ahorita porque guarda mucho '
                                           'calor por dentro y te puedes quemar.',
                         'resumen_visual': '¡Sonó la alarma del pollo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'En otra ollita más pequeña, pon los tomatillos limpios y cúbrelos con '
                                            'agua nueva. Enciende la estufa a fuego medio. Te aviso en 10 minutos para '
                                            'que hiervan y se pongan suavecitos.',
                         'imagen': 'pollo-salsa-verde-paso6.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la lumbre siga prendida.',
                         'resumen_visual': 'En otra ollita más pequeña, pon los tomatillos limpios y cúbrelos con agua '
                                           'nueva.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo', 'estufa'],
                         'detalle_hablado': '¡Listo! Apaga la estufa de los tomatillos. Sácalos del agua caliente con '
                                            'una cuchara grande y déjalos en un platito para que se entibien un poco.',
                         'imagen': 'pollo-salsa-verde-paso7.jpeg',
                         'nota_seguridad': 'Tira el agua donde hirvieron con mucho cuidado en el fregadero para no '
                                           'salpicarte los pies.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Revisa si el pollo ya no te quema las manos. Si ya está tibio, deshébralo '
                                            'muy finito usando tus dedos bien limpios o ayudándote con dos tenedores.',
                         'imagen': 'pollo-salsa-verde-paso8.jpeg',
                         'nota_seguridad': 'Hacer las tiritas de pollo muy finitas y cortitas te ayudará a que sea '
                                           'mucho más fácil y seguro de masticar.',
                         'resumen_visual': 'Revisa si el pollo ya no te quema las manos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Pon en el vaso de la licuadora los tomatillos tibios, el diente de ajo '
                                            'pelado, el otro pedacito de cebolla, el cilantro y una pizca de sal. '
                                            'Licúa todo muy bien.',
                         'imagen': 'pollo-salsa-verde-paso9.jpeg',
                         'nota_seguridad': 'Pon un trapo limpio doblado sobre la tapa de la licuadora y sujétala bien '
                                           'firme con la mano antes de prenderla.',
                         'resumen_visual': 'Pon en el vaso de la licuadora los tomatillos tibios, el diente de ajo '
                                           'pelado, el otro pedacito d...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende de nuevo tu estufa a fuego medio-bajo. Pon una cazuela o sartén '
                                            'profundo y agrégale la cucharadita de aceite para que se caliente un '
                                            'poquito.',
                         'imagen': 'pollo-salsa-verde-paso10.jpeg',
                         'nota_seguridad': 'Recuerda acomodar el mango de la cazuela hacia adentro de la estufa.',
                         'resumen_visual': 'Enciende de nuevo tu estufa a fuego medio-bajo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Vacía la salsa verde de la licuadora a la cazuela. Hazlo despacito y '
                                            'desde abajo. Te pondré 5 minutitos para que la salsa hierva y se guise '
                                            'bien rico.',
                         'imagen': 'pollo-salsa-verde-paso11.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si el aceite '
                                           'caliente brinca.',
                         'resumen_visual': 'Vacía la salsa verde de la licuadora a la cazuela.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ahora agrega todo el pollo deshebrado a la cazuela. Revuelve muy '
                                            'suavecito para que la carne se bañe con la salsa. Te pongo los últimos 5 '
                                            'minutos.',
                         'imagen': 'pollo-salsa-verde-paso12.jpeg',
                         'nota_seguridad': 'Si ves que el guisado se está secando mucho, ponle un chorrito del caldito '
                                           'tibio donde cociste el pollo.',
                         'resumen_visual': 'Ahora agrega todo el pollo deshebrado a la cazuela.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Ya quedó listo tu guisado! Apaga la estufa de inmediato para que tu '
                                            'salsita no se evapore y te quede bien jugoso.',
                         'imagen': 'pollo-salsa-verde-paso13.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada hacia arriba.',
                         'resumen_visual': '¡Ya quedó listo tu guisado!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar la olla unos minutitos en la estufa apagada. Sirve tu '
                                            'pollito verde en un plato hondo o cómelo con unas tortillitas suaves. '
                                            '¡Que lo disfrutes mucho!',
                         'imagen': 'pollo-salsa-verde-paso14.jpeg',
                         'nota_seguridad': 'Toca el guisado un poquito con los labios antes de dar el primer bocado '
                                           'grande para asegurar que no te quema.',
                         'resumen_visual': 'Deja reposar la olla unos minutitos en la estufa apagada.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'pollo-deshebrado-salsa-verde',
        'tiempo_total_min': 57,
        'titulo': 'Pollo deshebrado en salsa verde'},
    {   'descripcion': 'Puré muy cremoso de papa con leche y quesito fresco. Es ideal como guarnición, muy suave de '
                       'masticar y amigable con su estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [('Papa', '500 g (unas 3 papas medianas)'), ('Leche', '120 ml (media taza)')],
                            'salsa': [('Sal', 'Al gusto')],
                            'servicio': [   ('Queso fresco (panela o canasto)', '70 g (un buen pedazo)'),
                                            ('Mantequilla', '10 g (una cucharadita copeteada)')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar un puré de papa bien suavecito y reconfortante. Primero, '
                                            'lávate muy bien las manos y pon todos tus ingredientes en la mesa.',
                         'imagen': 'pure-papa-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para que no vayas a '
                                           'resbalar.',
                         'resumen_visual': 'Vamos a preparar un puré de papa bien suavecito y reconfortante.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien las papas bajo el chorro de agua para quitarles toda la '
                                            'tierra. Siéntate a la mesa y pélalas con toda la calma usando un '
                                            'pelapapas o un cuchillito.',
                         'imagen': 'pure-papa-paso2.jpeg',
                         'nota_seguridad': 'Hacer esto sentada evita que te canses. Usa un cuchillo ligero para no '
                                           'forzar tus manos.',
                         'resumen_visual': 'Lava muy bien las papas bajo el chorro de agua para quitarles toda la '
                                           'tierra.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Ahí mismo sentada, corta las papas ya peladas en cuadritos del mismo '
                                            'tamaño. Así se cocerán mucho más rápido y parejito.',
                         'imagen': 'pure-papa-paso3.jpeg',
                         'nota_seguridad': 'Corta sobre una tabla firme para que la papa no se ruede y te vayas a '
                                           'cortar.',
                         'resumen_visual': 'Ahí mismo sentada, corta las papas ya peladas en cuadritos del mismo '
                                           'tamaño.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Pon los cuadritos de papa en una olla mediana y vacíales agua limpia de '
                                            'garrafón hasta que las tape por completo.',
                         'imagen': 'pure-papa-paso4.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo golpees al pasar.',
                         'resumen_visual': 'Pon los cuadritos de papa en una olla mediana y vacíales agua limpia de '
                                           'garrafón hasta que las ta...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego alto. Vamos a esperar a que el agua empiece a '
                                            'hervir fuerte. Te pondré un aviso de 15 minutos para que vengas a '
                                            'revisar.',
                         'imagen': 'pure-papa-paso5.jpeg',
                         'nota_seguridad': 'No te alejes mucho de la cocina mientras la lumbre esté alta.',
                         'resumen_visual': 'Enciende tu estufa a fuego alto.',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Cuando el agua ya esté hirviendo, bájale a la flama a fuego medio y ponle '
                                            'su tapadera dejando una pequeña rendija. Te pongo otros 15 minutos para '
                                            'que las papas se ablanden por completo.',
                         'imagen': 'pure-papa-paso6.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Cuando el agua ya esté hirviendo, bájale a la flama a fuego medio y ponle '
                                           'su tapadera dejando una...',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado. Pica un cuadrito de papa '
                                            'con un tenedor; si entra como en mantequilla y se deshace suavemente, ya '
                                            'están listas.',
                         'imagen': 'pure-papa-paso7.jpeg',
                         'nota_seguridad': 'Levanta la tapa hacia el lado contrario de tu cara para que el vapor '
                                           'caliente no te queme.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Apaga la estufa en este momento para poder tirar el agua caliente con '
                                            'total seguridad.',
                         'imagen': 'pure-papa-paso8.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada hacia arriba.',
                         'resumen_visual': 'Apaga la estufa en este momento para poder tirar el agua caliente con '
                                           'total seguridad.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Lleva la olla al fregadero. Con mucho cuidado escúrreles toda el agua, '
                                            'puedes ayudarte con la misma tapa de la olla o vaciarlas despacito en un '
                                            'colador grande.',
                         'imagen': 'pure-papa-paso9.jpeg',
                         'nota_seguridad': 'Usa trapos gruesos para agarrar la olla porque estará muy caliente y '
                                           'pesará un poco por el agua.',
                         'resumen_visual': 'Lleva la olla al fregadero.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Ahí mismo en la olla, con las papas aún muy calientes, aplástalas con un '
                                            'machacador de frijoles o un tenedor grande hasta que se haga una masita '
                                            'suave y sin grumos.',
                         'imagen': 'pure-papa-paso10.jpeg',
                         'nota_seguridad': 'Machacar las papas en caliente hace que el puré quede mucho más liso y '
                                           'esponjoso, costándote menos trabajo.',
                         'resumen_visual': 'Ahí mismo en la olla, con las papas aún muy calientes, aplástalas con un '
                                           'machacador de frijoles o...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Agrega de inmediato la cucharadita de mantequilla para que se derrita con '
                                            'el calor de la papa, la media taza de leche, sal a tu gusto y el queso '
                                            'fresco desmoronado. Mezcla todo muy bien con una cuchara grande.',
                         'imagen': 'pure-papa-paso11.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Agrega de inmediato la cucharadita de mantequilla para que se derrita con '
                                           'el calor de la papa, la...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu puré de papa tibiecito. Es excelente y muy llenador para '
                                            'acompañar cualquier guisadito. ¡Que lo disfrutes mucho y buen provecho!',
                         'imagen': 'pure-papa-paso12.jpeg',
                         'nota_seguridad': 'Tócalo un poquito con los labios antes de dar el primer bocado para '
                                           'asegurar que no te quema.',
                         'resumen_visual': 'Sirve tu puré de papa tibiecito.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'pure-papa-queso',
        'tiempo_total_min': 42,
        'titulo': 'Puré de papa con queso'},
    {   'descripcion': 'Quesadillas de maíz rellenas de champiñones guisaditos y queso Oaxaca derretido. Una comida '
                       'muy calientita, de textura suave y fácil de digerir.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Tortillas de maíz', '4 piezas'),
                                        ('Champiñones frescos', '200 g (aprox. una charolita chica)'),
                                        ('Queso Oaxaca', '80 g (un trozo pequeño)'),
                                        ('Cebolla', '30 g (un pedacito)'),
                                        ('Aceite vegetal o mantequilla', '5 ml (una cucharadita)')],
                            'salsa': [('Sal', 'Una pizquita')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unas quesadillas muy ricas y suavecitas. Primero, lávate '
                                            'bien las manos y pon tus ingredientes sobre la mesa.',
                         'imagen': 'quesadillas-champinones-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para que no haya '
                                           'riesgo de resbalones.',
                         'resumen_visual': 'Vamos a preparar unas quesadillas muy ricas y suavecitas.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Limpia los champiñones pasándoles un trapito limpio y húmedo para '
                                            'quitarles la tierrita. Si prefieres enjuagarlos, hazlo súper rápido y '
                                            'sécalos, para que no chupen tanta agua.',
                         'imagen': 'quesadillas-champinones-paso2.jpeg',
                         'nota_seguridad': 'Evita dejarlos remojando en agua porque se hacen esponjosos y pierden su '
                                           'sabor.',
                         'resumen_visual': 'Limpia los champiñones pasándoles un trapito limpio y húmedo para '
                                           'quitarles la tierrita.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Siéntate a la mesa para no cansarte. Córtale la puntita seca al tallo de '
                                            'los champiñones y pícalos en cuadritos muy chiquitos. Así serán muy '
                                            'fáciles de masticar.',
                         'imagen': 'quesadillas-champinones-paso3.jpeg',
                         'nota_seguridad': 'Usa una tabla bien firme y un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Siéntate a la mesa para no cansarte.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Ahí mismo, pica finamente el pedacito de cebolla. Deshebra el queso '
                                            'Oaxaca con tus manos limpias y separa todo en platitos para tenerlo '
                                            'listo.',
                         'imagen': 'quesadillas-champinones-paso4.jpeg',
                         'nota_seguridad': 'Asegúrate de lavarte las manos de nuevo después de agarrar los champiñones '
                                           'crudos.',
                         'resumen_visual': 'Ahí mismo, pica finamente el pedacito de cebolla.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una sartén mediana y agrégale la '
                                            'cucharadita de aceite o mantequilla para que se caliente.',
                         'imagen': 'quesadillas-champinones-paso5.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la sartén volteado hacia el centro de la estufa para '
                                           'que no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Agrega la cebolla picadita a la sartén. Muévela suavecito con una '
                                            'cuchara. Te pondré 3 minutos; sabrás que está lista cuando la veas '
                                            'transparente y huela muy rico.',
                         'imagen': 'quesadillas-champinones-paso6.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la estufa para que la cebolla no se te vaya a quemar.',
                         'resumen_visual': 'Agrega la cebolla picadita a la sartén.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['aceite', 'cuchillo', 'estufa'],
                         'detalle_hablado': 'Ahora vacía los champiñones picados y ponles su pizca de sal. Al '
                                            'principio soltarán su juguito y se verán mojados. Te pondré 5 minutos '
                                            'para que se cuezan.',
                         'imagen': 'quesadillas-champinones-paso7.jpeg',
                         'nota_seguridad': 'Aléjate un pasito al echarlos por si el aceite brinca un poquito.',
                         'resumen_visual': 'Ahora vacía los champiñones picados y ponles su pizca de sal.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': 'Sigue moviendo de vez en cuando. Estarán listos cuando veas que el fondo '
                                            'del sartén ya casi no tiene líquido, y los champiñones se vean de un '
                                            'color café oscuro y muy tiernitos.',
                         'imagen': 'quesadillas-champinones-paso8.jpeg',
                         'nota_seguridad': 'Cuidado con el vapor calientito que sale de la sartén al mover.',
                         'resumen_visual': 'Sigue moviendo de vez en cuando.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Cuando los champiñones ya estén en su punto, apaga esa hornilla de la '
                                            'estufa.',
                         'imagen': 'quesadillas-champinones-paso9.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Cuando los champiñones ya estén en su punto, apaga esa hornilla de la '
                                           'estufa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende otra hornilla a fuego muy bajito y pon a calentar tu comal o un '
                                            'sartén plano. Pon las tortillas de maíz unos segunditos por lado para que '
                                            'se pongan suavecitas y flexibles.',
                         'imagen': 'quesadillas-champinones-paso10.jpeg',
                         'nota_seguridad': 'Voltea las tortillas usando unas pinzas para no quemarte los dedos.',
                         'resumen_visual': 'Enciende otra hornilla a fuego muy bajito y pon a calentar tu comal o un '
                                           'sartén plano.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ponle a cada tortilla un buen puñito de queso Oaxaca y un par de '
                                            'cucharadas de los champiñones. Dóblalas por la mitad con cuidado formando '
                                            'las quesadillas.',
                         'imagen': 'quesadillas-champinones-paso11.jpeg',
                         'nota_seguridad': 'Apóyate con una cuchara para poner el relleno y no tocar el metal caliente '
                                           'del comal.',
                         'resumen_visual': 'Ponle a cada tortilla un buen puñito de queso Oaxaca y un par de '
                                           'cucharadas de los champiñones.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja las quesadillas en el comal a fuego muy bajo. Te pondré 3 minutos, '
                                            'pero fíjate bien: estarán listas de este lado cuando veas que la tortilla '
                                            'se ve doradita y el queso empieza a derretirse.',
                         'imagen': 'quesadillas-champinones-paso12.jpeg',
                         'nota_seguridad': 'No dejes la cocina sola, cuida que la tortilla no se queme ni se haga muy '
                                           'dura.',
                         'resumen_visual': 'Deja las quesadillas en el comal a fuego muy bajo.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Con ayuda de una espátula ancha, voltea tus quesadillas. Espera a que el '
                                            'otro lado también se vea doradito y notes que el queso ya está '
                                            'completamente fundido por dentro.',
                         'imagen': 'quesadillas-champinones-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Con ayuda de una espátula ancha, voltea tus quesadillas.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Ya quedaron listas! Apaga la estufa de inmediato.',
                         'imagen': 'quesadillas-champinones-paso14.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': '¡Ya quedaron listas!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Pasa tus quesadillas a un plato y déjalas reposar un par de minutos. El '
                                            'queso derretido guarda mucho calor. Puedes cortarlas a la mitad para '
                                            'comerlas más a gusto. ¡Buen provecho!',
                         'imagen': 'quesadillas-champinones-paso15.jpeg',
                         'nota_seguridad': 'Tócalas un poquito con los labios antes de dar la primera mordida para '
                                           'asegurar que el relleno no te queme la boca.',
                         'resumen_visual': 'Pasa tus quesadillas a un plato y déjalas reposar un par de minutos.',
                         'temporizador_segundos': 120}],
        'porciones': 2,
        'slug': 'quesadillas-champinones',
        'tiempo_total_min': 30,
        'titulo': 'Quesadillas de champiñones'},
    {   'descripcion': 'Sopa calientita de fideo dorado en caldito de jitomate. Muy casera, reconfortante y fácil de '
                       'comer para consentir a su estómago.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   ('Fideo delgado (del número 0 o 1)', '1 bolsita de 200 gramos'),
                                        ('Aceite vegetal o manteca', '2 cucharadas'),
                                        ('Caldo de pollo o agua', '4 tazas (un litro)'),
                                        ('Sal', '1/2 cucharadita o al gusto')],
                            'salsa': [   ('Jitomates', '3 medianos'),
                                         ('Cebolla', 'Un pedacito (1/4 de pieza)'),
                                         ('Ajo', '1 diente pelado')],
                            'servicio': [('Queso fresco desmoronado y limón', 'Al gusto (opcional)')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar una rica sopita de fideo. Primero, lávate bien las manos '
                                            'y pon todos tus ingredientes en la mesa para no dar vueltas.',
                         'imagen': 'fideo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar una rica sopita de fideo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo', 'licuadora'],
                         'detalle_hablado': 'Lava muy bien los jitomates, quítales el ombliguito verde y pártelos en '
                                            'cuartos. Ponlos en el vaso de la licuadora con la cebolla, el ajo y media '
                                            'taza de agua.',
                         'imagen': 'fideo-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para picar los jitomates '
                                           'con toda la calma.',
                         'resumen_visual': 'Lava muy bien los jitomates, quítales el ombliguito verde y pártelos en '
                                           'cuartos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa todo muy bien por un minuto hasta que quede una salsa suavecita, '
                                            'sin grumos grandes. Déjala lista ahí en el vaso.',
                         'imagen': 'fideo-paso3.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa de la licuadora antes de prenderla.',
                         'resumen_visual': 'Licúa todo muy bien por un minuto hasta que quede una salsa suavecita, sin '
                                           'grumos grandes.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una olla mediana o cazuela y '
                                            'agrégale las dos cucharadas de aceite para que se vaya calentando.',
                         'imagen': 'fideo-paso4.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vacía toda la bolsita de fideo en la olla. Empieza a moverlo suavecito, '
                                            'pero sin parar, con una cuchara de madera larga. Te pongo 2 minutos.',
                         'imagen': 'fideo-paso5.jpeg',
                         'nota_seguridad': 'No te alejes de la estufa. El fideo es delgadito y se quema muy rápido si '
                                           'dejas de moverlo.',
                         'resumen_visual': 'Vacía toda la bolsita de fideo en la olla.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': '¡Listo! Cuando veas que el fideo agarró un color doradito parejo (como '
                                            'color paja), vacíale la salsa de la licuadora. Hazlo despacito y desde '
                                            'abajito.',
                         'imagen': 'fideo-paso6.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa porque va a chillar '
                                           'y puede brincar el aceite caliente.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ponle su sal al gusto. Revuelve bien y deja que la salsa hierva a fuego '
                                            'suave para que se guise el jitomate y cambie a un color rojo oscuro. Te '
                                            'aviso en 3 minutos.',
                         'imagen': 'fideo-paso7.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ponle su sal al gusto.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Ahora, agrega las 4 tazas de agua (o caldo de pollo) con mucho cuidado. '
                                            'Revuelve despacito para que el fideo que se pegó al fondo se suelte.',
                         'imagen': 'fideo-paso8.jpeg',
                         'nota_seguridad': 'Si el agua que le vas a poner está caliente, usa un trapo para agarrar la '
                                           'jarra y no quemarte.',
                         'resumen_visual': 'Ahora, agrega las 4 tazas de agua (o caldo de pollo) con mucho cuidado.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'estufa'],
                         'detalle_hablado': 'Espera a que el caldo empiece a hervir de nuevo. Cuando veas que '
                                            'burbujea, bájale a la lumbre a un fuego muy suavecito y tapa tu olla '
                                            'dejando una pequeña rendija.',
                         'imagen': 'fideo-paso9.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Espera a que el caldo empiece a hervir de nuevo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Vamos a dejar que el fideo se cueza y se ponga muy blandito. Te pondré un '
                                            'tiempo de 7 minutos. Puedes sentarte un rato a descansar.',
                         'imagen': 'fideo-paso10.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Vamos a dejar que el fideo se cueza y se ponga muy blandito.',
                         'temporizador_segundos': 420},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado. Saca un fideíto con el '
                                            'tenedor y pruébalo soplando antes. Si ya está muy suave, la sopa ya '
                                            'quedó.',
                         'imagen': 'fideo-paso11.jpeg',
                         'nota_seguridad': 'Levanta la tapa hacia el lado contrario de tu cara para que el vapor '
                                           'caliente no te dé directo en los ojos.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Apaga la estufa en este momento para que la sopa no se te reseque de más.',
                         'imagen': 'fideo-paso12.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada hacia arriba.',
                         'resumen_visual': 'Apaga la estufa en este momento para que la sopa no se te reseque de más.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja tu olla reposando ahí mismo en la estufa unos 5 minutitos. Te marco '
                                            'el tiempo para que el caldito asiente su sabor y no te vayas a quemar.',
                         'imagen': 'fideo-paso13.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja tu olla reposando ahí mismo en la estufa unos 5 minutitos.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu sopita de fideo en un plato hondo. Le puedes poner quesito '
                                            'fresco desmoronado encima y unas gotitas de limón. ¡Que la disfrutes '
                                            'mucho y buen provecho!',
                         'imagen': 'fideo-paso14.jpeg',
                         'nota_seguridad': 'Toca el caldito tantito con los labios antes de dar la primera cucharada '
                                           'para asegurar que la temperatura esté agradable.',
                         'resumen_visual': 'Sirve tu sopita de fideo en un plato hondo.',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'sopa-de-fideo',
        'tiempo_total_min': 29,
        'titulo': 'Sopa de fideo'},
    {   'descripcion': 'Caldo casero muy nutritivo con zanahoria, papa, chayote y calabacita cocidos hasta quedar '
                       'suavecitos y fáciles de digerir para su estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Zanahoria', '150 g (una grande o dos medianas)'),
                                        ('Papa', '200 g (una papa grande)'),
                                        ('Chayote', '150 g (medio chayote grande)'),
                                        ('Calabacita', '150 g (una mediana)')],
                            'salsa': [   ('Jitomate', '150 g (dos medianos)'),
                                         ('Cebolla', '40 g (un pedacito)'),
                                         ('Agua', '1.2 litros (unas 5 tazas)'),
                                         ('Aceite vegetal', '5 ml (una cucharadita)'),
                                         ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar una sopita de verduras muy reconfortante. Primero, '
                                            'lávate bien las manos y pon todos tus ingredientes en la mesa para '
                                            'tenerlos a la mano.',
                         'imagen': 'sopa-verduras-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones al caminar.',
                         'resumen_visual': 'Vamos a preparar una sopita de verduras muy reconfortante.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Lava muy bien todas las verduras bajo el chorro de agua. Pela la '
                                            'zanahoria, la papa y el chayote.',
                         'imagen': 'sopa-verduras-paso2.jpeg',
                         'nota_seguridad': 'Si te cansas de estar de pie, siéntate a la mesa para pelar y picar todo '
                                           'con calma. Ten cuidado con el chayote porque resbala un poco.',
                         'resumen_visual': 'Lava muy bien todas las verduras bajo el chorro de agua.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Ahí mismo sentada, corta la zanahoria, la papa y el chayote en cuadritos '
                                            'muy chiquitos para que se cuezan rápido y te sean muy fáciles de '
                                            'masticar. Ponlos en un plato.',
                         'imagen': 'sopa-verduras-paso3.jpeg',
                         'nota_seguridad': 'Usa una tabla firme. Recuerda quitarle el corazón blanco al centro del '
                                           'chayote porque es más duro.',
                         'resumen_visual': 'Ahí mismo sentada, corta la zanahoria, la papa y el chayote en cuadritos '
                                           'muy chiquitos para que s...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['cuchillo'],
                         'detalle_hablado': 'Corta las puntas de la calabacita y pícala también en cuadritos del mismo '
                                            'tamaño. Ponla en un platito aparte, porque esta verdura es más suave y se '
                                            'coce más rápido.',
                         'imagen': 'sopa-verduras-paso4.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Corta las puntas de la calabacita y pícala también en cuadritos del mismo '
                                           'tamaño.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Quítales el ombliguito a los jitomates, pártelos en cuartos y ponlos en '
                                            'el vaso de la licuadora junto con el pedacito de cebolla y media tacita '
                                            'de agua. Licúa todo muy bien por un minuto.',
                         'imagen': 'sopa-verduras-paso5.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa de la licuadora antes de prenderla.',
                         'resumen_visual': 'Quítales el ombliguito a los jitomates, pártelos en cuartos y ponlos en el '
                                           'vaso de la licuadora j...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Pon una olla de buen tamaño y agrégale '
                                            'la cucharadita de aceite para que se vaya calentando.',
                         'imagen': 'sopa-verduras-paso6.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': 'Vacía el jitomate licuado en la olla. Hazlo despacito y desde abajo. Te '
                                            'pondré 5 minutitos para que hierva, el jitomate agarre un color rojito y '
                                            'se guise muy rico.',
                         'imagen': 'sopa-verduras-paso7.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si el aceite '
                                           'caliente brinca un poco.',
                         'resumen_visual': 'Vacía el jitomate licuado en la olla.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Ahora agrega el resto del agua a la olla (poco más de un litro). Echa con '
                                            'mucho cuidado la zanahoria, la papa y el chayote picados.',
                         'imagen': 'sopa-verduras-paso8.jpeg',
                         'nota_seguridad': 'Echa las verduras pegando el plato a la olla para que no te salpique el '
                                           'caldo caliente en las manos.',
                         'resumen_visual': 'Ahora agrega el resto del agua a la olla (poco más de un litro).',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Tapa tu olla dejando una pequeña rendijita y bájale a la flama a un fuego '
                                            'suavecito. Te pondré 15 minutos para que estas verduras empiecen a '
                                            'ablandarse bien.',
                         'imagen': 'sopa-verduras-paso9.jpeg',
                         'nota_seguridad': 'No te vayas lejos de la cocina mientras la lumbre siga prendida.',
                         'resumen_visual': 'Tapa tu olla dejando una pequeña rendijita y bájale a la flama a un fuego '
                                           'suavecito.',
                         'temporizador_segundos': 900},
                     {   'alertas_seguridad': ['cuchillo', 'estufa', 'vapor'],
                         'detalle_hablado': '¡Sonó la alarma! Destapa la olla con cuidado y pica un cuadrito de '
                                            'zanahoria. Si ya se siente un poco suave, agrega la calabacita picada y '
                                            'ponle sal a tu gusto.',
                         'imagen': 'sopa-verduras-paso10.jpeg',
                         'nota_seguridad': 'Levanta la tapa hacia el lado contrario de tu cara para que el vapor '
                                           'caliente no te dé directo en los ojos.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Revuelve despacito y vuelve a tapar la olla. Te pondré los últimos 10 '
                                            'minutos para que todo termine de cocerse y la calabacita quede bien '
                                            'tiernita.',
                         'imagen': 'sopa-verduras-paso11.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Revuelve despacito y vuelve a tapar la olla.',
                         'temporizador_segundos': 600},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo el tiempo! Saca un cuadrito de chayote y uno de papa; sóplales un '
                                            'poco y apachúrralos con un tenedor. Si se deshacen fácil, tu sopita ya '
                                            'quedó en su punto.',
                         'imagen': 'sopa-verduras-paso12.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': '¡Listo el tiempo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Apaga la estufa de inmediato para que tu sopa no se consuma de más y las '
                                            'verduras no se desbaraten por completo.',
                         'imagen': 'sopa-verduras-paso13.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada hacia arriba.',
                         'resumen_visual': 'Apaga la estufa de inmediato para que tu sopa no se consuma de más y las '
                                           'verduras no se desbarate...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja tu olla reposando ahí mismo en la estufa unos 5 minutitos. Te marco '
                                            'el tiempo para que el caldito asiente su sabor y se enfríe un poco, así '
                                            'no te quemas.',
                         'imagen': 'sopa-verduras-paso14.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja tu olla reposando ahí mismo en la estufa unos 5 minutitos.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu sopita de verduras en un plato hondo. Tócala tantito con los '
                                            'labios antes de dar el primer bocado grande. ¡Que te aproveche mucho y te '
                                            'caiga muy bien!',
                         'imagen': 'sopa-verduras-paso15.jpeg',
                         'nota_seguridad': 'Procura poner un plato extendido debajo de tu plato hondo para que no te '
                                           'queme las manos al llevarlo a la mesa.',
                         'resumen_visual': 'Sirve tu sopita de verduras en un plato hondo.',
                         'temporizador_segundos': None}],
        'porciones': 4,
        'slug': 'sopa-verduras',
        'tiempo_total_min': 47,
        'titulo': 'Sopa de verduras'},
    {   'descripcion': 'Pollo deshebrado muy finito con jitomate y cebollita. Jugosito, bien cocido y sin nada de '
                       'picante, ideal para cuidar su estómago.',
        'dificultad': 'media',
        'ingredientes': {   'base': [   ('Pechuga de pollo sin hueso', '450 g (aprox. 2 pechugas chicas)'),
                                        ('Cebolla', '150 g (media cebolla grande)'),
                                        ('Agua', '700 ml (unas 3 tazas)'),
                                        ('Aceite vegetal o manteca', '5 ml (una cucharadita)')],
                            'salsa': [   ('Jitomate', '300 g (unos 3 medianos)'),
                                         ('Ajo', '1 diente pelado'),
                                         ('Sal', 'Al gusto')],
                            'servicio': []},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar una tinga de pollo muy rica y segura de comer. Primero, '
                                            'lávate bien las manos y pon todos tus ingredientes en la mesa para no dar '
                                            'muchas vueltas.',
                         'imagen': 'tinga-pollo-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones.',
                         'resumen_visual': 'Vamos a preparar una tinga de pollo muy rica y segura de comer.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['agua_caliente', 'cuchillo'],
                         'detalle_hablado': 'En una olla mediana, pon la pechuga de pollo, un pedacito muy chiquito de '
                                            'la cebolla y sal. Vacía el agua limpia cuidando que cubra bien la carne.',
                         'imagen': 'tinga-pollo-paso2.jpeg',
                         'nota_seguridad': 'Recuerda no lavar el pollo crudo en el fregadero para evitar salpicar '
                                           'bacterias por todos lados. Ponlo directo en la olla.',
                         'resumen_visual': 'En una olla mediana, pon la pechuga de pollo, un pedacito muy chiquito de '
                                           'la cebolla y sal.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio. Vamos a dejar que el pollo hierva y se '
                                            'cueza muy, muy bien por dentro. Te pondré un tiempo de 30 minutos para '
                                            'asegurar que no quede nada crudo.',
                         'imagen': 'tinga-pollo-paso3.jpeg',
                         'nota_seguridad': 'Acomoda el mango de la olla volteado hacia el centro de la estufa para que '
                                           'no lo vayas a golpear al pasar.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio.',
                         'temporizador_segundos': 1800},
                     {   'alertas_seguridad': ['cuchillo', 'estufa'],
                         'detalle_hablado': 'Mientras el pollo está en la lumbre, siéntate a la mesa. Corta el resto '
                                            'de la cebolla en tiritas muy, muy delgaditas para que te sean muy fáciles '
                                            'de masticar y digerir.',
                         'imagen': 'tinga-pollo-paso4.jpeg',
                         'nota_seguridad': 'Usa una tabla firme y un cuchillo ligero que no te canse la mano.',
                         'resumen_visual': 'Mientras el pollo está en la lumbre, siéntate a la mesa.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Lava muy bien los jitomates, quítales el ombliguito verde y pártelos en '
                                            'cuartos. Ponlos en el vaso de la licuadora con el diente de ajo pelado y '
                                            'media tacita de agua.',
                         'imagen': 'tinga-pollo-paso5.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Lava muy bien los jitomates, quítales el ombliguito verde y pártelos en '
                                           'cuartos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['licuadora'],
                         'detalle_hablado': 'Licúa el jitomate con el ajo por un buen rato hasta que te quede una '
                                            'salsita muy tersa y sin grumos. Déjala ahí lista en el vaso.',
                         'imagen': 'tinga-pollo-paso6.jpeg',
                         'nota_seguridad': 'Asegúrate de poner bien la tapa a la licuadora antes de prenderla.',
                         'resumen_visual': 'Licúa el jitomate con el ajo por un buen rato hasta que te quede una '
                                           'salsita muy tersa y sin grumos.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Sonó la alarma! Saca la pechuga de la olla con unas pinzas largas, ponla '
                                            'en un plato hondo y apaga esa hornilla. Deja enfriar la carne un rato. No '
                                            'tires el caldo, lo usaremos después.',
                         'imagen': 'tinga-pollo-paso7.jpeg',
                         'nota_seguridad': '¡Cuidado! No toques la carne con las manos ahorita porque guarda mucho '
                                           'calor por dentro y te puedes quemar.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Revisa si el pollo ya está tibio. Deshébralo muy, muy finito usando tus '
                                            'dedos bien limpios o ayudándote con dos tenedores.',
                         'imagen': 'tinga-pollo-paso8.jpeg',
                         'nota_seguridad': 'Hacer las tiritas de pollo muy finitas y cortitas te ayudará a que el '
                                           'guisado sea muy fácil y seguro de comer.',
                         'resumen_visual': 'Revisa si el pollo ya está tibio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Enciende de nuevo tu estufa a fuego bajo. Pon una cazuela o sartén '
                                            'extendido y agrégale la cucharadita de aceite para que se vaya '
                                            'calentando.',
                         'imagen': 'tinga-pollo-paso9.jpeg',
                         'nota_seguridad': 'Recuerda acomodar el mango de la cazuela hacia adentro de la estufa.',
                         'resumen_visual': 'Enciende de nuevo tu estufa a fuego bajo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega la cebolla en tiritas a la cazuela. Muévela suavecito con una '
                                            'cuchara de madera. Te pondré un tiempo de 4 minutos para que se acitrone '
                                            'y quede muy suavecita.',
                         'imagen': 'tinga-pollo-paso10.jpeg',
                         'nota_seguridad': 'Quédate cerquita de la estufa para que la cebolla no se te vaya a quemar.',
                         'resumen_visual': 'Agrega la cebolla en tiritas a la cazuela.',
                         'temporizador_segundos': 240},
                     {   'alertas_seguridad': ['aceite', 'estufa', 'licuadora'],
                         'detalle_hablado': '¡Listo! Ahora vacía la salsa de jitomate de la licuadora a la cazuela. '
                                            'Hazlo despacito y desde abajito. Te pondré 5 minutitos para que hierva y '
                                            'cambie a un color rojo oscuro.',
                         'imagen': 'tinga-pollo-paso11.jpeg',
                         'nota_seguridad': 'Aléjate un pasito hacia atrás cuando viertas la salsa por si el aceite '
                                           'caliente brinca.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Agrega todo el pollo deshebrado y media tacita del caldo tibio donde lo '
                                            'cociste. Ponle sal a tu gusto. Revuelve muy bien. Te pongo los últimos 5 '
                                            'minutos para que los sabores se mezclen.',
                         'imagen': 'tinga-pollo-paso12.jpeg',
                         'nota_seguridad': 'Mueve el guisado de vez en cuando para que no se pegue al fondo.',
                         'resumen_visual': 'Agrega todo el pollo deshebrado y media tacita del caldo tibio donde lo '
                                           'cociste.',
                         'temporizador_segundos': 300},
                     {   'alertas_seguridad': ['estufa', 'vapor'],
                         'detalle_hablado': '¡Ya quedó lista tu tinga! Apaga la estufa de inmediato para que la '
                                            'salsita de jitomate no se evapore y te quede bien jugosito el pollo.',
                         'imagen': 'tinga-pollo-paso13.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada.',
                         'resumen_visual': '¡Ya quedó lista tu tinga!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Deja reposar la olla unos minutitos en la estufa apagada. Te marco el '
                                            'tiempo para que el guisado asiente su sabor y se enfríe un poco.',
                         'imagen': 'tinga-pollo-paso14.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Deja reposar la olla unos minutitos en la estufa apagada.',
                         'temporizador_segundos': 180},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Sirve tu tinga de pollo calientita en un plato hondo o sobre unas '
                                            'tortillitas suaves de maíz. ¡Que la disfrutes mucho y buen provecho!',
                         'imagen': 'tinga-pollo-paso15.jpeg',
                         'nota_seguridad': 'Toca el guisado un poquito con los labios antes de dar el primer bocado '
                                           'grande para asegurar que no te quema.',
                         'resumen_visual': 'Sirve tu tinga de pollo calientita en un plato hondo o sobre unas '
                                           'tortillitas suaves de maíz.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'tinga-suave-pollo',
        'tiempo_total_min': 59,
        'titulo': 'Tinga suave de pollo'},
    {   'descripcion': 'Ricos tlacoyos caseros de masa de maíz rellenos de requesón pasteurizado, cocinados en el '
                       'comal sin freír. Muy suavecitos, bien cocidos y fáciles de digerir.',
        'dificultad': 'fácil',
        'ingredientes': {   'base': [   (   'Masa de maíz (de tortillería o de harina preparada)',
                                            '450 g (poco menos de medio kilo)'),
                                        (   'Requesón pasteurizado',
                                            '180 g (asegúrate de que el empaque diga pasteurizado)'),
                                        ('Agua tibia', '60 ml (un chorrito, para amasar)'),
                                        ('Aceite vegetal o manteca', '5 ml (solo para untar el comal)')],
                            'salsa': [],
                            'servicio': [   ('Salsa de jitomate suave (que no pique)', '150 g (para acompañar)'),
                                            ('Queso fresco desmoronado (opcional)', 'Al gusto')]},
        'pasos': [   {   'alertas_seguridad': [],
                         'detalle_hablado': 'Vamos a preparar unos tlacoyitos de requesón muy ricos y seguros para tu '
                                            'estómago. Primero, lávate bien las manos con agua y jabón, y pon todos '
                                            'tus ingredientes en la mesa.',
                         'imagen': 'tlacoyos-requeson-paso1.jpeg',
                         'nota_seguridad': 'Asegúrate de que el piso de la cocina esté bien seco para evitar '
                                           'resbalones.',
                         'resumen_visual': 'Vamos a preparar unos tlacoyitos de requesón muy ricos y seguros para tu '
                                           'estómago.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Siéntate a la mesa para no cansarte. Pon la masa de maíz en un tazón '
                                            'amplio. Agrégale el chorrito de agua tibia poco a poco.',
                         'imagen': 'tlacoyos-requeson-paso2.jpeg',
                         'nota_seguridad': 'El agua tibia ayuda a que la masa se ponga suavecita más rápido y no te '
                                           'duelan las manos al amasar.',
                         'resumen_visual': 'Siéntate a la mesa para no cansarte.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Amasa suavemente con tus manos limpias hasta que la masa se sienta como '
                                            'plastilina suave y no se agriete de las orillas. Si la sientes muy seca, '
                                            'ponle otro chorrito de agua.',
                         'imagen': 'tlacoyos-requeson-paso3.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Amasa suavemente con tus manos limpias hasta que la masa se sienta como '
                                           'plastilina suave y no se...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pon el requesón pasteurizado en un platito. Es muy importante que sea '
                                            'pasteurizado para proteger tu digestión. Machácalo un poquito con un '
                                            'tenedor para que sea fácil untarlo.',
                         'imagen': 'tlacoyos-requeson-paso4.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pon el requesón pasteurizado en un platito.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Divide tu masa en seis bolitas iguales. Toma una bolita, aplástala un '
                                            'poco con tus dos manos (como si fueras a hacer una tortilla gordita) y '
                                            'hazle un huequito en el centro.',
                         'imagen': 'tlacoyos-requeson-paso5.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Divide tu masa en seis bolitas iguales.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Ponle media cucharadita de requesón en medio. ¡No le pongas mucho! Si lo '
                                            'rellenas de más, se va a reventar al cocerlo.',
                         'imagen': 'tlacoyos-requeson-paso6.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Ponle media cucharadita de requesón en medio.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Cierra la masita pellizcando los bordes hacia el centro para tapar bien '
                                            'el queso. Dale forma alargadita de óvalo con tus manos, aplastando muy '
                                            'suavecito.',
                         'imagen': 'tlacoyos-requeson-paso7.jpeg',
                         'nota_seguridad': 'Hazlo con mucha calma para que la masita no se rompa de los lados.',
                         'resumen_visual': 'Cierra la masita pellizcando los bordes hacia el centro para tapar bien el '
                                           'queso.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Repite esto con todas las bolitas y ve poniendo los tlacoyos crudos en un '
                                            'plato. Puedes cubrirlos con un trapito limpio y húmedo para que no se '
                                            'resequen.',
                         'imagen': 'tlacoyos-requeson-paso8.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Repite esto con todas las bolitas y ve poniendo los tlacoyos crudos en un '
                                           'plato.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Enciende tu estufa a fuego medio-bajo. Pon tu comal a calentar.',
                         'imagen': 'tlacoyos-requeson-paso9.jpeg',
                         'nota_seguridad': 'Asegúrate de no traer mangas muy sueltas que puedan rozar con las llamas '
                                           'de la estufa.',
                         'resumen_visual': 'Enciende tu estufa a fuego medio-bajo.',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['aceite', 'estufa'],
                         'detalle_hablado': 'Con una servilleta de papel limpia o una brochita, úntale apenas unas '
                                            'gotitas de aceite al comal para que los tlacoyos no se peguen. No los '
                                            'vamos a freír, solo asar.',
                         'imagen': 'tlacoyos-requeson-paso10.jpeg',
                         'nota_seguridad': 'Ten cuidado de no acercar los dedos al metal caliente del comal.',
                         'resumen_visual': 'Con una servilleta de papel limpia o una brochita, úntale apenas unas '
                                           'gotitas de aceite al comal...',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': 'Pon los tlacoyos en el comal con cuidado. Te pondré un aviso de 6 minutos '
                                            'para que la masa se vaya cociendo despacito y no quede cruda por dentro.',
                         'imagen': 'tlacoyos-requeson-paso11.jpeg',
                         'nota_seguridad': 'No dejes la cocina sola, quédate cerquita vigilando.',
                         'resumen_visual': 'Pon los tlacoyos en el comal con cuidado.',
                         'temporizador_segundos': 360},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Sonó la alarma! Revisa un tlacoyo. Si ya se ve cocidito, doradito y se '
                                            'despega fácil, voltéalos todos usando una espátula ancha. Te pongo otros '
                                            '6 minutitos.',
                         'imagen': 'tlacoyos-requeson-paso12.jpeg',
                         'nota_seguridad': 'Usa siempre la espátula, no los voltees con la mano porque queman mucho y '
                                           'el queso puede salirse.',
                         'resumen_visual': '¡Sonó la alarma!',
                         'temporizador_segundos': 360},
                     {   'alertas_seguridad': ['estufa'],
                         'detalle_hablado': '¡Listo! Antes de apagar, abre un poquitito uno de los tlacoyos del centro '
                                            'con la espátula para confirmar que la masa esté completamente cocida y no '
                                            'se vea húmeda ni cruda. Si ya están, apaga la estufa.',
                         'imagen': 'tlacoyos-requeson-paso13.jpeg',
                         'nota_seguridad': 'Por favor, verifica muy bien con tus propios ojos que la perilla del gas '
                                           'sí quedó completamente cerrada. Comer masa cruda puede caer muy pesado.',
                         'resumen_visual': '¡Listo!',
                         'temporizador_segundos': None},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Pasa los tlacoyos a un plato y déjalos reposar un par de minutitos. El '
                                            'requesón de adentro guarda muchísimo calor. Te marco el tiempo.',
                         'imagen': 'tlacoyos-requeson-paso14.jpeg',
                         'nota_seguridad': None,
                         'resumen_visual': 'Pasa los tlacoyos a un plato y déjalos reposar un par de minutitos.',
                         'temporizador_segundos': 120},
                     {   'alertas_seguridad': [],
                         'detalle_hablado': 'Baña tus tlacoyos con un poco de salsa suave y ponles queso fresco '
                                            'desmoronado arriba. Córtalos en pedacitos en tu mismo plato para que sea '
                                            'muy fácil masticarlos. ¡Buen provecho!',
                         'imagen': 'tlacoyos-requeson-paso15.jpeg',
                         'nota_seguridad': 'Tócalos un poquito con los labios antes de dar el primer bocado para '
                                           'asegurar que la temperatura por dentro no te vaya a quemar.',
                         'resumen_visual': 'Baña tus tlacoyos con un poco de salsa suave y ponles queso fresco '
                                           'desmoronado arriba.',
                         'temporizador_segundos': None}],
        'porciones': 3,
        'slug': 'tlacoyos-requeson',
        'tiempo_total_min': 26,
        'titulo': 'Tlacoyos de requesón'}]

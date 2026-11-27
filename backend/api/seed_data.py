"""Contenido inicial de Aterriza.

Este archivo es la fuente de las guías que se cargan con la migración de datos.
Para cambiar el contenido puedes editar el admin de Django o modificar este
archivo y volver a sembrar la base de datos.
"""

GUIDES = [
    {
        "slug": "primeros-7-dias",
        "title": "Tus primeros 7 días",
        "summary": (
            "Los trámites que conviene resolver al llegar. No tienes que hacerlo "
            "todo el primer día: ve paso a paso."
        ),
        "category": "Primeros pasos",
        "emoji": "🚀",
        "featured": True,
        "official_url": "https://sede.extra.gob.es/",
        "official_label": "Sede de Extranjería",
        "steps": [
            {
                "title": "Empadrónate en tu municipio",
                "description": (
                    "Es el registro que te vincula a tu ciudad y suele ser requisito "
                    "para la sanidad, el banco o la universidad. Pide cita en tu "
                    "ayuntamiento y lleva pasaporte y contrato de alquiler (o una "
                    "autorización del titular)."
                ),
                "tip": "Pide un volante de empadronamiento y guárdalo.",
            },
            {
                "title": "Solicita tu NIE o TIE",
                "description": (
                    "El NIE identifica a las personas extranjeras; el TIE es la tarjeta "
                    "física. Consulta en Extranjería o en la comisaría qué necesitas "
                    "según tu visado y pide cita previa."
                ),
                "tip": "Las citas suelen tardar: pide la primera cuanto antes.",
            },
            {
                "title": "Elige cómo cubrir tu salud",
                "description": (
                    "Según tu visado y tu comunidad, puedes tener tarjeta sanitaria "
                    "pública o necesitar un seguro privado. Infórmate en tu universidad "
                    "y en tu centro de salud."
                ),
                "tip": "No esperes a enfermarte para resolverlo.",
            },
            {
                "title": "Abre una cuenta bancaria",
                "description": (
                    "La necesitarás para la matrícula, el alquiler o una beca. Busca una "
                    "cuenta sin comisiones para estudiantes."
                ),
                "tip": "Pregunta si piden NIE o empadronamiento.",
            },
            {
                "title": "Contrata móvil e Internet",
                "description": (
                    "Puedes empezar con una tarjeta prepago y cambiar después. Si "
                    "alquilas, comprueba si la fibra ya está instalada en la vivienda."
                ),
                "tip": "Evita permanencias largas al principio.",
            },
            {
                "title": "Activa el transporte público",
                "description": (
                    "Saca la tarjeta de transporte de tu ciudad y pregunta por el abono "
                    "joven o universitario."
                ),
                "tip": "Muchos abonos tienen descuentos importantes para estudiantes.",
            },
        ],
    },
    {
        "slug": "empadronamiento",
        "title": "Empadronamiento",
        "summary": (
            "Registrarte en el ayuntamiento de la ciudad donde vives. Es rápido y te "
            "abre muchas puertas."
        ),
        "category": "Documentos",
        "emoji": "🏛️",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Pide cita en tu ayuntamiento",
                "description": (
                    "Busca «empadronamiento» en la web de tu ayuntamiento. Algunos "
                    "municipios permiten hacerlo online o por teléfono."
                ),
            },
            {
                "title": "Reúne los documentos",
                "description": (
                    "Normalmente: pasaporte, contrato de alquiler o autorización del "
                    "propietario y, a veces, un formulario del ayuntamiento."
                ),
            },
            {
                "title": "Inscríbete en el domicilio",
                "description": (
                    "Si no apareces en el contrato, el titular o los residentes deben "
                    "autorizarte. En pisos compartidos es habitual firmar un documento "
                    "de consentimiento."
                ),
            },
            {
                "title": "Pide el volante de empadronamiento",
                "description": (
                    "Es un justificante de que estás registrado. Te lo pedirán para la "
                    "sanidad, el banco, la universidad o el NIE."
                ),
                "tip": "Escanea el volante y guárdalo en tu carpeta de documentos.",
            },
        ],
    },
    {
        "slug": "nie-tie",
        "title": "NIE y TIE",
        "summary": (
            "El número que te identifica como extranjero y la tarjeta que lo acredita. "
            "Depende de tu visado y de tu país."
        ),
        "category": "Documentos",
        "emoji": "🪪",
        "official_url": "https://sede.extra.gob.es/",
        "official_label": "Cita y trámites de Extranjería",
        "steps": [
            {
                "title": "Comprueba qué trámite te corresponde",
                "description": (
                    "No es lo mismo una estancia corta que una autorización por "
                    "estudios. Revisa tu visado y pregunta en la oficina internacional "
                    "de tu universidad."
                ),
            },
            {
                "title": "Pide cita previa",
                "description": (
                    "Las citas se piden en la Sede Electrónica de Extranjería o, en "
                    "algunos casos, en la comisaría de policía. Mira también las "
                    "instrucciones de tu provincia."
                ),
            },
            {
                "title": "Paga la tasa",
                "description": (
                    "Suele pagarse con el modelo 790 y se abona en un banco. Guarda el "
                    "justificante."
                ),
            },
            {
                "title": "Acude con originales y copias",
                "description": (
                    "Lleva pasaporte, formulario, fotos recientes, matrícula, seguro "
                    "médico y justificante de medios económicos, según tu caso."
                ),
            },
            {
                "title": "Recoge o renueva la tarjeta",
                "description": (
                    "Revisa la fecha de caducidad y pide cita para renovarla con "
                    "antelación."
                ),
                "tip": "Haz fotos o escaneos de todo. No lleves los originales a clase.",
            },
        ],
    },
    {
        "slug": "documentos-seguros",
        "title": "Guarda tus documentos",
        "summary": (
            "Ten localizados pasaporte, visado, NIE, seguro y matrícula. Sin "
            "complicaciones y sin riesgos."
        ),
        "category": "Documentos",
        "emoji": "🔐",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Haz una copia digital de cada documento",
                "description": (
                    "Escanea o fotografía pasaporte, visado, NIE/TIE, seguro médico, "
                    "matrícula y contrato de alquiler."
                ),
            },
            {
                "title": "Guarda las copias en dos sitios seguros",
                "description": (
                    "Por ejemplo, una carpeta cifrada en la nube y un USB. Evita "
                    "enviarlos por chats o correos sin protección."
                ),
            },
            {
                "title": "Apunta las fechas de caducidad",
                "description": (
                    "Visado, NIE/TIE, seguro y pasaporte. Añade recordatorios en el "
                    "calendario del móvil."
                ),
            },
            {
                "title": "Lleva solo lo necesario",
                "description": (
                    "En el día a día basta con una fotocopia o una imagen. Los "
                    "originales, en un lugar seguro de casa."
                ),
                "tip": "Esta web no guarda documentos: solo te ayuda a organizarte.",
            },
        ],
    },
    {
        "slug": "cuenta-banco",
        "title": "Abrir una cuenta bancaria",
        "summary": (
            "Una cuenta para cobrar, pagar el alquiler y recibir becas, sin comisiones "
            "raras."
        ),
        "category": "Dinero",
        "emoji": "💳",
        "official_url": "https://clientebancario.bde.es/",
        "official_label": "Comparador del Banco de España",
        "steps": [
            {
                "title": "Compara cuentas para estudiantes",
                "description": (
                    "Busca «cuenta joven» o «cuenta sin comisiones». Revisa comisiones "
                    "de mantenimiento, tarjetas y transferencias."
                ),
            },
            {
                "title": "Prepara la documentación",
                "description": (
                    "Suelen pedir pasaporte o NIE, empadronamiento, matrícula y, a "
                    "veces, justificante de ingresos o beca."
                ),
            },
            {
                "title": "Abre la cuenta",
                "description": (
                    "Puedes pedir cita en una oficina o hacerlo online. Si acabas de "
                    "llegar, la oficina puede resolver mejor tus dudas."
                ),
            },
            {
                "title": "Activa la app y la tarjeta",
                "description": (
                    "Configura las notificaciones de pagos y guarda el IBAN en un lugar "
                    "seguro."
                ),
                "tip": (
                    "Pregunta expresamente si la cuenta tiene comisiones y cómo evitarlas."
                ),
            },
        ],
    },
    {
        "slug": "nomina-impuestos",
        "title": "Entiende tu nómina",
        "summary": "Tu salario, las deducciones y los impuestos básicos sin miedo.",
        "category": "Dinero",
        "emoji": "🧾",
        "official_url": "https://sede.agenciatributaria.gob.es/",
        "official_label": "Agencia Tributaria",
        "steps": [
            {
                "title": "Lee el encabezado de la nómina",
                "description": (
                    "Aparecen la empresa, el periodo y tus datos. Comprueba que "
                    "coinciden con tu contrato."
                ),
            },
            {
                "title": "Distingue bruto y neto",
                "description": (
                    "El salario bruto es antes de impuestos; el neto es lo que llega a "
                    "tu cuenta. La diferencia incluye IRPF y Seguridad Social."
                ),
            },
            {
                "title": "Revisa las deducciones",
                "description": (
                    "Comprueba los conceptos y los importes. Si algo no cuadra, "
                    "pregunta a la empresa o a un sindicato."
                ),
            },
            {
                "title": "Guarda todas las nóminas",
                "description": (
                    "Te las pedirán para renovar el NIE, alquilar o hacer la "
                    "declaración de la renta."
                ),
            },
            {
                "title": "Infórmate sobre la declaración",
                "description": (
                    "No todo el mundo está obligado a presentarla. Consulta la Agencia "
                    "Tributaria o pide ayuda en tu universidad."
                ),
                "tip": "Una nómina no es un contrato: conserva ambos.",
            },
        ],
    },
    {
        "slug": "medico",
        "title": "Médico y tarjeta sanitaria",
        "summary": "Cómo conseguir tarjeta sanitaria, pedir cita y saber dónde ir.",
        "category": "Salud",
        "emoji": "🏥",
        "official_url": "https://www.mscbs.gob.es/",
        "official_label": "Ministerio de Sanidad",
        "steps": [
            {
                "title": "Averigua qué cobertura tienes",
                "description": (
                    "Puede ser tarjeta sanitaria pública, seguro privado del visado o "
                    "tarjeta sanitaria europea. Pregunta en tu universidad y en tu "
                    "comunidad autónoma."
                ),
            },
            {
                "title": "Empadrónate si te lo piden",
                "description": (
                    "Muchas comunidades piden el volante de empadronamiento para darte "
                    "la tarjeta sanitaria."
                ),
            },
            {
                "title": "Solicita la tarjeta en tu centro de salud",
                "description": (
                    "Busca el centro de atención primaria que te corresponde y pide "
                    "cita para solicitarla."
                ),
            },
            {
                "title": "Aprende a pedir cita",
                "description": (
                    "Se suele pedir por la app o web de tu comunidad, por teléfono o en "
                    "el mostrador. Para urgencias graves, llama al 112."
                ),
            },
            {
                "title": "Guarda tus datos sanitarios",
                "description": (
                    "Apunta tu número de la Seguridad Social o de póliza, tu centro de "
                    "salud y las urgencias de tu zona."
                ),
                "tip": (
                    "Las farmacias con cruz verde dan consejo básico y venden "
                    "medicamentos sin receta."
                ),
            },
        ],
    },
    {
        "slug": "alquiler",
        "title": "Alquilar una habitación o piso",
        "summary": "Encontrar alojamiento sin caer en estafas.",
        "category": "Vivienda",
        "emoji": "🏠",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Fija un presupuesto realista",
                "description": (
                    "Suma alquiler, gastos, fianza y transporte. En pisos compartidos, "
                    "pregunta qué está incluido."
                ),
            },
            {
                "title": "Busca en varios sitios",
                "description": (
                    "Portales inmobiliarios, grupos de tu universidad y residencias. "
                    "Desconfía de precios muy por debajo del mercado."
                ),
            },
            {
                "title": "Visita antes de pagar",
                "description": (
                    "Visita en persona o por videollamada. Nunca pagues una fianza sin "
                    "ver el contrato ni el alojamiento."
                ),
            },
            {
                "title": "Revisa el contrato",
                "description": (
                    "Comprueba duración, fianza, gastos incluidos, normas y quién es el "
                    "propietario."
                ),
            },
            {
                "title": "Documenta el estado y los pagos",
                "description": (
                    "Haz fotos al entrar y guarda recibos o transferencias. Así evitas "
                    "problemas al salir."
                ),
                "tip": (
                    "Si te piden dinero por una habitación que no has visto, es una "
                    "señal de alarma."
                ),
            },
        ],
    },
    {
        "slug": "matricula",
        "title": "Matrícula universitaria",
        "summary": "Matricularte sin perder plazos ni papeles.",
        "category": "Universidad",
        "emoji": "🎓",
        "official_url": "https://www.universidades.gob.es/",
        "official_label": "Ministerio de Universidades",
        "steps": [
            {
                "title": "Revisa plazos y requisitos",
                "description": (
                    "Consulta la web de tu universidad y la oficina de estudiantes "
                    "internacionales. Cada grado y cada universidad tiene fechas "
                    "distintas."
                ),
            },
            {
                "title": "Prepara la documentación",
                "description": (
                    "Título o equivalencia, pasaporte/NIE, seguro médico, fotos y "
                    "justificante de pago, según el caso."
                ),
            },
            {
                "title": "Paga y guarda el justificante",
                "description": (
                    "La matrícula puede pagarse en varios plazos. Conserva el resguardo."
                ),
            },
            {
                "title": "Activa tu cuenta de la universidad",
                "description": (
                    "Correo, campus virtual y carné. Ahí llegarán los avisos "
                    "importantes."
                ),
            },
            {
                "title": "Pregunta por becas y descuentos",
                "description": (
                    "Hay ayudas para estudiantes, pero suelen tener plazos. Pregunta en "
                    "la oficina internacional."
                ),
                "tip": (
                    "Guarda una copia de la matrícula: te la pedirán para el NIE y "
                    "para el banco."
                ),
            },
        ],
    },
    {
        "slug": "movil-internet",
        "title": "Móvil, Internet y suministros",
        "summary": (
            "Móvil, fibra, luz y agua: lo básico para estar conectado y vivir en casa."
        ),
        "category": "Primeros pasos",
        "emoji": "📱",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Empieza con una tarjeta prepago",
                "description": (
                    "Es la opción más rápida al llegar: compras la SIM, recargas y no "
                    "tienes permanencia."
                ),
            },
            {
                "title": "Compara tarifas",
                "description": (
                    "Mira cobertura, datos y precio. Pregunta en tu universidad por "
                    "acuerdos con operadores."
                ),
            },
            {
                "title": "Contrata Internet en casa",
                "description": (
                    "Comprueba si la vivienda tiene fibra instalada y si el contrato es "
                    "sin permanencia."
                ),
            },
            {
                "title": "Pon la luz y el agua a tu nombre",
                "description": (
                    "Si alquilas, pregunta al propietario cómo están contratados los "
                    "suministros. Cambiar de titular requiere datos y a veces una "
                    "fianza."
                ),
            },
            {
                "title": "Guarda las facturas",
                "description": (
                    "Te servirán para reclamar o justificar gastos. Activa la factura "
                    "electrónica."
                ),
                "tip": (
                    "No firmes permanencias largas si no sabes cuánto tiempo te "
                    "quedarás."
                ),
            },
        ],
    },
    {
        "slug": "transporte",
        "title": "Transporte público",
        "summary": "Moverte por la ciudad sin pagar de más.",
        "category": "Moverse y hablar",
        "emoji": "🚇",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Localiza metro, bus y tren",
                "description": (
                    "Mira el mapa de transporte de tu ciudad y las apps oficiales de "
                    "rutas."
                ),
            },
            {
                "title": "Saca la tarjeta de transporte",
                "description": (
                    "Muchas ciudades tienen tarjeta recargable. Pregunta por el abono "
                    "joven o universitario."
                ),
            },
            {
                "title": "Valida siempre el billete",
                "description": (
                    "Aunque no haya tornos, valida al entrar o al salir. Las multas por "
                    "no validar son habituales."
                ),
            },
            {
                "title": "Calcula tus trayectos",
                "description": (
                    "Compara el abono mensual y los billetes sueltos según cuántos "
                    "viajes hagas."
                ),
                "tip": (
                    "Pregunta en la universidad: muchos campus tienen descuentos o "
                    "abonos especiales."
                ),
            },
        ],
    },
    {
        "slug": "cocina",
        "title": "Cocinar lo básico",
        "summary": (
            "Cinco platos sencillos y baratos para no depender de la comida a domicilio."
        ),
        "category": "Vida diaria",
        "emoji": "🍳",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Prepara lo básico",
                "description": (
                    "Una olla, una sartén, una tabla, un cuchillo y un par de tuppers "
                    "son suficientes para empezar."
                ),
            },
            {
                "title": "Pasta con tomate",
                "description": (
                    "Cuece pasta 8-10 minutos. Mientras, sofríe tomate triturado con "
                    "aceite, ajo y sal. Mezcla y listo."
                ),
            },
            {
                "title": "Arroz con verduras y huevo",
                "description": (
                    "Cuece arroz, saltea verduras y añade un huevo. Puedes usar arroz "
                    "del día anterior."
                ),
            },
            {
                "title": "Tortilla francesa y ensalada",
                "description": (
                    "Bate dos huevos con una pizca de sal, cuájalos en la sartén y "
                    "acompaña con ensalada o pan."
                ),
            },
            {
                "title": "Pollo a la plancha con patata",
                "description": (
                    "Cocina el pollo hasta que esté dorado por dentro y acompaña con "
                    "patata cocida o asada."
                ),
            },
            {
                "title": "Cocina de más y congela",
                "description": (
                    "Dos raciones hoy son una comida resuelta mañana. Etiqueta el "
                    "tupper con la fecha."
                ),
                "tip": (
                    "Lávate las manos, cocina bien el pollo y guarda la comida fría en "
                    "la nevera cuanto antes."
                ),
            },
        ],
    },
    {
        "slug": "lavadora",
        "title": "Lavadora, ropa y limpieza",
        "summary": "Lavar, tender, planchar y mantener la casa sin dramas.",
        "category": "Vida diaria",
        "emoji": "🧺",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Separa la ropa",
                "description": (
                    "Blancos, colores y prendas delicadas. Revisa las etiquetas antes "
                    "de lavar."
                ),
            },
            {
                "title": "No llenes demasiado el tambor",
                "description": (
                    "La ropa debe moverse. Llena hasta unas tres cuartas partes."
                ),
            },
            {
                "title": "Dosifica el detergente",
                "description": (
                    "Más jabón no lava mejor. Usa la medida del envase y el programa "
                    "adecuado."
                ),
            },
            {
                "title": "Elige un programa normal",
                "description": (
                    "30-40 °C suele bastar para ropa de uso diario. Reserva el agua "
                    "caliente para sábanas y toallas."
                ),
            },
            {
                "title": "Tiende y plancha",
                "description": (
                    "Cuelga la ropa al aire o usa secadora si la hay. Plancha solo lo "
                    "necesario."
                ),
            },
            {
                "title": "Limpieza semanal",
                "description": (
                    "Baño, cocina, suelos y basura. Dedica 15 minutos al día a una zona "
                    "y evita acumular."
                ),
                "tip": (
                    "Los símbolos de la etiqueta indican temperatura, secadora y "
                    "plancha. Ante la duda, agua fría."
                ),
            },
        ],
    },
    {
        "slug": "compra-presupuesto",
        "title": "Compra y presupuesto",
        "summary": "Comprar bien y llegar a fin de mes.",
        "category": "Dinero",
        "emoji": "🛒",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Planifica el menú de la semana",
                "description": (
                    "Decide 4-5 comidas y haz la lista con lo que ya tienes en casa."
                ),
            },
            {
                "title": "Compra con lista y sin hambre",
                "description": "La lista evita compras impulsivas y desperdicio.",
            },
            {
                "title": "Compara el precio por kilo",
                "description": (
                    "El paquete grande no siempre es el más barato. Mira la etiqueta "
                    "por kg o litro."
                ),
            },
            {
                "title": "Fija un límite semanal",
                "description": (
                    "Separa alquiler y facturas primero. Para comida, usa un límite "
                    "semanal realista."
                ),
            },
            {
                "title": "Apunta los gastos",
                "description": (
                    "Una nota en el móvil o una hoja de cálculo basta. Revisa cada "
                    "semana en qué se te va el dinero."
                ),
            },
            {
                "title": "Guarda tickets y facturas",
                "description": (
                    "Te servirán para reclamar y para controlar tus gastos."
                ),
                "tip": (
                    "Marca la compra como hecha cada semana: el hábito es lo que más "
                    "ahorra."
                ),
            },
        ],
    },
    {
        "slug": "idioma-costumbres",
        "title": "Idioma y costumbres",
        "summary": "Mejorar el idioma y entender las costumbres del día a día.",
        "category": "Moverse y hablar",
        "emoji": "🗣️",
        "official_url": "",
        "official_label": "",
        "steps": [
            {
                "title": "Practica un poco cada día",
                "description": (
                    "10 minutos de vocabulario o una serie con subtítulos ayudan más "
                    "que estudiar una hora un domingo."
                ),
            },
            {
                "title": "Apúntate a un intercambio de idiomas",
                "description": (
                    "Las universidades y asociaciones de estudiantes organizan "
                    "tándems y actividades."
                ),
            },
            {
                "title": "Aprende frases de supervivencia",
                "description": (
                    "Tienda, médico, transporte, urgencias y clases. Anótalas en el "
                    "móvil."
                ),
            },
            {
                "title": "Pregunta antes de asumir",
                "description": (
                    "Los horarios, la comida y las normas sociales cambian. Preguntar "
                    "es normal y ayuda a integrarse."
                ),
            },
            {
                "title": "Conoce a gente local",
                "description": (
                    "Asociaciones, voluntariado, deporte o grupos de la universidad. "
                    "Las amistades también son adaptación."
                ),
                "tip": (
                    "Equivocarte al hablar es parte del proceso. La mayoría de la gente "
                    "valora que lo intentes."
                ),
            },
        ],
    },
]

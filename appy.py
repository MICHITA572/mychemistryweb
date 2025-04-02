import streamlit as st

# Definir los elementos químicos con sus propiedades
elementos = [
    {"numero": 1, "simbolo": "H", "nombre": "Hidrógeno", "uso": "Combustible y producción de amoníaco", "ubicacion": "En el agua y compuestos orgánicos"},
    {"numero": 2, "simbolo": "He", "nombre": "Helio", "uso": "Globos y refrigerante", "ubicacion": "Atmósfera y gas natural"},
    {"numero": 3, "simbolo": "Li", "nombre": "Litio", "uso": "Baterías y medicina", "ubicacion": "Minerales como espodumena"},
    { "numero": 4, "simbolo": "Be", "nombre": "Berilio", "uso": "Componentes aeroespaciales y electrónicos","ubicacion": "En minerales como el berilo"},{
  "numero": 5,
  "simbolo": "B",
  "nombre": "Boro",
  "uso": "Vidrio resistente al calor y detergentes",
  "ubicacion": "En minerales como el bórax"
}{
  "numero": 6,
  "simbolo": "C",
  "nombre": "Carbono",
  "uso": "Fundamental en compuestos orgánicos y materiales como el grafito y diamante",
  "ubicacion": "En la naturaleza, como en combustibles fósiles y biomasa"
},
{
  "numero": 7,
  "simbolo": "N",
  "nombre": "Nitrógeno",
  "uso": "Producción de fertilizantes y gas inerte en procesos industriales",
  "ubicacion": "En la atmósfera terrestre"
},
{
  "numero": 8,
  "simbolo": "O",
  "nombre": "Oxígeno",
  "uso": "Respiración y procesos de combustión",
  "ubicacion": "En el aire y agua"
},
{
  "numero": 9,
  "simbolo": "F",
  "nombre": "Flúor",
  "uso": "Producción de refrigerantes y fluoración del agua potable",
  "ubicacion": "En minerales como la fluorita"
},
{
  "numero": 10,
  "simbolo": "Ne",
  "nombre": "Neón",
  "uso": "Lámparas de neón y señalización luminosa",
  "ubicacion": "En la atmósfera terrestre"
}
{
  "numero": 11,
  "simbolo": "Na",
  "nombre": "Sodio",
  "uso": "Producción de sales y tratamiento de agua",
  "ubicacion": "En sales minerales como el cloruro de sodio"
},
{
  "numero": 12,
  "simbolo": "Mg",
  "nombre": "Magnesio",
  "uso": "Aleaciones ligeras y suplementos alimenticios",
  "ubicacion": "En minerales como la dolomita"
},
{
  "numero": 13,
  "simbolo": "Al",
  "nombre": "Aluminio",
  "uso": "Material estructural ligero y envolturas de alimentos",
  "ubicacion": "En minerales como la bauxita"
},
{
  "numero": 14,
  "simbolo": "Si",
  "nombre": "Silicio",
  "uso": "Fabricación de microchips y materiales de construcción",
  "ubicacion": "En la arena y silicatos"
},
{
  "numero": 15,
  "simbolo": "P",
  "nombre": "Fósforo",
  "uso": "Producción de fertilizantes y detergentes",
  "ubicacion": "En minerales fosfatados"
},
{
  "numero": 16,
  "simbolo": "S",
  "nombre": "Azufre",
  "uso": "Producción de ácido sulfúrico y productos químicos",
  "ubicacion": "En depósitos volcánicos y minerales"
},
{
  "numero": 17,
  "simbolo": "Cl",
  "nombre": "Cloro",
  "uso": "Desinfección del agua y producción de plásticos",
  "ubicacion": "En sales minerales como el cloruro de sodio"
},
{
  "numero": 18,
  "simbolo": "Ar",
  "nombre": "Argón",
  "uso": "Gas inerte en soldadura y lámparas fluorescentes",
  "ubicacion": "En la atmósfera terrestre"
},
{
  "numero": 19,
  "simbolo": "K",
  "nombre": "Potasio",
  "uso": "Producción de fertilizantes y equilibrio electrolítico en el cuerpo",
  "ubicacion": "En minerales como la silvita"
},
{
  "numero": 20,
  "simbolo": "Ca",
  "nombre": "Calcio",
  "uso": "Producción de cemento y fortalecimiento de huesos",
  "ubicacion": "En minerales como la calcita"
}
{
  "numero": 21,
  "simbolo": "Sc",
  "nombre": "Escandio",
  "uso": "Aleaciones ligeras en la industria aeroespacial",
  "ubicacion": "En minerales como la thortveitita"
},
{
  "numero": 22,
  "simbolo": "Ti",
  "nombre": "Titanio",
  "uso": "Material resistente para prótesis y aeronaves",
  "ubicacion": "En minerales como el rutilo y la ilmenita"
},
{
  "numero": 23,
  "simbolo": "V",
  "nombre": "Vanadio",
  "uso": "Fortalecimiento de aleaciones de acero",
  "ubicacion": "En minerales como la vanadinita"
},
{
  "numero": 24,
  "simbolo": "Cr",
  "nombre": "Cromo",
  "uso": "Producción de acero inoxidable y recubrimientos",
  "ubicacion": "En minerales como la cromita"
},
{
  "numero": 25,
  "simbolo": "Mn",
  "nombre": "Manganeso",
  "uso": "Aleaciones y pilas secas",
  "ubicacion": "En minerales como la pirolusita"
},
{
  "numero": 26,
  "simbolo": "Fe",
  "nombre": "Hierro",
  "uso": "Producción de acero y herramientas",
  "ubicacion": "En minerales como la hematita y magnetita"
},
{
  "numero": 27,
  "simbolo": "Co",
  "nombre": "Cobalto",
  "uso": "Baterías recargables y aleaciones magnéticas",
  "ubicacion": "En minerales como la cobaltita"
},
{
  "numero": 28,
  "simbolo": "Ni",
  "nombre": "Níquel",
  "uso": "Monedas, baterías y aleaciones resistentes a la corrosión",
  "ubicacion": "En minerales como la pentlandita"
},
{
  "numero": 29,
  "simbolo": "Cu",
  "nombre": "Cobre",
  "uso": "Cableado eléctrico y monedas",
  "ubicacion": "En minerales como la calcopirita y la malaquita"
},
{
  "numero": 30,
  "simbolo": "Zn",
  "nombre": "Zinc",
  "uso": "Galvanización de metales y producción de baterías",
  "ubicacion": "En minerales como la esfalerita"
}
{
  "numero": 31,
  "simbolo": "Ga",
  "nombre": "Galio",
  "uso": "Electrónica y termómetros de alta precisión",
  "ubicacion": "En minerales como la bauxita"
},
{
  "numero": 32,
  "simbolo": "Ge",
  "nombre": "Germanio",
  "uso": "Fabricación de semiconductores y óptica infrarroja",
  "ubicacion": "En minerales como la esfalerita"
},
{
  "numero": 33,
  "simbolo": "As",
  "nombre": "Arsénico",
  "uso": "Producción de pesticidas y semiconductores",
  "ubicacion": "En minerales como la arsenopirita"
},
{
  "numero": 34,
  "simbolo": "Se",
  "nombre": "Selenio",
  "uso": "Fotocopiadoras y vidrios resistentes al calor",
  "ubicacion": "En minerales como la pirita"
},
{
  "numero": 35,
  "simbolo": "Br",
  "nombre": "Bromo",
  "uso": "Producción de retardantes de fuego y pesticidas",
  "ubicacion": "En sales naturales del agua marina"
},
{
  "numero": 36,
  "simbolo": "Kr",
  "nombre": "Kriptón",
  "uso": "Lámparas fluorescentes y fotografía de alta velocidad",
  "ubicacion": "En la atmósfera terrestre"
},
{
  "numero": 37,
  "simbolo": "Rb",
  "nombre": "Rubidio",
  "uso": "Investigación científica y relojes atómicos",
  "ubicacion": "En minerales como la lepidolita"
},
{
  "numero": 38,
  "simbolo": "Sr",
  "nombre": "Estroncio",
  "uso": "Fuegos artificiales y productos de cerámica",
  "ubicacion": "En minerales como la celestina"
},
{
  "numero": 39,
  "simbolo": "Y",
  "nombre": "Itrio",
  "uso": "Producción de láseres y superconductores",
  "ubicacion": "En minerales como la xenotima"
},
{
  "numero": 40,
  "simbolo": "Zr",
  "nombre": "Zirconio",
  "uso": "Materiales resistentes al calor y reactores nucleares",
  "ubicacion": "En minerales como el circón"
},
{
  "numero": 41,
  "simbolo": "Nb",
  "nombre": "Niobio",
  "uso": "Aleaciones para turbinas y componentes electrónicos",
  "ubicacion": "En minerales como la columbita"
},
{
  "numero": 42,
  "simbolo": "Mo",
  "nombre": "Molibdeno",
  "uso": "Producción de aleaciones resistentes al calor y catalizadores",
  "ubicacion": "En minerales como la molibdenita"
},
{
  "numero": 43,
  "simbolo": "Tc",
  "nombre": "Tecnecio",
  "uso": "Diagnóstico médico por imagen y catalizadores",
  "ubicacion": "Sintético o en trazas en la naturaleza"
},
{
  "numero": 44,
  "simbolo": "Ru",
  "nombre": "Rutenio",
  "uso": "Aleaciones resistentes y productos electrónicos",
  "ubicacion": "En minerales como la pentlandita"
},
{
  "numero": 45,
  "simbolo": "Rh",
  "nombre": "Rodio",
  "uso": "Catalizadores automotrices y joyería",
  "ubicacion": "En minerales como la rodocrosita"
},
{
  "numero": 46,
  "simbolo": "Pd",
  "nombre": "Paladio",
  "uso": "Catalizadores y electrónica",
  "ubicacion": "En minerales como la cooperita"
},
{
  "numero": 47,
  "simbolo": "Ag",
  "nombre": "Plata",
  "uso": "Monedas, joyería y electrónica",
  "ubicacion": "En minerales como la argentita y galena"
},
{
  "numero": 48,
  "simbolo": "Cd",
  "nombre": "Cadmio",
  "uso": "Baterías recargables y revestimientos metálicos",
  "ubicacion": "En minerales como la esfalerita"
},
{
  "numero": 49,
  "simbolo": "In",
  "nombre": "Indio",
  "uso": "Pantallas táctiles y aleaciones",
  "ubicacion": "En minerales como la esfalerita"
},
{
  "numero": 50,
  "simbolo": "Sn",
  "nombre": "Estaño",
  "uso": "Soldadura y recubrimientos",
  "ubicacion": "En minerales como la casiterita"
}
{
  "numero": 51,
  "simbolo": "Sb",
  "nombre": "Antimonio",
  "uso": "Producción de aleaciones y semiconductores",
  "ubicacion": "En minerales como la estibina"
},
{
  "numero": 52,
  "simbolo": "Te",
  "nombre": "Telurio",
  "uso": "Semiconductores y aleaciones",
  "ubicacion": "En minerales como la calaverita"
},
{
  "numero": 53,
  "simbolo": "I",
  "nombre": "Yodo",
  "uso": "Antisépticos y producción de medicamentos",
  "ubicacion": "En algas y depósitos marinos"
},
{
  "numero": 54,
  "simbolo": "Xe",
  "nombre": "Xenón",
  "uso": "Lámparas y investigación médica",
  "ubicacion": "En la atmósfera terrestre"
},
{
  "numero": 55,
  "simbolo": "Cs",
  "nombre": "Cesio",
  "uso": "Relojes atómicos y investigación científica",
  "ubicacion": "En minerales como la polucita"
},
{
  "numero": 56,
  "simbolo": "Ba",
  "nombre": "Bario",
  "uso": "Materiales de radiología y fuegos artificiales",
  "ubicacion": "En minerales como la barita"
},
{
  "numero": 57,
  "simbolo": "La",
  "nombre": "Lantano",
  "uso": "Aleaciones y lentes especiales",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 58,
  "simbolo": "Ce",
  "nombre": "Cerio",
  "uso": "Catalizadores y vidrios resistentes al calor",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 59,
  "simbolo": "Pr",
  "nombre": "Praseodimio",
  "uso": "Láseres y imanes fuertes",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 60,
  "simbolo": "Nd",
  "nombre": "Neodimio",
  "uso": "Imanes permanentes y láseres",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 61,
  "simbolo": "Pm",
  "nombre": "Prometio",
  "uso": "Investigación científica y baterías nucleares",
  "ubicacion": "Sintético o en trazas naturales"
},
{
  "numero": 62,
  "simbolo": "Sm",
  "nombre": "Samario",
  "uso": "Imanes y reactores nucleares",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 63,
  "simbolo": "Eu",
  "nombre": "Europio",
  "uso": "Fósforos para pantallas y lámparas fluorescentes",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 64,
  "simbolo": "Gd",
  "nombre": "Gadolinio",
  "uso": "Materiales magnéticos y resonancia magnética",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 65,
  "simbolo": "Tb",
  "nombre": "Terbio",
  "uso": "Pantallas electrónicas y láseres",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 66,
  "simbolo": "Dy",
  "nombre": "Disprosio",
  "uso": "Imanes y reactores nucleares",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 67,
  "simbolo": "Ho",
  "nombre": "Holmio",
  "uso": "Láseres y materiales magnéticos",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 68,
  "simbolo": "Er",
  "nombre": "Erbio",
  "uso": "Materiales ópticos y láseres",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 69,
  "simbolo": "Tm",
  "nombre": "Tulio",
  "uso": "Láseres y tecnología médica",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 70,
  "simbolo": "Yb",
  "nombre": "Iterbio",
  "uso": "Aleaciones y investigación científica",
  "ubicacion": "En minerales como la bastnasita"
},
{
  "numero": 71,
  "simbolo": "Lu",
  "nombre": "Lutecio",
  "uso": "Catalizadores y investigación médica",
  "ubicacion": "En minerales como la monazita"
},
{
  "numero": 72,
  "simbolo": "Hf",
  "nombre": "Hafnio",
  "uso": "Reactores nucleares y aleaciones resistentes al calor",
  "ubicacion": "En minerales como el circón"
},
{
  "numero": 73,
  "simbolo": "Ta",
  "nombre": "Tántalo",
  "uso": "Componentes electrónicos y aleaciones resistentes",
  "ubicacion": "En minerales como la tantalita"
},
{
  "numero": 74,
  "simbolo": "W",
  "nombre": "Tungsteno",
  "uso": "Filamentos de lámparas y herramientas de corte",
  "ubicacion": "En minerales como la scheelita"
},
{
  "numero": 75,
  "simbolo": "Re",
  "nombre": "Renio",
  "uso": "Aleaciones para motores y catalizadores",
  "ubicacion": "En minerales como la molibdenita"
},
{
  "numero": 76,
  "simbolo": "Os",
  "nombre": "Osmio",
  "uso": "Aleaciones duras y puntas de pluma",
  "ubicacion": "En minerales como la osmiridio"
},
{
  "numero": 77,
  "simbolo": "Ir",
  "nombre": "Iridio",
  "uso": "Aleaciones resistentes y componentes electrónicos",
  "ubicacion": "En minerales como el iridosmina"
},
{
  "numero": 78,
  "simbolo": "Pt",
  "nombre": "Platino",
  "uso": "Joyas, catalizadores y electrónica",
  "ubicacion": "En minerales como la cooperita"
},
{
  "numero": 79,
  "simbolo": "Au",
  "nombre": "Oro",
  "uso": "Joyas, monedas y electrónica",
  "ubicacion": "En minerales como el oro nativo"
},
{
  "numero": 80,
  "simbolo": "Hg",
  "nombre": "Mercurio",
  "uso": "Termómetros y reactivos químicos",
  "ubicacion": "En minerales como el cinabrio"
},
{
  "numero": 81,
  "simbolo": "Tl",
  "nombre": "Talio",
  "uso": "Componentes electrónicos y investigación médica",
  "ubicacion": "En minerales como la lorandita"
},
{
  "numero": 82,
  "simbolo": "Pb",
  "nombre": "Plomo",
  "uso": "Baterías, revestimientos y soldadura",
  "ubicacion": "En minerales como la galena"
},
{
  "numero": 83,
  "simbolo": "Bi",
  "nombre": "Bismuto",
  "uso": "Aleaciones y medicamentos",
  "ubicacion": "En minerales como la bismutita"
},
{
  "numero": 84,
  "simbolo": "Po",
  "nombre": "Polonio",
  "uso": "Fuente de calor en generadores nucleares",
  "ubicacion": "Sintético o en trazas naturales"
},
{
  "numero": 85,
  "simbolo": "At",
  "nombre": "Astato",
  "uso": "Investigación médica y científica",
  "ubicacion": "Sintético o en trazas naturales"
},
{
  "numero": 86,
  "simbolo": "Rn",
  "nombre": "Radón",
  "uso": "Investigación científica y radioterapia",
  "ubicacion": "En trazas naturales del suelo"
},
{
  "numero": 87,
  "simbolo": "Fr",
  "nombre": "Francio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético o en trazas naturales"
},
{
  "numero": 88,
  "simbolo": "Ra",
  "nombre": "Radio",
  "uso": "Radioterapia y luminiscencia",
  "ubicacion": "En minerales como la uraninita"
},{
  "numero": 89,
  "simbolo": "Ac",
  "nombre": "Actinio",
  "uso": "Fuente de neutrones y estudio en energía nuclear",
  "ubicacion": "En minerales como la uraninita"
},
{
  "numero": 90,
  "simbolo": "Th",
  "nombre": "Torio",
  "uso": "Reactores nucleares y aleaciones metálicas",
  "ubicacion": "En minerales como la torita"
},
{
  "numero": 91,
  "simbolo": "Pa",
  "nombre": "Protactinio",
  "uso": "Investigación científica y estudios nucleares",
  "ubicacion": "En trazas en minerales de uranio"
},
{
  "numero": 92,
  "simbolo": "U",
  "nombre": "Uranio",
  "uso": "Combustible en reactores nucleares y armamento",
  "ubicacion": "En minerales como la uraninita"
},
{
  "numero": 93,
  "simbolo": "Np",
  "nombre": "Neptunio",
  "uso": "Investigación científica y detección de radiación",
  "ubicacion": "Sintético o trazas en minerales de uranio"
},
{
  "numero": 94,
  "simbolo": "Pu",
  "nombre": "Plutonio",
  "uso": "Reactores nucleares y armamento",
  "ubicacion": "Sintético o en trazas naturales"
},
{
  "numero": 95,
  "simbolo": "Am",
  "nombre": "Americio",
  "uso": "Detectores de humo e investigación nuclear",
  "ubicacion": "Sintético"
},
{
  "numero": 96,
  "simbolo": "Cm",
  "nombre": "Curio",
  "uso": "Fuente de neutrones y investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 97,
  "simbolo": "Bk",
  "nombre": "Berkelio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 98,
  "simbolo": "Cf",
  "nombre": "Californio",
  "uso": "Fuente de neutrones y tratamiento de cáncer",
  "ubicacion": "Sintético"
},
{
  "numero": 99,
  "simbolo": "Es",
  "nombre": "Einstenio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 100,
  "simbolo": "Fm",
  "nombre": "Fermio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
}
{
  "numero": 101,
  "simbolo": "Md",
  "nombre": "Mendelevio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 102,
  "simbolo": "No",
  "nombre": "Nobelio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 103,
  "simbolo": "Lr",
  "nombre": "Lawrencio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 104,
  "simbolo": "Rf",
  "nombre": "Rutherfordio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 105,
  "simbolo": "Db",
  "nombre": "Dubnio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 106,
  "simbolo": "Sg",
  "nombre": "Seaborgio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 107,
  "simbolo": "Bh",
  "nombre": "Bohrio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 108,
  "simbolo": "Hs",
  "nombre": "Hassio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 109,
  "simbolo": "Mt",
  "nombre": "Meitnerio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 110,
  "simbolo": "Ds",
  "nombre": "Darmstadtio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 111,
  "simbolo": "Rg",
  "nombre": "Roentgenio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 112,
  "simbolo": "Cn",
  "nombre": "Copernicio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 113,
  "simbolo": "Nh",
  "nombre": "Nihonio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 114,
  "simbolo": "Fl",
  "nombre": "Flerovio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 115,
  "simbolo": "Mc",
  "nombre": "Moscovio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 116,
  "simbolo": "Lv",
  "nombre": "Livermorio",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 117,
  "simbolo": "Ts",
  "nombre": "Tenesino",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
},
{
  "numero": 118,
  "simbolo": "Og",
  "nombre": "Oganesón",
  "uso": "Investigación científica",
  "ubicacion": "Sintético"
}


    # Se pueden agregar más elementos aquí...
]

# Configurar la página de Streamlit
st.set_page_config(page_title="Tabla Periódica Interactiva")
st.title("Tabla Periódica Interactiva")

# Crear la interfaz para mostrar los elementos
seleccion = st.selectbox("Selecciona un elemento", [f"{el['nombre']} ({el['simbolo']})" for el in elementos])

# Mostrar información del elemento seleccionado
for el in elementos:
    if seleccion == f"{el['nombre']} ({el['simbolo']})":
        st.subheader(f"{el['nombre']} ({el['simbolo']})")
        st.write(f"**Número Atómico:** {el['numero']}")
        st.write(f"**Ubicación:** {el['ubicacion']}")
        st.write(f"**Uso:** {el['uso']}")

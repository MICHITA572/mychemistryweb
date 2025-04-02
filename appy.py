import streamlit as st

# Definir los elementos químicos con sus propiedades
elementos = [
    {"numero": 1, "simbolo": "H", "nombre": "Hidrógeno", "uso": "Combustible y producción de amoníaco", "ubicacion": "En el agua y compuestos orgánicos"},
    {"numero": 2, "simbolo": "He", "nombre": "Helio", "uso": "Globos y refrigerante", "ubicacion": "Atmósfera y gas natural"},
    {"numero": 3, "simbolo": "Li", "nombre": "Litio", "uso": "Baterías y medicina", "ubicacion": "Minerales como espodumena"},
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

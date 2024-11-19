# Definimos hechos básicos de la base de conocimiento (relaciones familiares)
familia = {
    'juan': {'padre': 'pedro', 'madre': 'ana'},
    'maria': {'padre': 'pedro', 'madre': 'ana'},
    'pedro': {'padre': 'carlos', 'madre': 'marta'},
    'ana': {'padre': 'jose', 'madre': 'elena'},
    'carlos': {'padre': 'jose', 'madre': 'elena'},
    'marta': {'padre': 'juan', 'madre': 'lina'}
}

# Definimos reglas (reglas lógicas)
def es_padre(de, hijo):
    return familia.get(hijo, {}).get('padre') == de

def es_madre(de, hijo):
    return familia.get(hijo, {}).get('madre') == de

def es_hermano(o1, o2):
    """Verifica si dos personas son hermanos."""
    return (familia.get(o1, {}).get('padre') == familia.get(o2, {}).get('padre') and
            familia.get(o1, {}).get('madre') == familia.get(o2, {}).get('madre') and
            o1 != o2)

# Backtracking: Intentar encontrar relaciones a partir de una consulta
def consulta(relacion, *personas):
    if relacion == 'es_padre':
        for persona in familia:
            for hijo in familia:
                if es_padre(persona, hijo):
                    if persona in personas and hijo in personas:
                        return True
    elif relacion == 'es_madre':
        for persona in familia:
            for hijo in familia:
                if es_madre(persona, hijo):
                    if persona in personas and hijo in personas:
                        return True
    elif relacion == 'es_hermano':
        for o1 in familia:
            for o2 in familia:
                if es_hermano(o1, o2):
                    if o1 in personas and o2 in personas:
                        return True
    return False

# Función de prueba
def test_backtracking():
    # Probar las consultas
    print(consulta('es_padre', 'pedro', 'juan'))  # True: Pedro es padre de Juan
    print(consulta('es_madre', 'ana', 'juan'))  # True: Ana es madre de Juan
    print(consulta('es_hermano', 'juan', 'maria'))  # True: Juan y Maria son hermanos

if __name__ == "__main__":
    test_backtracking()
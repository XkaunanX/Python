# test_entorno.py

def test_funciones_basicas():
    try:
        # Comprobación de suma básica
        assert 2 + 2 == 4, "Error en la suma de 2 + 2"
        
        # Comprobación de tipo de datos
        assert isinstance(5, int), "Error: 5 no es un entero"
        
        # Comprobación de comparación de cadenas
        assert "Hola".lower() == "hola", "Error: 'Hola'.lower() debería ser igual a 'hola'"
        
        # Comprobación de operación booleana
        assert (True and False) == False, "Error en operación booleana"
        
        # Comprobación de estructura de datos
        mi_lista = [1, 2, 3]
        assert 2 in mi_lista, "Error: El número 2 no está en la lista"

        # Si todas las comprobaciones pasaron, informamos que todo está bien.
        print("¡Todo está funcionando correctamente!")
        
    except AssertionError as e:
        print(f"¡Test fallido! - {e}")

if __name__ == "__main__":
    test_funciones_basicas()
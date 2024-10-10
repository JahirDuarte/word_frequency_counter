from faker import Faker

# Crear una instancia de Faker
fake = Faker()

# Método para generar una lista de palabras aleatorias
def generate_random_words(count=10):
    return [fake.word() for _ in range(count)]

# Método para generar un párrafo con palabras aleatorias
def generate_random_text():
    return fake.text()

# Ejemplo de uso
if __name__ == "__main__":
    # Generar 10 palabras aleatorias
    words = generate_random_words(10)
    print("Random Words:", words)

    # Generar un párrafo de texto aleatorio
    text = generate_random_text()
    print("Random Text:", text)
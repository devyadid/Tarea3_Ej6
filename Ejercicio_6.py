# persona_estudiante.py

from datetime import datetime

class Persona:
    """Clase base que representa una persona."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """Devuelve los datos básicos de la persona."""
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Estudiante(Persona):
    """Subclase que representa a un estudiante."""
    def __init__(self, nombre, edad, universidad):
        # Llama al constructor de Persona
        super().__init__(nombre, edad)
        self.universidad = universidad

    def __str__(self):
        """Devuelve los datos del estudiante incluyendo la universidad."""
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Universidad: {self.universidad}"

if __name__ == "__main__":
    # Fecha y hora de ejecución para la captura
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Ejecución realizada el: {ahora}\n")

    # Crear instancias y mostrar información
    persona = Persona("Carlos", 40)
    estudiante = Estudiante("Ana", 22, "Universidad Nacional")

    print("Persona:")
    print(persona)
    print("\nEstudiante:")
    print(estudiante)

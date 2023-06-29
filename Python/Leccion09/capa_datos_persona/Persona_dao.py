




if __name__ == '__main__':

    # Actualizar un registro
    persona1 = Persona(1, 'Juan', 'Pena', 'jjpena@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')


    # Insertar un registro
    persona1 = Persona(nombre='Mateo', apellido='Torres', email='tmateo@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    # Eliminar un registro
    persona1 = Persona(id_persona=8)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

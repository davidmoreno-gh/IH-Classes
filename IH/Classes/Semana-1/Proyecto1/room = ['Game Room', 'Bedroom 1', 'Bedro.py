room = ['Game Room', 'Bedroom 1', 'Bedroom 2', 'Living Room']

def hab_list():
    print("Lista de habitaciones: ")
    print("Game Room")
    print("Bedroom 1")
    print("Bedroom 2")
    print("Living Room")

gameroom_items = ['Sofa', 'Piano']

bedroom1_items = ['Queen bed']

bedroom2_items = ['Double bed', 'Dresser']

livingroom_items = ['Dining table', 'Silla norte', 'Silla sur', 'Silla este', 'Silla oeste']


def moverse(actual_room):
    hab_list()
    hab = input("¿A que habitación quiere ir?")
    while hab not in room:
        hab = input("Elija una habitación existente")
    if hab == 'Game Room':
        actual_room = room[0]
    return actual_room

    elif hab == 'Bedroom 1':
        actual_room = room[1]
         return actual_room

    elif hab == 'Bedroom 2':
        actual_room = room[2]
        return actual_room

    elif hab == 'Living Room':
        actual_room = room[3]
        return actual_room

# asfasdfassdfasdf













def examinar(actual_room):
    if actual_room == 'Game Room':
        print(gameroom_items)
        exam_input = input("¿Que quieres examinar?")
        while exam_input not in gameroom_items:
            exam_input = input("Elija uno de los objetos disponibles.")
        if exam_input == 'Sofa':
            print("Tras examinar detenidamente el sofá encuentras... que no tiene nada de especial.")
    elif actual_room == 'Bedroom 1':
        print(bedroom1_items)
    elif actual_room == 'Bedroom 2':
        print(bedroom2_items)
    elif actual_room == 'Living Room':
        print(livingroom_items)


def juego():
    key_inv = ()
    actual_room = room[0]
    ganaste = False
    print("Empieza el juego.")
    accion='d'      # luego borra esto y el sal de abajo
    while not ganaste and accion!='sal':
        print(f"Estás en la {actual_room}")
        accion = input("¿Qué quieres hacer? (moverse/examinar): ").lower()
        if accion == "moverse":
            print("Moviendose...")
            actual_room = moverse(actual_room)
        elif accion == "examinar":
            print("Al examinar encuentras:")
            key_inv = examinar(actual_room)
        else:
            print("Acción no válida. Intenta nuevamente.")
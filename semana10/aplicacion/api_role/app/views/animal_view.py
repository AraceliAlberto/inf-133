def render_animal_list(animals):
    return [
        {
            "id": animal.id,
            "name": animal.name,
            "species": animal.species,
        }
        for animal in animals
    ]

def render_animal_detail(animal):
    return {
        "id": animal.id,
        "name": animal.name,
        "species": animal.species,
    }
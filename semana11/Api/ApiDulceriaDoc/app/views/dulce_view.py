def render_dulce_list(dulces):
    # Representa una lista de dulcees como una lista de diccionarios
    return [
        {
            "id": dulce.id,
            "marca": dulce.marca,
            "peso": dulce.peso,
            "sabor": dulce.sabor,
            "origen": dulce.origen,
        }
        for dulce in dulces
    ]


def render_dulce_detail(dulce):
    # Representa los detalles de un dulce como un diccionario
    return {
        "id": dulce.id,
        "marca": dulce.marca,
        "peso": dulce.peso,
        "sabor": dulce.sabor,
        "origen": dulce.origen,
    }
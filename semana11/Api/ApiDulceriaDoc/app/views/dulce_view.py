def render_dulce_list(dulces):
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
    return {
        "id": dulce.id,
        "marca": dulce.marca,
        "peso": dulce.peso,
        "sabor": dulce.sabor,
        "origen": dulce.origen,
    }
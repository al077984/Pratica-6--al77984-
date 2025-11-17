def obtener_seccion(seccion):
    """Devuelve inercia equivalente, módulos de elasticidad y distancias a fibras."""
    secciones = {
        "acero-hormigon": {"I_eq": 0.002, "Es": 200000, "Ec": 25000, "y_sup": 0.3, "y_inf": 0.3},
        "hormigon_simple": {"I_eq": 0.0015, "Es": 0, "Ec": 25000, "y_sup": 0.25, "y_inf": 0.25},
        "acero": {"I_eq": 0.001, "Es": 200000, "Ec": 0, "y_sup": 0.2, "y_inf": 0.2}
    }
    if seccion not in secciones:
        raise ValueError("Sección no definida. Elija: acero-hormigon, hormigon_simple, acero")
    return secciones[seccion]
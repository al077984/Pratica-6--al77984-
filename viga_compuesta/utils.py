def validar_positivo(valor, nombre):
    """Verifica que un valor numérico sea positivo."""
    if valor <= 0:
        raise ValueError(f"{nombre} debe ser un número positivo.")
    return valor
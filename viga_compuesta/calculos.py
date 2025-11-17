def calcular_momento_max(q, L):
    """Momento máximo para viga simplemente apoyada."""
    return (q * L**2) / 8  # kN·m

def esfuerzo_maximo(M_max, I_eq, y):
    """Esfuerzo máximo en fibra (aproximado, revisar unidades)."""
    return M_max * y / I_eq  
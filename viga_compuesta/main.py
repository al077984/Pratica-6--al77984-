from secciones import obtener_seccion
from calculos import calcular_momento_max, esfuerzo_maximo
from utils import validar_positivo

def main():
    print("=== Análisis simplificado de viga compuesta ===")
    try:
        L = validar_positivo(float(input("Ingrese la longitud de la viga L (m): ")), "Longitud L")
        q = validar_positivo(float(input("Ingrese la carga distribuida q (kN/m): ")), "Carga q")
        seccion = input("Ingrese tipo de sección (acero-hormigon / hormigon_simple / acero): ").strip().lower()

        datos = obtener_seccion(seccion)
        M_max = calcular_momento_max(q, L)
        sigma_sup = esfuerzo_maximo(M_max, datos["I_eq"], datos["y_sup"])
        sigma_inf = esfuerzo_maximo(M_max, datos["I_eq"], datos["y_inf"])

        print(f"\nMomento máximo M_max: {M_max:.2f} kN·m")
        print(f"Esfuerzo máximo en fibra superior: {sigma_sup:.2f} MPa")
        print(f"Esfuerzo máximo en fibra inferior: {sigma_inf:.2f} MPa")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
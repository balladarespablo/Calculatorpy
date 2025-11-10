import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números.")
    
    arr = np.array(lista).reshape(3, 3)
    
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),
            arr.mean(axis=1).tolist(), 
            arr.mean().tolist()
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().tolist()
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().tolist()
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().tolist()
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().tolist()
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().tolist()
        ]
    }
    
    return calculations

if __name__ == "__main__":
    # Pedir números al usuario
    print("Ingresa 9 números separados por comas:")
    entrada = input("Ejemplo: 1,3,5,6,7,9,2,4,8 → ")
    
    # Convertir a lista de números
    numeros = [float(num) for num in entrada.split(',')]
    
    # Calcular y mostrar resultado
    resultado = calculate(numeros)
    print("\nResultado:", resultado)
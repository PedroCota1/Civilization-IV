# script.py

def greet(name):
    """Função para exibir uma mensagem de saudação."""
    print(f"Olá, {name}!")

def sum_numbers(a, b):
    """Função para somar dois números."""
    return a + b

def subtract_numbers(a, b):
    """Função para subtrair dois números."""
    return a - b

def multiply_numbers(a, b):
    """Função para multiplicar dois números."""
    return a * b

def divide_numbers(a, b):
    """Função para dividir dois números."""
    if b == 0:
        print("Erro: divisão por zero.")
        return None
    return a / b

# Testando as funções
if __name__ == "__main__":
    print("Testando funções:")
    greet("Mundo")
    print("5 + 3 =", sum_numbers(5, 3))
    print("5 - 3 =", subtract_numbers(5, 3))
    print("5 * 3 =", multiply_numbers(5, 3))
    print("5 / 3 =", divide_numbers(5, 3))

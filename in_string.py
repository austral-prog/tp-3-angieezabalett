def check_vowels():
    # Código a implementar utilizando input.
nombre = input("Ingrese un nombre:")
letraa = f"contiene a: {("a" in nombre)}"
letrae = f"contiene e: {("e" in nombre)}"
letrai = f"contiene i: {("i" in nombre)}"
letrao = f"contiene o: {("o" in nombre)}"
letrau = f"contiene u: {("u" in nombre)}"
print (f"{(letraa)}\n{(letrae)}\n{(letrai)}\n{(letrao)}\n{(letrau)}")
python tp3_in_string_test.py
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

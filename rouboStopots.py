import pandas as pd

def obter_info_letra_pandas(arquivo_csv, letra):
    try:
        # Procura a linha com base na letra na primeira coluna
        linha_desejada = arquivo_csv[arquivo_csv.iloc[:, 0] == letra.upper()]

        if not linha_desejada.empty:
            return linha_desejada.iloc[0]
        else:
            return f"Nenhuma linha encontrada com a letra {letra}."

    except FileNotFoundError:
        return "Arquivo CSV não encontrado."
    except Exception as e:
        return f"Erro: {e}"

# Exemplo de uso
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRYcZwdsv29H7gU4IdxWS32HZ8L6XkTjzVD-Mt8bI9aAbunIWUOEzwKoN_TIy7vA5kijgyHjM7nmVqP/pub?output=csv'
arquivo_csv = pd.read_csv(url)
letra = input("Digite a letra para encontrar a linha desejada: ")

info_linha = obter_info_letra_pandas(arquivo_csv, letra)

if isinstance(info_linha, pd.Series):
    print("Informações da linha desejada:")
    print(info_linha)
else:
    print(info_linha)

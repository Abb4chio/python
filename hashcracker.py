#!/usr/bin/env python3

import crypt
import sys

# Verifica se o número de argumentos está correto
if len(sys.argv) != 4:
    print("Modo de uso:", sys.argv[0], "salt (até o 3 $) hash-inteiro wordlist")
    sys.exit(1)

# Atribuição dos argumentos
salt = sys.argv[1]
target_hash = sys.argv[2]
wordlist = sys.argv[3]

# Tenta abrir o arquivo de wordlist e calcular os hashes
try:
    with open(wordlist, 'r', encoding='utf-8') as f:
        for senha in f:
            senha = senha.strip()  # Remove espaços em branco
            # Gera o hash da senha usando o salt
            r = crypt.crypt(senha, salt)
            # Verifica se o hash gerado corresponde ao hash-alvo
            if r == target_hash:
                print("Senha encontrada:", senha)
                break  # Interrompe o loop ao encontrar a senha
        else:
            print("Senha não encontrada.")
except FileNotFoundError:
    print(f"Erro: Não foi possível encontrar o arquivo {wordlist}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

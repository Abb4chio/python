#!/usr/bin/env python3

import crypt
import sys

if len(sys.argv) != 4:
    print("Modo de uso:", sys.argv[0], "salt (até o 3 $) hash-inteiro wordlist")
    sys.exit(1)

salt = sys.argv[1]
target_hash = sys.argv[2]
wordlist = sys.argv[3]

try:
    with open(wordlist, 'r', encoding='utf-8') as f:
        for senha in f:
            senha = senha.strip()  
            r = crypt.crypt(senha, salt)
            if r == target_hash:
                print("Senha encontrada:", senha)
                break
        else:
            print("Senha não encontrada.")
except FileNotFoundError:
    print(f"Erro: Não foi possível encontrar o arquivo {wordlist}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

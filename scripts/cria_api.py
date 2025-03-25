#!/usr/bin/env python3
import os
import sys


def create_files(param):
    print(f'Criando e abrindo arquivos para {param}...')
    # Lista de comandos
    commands = [
        f'touch core/models/{param}.py core/serializers/{param}.py core/views/{param}.py',
        f'code core/models/{param}.py core/models/__init__.py core/serializers/{param}.py '
        f'core/serializers/__init__.py core/views/{param}.py core/views/__init__.py core/admin.py app/urls.py',
    ]

    # Executa cada comando
    for cmd in commands:
        os.system(cmd)


if __name__ == '__main__':
    ARG_COUNT = 2
    if len(sys.argv) != ARG_COUNT:
        print(f'Uso: python {sys.argv[0]} <parametro>')
        sys.exit(1)

    parametro = sys.argv[1]
    create_files(parametro)

import sys


def obter_input_num(prompt: str = None, minino: int = None, maximo: int = None) -> int:
    while True:
        try:
            entrada = int(input(f'\n{prompt}: '))
            if (minino is not None and entrada < minino) or (maximo is not None and entrada > maximo):
                print(
                    f"Por favor digite entre número {minino} e {maximo}"
                )
                continue
            return entrada
        except ValueError:
            print("Entrada inválida! Digite apenas números")
        except KeyboardInterrupt:
            sys.exit(0)


def obter_input_text(prompt: str) -> str:
    while True:
        try:
            entrada = input(f"{prompt}: ")
            if entrada:
                return entrada
            print("Entrada inválida! Não pode estar vazia")
        except KeyboardInterrupt:
            sys.exit(0)

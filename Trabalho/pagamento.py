# pagamento.py

class Pagamento:
    JUROS_MENSAL = 0.02

    def __init__(self):
        pass

    def pix(self, amount: float) -> bool:
        print("=== Pagamento via PIX ===")
        print(f"Valor a pagar: R${amount:.2f}")
        print(f"Pagamento de R${amount:.2f} realizado com sucesso via PIX!")
        return True

    def cartao(self, amount: float) -> bool:
        print("=== Pagamento via Cartão ===")
        tipo = int(input("Débito [1] ou Crédito? [2] "))
        if tipo == 1:
            print(
                f"Pagamento de R${amount:.2f} realizado com sucesso no débito!")
            return True

        elif tipo == 2:
            try:
                parcelas = int(input("Número de parcelas (1-10): "))
            except ValueError:
                print("Entrada inválida! Operação cancelada.")
                return False

            if parcelas < 1 or parcelas > 10:
                print("Número de parcelas inválido! Deve ser entre 1 e 10.")
                return False

            total_com_juros = amount * (1 + self.JUROS_MENSAL * parcelas)
            valor_parcela = total_com_juros / parcelas

            print(f"Total com juros ({parcelas}×): R${total_com_juros:.2f}")
            print(f"Parcelas de R${valor_parcela:.2f} cada.")
            print("Pagamento em crédito agendado com sucesso!")
            return True

        else:
            print("Tipo de pagamento inválido! Use 'debito' ou 'credito'.")
            return False

    def boleto(self, amount: float) -> bool:
        print("=== Pagamento via Boleto ===")
        print(f"Valor do boleto: R${amount:.2f}")
        print("Boleto gerado com sucesso! Pagamento será compensado em até 3 dias úteis.")
        return True


class Venda():

    quantidade_produto = 5

    def set_preco_produto(self, preco_produto):
        self.preco_produto = preco_produto

    def get_preco_produto(self):
        return self.preco_produto

    def get_quantidade_produto(self, quantidade):
        self.quantidade_produto = self.quantidade_produto - quantidade
        return self.quantidade_produto

    def set_valor_pago(self, valor_pago):
        self.valor_pago = valor_pago

    def get_valor_pago(self):
        return self.valor_pago

    def set_valor_desconto(self,valor_desconto):
        self.valor_desconto = valor_desconto

    def valor_com_desconto(self):
        return float(self.preco_produto)-float(self.valor_desconto)

    def total(self, preco_produto, quantidade):
        return float(self.preco_produto)*int(quantidade)

    def troco(self, total):
        return float(self.valor_pago)-float(total)









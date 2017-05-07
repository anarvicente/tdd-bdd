from behave import *

from Venda import *

@given(u'que o produto custa {preco_produto} e o cliente compra {quantidade_produto:d}')
def step_impl(context,preco_produto, quantidade_produto):
    context.venda = Venda()
    context.venda.set_preco_produto(preco_produto)
    context.produto = quantidade_produto

@when(u'pagar com {valor_pago}')
def step_impl(context, valor_pago):
    context.venda.set_valor_pago(valor_pago)

@then(u'o total da venda sera {total:f}')
def step_impl(context, total):
    context.venda.total = context.venda.total(context.venda.get_preco_produto(), context.produto)
    assert(total == context.venda.total)

@then(u'o troco sera {valor_retornado:f}')
def step_impl(context, valor_retornado):
    troco = context.venda.troco(context.venda.total)
    assert(valor_retornado == troco )

@then(u'a quantidade {nova_quantidade:d}')
def step_impl(context, nova_quantidade):
    quantidade = context.venda.get_quantidade_produto(context.produto)
    assert(nova_quantidade == quantidade)


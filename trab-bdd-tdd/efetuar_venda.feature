Feature: Efetuar venda
  
     Eu, como vendedor, desejo um sistema que calcule o preco total da venda e 
     o troco do cliente para maior agilidade na venda.
     

     
    Scenario Outline: Venda sem desconto
      Given que o produto custa <preco_produto> e o cliente compra <quantidade_produto>
      When pagar com <valor_pago>
      Then o total da venda sera <total>
      And o troco sera <valor_retornado>
      And a quantidade <nova_quantidade>

    Scenario Outline: Venda com desconto
      But o produto tem um desconto de <valor_desconto>
      Then o valor do produto serah <valor_com_desconto>
      And o troco serah de <valor_retornado_com_desconto>
      And a quantidade <nova_quantidade>

      Examples: Values
      |preco_produto|quantidade_produto|valor_pago|valor_retornado|nova_quantidade| total|
      | 100.0|1|200.0|100.0|4| 100.0                                                    |
      | 200.0|2|400.0|0.0|3|400.0|
      
    

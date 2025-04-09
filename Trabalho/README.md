# Sistema de Loja com POO

Este projeto é um sistema de controle para uma loja virtual desenvolvido em Python utilizando os conceitos de Programação Orientada a Objetos (POO).

## Visão Geral

O sistema permite que o cliente:

1. Visualize os produtos disponíveis na loja.
2. Adicione produtos ao carrinho de compras (com verificação de estoque e quantidade permitida).
3. Aplique descontos em produtos específicos.
4. Visualize os itens do carrinho.
5. Finalize a compra com um pagamento simulado, informando se o valor pago foi suficiente e devolvendo o troco.
6. Controle o estoque dos produtos.
7. Navegue por um menu interativo no terminal.

## Requisitos do Projeto

O sistema foi dividido em múltiplas classes, cada uma responsável por uma parte do funcionamento do sistema:

- **Produto:**  
  Gerencia os atributos do produto, como nome, preço e quantidade em estoque. Possui também o método para aplicar desconto.

- **Carrinho:**  
  Responsável por armazenar os produtos adicionados, calcular o total da compra e esvaziar o carrinho após o pagamento.

- **Loja:**  
  Gerencia os produtos, a exibição dos mesmos e o processo de pagamento, integrando as funcionalidades de Produto e Carrinho.

Um arquivo `main.py` contém o menu interativo que permite ao usuário navegar pelas opções e interagir com o sistema.

## Estrutura do Projeto

A estrutura de diretórios e arquivos do projeto é a seguinte:

```
Trabalho/
├── main.py         # Arquivo principal com o menu interativo
├── produto.py      # Define a classe Produto
├── pagamento.py    # Define a classe pagamento
├── carrinho.py     # Define a classe Carrinho
└── loja.py         # Define a classe Loja, que integra Produto e Carrinho
```

## Funcionalidades

- **Exibição de Produtos:**  
  Lista todos os produtos disponíveis com nome, preço e estoque.

- **Adição de Produtos ao Carrinho:**  
  Permite adicionar produtos ao carrinho com verificação da quantidade (permitida de 1 a 99) e do estoque disponível.

- **Aplicação de Descontos:**  
  Permite aplicar um desconto percentual ao preço de um produto.

- **Cálculo do Total da Compra:**  
  Calcula o total dos produtos adicionados ao carrinho.

- **Simulação de Pagamento:**  
  Recebe o valor pago pelo usuário, informa se o pagamento foi suficiente e, em caso afirmativo, calcula o troco e esvazia o carrinho.

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/hugo-loiola12/NovasTecnologias.git
   cd NovasTecnologias
   cd Trabalho
   ```

2. **Execute o programa:**

   Certifique-se de ter o Python instalado (recomendado Python 3.x).

   ```bash
   python main.py
   # ou
   python3 main.py
   ```

   Isso iniciará o menu interativo no terminal.

## Exemplo de Uso

Ao executar o programa, o menu exibirá opções para visualizar produtos, adicionar produtos ao carrinho, aplicar descontos, visualizar o carrinho, finalizar a compra ou sair do sistema.

---

Este projeto é licenciado sob a [MIT License](LICENSE).

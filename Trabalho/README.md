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
   ```

   Isso iniciará o menu interativo no terminal.

## Exemplo de Uso

Ao executar o programa, o menu exibirá opções para visualizar produtos, adicionar produtos ao carrinho, aplicar descontos, visualizar o carrinho, finalizar a compra ou sair do sistema.

## Projeto Base

O projeto foi desenvolvido conforme o seguinte enunciado:

> **Projeto: Sistema de Loja com POO**  
> **Enunciado:**  
> Você foi contratado para desenvolver o sistema de controle de uma loja virtual usando Programação Orientada a Objetos (POO) em Python.  
> O sistema deverá permitir que o cliente:
>
> - Visualize os produtos disponíveis na loja;
> - Adicione produtos ao carrinho de compras;
> - Aplique descontos em produtos específicos;
> - Visualize os itens do carrinho;
> - Finalize a compra com um pagamento simulado;
> - Controle o estoque dos produtos;
> - Navegue por um menu interativo no terminal.
>
> **Requisitos obrigatórios:**
>
> - O sistema deve ser dividido em múltiplas classes, representando:
>   - **Produto:** com nome, preço, e quantidade em estoque.
>   - **Carrinho:** responsável por armazenar os produtos adicionados, calcular o total e esvaziar o carrinho após o pagamento.
>   - **Loja:** responsável por gerenciar os produtos, a exibição e o processo de pagamento.
> - Um arquivo `main.py` com o menu interativo que permita o usuário navegar pelas opções.
>
> **Funcionalidades esperadas:**
>
> - Exibir produtos com nome, preço e estoque.
> - Adicionar produtos ao carrinho com verificação de estoque.
> - Aplicar desconto em percentual ao preço de um produto.
> - Calcular o total da compra com base nos produtos no carrinho.
> - Simular o pagamento: o usuário digita o valor pago e o sistema informa se o pagamento foi suficiente, devolvendo o troco.
> - Após o pagamento, o carrinho deve ser esvaziado.

Esse README foi elaborado com base nos requisitos originais do projeto, garantindo uma implementação clara e organizada.

---

Este projeto é licenciado sob a [MIT License](LICENSE).

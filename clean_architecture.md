# Clean Architecture

https://www.youtube.com/watch?v=2nvbgwFE_0Y&list=PLAgbpJQADBGK0opZ8ZuDX3zDjQck_QKMy&index=1

![Visao Geral](./assets_md/visao_geral%20.jpg)

**Clean Architecture** é uma arquitetura de software proposta por Robert Cecil Martin (ou Uncle Bob, como é mais conhecido) que tem por objetivo padronizar e organizar o código desenvolvido, favorecer a sua reusabilidade, assim como independência de tecnologia.

Por mais que a Clean Architecture foi criada em meados de 2012, está repleta de princípios atemporais que podem ser aplicados independente da tecnologia utilizada e linguagem de programação.

Exemplo: Mudar do Django para o FastAPI com facilidade, ou trocar o ORM.

Isto é conseguido não permitindo que o dado puro gerado por uma camada externa, seja recebido AS IS para uma camada interna, exemplo: o BODY HTML de uma requisição capturado pelo framework como FastAPI ser passado para a camada de Casos de Uso. Não queremos que nada de um círculo externo interfire no círculo interno.

## Princípios

Clean Architeture é sobre princípios, o próprio livro do Uncle Bob não foca em mostrar códigos de qualquer linguagem (tem apenas "piceladas").


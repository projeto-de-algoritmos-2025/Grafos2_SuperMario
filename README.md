# Super Mario

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/1029249  |  Júlia Takaki Neves |
| 22/2006392  |  Renan Batista Gonçalves Pariz |

## Sobre 
# Projeto: Simulação de Mapa do Super Mario com Algoritmos de Grafos

Para explorar os conceitos abordados na disciplina de **Grafos 2**, a dupla escolheu desenvolver uma aplicação prática inspirada no universo do **Super Mario Bros**, onde as fases do jogo são representadas como **nós em um grafo**, e os caminhos entre elas como **arestas com pesos variados**.

O projeto foi dividido de forma equilibrada entre os integrantes, com cada um responsável por implementar e testar partes específicas da lógica de grafos, como os algoritmos de **Prim**, **Kruskal** e **Dijkstra**.

---

## Aplicações do Algoritmo de Dijkstra

O algoritmo de **Dijkstra** é ideal para encontrar o caminho mais curto entre dois pontos, considerando pesos (como tempo, dificuldade ou inimigos).

### Exemplo prático: Caminho mais fácil até o castelo
- **Objetivo:** Ajudar Mario a encontrar o caminho mais seguro ou mais rápido do mundo 1-1 até o castelo final.
- **Como funciona:** A partir de uma fase inicial, o algoritmo percorre o grafo priorizando caminhos de menor peso até alcançar o destino, simulando uma jornada otimizada por fases.

#### Função: `Dijkstra(mapa, origem, destino)`
- Retorna o caminho de menor custo entre duas fases.
- Pode considerar o número de inimigos, distância ou dificuldade.

---

## Aplicações do Algoritmo de Prim

O algoritmo de **Prim** constrói uma **árvore geradora mínima**, conectando todos os vértices com o menor custo total.

### Exemplo prático: Construção do mapa do mundo
- **Objetivo:** Criar um mapa onde todas as fases estão conectadas de maneira eficiente, como se os desenvolvedores estivessem planejando a estrutura do jogo com economia de recursos.

#### Função: `Prim(mapa)`
- Conecta todas as fases com o menor custo possível.
- Garante que Mario possa visitar qualquer fase sem ciclos redundantes.

---

## Aplicações do Algoritmo de Kruskal

Assim como Prim, o algoritmo de **Kruskal** também gera uma árvore mínima, porém parte das arestas mais leves primeiro, sendo ideal para trabalhar com mapas esparsos.

### Exemplo prático: Otimização das rotas entre mundos
- **Objetivo:** Selecionar os melhores caminhos possíveis entre todas as fases sem formar ciclos, priorizando conexões mais vantajosas.

#### Função: `Kruskal(mapa)`
- Garante que o mapa tenha a menor soma de custos nas rotas.
- Pode ser usado para reestruturar o mapa do jogo de forma estratégica.

---

## Conclusão

Com esse projeto, os conceitos de grafos estudados em sala foram aplicados em um cenário lúdico e interativo, permitindo visualizar com clareza como esses algoritmos funcionam em contextos práticos de planejamento, navegação e otimização.



### Vídeo da Apresentação:
Aqui está disponível o [vídeo]() da apresentação do projeto.

## Screenshots
Funcionamento do Dijkstra:
<center>
  <img src="assets/" alt="">
  <img src="assets/" alt="">
</center>

Funcionamento do Prim:
<center>
  <img src="assets/.png" alt="">

</center>

## Instalação 
**Linguagem**: Python (qualquer versão a partir da versão partir da 3.6.)<br>

## Uso 
Após garantir a instalação do Python, para rodar o código de Dijkstra basta estar na pasta do projeto e digitar `python Dijkstra.py` no terminal. <br>
De maneira análoga, para rodar o código de Prim basta estar na página do projeto e digitar `python Prim.py`.
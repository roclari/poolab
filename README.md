# Laboratório de Programação Orientada a Objetos
👨🏻‍💻 Repositório para descrição teórica e prática dos conceitos de "Polimorfismo", "Herança" e "Encapsulamento". Segunda avaliação para a disciplina de Laboratório de Programação Orientada a Objetos. 

<h2 align="center">UNIVERSIDADE DE VASSOURAS - Campus Maricá</h2>
<h3 align="center">Engenharia de Software | 2023.1</h3>
<h3 align="center">Larissa Rocha</h3>


<h2 align="center">HERANÇA, POLIMORFISMO & ENCAPSULAMENTO</h2>

<h3 align="center">O que é Herança?</h3>

<p align="justify">A herança em orientação a objetos permite criar uma nova classe (classe filha ou derivada) com base em uma classe existente (classe pai ou base), herdando assim os atributos e métodos da classe pai. Considerando o exemplo de um conjunto de animais diferentes: um cachorro, um gato e uma vaca, onde todos os três são derivados de uma classe base: a classe Animal. A partir dela se adquire seus atributos e métodos, como por exemplo “emitir som”. Isso permite que as subclasses Cachorro, Gato e Vaca compartilhem comportamentos da classe base.</p>

<h3 align="center">O que é Polimorfismo?</h3>

<p align="justify">O polimorfismo é um princípio importante da orientação a objetos que permite que objetos de diferentes classes sejam tratados de maneira uniforme, permitindo que um objeto seja referenciado de uma forma mais generalizada e comportando-se de maneiras diferentes com base no tipo real do objeto. Seguindo o exemplo anterior, pode-se criar uma função que interaja com as subclasses de animais para que elas realizem o som específico de cada uma, mas sem chamar a classe de cada uma delas, e sim de forma genérica. Sendo essa função “interagir com o animal”, torna-se capaz de interagir com diferentes animais (cachorro, gato, vaca) de forma polimórfica, chamando seus respectivos métodos como emitir som.</p>

<h3 align="center">O que é Encapsulamento?</h3>

<p align="justify">O encapsulamento é um princípio fundamental da orientação a objetos que permite ocultar os detalhes internos de uma classe, protegendo seus atributos e expondo apenas uma interface pública através de métodos. No caso do exemplo, pode-se adicionar o atributo nome da classe Animal como um detalhe privado, que só será acessado através de um método para obter o nome. Isto protege o atributo de acesso direto fora da classe, reforçando o encapsulamento.</p>

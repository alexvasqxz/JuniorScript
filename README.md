<h1>  $${\color{orange} Junior\color{gray} Script}$$</h1> 

Desarrollado por Gustavo Vasquez

<h2> Objetivo </h2> 

<p>Proveer un lenguaje de programación en español, amigable y divertido para facilitar el aprendizaje de programación 
y tecnologías en estudiantes del nivel básico (Primaria y Secundaria), quienes no han tenido algun acercamiento con 
la programación o bien, se les dificulta debido a barreras del idioma inglés o faltas de herramientas lo 
suficientemente amigables en cuanto a interfaz y usabilidad.</p>

<h2> Documentos </h2>

[Propuesta del Proyecto](https://docs.google.com/document/d/11z2FRLNSsaUyNhH4F56Ji7I2Z-IUF0dirjkuAZWErZw/edit?usp=share_link)

[Diagramas de Sintaxis](https://docs.google.com/document/d/1wHO3yVg2jM5AVRkd0oPpn_H7fm2oKyFxUV6hfe6DQbY/edit?usp=share_link)

[Avance 1 - Lexico y Sintaxis](https://docs.google.com/document/d/1hvA9DwypM8TK4CWNyRVYMjA5y9_A5_kaswBOoAzozGg/edit?usp=share_link)

[Avance 2 - Semantica](https://docs.google.com/document/d/1V1VJ3m8oHPbeFgsa1O4hcs0zZGeKQFAKQwYOEwGukjc/edit?usp=share_link)

[Historial de Cambios](https://docs.google.com/spreadsheets/d/1WmKcr7Q-DdMOmIYtfitnicqKML57uPOTN1yRzgrm4Jc/edit?usp=share_link)

<h2>  ${\color{orange} Avance  }$  ${\color{orange} 1  }$</h2>  

<p>En este avance 1, este documento se enfoca en presentar los diagramas de sintaxis del lenguaje de 
programación para mi proyecto final, llamado <i>JuniorScript.</i> Además de presentar los diagramas, 
se presentara su gramática normal, y de ser el caso, su factorización y/o eliminación de recursividad 
izquierda con propósito de mejorar el entendimiento de los diagramas y tener un código mas limpio a 
la hora de trasladarlo a Python Lex and Yacc.</p>

<h4> Overview Avance </h4>
<ul>
    <li>Se crean los tokens y expresiones regulares para todos los simbolos terminales del lenguaje</li>
    <li>Se crean todos los diagramas de sintaxis factorizados y sin recursion izquierda para todos los
    simbolos no terminales del lenguaje</li>
    <li>Se presentan pruebas unitarias para la parte del lexico del lenguaje</li>
    <li>Se presentan resultados como archivos de texto despues de haber ejecutado el lexico (lex) 
    "lexer_output.txt"</li>
</ul>

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/1.Example.png" width="800" />
<i> Imagen 1: </i>Ejemplo del proceso utilizado para definir la gramatica para cada diagrama, verificando que esten 
factorizados y no presenten recursividad del lado izquierdo.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/1.Lexer.png" width="800" />
<i> Imagen 2: </i>Archivo de texto a ser probado del lado izquierdo, y resultados despues de haber probado el lexico 
de JuniorScript del lado derecho.

<h2>  ${\color{orange} Avance  }$  ${\color{orange} 2  }$</h2>  

<p>En este avance 2, se muestran los diagramas de sintaxis a los que se les han agregado puntos neuronales como 
lógica para poder representar la creación del directorio de funciones, considerando las diferentes funciones 
que pueden crearse en el lenguaje de programación <i>JuniorScript</i> y sus variables, este avance presenta 
la posibilidad de guardar información sobre dichas funciones y variables para posteriormente utilizar esta 
información de alguna manera.</p>
<p>Es importante mencionar que en este lenguaje de programación, se permite la declaración de variables en 
cualquier lugar dentro de las funciones así como variables locales para el main(), llamado inicio.</p>

<h4> Overview Avance </h4>
<ul>
    <li>Se desarrollo la logica por medio de puntos neuronales para representar las acciones necesarias
    para guardar la información del programa, sus funciones, y las variables</li>
    <li>Se presenta el resulado del directorio de funciones en un archivo de texto "dir_func_output.txt"</li>
    <li>Se crean las direcciones virtuales globales y locales para variables, temporales y constantes</li>
    <li>Se crea un mapeado entre los tipos de variables y los tipos de operaciones y un valor entero</li>
    <li>Se crea el cubo semantico el cual dicta las reglas para realizar expresiones </li>
</ul>

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Puntos.png" width="800" />
<i> Imagen 3: </i>Puntos neuronales agregados para la creación del directorio de funciones.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Direcciones.png" width="800" />
<i> Imagen 4: </i>Direcciones Virtuales y sus limites.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Cubo.png" width="800" />
<i> Imagen 5: </i>Cubo Semántico.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Output.png" width="800" />
<i> Imagen 6: </i>Muestra del archivo resultado al momento de crear el directorio de funciones.
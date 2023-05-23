<h1>  $${\color{orange} Junior\color{gray} Script}$$</h1> 

Desarrollado por Gustavo Vasquez

<h2> Objetivo </h2> 

Proveer un lenguaje de programación en español, amigable y divertido para facilitar el aprendizaje de programación y tecnologías en estudiantes del nivel básico (Primaria y Secundaria), quienes no han tenido algun acercamiento con la programación o bien, se les dificulta debido a barreras del idioma inglés o faltas de herramientas lo suficientemente amigables en cuanto a interfaz y usabilidad.

<h2> Documentos </h2>

[Propuesta del Proyecto](https://docs.google.com/document/d/11z2FRLNSsaUyNhH4F56Ji7I2Z-IUF0dirjkuAZWErZw/edit?usp=share_link)

[Historial de Cambios](https://docs.google.com/spreadsheets/d/1WmKcr7Q-DdMOmIYtfitnicqKML57uPOTN1yRzgrm4Jc/edit?usp=share_link)

<h2>  ${\color{orange} Avance  }$  ${\color{orange} 1  }$</h2>  

En este avance 1, este documento se enfoca en presentar los diagramas de sintaxis del lenguaje de programación para mi proyecto final, llamado JuniorScript. Además de presentar los diagramas, se presentara su gramática normal, y de ser el caso, su factorización y/o eliminación de recursividad izquierda con propósito de mejorar el entendimiento de los diagramas y tener un código mas limpio a la hora de trasladarlo a Python Lex and Yacc.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/1.Example.png" width="600" />
<i> Imagen 1: </i>Ejemplo del proceso utilizado para definir la gramatica para cada diagrama, verificando que esten 
factorizados y no presenten recursividad del lado izquierdo.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/1.Lexer.png" width="600" />
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

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Puntos.png" width="500" />
<i> Imagen 3: </i>Puntos neuronales agregados para la creación del directorio de funciones.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Direcciones.png" width="500" />
<i> Imagen 4: </i>Direcciones Virtuales y sus limites.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Cubo.png" width="500" />
<i> Imagen 5: </i>Cubo Semántico.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/2.Output.png" width="500" />
<i> Imagen 6: </i>Muestra del archivo resultado al momento de crear el directorio de funciones.

<h2>  ${\color{orange} Avance  }$  ${\color{orange} 3  }$</h2>  

<p>En este avance 3, se muestran los diagramas de sintaxis a los que se les han agregado puntos neuronales como 
lógica para poder representar la creación de cuadruplos de expresiones aritmeticas y estatutos lineales sencillos, 
este avance presenta la posibilidad de guardar variables temporales sobre las funciones y generar una lista
de cuadruplos que muestran las direcciones de las constantes o variables siendo utilizadas en las
expresiones aritmeticas y estatutos, asi como la direccion virtual asignada para cada temporal</p>

<h4> Overview Avance </h4>
<ul>
    <li>Se desarrollo la logica por medio de puntos neuronales para representar las acciones necesarias
    para crear los cuadruplos de expresiones artimeticas y estatutos</li>
    <li>Se cubren expresiones aritmeticas logicas de tipo logico (YYY), comparacion (< >), sumas y restas (+ -),
    multiplicaciones y divisiones (* /)</li>
    <li>De igual forma se cubre asociatividad derecha y se distingue cuando se tiene una expresion dentro de otra
    por medio de parentesis e.j. 5 * (9 + 8)</li>
    <li>Se cubren estatutos como: imprimir, leer y asignar (=)</li>
    <li>En el caso de la asignacion y expresiones logicas, se valida que el tipo de los datos sea correcto haciendo
    uso del cubo semantico</li>
</ul>

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/3.PuntosI.png" width="500" />
<i> Imagen 7: </i>Puntos neuronales para expresiones aritmeticas.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/3.PuntosII.png" width="500" />
<i> Imagen 8: </i>Puntos neuronales para estatutos sencillos.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/3.OutputI.png" width="500" />
<i> Imagen 9: </i>Ejemplo impresion de cuadruplos antes del direccionamiento virtual.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/3.OutputII.png" width="500" />
<i> Imagen 9: </i>Ejemplo impresion de cuadruplos despues del direccionamiento virtual.

<h2>  ${\color{orange} Avance  }$  ${\color{orange} 4  }$</h2> 

<p>En este avance 4, se muestran los diagramas de sintaxis a los que se les han agregado puntos neuronales como 
lógica para poder representar la creación de cuadruplos de expresiones estatutos condicionales, como lo es el
if, while y for, conocidos como condicion, mientras, y para cada en el lenguaje <i>JuniorScript.</i> </p>
<p> De igual forma que en el avance 3, la creación de cuadruplos para estatutos condicionales funciona por
medio de direcciones virtuales, por lo que se vera el número de operación de los saltos, la dirección de la
respuesta que se esta evaluando y la línea de salto </p>
<p> Cabe mencionar que el ciclo for, en el lenguaje <i>JuniorScript.</i> conocido como desde y hasta,
es un ciclo controlado, por lo que toma una fotografía del limite superior para evitar modificaciones y un
posible ciclo infinito</p>

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/4.Puntos.png" width="500" />
<i> Imagen 10: </i>Puntos neuronales para estatutos condicionales.

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/4.for.png" width="500" />
<i> Imagen 11: </i>Ejemplo ciclo for, del lado izquierda los cuadruplos generador por JuniorScript

<h2>  ${\color{orange} Avance  }$  ${\color{orange} 5  }$</h2> 

<p> En este avance 5, se muestran los diagramas de sintaxis a los que se les han agregado puntos neuronales
como lógica para poder representar la declaración y llamada de estructuras homogenicas, como lo son
arreglos y matrices.</p>
<p> Se cubren casos como declaración de tamaños y dimensiones en la tabla de variables, direcciones
virtuales considerando el tamaño de las estructuras. A la hora de llamar el arreglo, se valida que los
indices sean enteros, que esten dentro de los limites inferiores y superiores y se realiza la lógica en
cuadruplos para poder acceder a la dirección virtual especifica de la casilla a la que se quiere acceder.</p>

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/5.Puntos.png" width="500" />
<i> Imagen 12: </i>Puntos neuronales para estructuras homogenicas. 

<img src="https://github.com/gussvas/JuniorScript/blob/main/Docs/images/5.Code.png" width="500" />
<i> Imagen 13: </i>Ejemplo de arreglo y matriz
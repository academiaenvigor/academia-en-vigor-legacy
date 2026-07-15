# CÓDIGO VIGOR

> Norma editorial interna de Academia En Vigor

| Metadato | Valor |
|---|---|
| **Nombre** | Código VIGOR |
| **Versión** | 0.1 |
| **Estado** | Borrador funcional |
| **Fecha** | 15 de julio de 2026 |
| **Responsable** | Academia En Vigor |
| **Ámbito de aplicación** | Todo el contenido, los datos, los recursos, los procesos editoriales y los sistemas de Academia En Vigor. Aplicación inicial: los 45 temas de Policía Nacional; extensión futura prevista: los 23 temas de Guardia Civil. |
| **Documentos relacionados** | `temario.json`; `temario-estructura-completa.md`; `docs/parte-y-atestado.md`; materiales de `temas/`; bancos de `data/tests/`; datos de exámenes oficiales de `data/`; sistema formado por `vigia_boe.py`, `vigia-estado.json` y `vigia-informe.md`; futuros Manual Editorial, Manual del Temario, Manual del Banco de Preguntas y Protocolo de El Vigía. |

## Preámbulo

El Código VIGOR fija los criterios que convierten información jurídica, pedagógica y operativa en material fiable para una oposición. Obliga por igual a profesores, preparadores, redactores, revisores, desarrolladores, colaboradores y sistemas de inteligencia artificial que intervengan en Academia En Vigor.

Este Código establece qué debe cumplirse. Los manuales posteriores definirán con mayor detalle cómo ejecutarlo. Si un procedimiento, plantilla o automatización contradice este Código, prevalece el Código VIGOR.

---

# CAPÍTULO 0. ESTADO DEL DOCUMENTO

## Artículo 1. Naturaleza y fuerza interna

1. El Código VIGOR es la norma editorial interna de mayor rango de Academia En Vigor.
2. Su cumplimiento es obligatorio en toda creación, revisión, actualización, publicación y retirada de contenido.
3. Ningún material podrá considerarse aprobado por el mero hecho de existir en el repositorio, haberse generado automáticamente o haberse publicado con anterioridad.

## Artículo 2. Alcance de la versión 0.1

1. La versión 0.1 es un **borrador funcional**: puede utilizarse desde su aprobación provisional para producir y revisar materiales.
2. Esta versión fija principios, responsabilidades, ciclos de vida, estados y criterios mínimos de aceptación.
3. Las cuestiones de formato, esquema de datos, nomenclatura técnica, validaciones automáticas, tiempos de respuesta y roles nominales se concretarán en los manuales correspondientes.

## Artículo 3. Aprobación y modificación

1. Toda modificación del Código deberá registrar versión, fecha, responsable, motivo y alcance.
2. Un cambio que rebaje el rigor, la trazabilidad o la utilidad pedagógica exigirá justificación expresa y revisión editorial.
3. Las versiones sustituidas se conservarán en el historial del repositorio.

---

# CAPÍTULO 1. OBJETO

## Artículo 4. Objeto del Código

El presente Código tiene por objeto:

1. unificar los criterios editoriales y técnicos de Academia En Vigor;
2. garantizar que cada contenido sea correcto, comprensible, examinable y trazable;
3. mantener sincronizados El Parte, El Atestado, los bancos de preguntas y los recursos derivados;
4. separar con claridad la detección de un cambio de su revisión, incorporación y publicación;
5. impedir la publicación de referencias oficiales no verificadas;
6. definir controles de calidad aplicables a trabajo humano y automatizado;
7. facilitar la actualización y la reutilización del conocimiento sin multiplicar inconsistencias.

---

# CAPÍTULO 2. MISIÓN

## Artículo 5. Misión

La misión de Academia En Vigor es proporcionar una preparación jurídicamente rigurosa, pedagógicamente clara y permanentemente mantenida que permita al alumno comprender, memorizar, aplicar y responder con precisión el programa oficial de la oposición.

La misión se cumple cuando el alumno puede estudiar con autonomía, detectar sus lagunas, entrenar todos los conceptos examinables y confiar en el estado real —no supuesto— de actualización del material.

---

# CAPÍTULO 3. VISIÓN

## Artículo 6. Visión

Academia En Vigor aspira a construir un sistema editorial vivo en el que:

1. el conocimiento se mantenga una sola vez y alimente materiales distintos sin contradicciones;
2. cualquier cambio normativo pueda rastrearse hasta todos los temas, preguntas y recursos afectados;
3. cada alumno reciba el nivel de profundidad adecuado para su momento de estudio;
4. la tecnología amplíe la capacidad del equipo sin sustituir el juicio jurídico, editorial y pedagógico;
5. la calidad pueda comprobarse mediante evidencias y no dependa de declaraciones comerciales.

---

# CAPÍTULO 4. VALORES

## Artículo 7. Valores institucionales

Academia En Vigor actuará conforme a los valores siguientes:

1. **Rigor.** Cada afirmación jurídica deberá corresponderse con una fuente válida y correctamente interpretada.
2. **Claridad.** La dificultad de una materia no justificará una explicación confusa.
3. **Utilidad.** Todo contenido deberá ayudar a comprender, recordar, practicar, actualizar o decidir.
4. **Honestidad.** Se distinguirá entre material oficial, interpretación, doctrina, ejemplo y contenido propio.
5. **Trazabilidad.** El origen, la revisión, la versión y el impacto de los cambios deberán poder reconstruirse.
6. **Coherencia.** Las distintas versiones y recursos expresarán el mismo conocimiento sin contradicciones.
7. **Responsabilidad.** Ninguna automatización convertirá una tarea pendiente en una falsa afirmación de trabajo terminado.
8. **Mejora continua.** Los errores, dudas y resultados de uso alimentarán revisiones concretas del sistema.

---

# CAPÍTULO 5. LOS 16 PRINCIPIOS VIGOR

## Artículo 8. Principio 1. El alumno como centro

Toda decisión editorial se evaluará por su efecto real sobre el aprendizaje del alumno. La comodidad del redactor, la estética o la facilidad técnica no prevalecerán sobre la comprensión, la precisión y la capacidad de responder en examen.

## Artículo 9. Principio 2. Comprender antes de memorizar

La memorización será más estable si parte de relaciones comprendidas. El material explicará primero la estructura y el sentido de los conceptos, y señalará después qué elementos exigen recuerdo literal, numérico o terminológico.

## Artículo 10. Principio 3. El temario que nunca duerme

El contenido se tratará como un sistema sujeto a vigilancia, revisión y mantenimiento continuos. La ausencia de alertas no equivale por sí sola a una garantía absoluta de vigencia.

## Artículo 11. Principio 4. Una única fuente de verdad

Cada concepto tendrá un núcleo maestro identificable del que derivarán El Parte, El Atestado, las preguntas y los recursos. No se mantendrán copias independientes como si fueran fuentes autónomas.

## Artículo 12. Principio 5. Ausencia de relleno

Cada párrafo, tabla, ejemplo o recurso deberá cumplir una función comprobable. Se eliminarán repeticiones que no refuercen deliberadamente el aprendizaje y explicaciones que aporten volumen sin aumentar dominio.

## Artículo 13. Principio 6. Explicar como un gran preparador

El material anticipará dónde se atasca el alumno, distinguirá conceptos próximos, ordenará la dificultad, propondrá una estrategia de estudio y hará visibles las trampas relevantes. No se limitará a copiar o parafrasear normas.

## Artículo 14. Principio 7. Rigor jurídico verificable

Las afirmaciones jurídicas deberán poder contrastarse con fuentes oficiales vigentes, identificadas con precisión suficiente. Cuando exista debate interpretativo, se indicará el criterio adoptado y su fundamento.

## Artículo 15. Principio 8. Pensar como el tribunal

La redacción identificará literalidad, excepciones, plazos, mayorías, competencias, órganos, términos intercambiables y términos que no lo son. Esta orientación nunca justificará inventar tendencias, frecuencias o preguntas oficiales.

## Artículo 16. Principio 9. Reducir la ansiedad mediante estructura

Los temas complejos se dividirán en bloques abordables, con objetivos, orden recomendado y comprobaciones intermedias. La estructura deberá permitir saber qué se está estudiando, qué falta y qué nivel de dominio se ha alcanzado.

## Artículo 17. Principio 10. Aprendizaje activo

Todo bloque relevante deberá permitir recuperar, comparar o aplicar lo aprendido mediante preguntas, casos, esquemas, repasos u otras actividades. Leer no se considerará suficiente para acreditar dominio.

## Artículo 18. Principio 11. Mejora continua

Las dudas recurrentes, errores detectados, cambios normativos, análisis de cobertura y resultados de los alumnos generarán acciones editoriales registradas y priorizadas.

## Artículo 19. Principio 12. Coherencia editorial

Las denominaciones, símbolos, jerarquías, criterios de cita, niveles de dificultad, estados y estilos se aplicarán de manera uniforme. Toda excepción deberá responder a una necesidad pedagógica o técnica documentada.

## Artículo 20. Principio 13. Reutilización del conocimiento

El conocimiento validado se estructurará para alimentar temarios, preguntas, repasos, audios, vídeos, infografías y avisos sin reescribir el fondo jurídico en cada formato.

## Artículo 21. Principio 14. Explicar mejor, no recortar lo difícil

La complejidad se resolverá descomponiendo, comparando y ejemplificando. No se eliminará un concepto examinable porque resulte difícil de explicar ni se ocultará una excepción relevante para simplificar el texto.

## Artículo 22. Principio 15. Transparencia y trazabilidad

El alumno y el equipo deberán poder conocer, según corresponda, la versión, la fecha de revisión, las fuentes, el estado de una alerta y los cambios que afectan al material. Una incertidumbre se declarará; no se maquillará como certeza.

## Artículo 23. Principio 16. Preparación útil para aprobar y para ejercer

El contenido se orientará al examen, pero conservará el sentido jurídico y profesional de lo estudiado. Los ejemplos policiales deberán ayudar a aplicar la norma sin sustituir protocolos operativos, formación reglada ni instrucciones vigentes.

---

# CAPÍTULO 6. LA REGLA DE ORO

## Artículo 24. Regla de Oro

> **Cada nuevo documento debe mejorar todos los anteriores y facilitar todos los posteriores.**

Para cumplir esta regla:

1. todo documento nuevo deberá reutilizar conocimiento validado y corregir las deficiencias conocidas que entren en su ámbito;
2. sus decisiones deberán quedar estructuradas para no obligar a rehacer innecesariamente los materiales futuros;
3. si descubre un error anterior, no deberá reproducirlo: lo registrará y activará su corrección;
4. la mejora no autoriza cambios silenciosos que rompan compatibilidad, trazabilidad o sincronización.

---

# CAPÍTULO 7. REGLAS EDITORIALES OBLIGATORIAS

## Artículo 25. Jerarquía de fuentes

1. Se priorizarán las fuentes primarias y oficiales: BOE, legislación consolidada, diarios oficiales de la Unión Europea, EUR-Lex, resoluciones y documentación oficial del órgano competente, convocatorias y programas oficiales.
2. Las fuentes secundarias podrán utilizarse para comprender o contrastar, pero no sustituirán la verificación oficial de una afirmación normativa.
3. Las fuentes deberán registrarse con identificador, título, versión o fecha de consulta y ámbito del contenido que respaldan.
4. La legislación consolidada facilita el estudio, pero deberá atenderse a las disposiciones modificadoras, correcciones de errores, vigencia, régimen transitorio y fecha de efectos cuando sean relevantes.

## Artículo 26. Núcleo maestro de conocimiento

1. Cada tema dispondrá de un núcleo maestro identificable que contenga conceptos, relaciones, fuentes, artículos, versiones y reglas de derivación.
2. El Parte y El Atestado serán vistas sincronizadas del núcleo maestro, no documentos jurídicamente independientes.
3. Toda edición directa de una vista derivada deberá trasladarse primero al núcleo maestro o registrarse como incidencia hasta que pueda integrarse.
4. El manual técnico definirá la estructura concreta del núcleo maestro y sus identificadores estables.

## Artículo 27. El Parte

1. **El Parte** es el Temario Esencial.
2. Debe permitir estudiar, memorizar, repasar y localizar con rapidez todos los conceptos examinables.
3. Será directo, pero no incompleto. Su extensión dependerá de la materia y no de un límite artificial de páginas.
4. Condensará explicaciones, no eliminará reglas, excepciones o matices capaces de cambiar una respuesta de examen.

## Artículo 28. El Atestado

1. **El Atestado** es el Temario Completo.
2. Debe permitir comprender y dominar la materia sin acudir de forma constante a fuentes externas.
3. Desarrollará fundamentos, conexiones, ejemplos, confusiones y trampas de examen sin introducir contenido ornamental.
4. La mayor extensión solo será admisible cuando aporte comprensión, precisión o capacidad de aplicación.

## Artículo 29. Sincronización entre versiones y recursos

1. Todo concepto tendrá un identificador estable y una relación explícita con sus fuentes, apariciones y preguntas.
2. Una modificación del núcleo maestro deberá generar una lista de vistas, preguntas y recursos potencialmente afectados.
3. Ninguna de las dos versiones podrá publicarse como actualizada si su pareja contiene información contradictoria sobre el mismo concepto.
4. Los recursos derivados deberán declarar la versión de conocimiento de la que proceden.

## Artículo 30. Las seis capas pedagógicas

Los temas utilizarán, cuando corresponda, las siguientes capas oficiales:

1. **Mapa del tema.** Indicará contenido, estructura, dificultad, importancia, división recomendada y tiempo aproximado cuando pueda estimarse con fundamento.
2. **Contenido.** Desarrollará la materia con rigor jurídico, orden lógico y referencias suficientes.
3. **Hablemos claro.** Explicará el concepto en lenguaje sencillo sin perder precisión ni alterar su alcance.
4. **En la calle.** Aplicará el concepto a ejemplos prácticos, cotidianos o policiales plausibles.
5. **Lo que cae.** Reunirá trampas, excepciones, confusiones, cambios terminológicos posibles y aspectos especialmente examinables.
6. **Ha caído.** Incluirá únicamente preguntas o referencias oficiales verificadas y trazables.

Las capas no son apartados de relleno. Podrán repetirse dentro de un tema cuando ayuden a resolver un bloque concreto, pero deberán mantener su función.

## Artículo 31. Tratamiento de la dificultad

1. Todo bloque especialmente complejo deberá reconocer la dificultad con precisión y proponer una estrategia concreta de estudio.
2. La estrategia podrá dividir el bloque, ordenar prerequisitos, señalar mínimos de primera vuelta y proponer un test antes de avanzar.
3. No se empleará motivación genérica para sustituir una explicación o un plan de trabajo.
4. La reducción de dificultad no deberá borrar excepciones, condiciones o distinciones examinables.

## Artículo 32. Lenguaje y estilo

1. Se utilizará español claro, preciso y natural, con párrafos y oraciones de longitud controlada.
2. La primera mención de una sigla deberá desarrollar su nombre, salvo abreviaturas universalmente reconocibles en el contexto.
3. Los términos jurídicos se conservarán cuando sean necesarios y se explicarán cuando puedan bloquear la comprensión.
4. Se evitarán absolutos no demostrables, grandilocuencia, superioridad comercial, infantilización y falsa seguridad.
5. No se utilizará la expresión **«En cristiano»** como capa, etiqueta o criterio editorial. La denominación oficial es **Hablemos claro**.

## Artículo 33. Exactitud, fechas y vigencia

1. Toda cifra, plazo, mayoría, competencia, composición, fecha o excepción deberá verificarse de forma específica.
2. Las expresiones «actual», «vigente», «última convocatoria» o equivalentes deberán vincularse a una fecha y a una fuente.
3. Cuando una norma tenga entrada en vigor diferida, régimen transitorio o efectos parciales, se distinguirán publicación, vigencia y aplicabilidad.
4. No se presentará como consolidado un cambio todavía pendiente de corrección, desarrollo o interpretación necesaria para el temario.

## Artículo 34. Referencias oficiales y capa Ha caído

1. Una pregunta solo podrá marcarse como oficial tras verificar su procedencia en el documento oficial o en una reproducción cuya autenticidad esté acreditada.
2. La referencia registrará, como mínimo, convocatoria, promoción o edición cuando proceda, número o localizador de pregunta, fuente, respuesta oficial y estado de verificación.
3. Si se resume o adapta un enunciado, se indicará expresamente; no se presentará la adaptación como transcripción literal.
4. Una pregunta o examen con identidad dudosa, duplicada o contradictoria permanecerá en cuarentena y no computará en frecuencias históricas.
5. La ausencia de evidencia se expresará como ausencia de verificación, nunca como prueba de que un contenido no ha sido preguntado.

## Artículo 35. Banco de preguntas

1. Cada pregunta deberá vincularse con tema, punto, subpunto, concepto, norma, artículo cuando proceda, dificultad, tipo, respuesta correcta, explicación, estado de revisión, versión normativa, origen y relaciones con otras preguntas.
2. Todas las preguntas propias deberán poder responderse con el temario publicado o con el ámbito de estudio expresamente indicado.
3. Los distractores serán plausibles, homogéneos y jurídicamente controlados. No deberán convertir la respuesta correcta en evidente por forma, longitud o absurdo.
4. Las preguntas equivalentes deberán probar un ángulo distinto y aportar cobertura real; un simple cambio superficial no crea una pregunta nueva.
5. La distribución de respuestas correctas se controlará en cada test. El barajado de opciones no sustituye el diseño equilibrado.
6. La generación de tests se basará en una matriz de cobertura que considere importancia, extensión, dificultad, frecuencia histórica verificada y número de conceptos examinables.

## Artículo 36. Uso de inteligencia artificial y automatización

1. La inteligencia artificial podrá redactar, transformar, comparar, clasificar, proponer preguntas y detectar posibles impactos.
2. No podrá atribuir carácter oficial, declarar una revisión jurídica superada ni publicar por sí sola una actualización de impacto medio o alto.
3. Toda salida automatizada deberá conservar las fuentes y el contexto necesarios para su revisión.
4. El revisor responderá por el material aprobado; la mención de una herramienta no sustituye la responsabilidad editorial.
5. Los sistemas automáticos deberán fallar de forma visible: si no pueden comprobar una fuente o completar un proceso, registrarán el error y no producirán una confirmación positiva.

---

# CAPÍTULO 8. LO QUE ESTÁ PROHIBIDO

## Artículo 37. Prohibiciones editoriales y técnicas

Queda prohibido:

1. inventar preguntas, años, convocatorias, frecuencias, estadísticas o referencias oficiales;
2. afirmar que un material está actualizado únicamente porque El Vigía no haya emitido una alerta;
3. confundir «cambio detectado» con «actualización realizada»;
4. copiar una norma sin explicar los conceptos que el alumno necesita comprender;
5. simplificar hasta alterar el sentido jurídico o eliminar una excepción examinable;
6. publicar contenido sin fuente suficiente cuando la afirmación requiera verificación;
7. presentar como literal un texto resumido, reconstruido o adaptado;
8. editar El Parte y El Atestado por separado sin resolver la sincronización del concepto afectado;
9. crear preguntas ambiguas, con más de una respuesta defendible o con distractores absurdos;
10. generar tests aleatorios sin reglas de cobertura;
11. inflar el banco con duplicados disfrazados;
12. utilizar preguntas que no puedan contestarse con el material asignado;
13. ocultar dudas, errores, conflictos de fuentes o revisiones pendientes;
14. eliminar contenido útil sin registrar el motivo, el impacto y la decisión;
15. publicar una salida de inteligencia artificial sin la revisión exigida por su riesgo;
16. utilizar motivación vacía, tono grandilocuente o promesas comerciales como sustituto de calidad demostrable;
17. usar la etiqueta **«En cristiano»** en nuevos materiales;
18. marcar un estado como aprobado, validado o publicado sin haber superado sus controles de entrada y salida.

---

# CAPÍTULO 9. CICLO DE VIDA DE UN TEMA

## Artículo 38. Estados del tema

Todo tema recorrerá, como mínimo, los siguientes estados:

1. **Alcance definido.** Programa oficial, epígrafes, fuentes y límites identificados.
2. **Investigación documentada.** Fuentes reunidas, vigencia comprobada y dudas registradas.
3. **Núcleo maestro redactado.** Conceptos y relaciones incorporados con identificadores y trazabilidad.
4. **Revisión jurídica.** Exactitud, fuentes, vigencia, excepciones y terminología comprobadas.
5. **Revisión pedagógica.** Orden, dificultad, ejemplos, claridad y estrategia de estudio comprobados.
6. **Vistas derivadas.** El Parte y El Atestado generados o actualizados desde el mismo núcleo.
7. **Cobertura de preguntas.** Conceptos examinables mapeados y entrenados con los ángulos necesarios.
8. **Control de sincronización.** Ausencia de contradicciones entre versiones, preguntas y recursos.
9. **Control de calidad final.** Estructura, referencias, enlaces, metadatos, lenguaje y presentación revisados.
10. **Publicado.** Versión identificada, fecha declarada e historial disponible.
11. **En mantenimiento.** Bajo vigilancia, con incidencias y resultados de uso incorporables.
12. **En revisión o retirado.** Bloqueado temporalmente o sustituido cuando exista un riesgo no resuelto.

## Artículo 39. Puertas de calidad del tema

1. Ningún tema avanzará a publicación con epígrafes oficiales sin cubrir, fuentes críticas sin verificar o contradicciones entre El Parte y El Atestado.
2. Un tema podrá publicarse por fases únicamente si el alcance disponible se identifica sin inducir a creer que está completo.
3. La revisión jurídica y la revisión pedagógica son controles distintos. Una no sustituye a la otra.
4. Los estados y responsables deberán quedar registrados de forma legible por personas y sistemas.

## Artículo 40. Mensajes del preparador

Cuando la dificultad lo requiera, el tema incluirá un mensaje del preparador que:

1. identifique el obstáculo concreto;
2. proponga una división practicable;
3. indique qué estudiar y comprobar antes de avanzar;
4. explique por qué ese dominio puede aportar ventaja en examen;
5. evite asegurar resultados o apelar solo al esfuerzo.

---

# CAPÍTULO 10. CICLO DE VIDA DE UNA PREGUNTA

## Artículo 41. Estados de la pregunta

Toda pregunta recorrerá, como mínimo, los siguientes estados:

1. **Propuesta.** Enunciado inicial vinculado a un objetivo de cobertura.
2. **Trazada.** Concepto, fuente, artículo, sección del temario y versión normativa identificados.
3. **Revisión técnica.** Respuesta, distractores, literalidad, ambigüedad y dificultad comprobados.
4. **Revisión pedagógica.** Utilidad, claridad y explicación razonada comprobadas.
5. **Revisión de equivalencia.** Comparación con preguntas relacionadas para descartar duplicación superficial.
6. **Aprobada.** Controles superados y responsable registrado.
7. **Publicada.** Disponible para generación de tests conforme a reglas de cobertura.
8. **Monitorizada.** Rendimiento, impugnaciones, errores y cambios de norma observados.
9. **En revisión.** Suspendida por duda o impacto detectado.
10. **Retirada o archivada.** Excluida de tests activos, con motivo e historial conservados.

## Artículo 42. Requisitos mínimos de una pregunta

Una pregunta no podrá aprobarse sin:

1. identificador estable;
2. clasificación completa en tema, punto, subpunto y concepto;
3. tipo y dificultad definidos conforme al manual;
4. opciones y respuesta correcta inequívocas;
5. explicación que justifique la correcta y, cuando aporte valor, descarte las restantes;
6. fuente y versión normativa;
7. vínculo con la sección del temario que permite responderla;
8. origen identificado como oficial o propio;
9. estado de revisión y responsable;
10. relación con preguntas equivalentes, inversas, comparativas o dependientes.

## Artículo 43. Preguntas oficiales

1. La pregunta oficial se conservará separada de sus adaptaciones propias.
2. Las correcciones, anulaciones y plantillas definitivas prevalecerán sobre plantillas provisionales.
3. Si no puede verificarse con certeza la convocatoria, el enunciado o la respuesta, la pregunta quedará en cuarentena.
4. Las preguntas en cuarentena no se mostrarán como oficiales ni alimentarán estadísticas, frecuencias o decisiones de cobertura.

## Artículo 44. Generación de tests

1. Los tests por punto, por varios puntos, acumulativos, completos, de 25, de 50, por dificultad o de falladas se generarán mediante reglas declaradas.
2. Un test completo deberá cubrir el conjunto del tema con ponderaciones justificables y límites que eviten monopolios de un solo apartado.
3. El algoritmo controlará repetición reciente, familias equivalentes, dificultad, tipo de pregunta y distribución de respuestas.
4. La aleatoriedad servirá para variar una selección válida; nunca para decidir por sí sola qué conocimientos se evalúan.

---

# CAPÍTULO 11. CICLO DE VIDA DE UNA ACTUALIZACIÓN

## Artículo 45. Estados obligatorios de El Vigía

Toda posible actualización se gestionará mediante estos estados diferenciados:

1. **Cambio detectado.** Una fuente vigilada presenta una novedad o diferencia.
2. **Cambio pendiente de revisión.** La alerta ha sido registrada y espera verificación humana o técnica suficiente.
3. **Impacto identificado.** Se ha determinado si el cambio afecta al programa y con qué nivel.
4. **Contenidos afectados.** Se han localizado conceptos, temas, versiones, preguntas, recursos y avisos que deben revisarse.
5. **Actualización realizada.** Los cambios se han aplicado en el núcleo maestro y se han propagado a los derivados.
6. **Revisión de calidad.** Se han comprobado exactitud, sincronización, cobertura y presentación.
7. **Publicación.** La nueva versión está disponible y la anterior permanece trazable.
8. **Aviso al alumno.** Se informa de qué cambió, desde cuándo, qué debe sustituirse y qué acción se recomienda.

## Artículo 46. Niveles de impacto

1. **Bajo.** Cambio formal o menor que no altera una respuesta de examen ni la comprensión sustantiva, aunque pueda exigir corrección editorial.
2. **Medio.** Cambio que modifica un concepto, dato, ejemplo, explicación o conjunto limitado de preguntas.
3. **Alto.** Cambio que altera el programa, la vigencia de un bloque, competencias, plazos, respuestas correctas, estructura normativa o una parte amplia del temario.
4. El nivel se asignará por impacto educativo y examinable, no por la jerarquía formal de la disposición ni por su extensión.

## Artículo 47. Fuentes vigiladas

El Vigía deberá cubrir, según la materia:

1. BOE y demás diarios oficiales competentes;
2. legislación consolidada y normas modificadoras;
3. normativa y publicaciones oficiales de la Unión Europea;
4. correcciones de errores;
5. disposiciones transitorias, derogatorias y finales;
6. cambios de vigencia, entrada en vigor y fecha de efectos;
7. convocatorias, bases y programa oficial;
8. plantillas, resoluciones y comunicaciones oficiales relevantes.

## Artículo 48. Reglas de actualización

1. Detectar una nueva fecha de consolidación no demuestra por sí mismo que exista un cambio material relevante para el temario.
2. Una alerta no podrá cerrarse sin registrar fuente, decisión, impacto y responsable.
3. Si la revisión concluye que no existe impacto, se conservará la justificación.
4. Las actualizaciones de impacto medio o alto exigirán revisión humana antes de publicarse.
5. El aviso al alumno deberá ser proporcional: evitará alarmas por cambios irrelevantes y no minimizará cambios que alteren respuestas.
6. El historial permitirá saber qué versión conocía cada pregunta y recurso en el momento de su publicación.

---

# CAPÍTULO 12. ESTÁNDAR DE EXCELENCIA

## Artículo 49. Criterios de aceptación

Un material alcanza el estándar de excelencia de Academia En Vigor únicamente cuando cumple de forma conjunta:

1. **Cobertura.** Incluye todos los conceptos de su alcance declarado y permite comprobarlos.
2. **Exactitud.** No contiene errores jurídicos, contradicciones internas ni datos sin verificar que se presenten como ciertos.
3. **Vigencia.** Declara la fecha y versión de revisión y ha superado el control correspondiente.
4. **Trazabilidad.** Cada afirmación crítica, pregunta oficial y actualización puede reconstruirse hasta su fuente y decisión.
5. **Sincronización.** El Parte, El Atestado, las preguntas y los recursos comparten el mismo conocimiento vigente.
6. **Claridad.** Un alumno del nivel previsto puede comprender el contenido sin que la simplificación altere la norma.
7. **Utilidad examinable.** Diferencia lo esencial, lo literal, las excepciones, las trampas y las aplicaciones relevantes.
8. **Calidad pedagógica.** Ordena la dificultad, activa la recuperación y ofrece explicaciones y ejemplos con función concreta.
9. **Calidad de pregunta.** Evalúa el concepto pretendido sin ambigüedad, pistas formales ni duplicación inútil.
10. **Mantenibilidad.** Usa identificadores, metadatos y estructuras que permiten actualizar sin búsquedas manuales ciegas.
11. **Accesibilidad editorial.** Emplea estructura, tablas, imágenes y lenguaje de manera legible y compatible con los formatos previstos.
12. **Revisión responsable.** Registra quién o qué realizó cada control y qué intervención humana fue necesaria.

## Artículo 50. Defectos bloqueantes

Impedirán la publicación o exigirán retirada temporal:

1. una respuesta de examen incorrecta o con más de una opción defendible;
2. una norma derogada o una versión normativa inadecuada presentada como vigente;
3. una referencia oficial inventada, no verificable o mal atribuida;
4. un epígrafe del programa omitido sin declaración expresa;
5. contradicciones sustantivas entre El Parte y El Atestado;
6. ausencia de trazabilidad en un cambio de impacto alto;
7. fallos técnicos que impidan acceder al contenido esencial o conocer su versión;
8. una alerta conocida que pueda cambiar respuestas y no se muestre como pendiente de revisión.

## Artículo 51. Calidad medible

1. Los manuales definirán indicadores de cobertura, sincronización, defectos, revisión, actualización y rendimiento de preguntas.
2. Ningún indicador aislado acreditará calidad. El número de páginas, preguntas o actualizaciones no será una medida suficiente.
3. Las métricas deberán detectar incentivos perversos, como inflar preguntas equivalentes o marcar alertas irrelevantes para aparentar actividad.

---

# CAPÍTULO 13. DEFINICIONES OFICIALES

## Artículo 52. Identidad y sistemas

1. **Academia En Vigor:** marca y organización responsable del proyecto editorial y formativo.
2. **Método VIGOR:** sistema de producción y aprendizaje que integra estructura, comprensión, aplicación, práctica, trazabilidad y actualización continua.
3. **El temario que nunca duerme:** lema principal y compromiso de vigilancia y mantenimiento continuos; no constituye una garantía automática de ausencia de errores o cambios pendientes.
4. **El Vigía:** sistema humano y técnico que detecta, clasifica, sigue y comunica cambios relevantes hasta su cierre editorial.

## Artículo 53. Productos editoriales

1. **Temario Esencial — El Parte:** vista directa y completa de lo examinable, optimizada para estudio, memorización, repaso y consulta rápida.
2. **Temario Completo — El Atestado:** vista desarrollada del mismo conocimiento, optimizada para comprensión profunda, ejemplos, conexiones y resolución de confusiones.
3. **Núcleo maestro de conocimiento:** representación canónica de conceptos, fuentes, relaciones, versiones y reglas de derivación de la que proceden las vistas y recursos.
4. **Recurso derivado:** audio, vídeo, infografía, esquema, resumen, ficha, aviso u otro formato creado a partir del núcleo maestro.

## Artículo 54. Capas pedagógicas

1. **Mapa del tema:** orientación previa sobre alcance, estructura, dificultad, importancia y plan de estudio.
2. **Contenido:** desarrollo riguroso y actualizado de la materia.
3. **Hablemos claro:** explicación sencilla y jurídicamente fiel.
4. **En la calle:** aplicación práctica, cotidiana o policial del concepto.
5. **Lo que cae:** análisis de examinabilidad, trampas, excepciones y confusiones.
6. **Ha caído:** evidencia oficial verificada sobre preguntas o referencias reales.

## Artículo 55. Datos, preguntas y cobertura

1. **Concepto examinable:** unidad de conocimiento susceptible de ser exigida directa o indirectamente conforme al programa y a sus fuentes.
2. **Pregunta propia:** pregunta creada por Academia En Vigor para entrenar un concepto; nunca se presentará como oficial.
3. **Pregunta oficial:** pregunta cuya procedencia y respuesta han sido verificadas en una fuente oficial o auténtica.
4. **Pregunta equivalente:** pregunta relacionada con otra que evalúa el mismo concepto desde un ángulo distinto y justificado.
5. **Familia de preguntas:** conjunto de preguntas vinculadas a un concepto o regla común y controladas para evitar repetición superficial.
6. **Matriz de cobertura:** relación entre conceptos examinables y las preguntas que los evalúan, con ponderaciones y ángulos de evaluación.
7. **Versión normativa:** conjunto identificable de textos, vigencias y fechas de efectos utilizado para redactar o validar un contenido.

## Artículo 56. Estados editoriales

1. **Trazabilidad:** capacidad de reconstruir el origen, transformación, revisión, versión e impacto de un contenido o decisión.
2. **Cuarentena:** estado que excluye temporalmente un contenido de publicación, estadísticas o generación de tests por existir una duda relevante.
3. **Publicado:** estado alcanzado tras superar los controles obligatorios y hacer disponible una versión identificada.
4. **Actualizado:** estado que solo puede declararse después de aplicar, revisar y publicar los cambios relevantes conocidos para el alcance y fecha indicados.
5. **Sincronizado:** estado en el que todas las representaciones activas de un concepto expresan la misma regla jurídica y versión aplicable.
6. **Incidencia editorial:** registro de un error, duda, contradicción, mejora o tarea que requiere decisión o acción.

---

# CAPÍTULO 14. COMPROMISO EDITORIAL

## Artículo 57. Compromiso de Academia En Vigor

Academia En Vigor se compromete a:

1. enseñar con claridad sin sacrificar precisión;
2. mantener una única base de conocimiento trazable;
3. vigilar las fuentes relevantes y comunicar el estado real de cada cambio;
4. corregir los errores de forma visible, proporcionada y completa;
5. diferenciar siempre contenido oficial, contenido propio e interpretación;
6. no utilizar automatización para ocultar trabajo pendiente;
7. proteger al alumno frente a materiales ambiguos, desactualizados o falsamente atribuidos;
8. revisar el sistema editorial a partir de evidencias, no de impresiones aisladas;
9. conservar el historial necesario para comprender qué cambió, por qué y con qué impacto;
10. aplicar este Código antes de declarar terminado cualquier tema, pregunta o actualización.

## Artículo 58. Responsabilidad compartida

1. Quien crea contenido deberá aportar fuentes, estructura y metadatos suficientes.
2. Quien revisa deberá comprobar y no limitarse a confirmar.
3. Quien publica deberá verificar que se han superado las puertas de calidad.
4. Quien detecta un error deberá registrarlo y evitar su propagación.
5. La responsabilidad final corresponde a Academia En Vigor, incluso cuando intervengan proveedores, colaboradores o sistemas automáticos.

---

# CAPÍTULO 15. HISTORIAL DE VERSIONES

## Artículo 59. Registro de versiones

| Versión | Fecha | Estado | Responsable | Cambios principales |
|---|---|---|---|---|
| 0.1 | 15-07-2026 | Borrador funcional | Academia En Vigor | Primera redacción completa. Define misión, visión, valores, 16 Principios VIGOR, Regla de Oro, reglas obligatorias, prohibiciones, ciclos de vida, estados de El Vigía, estándar de excelencia, definiciones y compromiso editorial. |

## Artículo 60. Próxima revisión

La versión 0.2 deberá revisar este Código después de redactar los manuales operativos y de aplicar el sistema al Tema 3. La revisión deberá resolver ambigüedades detectadas durante el piloto sin rebajar los controles establecidos.

---

**Fin del Código VIGOR · versión 0.1**

# Tests de Academia En Vigor

Los tests de la plataforma se guardan en **JSON UTF-8**. El JSON es la fuente canónica: la interfaz web debe leerlo y renderizarlo, sin mantener una segunda copia de las preguntas en HTML o Markdown.

## Esquema 1.0

- `id`: identificador estable del test.
- `schema_version`: versión del contrato de datos.
- `metadata`: título, descripción, tema, bloque, duración, número de preguntas y estado editorial.
- `settings`: reglas de presentación, barajado y puntuación.
- `coverage`: apartados y conceptos del Atestado que se evalúan.
- `questions`: colección de preguntas.

Cada pregunta contiene:

- `id`: identificador estable y único.
- `type`: actualmente `single_choice`.
- `difficulty`: `basic`, `intermediate` o `advanced`.
- `concept`: concepto principal evaluado.
- `section_refs`: apartados del Atestado relacionados.
- `prompt`: enunciado.
- `options`: tres objetos con `id` y `text`.
- `correct_option_id`: identificador de la respuesta correcta.
- `explanation`: explicación que se muestra después de corregir.
- `source_note`: fundamento normativo o doctrinal.

## Descripciones para la plataforma

Cada test debe incluir una `description` breve, clara y orientada al alumno. La misma descripción se conserva en dos lugares:

- `index.json`: permite mostrarla en la lista o tarjeta del test sin descargar el archivo completo;
- `metadata.description` del test: permite mostrarla en la pantalla previa aunque el archivo se cargue directamente.

Ambos valores deben ser idénticos. La descripción debe indicar qué se practica, el tipo de razonamiento exigido y los bloques principales, sin revelar respuestas.

## Reglas para la interfaz

1. No identificar visualmente la respuesta correcta antes de entregar el test.
2. Barajar preguntas y opciones conservando los identificadores.
3. Permitir dejar preguntas sin contestar.
4. Corregir al finalizar, no después de cada clic, salvo en modo aprendizaje.
5. Mostrar explicación y fundamento después de corregir.
6. Guardar resultados por `test.id`, `question.id` y versión del test.
7. No depender de la posición A/B/C para corregir: debe compararse el `id` de la opción elegida con `correct_option_id`.

En una plataforma con backend, la API pública de inicio debería omitir `correct_option_id` y `explanation`; esos campos se devolverían al entregar el intento. En un sitio completamente estático los datos serán inspeccionables desde el navegador, aunque la experiencia normal de uso seguirá funcionando.

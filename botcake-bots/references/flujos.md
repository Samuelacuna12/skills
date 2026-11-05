# Construcción de flujos

## Plano recomendado

`Entrada → exclusiones → intención → captura mínima → respuesta/consulta → siguiente paso → salida`

Haz una ficha por bloque: nombre, entrada, mensaje, variable leída, dato guardado, condición de salida, destino y error. Los nombres `F00_Entrada`, `F10_Calificar`, `F20_Resolver` y `F90_Humano` son convenciones sugeridas.

## Construir en el editor

1. Abre Flows y crea un flujo con un nombre reconocible y propósito único.
2. Añade el primer mensaje y los botones necesarios. Configura cada destino y un camino para texto libre.
3. Para capturar, crea primero el campo y añade Input; selecciona tipo, campo de destino, validación y comportamiento cuando el cliente omite o da un dato incorrecto.
4. Añade condiciones basadas en valores reales. Incluye siempre un camino para valor vacío o no reconocido.
5. Configura IA o JSON API solo donde aporte flexibilidad o consulta externa.
6. Revisa conexiones, guarda y prueba antes de enlazar el disparador.

La documentación de configuración describe Input, Custom Fields, Next Step y bloques de contenido; inspecciona los nombres actuales de cada control. Fuente: [Message setup](https://docs.pancake.biz/botcake/st-f6/st-p1/st-s1?lang=en).

## Estado y prevención de bucles

| Estado propuesto | Comportamiento |
|---|---|
| nuevo | Presentar ayuda y reconocer intención |
| capturando | Pedir únicamente los datos pendientes |
| esperando_api | Evitar otra creación hasta resolver el resultado |
| pendiente_confirmacion | Mostrar resumen y permitir corregir |
| convertido | Cerrar y detener el seguimiento de captación |
| humano | Ceder la conversación al responsable |
| baja | Excluir de mensajes comerciales |

Implementa estos estados con las herramientas disponibles; un nombre en el diseño no crea una condición real. Prueba doble clic, mensajes consecutivos y volver a entrar con datos anteriores. Define cuándo empieza una nueva solicitud sin borrar indiscriminadamente el historial.

## Atención humana

Define motivos: solicitud explícita, reclamación, información ausente o fallos reiterados. Configura la transferencia/asignación real y la pausa correspondiente; una frase «te paso con un asesor» no ejecuta la transferencia. Pasa resumen, motivo y datos necesarios. Fuera de horario, informa el horario real sin prometer respuesta inmediata.

Botcake describe pausa de automatización al intervenir un agente. Verifica el comportamiento en la cuenta y cómo se reanuda, incluyendo secuencias y otros sistemas conectados. Fuente: [Soluciones Botcake](https://botcake.io/es/solutions).

## WhatsApp Flow es un objeto distinto

Un formulario WhatsApp Flow se administra en WhatsApp Manager → Flow. La guía distingue borrador y publicado; advierte que la estructura publicada exige crear otro flow para cambios. Su distribución se configura mediante un botón en una plantilla. Antes de publicar, prueba campos, navegación y recepción de respuestas. No confundas su identificador Meta con el `flow_id` de un flujo de mensajes Botcake.

Fuente: [WhatsApp Flow](https://docs.pancake.biz/botcake/st-f4/st-p4/st-s4?lang=en).

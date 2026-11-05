# Agentes IA y prompts

## Configuración del agente

En la guía actual, el agente reúne selección de modelo, instrucciones rápidas o detalladas, seguimiento, documentos y Preview. Guarda los cambios y verifica qué agente está seleccionado por defecto para respuestas globales. Si se usa IA dentro de un flujo, comprueba la selección del agente en ese bloque. La guía presenta parámetros de generación; utiliza solo los expuestos para el modelo seleccionado, sin imponer valores universales.

Fuente: [AI Usage Guide](https://docs.pancake.biz/botcake/st-f4/st-p5/st-s1/st-ss1?lang=en).

## Preparar conocimiento confiable

Construye documentos breves por oferta o proceso: descripción, precios/moneda/vigencia, variantes, cobertura, tiempos, políticas y preguntas frecuentes. Identifica propietario y fecha. Resuelve contradicciones antes de cargar documentos. Separa datos estables del negocio de inventario, agenda y estado de pedidos, que requieren consulta actual cuando sean relevantes.

Adjuntar documentos proporciona contexto; no demuestra entrenamiento permanente del modelo ni que cada dato será recuperado. Prueba preguntas cuya respuesta solo aparezca en los documentos.

## Redactar

Copia [prompt-base.txt](../assets/prompt-base.txt), sustituye marcadores y elimina bloques que no apliquen. Los marcadores `[[...]]` son instrucciones de edición; no son variables Botcake. Inserta variables reales con el selector de la interfaz, y verifica su valor en pruebas.

Un prompt útil especifica identidad, objetivo, fuentes, etapas, preguntas mínimas, límites, herramientas disponibles, salida humana y ejemplos. Separa reglas obligatorias de estilo. No acumules instrucciones contradictorias como «nunca preguntes» y «recoge todos los datos».

| Problema | Mejor instrucción |
|---|---|
| Inventa precios | Solo cotiza importes presentes en catálogo vigente; si falta el dato, escala |
| Interroga al cliente | Reutiliza información ya dada y pregunta por un dato faltante cada vez |
| Confirma citas inexistentes | Llama solicitud a la preferencia; confirma únicamente tras respuesta de agenda |
| Habla sin cerrar | Después de resolver, ofrece el siguiente paso relacionado con la intención |
| Repite todo | Resume lo relevante y no reinicies el saludo en cada turno |
| Promete tareas externas | Describe únicamente acciones configuradas y verifica su resultado |

## IA dentro de un flujo

El bloque IA documentado permite definir la pregunta del cliente, seleccionar agente, añadir instrucciones/contexto, guardar respuesta en Custom Fields y acciones de éxito/fallo. Mapea una pregunta real; una etiqueta como «mensaje» no equivale al contenido del usuario. Decide si la respuesta la envía el bloque o si se guarda para el siguiente mensaje y evita enviarla dos veces.

Fuente: [How to Use AI in a Flow](https://docs.pancake.biz/botcake/st-f4/st-p5/st-s1/st-ss3?lang=en).

Cualquier retorno a un bloque anterior debe pasar por una nueva entrada del usuario o una condición de espera/salida. No conectes una respuesta IA a sí misma en ejecución inmediata.

## Evaluar y mejorar

Ejecuta [pruebas.csv](../assets/pruebas.csv) con conversaciones nuevas y con contexto. Valora precisión, siguiente paso, captura, tratamiento de datos desconocidos, humano y duplicación. Prueba varias redacciones para intenciones críticas: una respuesta correcta aislada no garantiza estabilidad.

Cuando falle, clasifica: conocimiento ausente, instrucción ambigua, variable vacía, agente equivocado, herramienta no configurada o disparador. Corrige la causa en su capa. No intentes arreglar con más prompt un error de permisos, plantilla o integración.

# Disparadores: cómo iniciar el bot

Un flujo guardado puede estar correctamente construido y no recibir nunca un evento. Documenta siempre canal, evento, condición, destino, prioridad, frecuencia y exclusiones.

## Palabras clave: procedimiento verificable

La guía oficial sitúa esta función en Automation → Keywords → Create new keyword. Elige el modo de coincidencia, introduce las palabras, guarda y asigna respuesta/acción. Entre los modos documentados están contenido exacto, contiene, contiene todas, empieza por y exclusiones. La guía advierte que, si coinciden palabras distintas en un mensaje, puede prevalecer la primera en la lista: ordena y prueba conflictos.

Fuente: [Keywords](https://docs.pancake.biz/botcake/st-f3/st-p4/st-s5?lang=en).

Ejemplo recomendado: `COTIZAR` exacto para una entrada controlada; prueba también `cotizar`, espacios, tildes y texto añadido. No asumas normalización. Evita `no` o `si` como coincidencias amplias: pueden interceptar frases de otro contexto.

## Mapa de entradas

| Entrada | Configuración a inspeccionar | Prueba útil |
|---|---|---|
| Primera conversación | Welcome Message del canal | Contacto nuevo; comparar con recurrente |
| Mensaje sin coincidencia | Default reply y prioridad IA | Texto inesperado y pregunta conocida |
| Palabra clave | Keywords y orden | Exacta, parcial y dos keywords juntas |
| Menú o botón | Destino del botón | Cada botón llega al bloque correcto |
| Comentario | Configuración general o por publicación | Publicación objetivo y otra excluida |
| Anuncio a mensajes | Configuración del anuncio/canal y entrada | Recorrido desde anuncio de prueba |
| Enlace o QR | Herramienta de crecimiento soportada | Abrir desde otro dispositivo y enviar mensaje |
| Regla por evento | Automation → Rules | Evento real y condición que no se cumple |
| Secuencia | Suscripción + mensajes activos | Alta, intervalo y cancelación |
| API/Make | Destino e identificador real del contacto | Un contacto de prueba y revisión de respuesta |

El índice oficial incluye Welcome Message, Default reply, Sequences y Rules. Esto no garantiza que todas las entradas de la tabla estén disponibles en todos los canales. Los anuncios y enlaces requieren verificar su mecanismo concreto; abrir un chat no demuestra que el evento ya ocurrió.

Fuente: [Automation](https://docs.pancake.biz/botcake/st-f3/st-p4?lang=en).

## Comentarios

En Comments → General Settings se documentan controles separados para respuesta pública e inbox. Configura solo los que necesite el caso; guarda los textos. La opción de responder únicamente según cada publicación hace que la configuración general no aplique. La guía pide personalización o variación en la respuesta pública; revisa las variables desde la interfaz. Prueba con una cuenta de cliente y no expongas teléfonos ni datos de pedido en público.

Fuente: [Comments General](https://docs.pancake.biz/botcake/st-f3/st-p6/st-s1?lang=en).

## Secuencias y seguimiento

La documentación permite crear una secuencia en Automation → Sequence, fijar tiempos desde la suscripción, elegir contenido y habilitar mensajes. Además hay que suscribir al contacto, mediante la configuración disponible de etiquetas o una regla. Si dependes de etiquetas de Pancake, comprueba sincronización.

Fuente: [Sequences](https://docs.pancake.biz/botcake/st-f3/st-p4/st-s6?lang=en).

Diseño recomendado: espera → volver a comprobar baja/humano/conversión/eligibilidad → enviar → salida. Cancelar seguimientos al responder o convertir según objetivo. No heredes ejemplos antiguos de etiquetas de mensaje como autorización vigente. En WhatsApp revisa plantilla cuando corresponda y en otros canales verifica sus reglas específicas.

## Activación sin solapamientos

1. Prueba primero flujo/agente en vista previa.
2. Guarda destino y enlaza un único disparador de prueba.
3. Envía el evento desde el canal real con un contacto autorizado.
4. Comprueba una sola respuesta, datos guardados y destino final.
5. Prueba una condición excluida y la toma humana.
6. Activa el alcance autorizado y registra cómo pausarlo.

No uses un envío masivo para comprobar un disparador. Para API consulta [integraciones](integraciones.md).

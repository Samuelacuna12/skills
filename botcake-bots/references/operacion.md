# Pruebas, lanzamiento y diagnóstico

## Comprobar de extremo a extremo

Utiliza contactos de prueba autorizados y datos sintéticos. Registra caso, canal, entrada, resultado esperado, resultado observado y evidencia anonimizada. Cubre al menos: entrada correcta, exclusión, dato inválido, pregunta sin fuente, transferencia humana, baja, error de integración y mensaje duplicado.

Antes de activar, comprueba:

- Página y canal correctos; flujo y agente guardados y seleccionados.
- Disparador enlazado y prioridad frente a reglas existentes.
- Campos guardan valores; siguiente bloque los recibe.
- Pedido/cita solo se confirma con respuesta externa válida.
- Humano, baja y conversión detienen seguimientos pertinentes.
- Horarios, zona y reglas del canal revisados.
- Conoces la regla que se debe pausar y conservas la configuración anterior.

## WhatsApp proactivo

Distingue respuesta dentro de la ventana de atención de un envío proactivo fuera de ella. La guía de Botcake describe uso de plantilla aprobada cuando la ventana está cerrada y mapeo de todas sus variables; revisa estado, idioma y parámetros antes de enviar. Los costes, categorías, límites y excepciones deben consultarse en las fuentes actuales de Meta y en la cuenta, sin reutilizar tarifas o reglas antiguas.

Fuente: [Template Management](https://docs.pancake.biz/botcake/st-f4/st-p4/st-s2?lang=en); [política oficial de WhatsApp](https://business.whatsapp.com/policy).

## Diagnóstico por capa

| Síntoma | Verificar primero | Corrección orientada |
|---|---|---|
| No responde | Llegada del mensaje, conexión, regla activa, destino | Corregir la primera capa que falla |
| Preview funciona, canal no | Disparador, elegibilidad, prioridad | Reproducir evento real |
| Responde dos veces | IA global, default reply, keywords, otra app | Definir un solo dueño por evento |
| Keyword equivocada | Coincidencia amplia y orden | Acotar y probar ambas intenciones |
| IA ignora prompt | Agente seleccionado y cambios guardados | Probar con contexto nuevo |
| Respuesta inventada | Fuente ausente/contradictoria o dato dinámico | Corregir conocimiento o consultar sistema |
| Campo vacío | Captura, selección de campo y JSON Path | Revisar respuesta real y mapeo |
| API 401/403 | Token, permisos y página | Corregir credencial sin rotar todo por rutina |
| API timeout | Estado incierto de la acción | Verificar entrega antes de repetir |
| Secuencia no inicia | Suscripción y mensaje habilitado | Probar alta real |
| Sigue hablando con humano | Pausa local y otras automatizaciones | Aplicar exclusión en todos los caminos |
| Plantilla falla | Estado, idioma y variables | Corregir los parámetros faltantes |
| Bot reinicia siempre | Estado y campo de intención | Retomar desde etapa vigente |

Para errores desconocidos, copia código y mensaje sin secretos y consulta soporte/documentación; no traduzcas un error genérico en una causa definitiva.

## Lanzamiento y reversión

Empieza con el alcance autorizado más pequeño que permita verificar el objetivo. Observa primeros recorridos y después amplía si corresponde al encargo. Si aparece un fallo que genera envíos erróneos, pausa el disparador afectado, conserva evidencia y vuelve a la configuración anterior compatible. No borres contactos, claves o canales para revertir un cambio de flujo.

Mide denominadores explícitos: contactos que entraron, completaron captura, se transfirieron, convirtieron y dieron baja. Separa entrega, lectura, respuesta y conversión; una llamada API exitosa no prueba venta. Revisa preguntas sin respuesta y actualiza conocimiento con la aprobación comercial pertinente.

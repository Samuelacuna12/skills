# Configuración y canales

## Preparar el negocio

Completa el brief. Define una conversión medible: lead con datos válidos, solicitud de cita, ticket resuelto o pedido confirmado. Recopila catálogo, precios y vigencia, cobertura, tiempos, horarios, pagos, cambios, garantías y contacto humano. Si faltan datos, deja el caso como pendiente; no rellenes políticas por intuición.

Arquitectura recomendada: canal → disparador → flujo de entrada → captura/condiciones → agente o integración → resultado → salida. Usa flujos para pasos obligatorios y validación; usa IA para preguntas, intención y conversación flexible. La recomendación debe adaptarse al caso, no imponer una plantilla ecommerce a reservas o servicios.

## Conectar

1. Abre Botcake y selecciona la página exacta. Revisa el canal y permisos de administración.
2. En la integración correspondiente, sigue el asistente oficial para esa cuenta. Comprueba que la página/número figure conectado y que un mensaje de prueba llegue a la bandeja correcta.
3. Revisa automatizaciones existentes antes de añadir una nueva. Anota quién responde hoy: Pancake, Botcake, otra app o agente humano.
4. Configura zona horaria, horario del equipo y responsable de escalamiento según opciones disponibles.

### WhatsApp

La guía oficial distingue Cloud API y coexistencia con WhatsApp Business App. Antes de migrar, comprueba elegibilidad de coexistencia y consecuencias para el uso de la aplicación. Revisa WABA, número conectado/verificado y nombre visible. Los requisitos de plan y límites deben comprobarse en la cuenta actual. No desconectes números ni sustituyas la integración como solución automática a un fallo.

Fuente: [WhatsApp Integration](https://docs.pancake.biz/botcake/st-f2/st-p5?lang=en).

### Messenger e Instagram

Verifica propiedad/permisos y recepción de mensajes. No copies disparadores entre canales sin comprobar soporte. En Instagram revisa si la conexión se hizo directamente con una cuenta profesional o mediante Facebook: las funciones disponibles pueden diferir. Fuente: [actualizaciones oficiales](https://docs.pancake.biz/botcake/st-f9/st-p1?lang=en).

## Modelo de datos recomendado

Estos nombres son convenciones del proyecto, no campos nativos garantizados:

| Campo | Tipo lógico | Regla |
|---|---|---|
| nombre | texto | Pedir solo si falta |
| telefono | teléfono | Validar formato sin inferir identidad |
| interes | texto/opción | Oferta o servicio solicitado |
| ciudad | texto | Verificar cobertura |
| estado_comercial | opción | nuevo, calificado, pendiente, convertido |
| atencion_humana | booleano | Determina si el bot puede continuar |
| baja_mensajes | booleano | Excluir de seguimiento comercial |
| origen | texto | Solo atribución comprobada |
| referencia_externa | texto | ID retornado por CRM/POS/agenda |

Crea los Custom Fields antes de usarlos en un bloque Input; elige tipo y mapea respuestas. Las etiquetas sirven para segmentar; los campos conservan valores. Decide cuál es la fuente de verdad si sincronizas Pancake, CRM y Botcake. Fuente: [componentes de mensajes](https://docs.pancake.biz/botcake/st-f6/st-p1/st-s1?lang=en).

## IA actual frente a interfaz anterior

La documentación actual describe agentes con instrucciones, productos, documentos y vista previa. Algunas cuentas muestran integración con proveedor en Settings → Integrations → AI; otras presentan opciones distintas. Inspecciona la pantalla antes de dar una ruta exacta. No fijes un modelo, precio ni límite de archivos de una guía anterior como requisito permanente. Conecta credenciales mediante el mecanismo de la cuenta y verifica disponibilidad de uso/saldo sin copiar secretos al prompt.

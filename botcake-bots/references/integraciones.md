# Integraciones y disparo externo

## Seleccionar la vía

- MCP Botcake disponible: inspecciona herramientas, página y parámetros; usa lectura antes de mutaciones.
- Integración nativa: preferible cuando cubre autenticación, datos y acción necesarios.
- JSON API en flujo: para consultar o enviar información durante la conversación.
- Make/n8n o servicio propio: para eventos externos, transformación, control de duplicados y operaciones largas.

El changelog oficial anuncia MCP y remite a [mcp.botcake.io](https://mcp.botcake.io). No asumas que está instalado o conectado en otro entorno. Fuente: [Actualizaciones](https://docs.pancake.biz/botcake/st-f9/st-p1?lang=en).

## API para enviar un flujo

Contrato documentado: `POST https://botcake.io/api/public_api/v1/pages/{page_id}/flows/send_flow`, header `access-token`; cuerpo con `psid` del contacto, `flow_id` entero y `payload` opcional. Obtén identificadores de la cuenta; no fabriques el ID a partir de un teléfono. La guía sitúa la generación del token en Settings → Integration → API y advierte que renovarlo o eliminarlo afecta integraciones existentes.

Fuente: [API Reference](https://docs.pancake.biz/botcake/st-f7/st-p2?lang=en). Verifica el contrato vigente en [Developer Docs](https://developers.botcake.io/#/) antes de un envío real.

El helper [send_flow.py](../scripts/send_flow.py) prepara el cuerpo sin enviar por defecto. Para enviar requiere `--send`, configuración explícita y token en variable de entorno. No tiene reintentos automáticos: un timeout puede ocurrir después de la entrega. Conserva el estado incierto y revisa historial antes de repetir. Un HTTP correcto no demuestra entrega; comprueba también la respuesta y el mensaje en el contacto.

```sh
python3 scripts/send_flow.py --page-id PAGINA --psid CONTACTO --flow-id 123
# Solo con un contacto autorizado y configuración real:
# BOTCAKE_ACCESS_TOKEN configurado fuera del repositorio
python3 scripts/send_flow.py --page-id PAGINA --psid CONTACTO --flow-id 123 --send
```

## JSON API dentro de un flujo

La guía documenta Flows → bloque → Add content → JSON API. Configura método, URL, autenticación y cuerpo, prueba una operación de lectura o un destino de pruebas y mapea la respuesta a Custom Fields. Verifica el JSON Path contra la respuesta real. Incluye una rama para fallo o dato ausente. La documentación enumera GET, POST y DELETE; si la interfaz no ofrece el método requerido, usa una capa intermedia verificada.

Fuente: [Block JSON API](https://docs.pancake.biz/botcake/st-f3/st-p3/st-s1?lang=en).

No uses el botón de prueba sobre un endpoint de pedidos, cobros o reservas de producción sin tratarlo como una acción real. Guarda secretos en el mecanismo protegido disponible o en el servicio intermedio; evita campos de cliente que puedan interpolarse o exponerse.

## Make y webhooks

El catálogo de Make documenta `Send a Flow` y `Make API Call`. Comprueba sus campos y conexión en la versión instalada; no inventes un módulo disparador de Botcake. El escenario puede empezar por el evento del sistema origen o un webhook configurado. Fuente: [Make Botcake](https://apps.make.com/botcake).

Mapa recomendado:

`evento de CRM → validar autenticidad y datos → deduplicar por event_id → localizar contacto elegible → enviar flujo → registrar resultado`

El objeto siguiente es un contrato de ejemplo para un receptor propio, no un payload nativo de Botcake:

```json
{"event_id":"demo-001","event":"lead_qualified","contact_ref":"demo-contact","occurred_at":"2026-11-05T10:00:00-05:00"}
```

Acepta solo eventos válidos del origen esperado; minimiza datos y no registres tokens. Para una creación externa usa idempotencia si el proveedor la soporta, o control propio de operaciones. No asumas soporte de un header no documentado.

## CRM, POS y agenda

Mapea dirección de sincronización, campos, tipo, fuente de verdad y tratamiento de error. Para ecommerce, confirma variante, cantidad, precio final y envío antes de crear pedido. Para reservas, comprueba disponibilidad y guarda el ID confirmado por la agenda. Para soporte, valida acceso antes de revelar información de un pedido. La IA no debe convertir una propuesta de horario o un mensaje de pago en una confirmación real.

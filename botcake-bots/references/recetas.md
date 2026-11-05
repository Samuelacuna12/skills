# Recetas adaptables

Estas recetas son diseños de referencia propios; no son plantillas importables ni menús garantizados de Botcake. Usa datos reales del negocio y comprueba las funciones de cada canal.

## 1. Venta de productos

Objetivo: pedido confirmado por POS o derivación con datos completos.

1. Entrada por keyword `CATALOGO`, botón o anuncio verificado.
2. Comprobar baja/humano y recuperar interés anterior.
3. Preguntar producto y necesidad; consultar catálogo vigente.
4. Ofrecer opciones compatibles y pedir variante/cantidad.
5. Recoger ciudad, calcular envío desde fuente disponible y mostrar total desglosado.
6. Pedir datos mínimos y mostrar resumen corregible.
7. Tras aceptación, crear pedido mediante integración configurada. Guardar referencia externa.
8. Confirmar solo si el sistema devuelve el pedido; ante fallo, pasar a humano sin afirmar creación.
9. Detener seguimiento de captación; añadir seguimiento de servicio solo si corresponde.

Texto de comportamiento para añadir al prompt base: «Antes de cerrar, verifica variante, cantidad, cobertura y total. Nunca sustituyas stock desconocido por stock disponible. No marques pagado por una imagen o afirmación del cliente; verifica el sistema de pagos».

Pruebas clave: variante agotada, ciudad excluida, cambio de cantidad, doble confirmación y POS inaccesible.

## 2. Servicios y reservas

Objetivo: lead calificado o cita registrada.

1. Entrada por `AGENDAR` o botón soportado.
2. Identificar servicio y modalidad; consultar duración, condiciones y precio publicado.
3. Pedir ciudad/zona si afecta disponibilidad y horario preferido.
4. Si hay agenda integrada, consultar huecos y ofrecer los válidos. Si no la hay, registrar preferencia como solicitud.
5. Recoger nombre y contacto estrictamente necesarios.
6. Mostrar fecha completa, hora y zona horaria para evitar «mañana» ambiguo.
7. Ejecutar reserva y guardar ID; confirmar solamente tras resultado satisfactorio. Si falla, informar que sigue pendiente.
8. Crear recordatorio elegible y cancelar si hay anulación/reprogramación.

Texto para añadir: «Una preferencia de horario no es una reserva. No inventes cupos. Si no puedes consultar agenda, explica que un asesor confirmará disponibilidad y registra una solicitud».

Pruebas clave: fecha pasada, horario ocupado, zona distinta, reprogramación y ausencia de agenda.

## 3. Atención y seguimiento de pedidos

Objetivo: resolver una consulta con información autorizada o transferir contexto útil.

1. Entrada por `AYUDA`, menú o pregunta libre.
2. Distinguir FAQ, pedido, devolución o queja.
3. Resolver FAQ desde la política vigente.
4. Para pedido, pedir referencia y aplicar comprobación de acceso definida por el negocio antes de mostrar datos.
5. Consultar estado real, explicar qué significa y el siguiente paso disponible.
6. Si falta información, existe inconformidad o se pide humano, transferir y pausar automatización.
7. Registrar motivo y resultado sin duplicar tickets.

Texto para añadir: «No reveles datos de otros clientes. No prometas devolución, compensación o fecha de entrega que no esté autorizada por una política o respuesta del sistema».

Pruebas clave: referencia inexistente, datos que no coinciden, cliente enfadado, consulta fuera de horario y transferencia real.

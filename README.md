# Skills de Samuel Acuña

Skills reutilizables para trabajar con asistentes de IA.

## Botcake Bots

[Ver la skill](botcake-bots/SKILL.md) · [Fuentes](botcake-bots/references/fuentes.md)

Guía en español para diseñar, configurar, activar y depurar bots de Botcake: canales, flujos, disparadores, agentes IA, prompts, atención humana, CRM/POS, API y seguimiento. Incluye recetas de ventas, reservas y soporte, plantillas editables y casos de prueba.

### Instalar en Codex

Clona el repositorio y copia únicamente la carpeta `botcake-bots` dentro de `~/.codex/skills/`. Si ya existe una carpeta con ese nombre, revisa antes de sustituirla. Abre una nueva sesión para que se descubra la skill.

```sh
git clone https://github.com/Samuelacuna12/skills.git
mkdir -p ~/.codex/skills
cp -R skills/botcake-bots ~/.codex/skills/
```

Ejemplos:

- «Usa $botcake-bots para diseñar un bot de reservas en WhatsApp para mi negocio».
- «Usa $botcake-bots para crear el prompt y el flujo de ventas de mi catálogo».
- «Usa $botcake-bots para revisar por qué una keyword no activa mi flujo».
- «Usa $botcake-bots para disparar un flujo desde mi CRM sin duplicados».

### Contenido

| Recurso | Uso |
|---|---|
| `botcake-bots/SKILL.md` | Instrucciones y selección de referencias |
| `botcake-bots/references/` | Siete guías operativas y fuentes |
| `botcake-bots/assets/` | Brief, prompt, plan y matriz de pruebas |
| `botcake-bots/scripts/send_flow.py` | Preparar o enviar una llamada API explícita |

El helper no envía nada sin `--send`. La skill no es un bot alojado ni un archivo importable en Botcake: guía a un asistente para construir y verificar la configuración real. Los nombres de campos y ejemplos son editables. No incluye credenciales ni datos de clientes.

Consulta de documentación: 5 de noviembre de 2026. Las capacidades, políticas, precios y pantallas deben verificarse antes de usarse en producción. Proyecto independiente, sin afiliación oficial con Botcake.

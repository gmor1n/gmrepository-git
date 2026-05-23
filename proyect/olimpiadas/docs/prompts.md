
# 📰 Proyecto Olimpiadas — Memoria de Prompts, decisiones y conclusiones

## 🎯 Objetivo
Crear una web con estética de **periódico antiguo** para storytelling de Olimpiadas y, más adelante, **integrar gráficos interactivos de Flourish** (embebidos desde otra aplicación/servicio) sin que parezcan “pegotes”.

---

## 🧱 Estructura del repo (laboratorio)
Este repo se usa como laboratorio con múltiples proyectos:

- `proyect/olimpiadas/` → proyecto actual (periódico Olimpiadas)
- `proyect/otros/` → futuros experimentos

Estructura del proyecto de Olimpiadas:

## ✅ Hitos completados (paso a paso)
### 1) Copilot Chat funcionando
- Se activó Copilot Chat en VS Code y se aprendió a abrirlo.
- Se validó que Copilot usa contexto del archivo para sugerencias.

### 2) Base visual de periódico (frontend)
- Se creó una página HTML base.
- Se separó estilo en `styles.css`.
- Se construyó una cabecera tipo periódico (líneas + tipografía editorial).
- Se montó un layout en 2 columnas (izquierda: medallero / derecha: noticia).

### 3) Limpieza y control (evitar “basura”)
- Se detectó un problema típico: CSS pegado en `index.html` como texto visible.
- Se corrigió separando estrictamente:
  - HTML → estructura
  - CSS → estilo

---

## 🤖 Prompts probados (y qué ocurrió)

### Prompt A — “Mejora general de la portada”
**Objetivo:** que la IA haga una portada más avanzada manteniendo lo ya construido.

**Prompt (ejemplo):**
> tengo una página web estilo periódico antiguo con HTML y CSS.  
> quiero que la conviertas en una portada de periódico más avanzada sin cambiar la estructura general.  
> mejora distribución, bloques y jerarquía, pero no rehagas todo desde cero.

**Resultado observado:**
- La IA tiende a meter más contenido y reorganizar secciones.
- A veces rompe la estética “periódico” y se va a un layout moderno.

**Aprendizaje:**
- Si no se fuerza el estilo, la IA prioriza “estructura web moderna”.

---

### Prompt B — “Ten en cuenta Flourish (gráficos externos)”
**Objetivo:** que el diseño reserve espacios para gráficos que luego se embeben desde Flourish.

**Prompt (recomendado):**
> voy a integrar gráficos interactivos de Flourish más adelante (embed externo).  
> diseña la portada manteniendo estética de periódico antiguo y **reserva huecos** para gráficos dentro de la narrativa.  
> los huecos deben integrarse en las columnas como parte de la historia, no como secciones modernas separadas.

**Resultado observado:**
- La IA entiende la idea “habrá gráficos”, pero puede convertirlo en una web tipo “dashboard”.
- Se consiguen placeholders tipo “Aquí irá Flourish”, pero hay que vigilar que mantenga columnas/estilo.

**Aprendizaje:**
- Hay que indicar explícitamente: “mantén columnas y estética antigua”.

---

### Prompt C — “Reconducir cuando rompe el estilo”
**Objetivo:** corregir a Copilot cuando cambia el layout a web moderna.

**Prompt (recomendado):**
> el contenido está bien, pero has perdido el estilo de periódico antiguo.  
> mantén cabecera, tipografía clásica y estructura en columnas.  
> integra los gráficos como parte de la narrativa dentro de las columnas, no como secciones modernas.

**Aprendizaje:**
- Esto es “modo workshop”: IA propone → humano corrige dirección.

---

## 🧠 Problemas típicos detectados (y solución)
### Problema 1 — CSS aparece como texto en la página
**Síntoma:** se ve algo como `{ font-family: ... }` en el navegador.  
**Causa:** CSS pegado en `index.html`.  
**Solución:** moverlo a `styles.css` y dejar en `index.html` solo el `<link rel="stylesheet" ...>`.

### Problema 2 — Duplicidad de reglas CSS
**Síntoma:** dos bloques `h1 { ... }` con reglas diferentes.  
**Causa:** se fueron pegando mejoras sin limpiar.  
**Solución:** dejar un único `h1` final y borrar el duplicado.

### Problema 3 — “column-count” rompe listas/bloques cortos
**Síntoma:** el medallero se parte raro.  
**Causa:** `column-count` sirve para texto largo, no listas.  
**Solución:** no usar `column-count` en contenedores con listas; reservarlo (si acaso) para artículos largos.

---

## ✅ Conclusiones (lo más importante)
1) **La IA acelera, pero no diseña bien por defecto.**  
   Tiende a hacer “web moderna”, no “periódico antiguo”, si no se lo fuerzas.

2) **La clave es el control incremental (workshop real):**  
   - Cambios pequeños, comprobar, ajustar.  
   - Si se rompe estética, se corrige con prompt y/o rollback con Git.

3) **Separación estricta de responsabilidades (imprescindible):**  
   - `index.html` = estructura  
   - `styles.css` = estilo  
   - Flourish = contenido visual externo (embed)

4) **Para integrar Flourish sin que parezca pegote:**  
   El prompt debe pedir: “reserva huecos” + “integración narrativa en columnas”.

---

## 🧩 Próximos pasos (plan corto)
- Crear “placeholder” visual para Flourish (caja/slot) dentro de la columna derecha.
- Ajustar espaciado y jerarquía (titulares, secciones, separadores).
- Cuando haya embed real de Flourish: sustituir placeholder por el embed.
- Commit por hitos (diseño base, placeholders, integración Flourish, etc.).


# Prompts utilizados en el desarrollo

## 🎯 Objetivo

El objetivo de los prompts ha sido guiar la construcción progresiva de una experiencia visual tipo periódico, combinando diseño, estructura HTML y estilos CSS para lograr un resultado lo más realista posible.

Se ha seguido un enfoque iterativo, ajustando cada elemento paso a paso (estructura, tipografía, fondo, efectos visuales), priorizando la simplicidad y el control de los cambios.

---

## 🧠 Enfoque general

Se ha trabajado con prompts orientados a:

- Construcción progresiva (sin cambios masivos)
- Validación paso a paso
- Mejora incremental del diseño
- Separación clara de responsabilidades (HTML vs CSS)

Cada iteración ha buscado solucionar un único problema concreto, evitando introducir complejidad innecesaria.

---

## 🔧 Tipos de prompts utilizados

### 1. Estructura HTML

Prompts enfocados en definir la base del layout:

- Creación de cabecera de periódico
- Organización en columnas
- Separación de bloques de contenido
- Jerarquía de titulares y texto

Ejemplo:

> "Hazme una estructura tipo periódico con cabecera, titular y tres columnas, manteniendo HTML sencillo"

---

### 2. Estilos CSS (layout)

Prompts orientados a la distribución visual:

- Uso de grid para columnas
- Ajuste de márgenes y espacios
- Centrado del contenido
- Proporción tipo hoja vertical

Ejemplo:

> "Quiero que la página parezca una hoja de periódico, más alta que ancha y centrada"

---

### 3. Estilo visual (papel y realismo)

Prompts centrados en mejorar el aspecto:

- Fondo de papel envejecido
- Textura y suciedad
- Efecto de tinta imperfecta
- Separación entre fondo y hoja

Ejemplo:

> "Haz un efecto de papel envejecido con textura y traspaso sutil"

---

### 4. Debugging y ajustes

Prompts clave para corregir errores:

- Problemas de rutas de imágenes
- Conflictos en CSS
- Elementos que ocupaban toda la pantalla
- Ajuste del contenedor principal

Ejemplo:

> "No se ve la textura, revisa por qué el fondo ocupa toda la pantalla"

---

## ⚙️ Estrategia aplicada

Se ha seguido una estrategia basada en:

- Cambios controlados y aislados
- Validación visual tras cada paso
- Simplificación antes de añadir complejidad
- Identificación de problemas reales (no asumir errores)

Esto ha permitido mantener estabilidad en el diseño y evitar rupturas del layout.

---

## ✅ Resultado

Gracias a este enfoque de prompting:

- Se ha conseguido un diseño coherente tipo periódico
- Se ha implementado una hoja visual separada del fondo
- Se ha integrado una estética realista (papel + tinta)
- Se ha mantenido un código limpio y estructurado

---

## 🚀 Posibles mejoras en prompts

- Mayor reutilización de prompts tipo plantilla
- Definición de prompts más genéricos para layout
- Automatización de ajustes visuales repetitivos
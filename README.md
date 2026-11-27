# Aterriza 🧭

Guía web para estudiantes internacionales que llegan a España. Reúne trámites y tareas del día a día (empadronamiento, NIE, banco, salud, vivienda, universidad, cocina, presupuesto…) en guías paso a paso con buscador y progreso guardado en el navegador. No requiere registro.

## Requisitos

- Python 3.12 o superior
- Node.js 20.12 o superior
- Git

## Instalación paso a paso

**1. Clona el repositorio**

```bash
git clone https://github.com/Santiago21S/Aterriza.git
cd Aterriza
```

**2. Crea el entorno virtual e instala el backend**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

En Windows, crea el entorno con `py -m venv .venv` y actívalo con:

```powershell
.venv\Scripts\Activate.ps1
```

**3. Prepara la base de datos**

```bash
cd backend
python manage.py migrate
cd ..
```

**4. Instala el frontend**

```bash
cd frontend
npm install
cd ..
```

Si no tienes npm, puedes usar `yarn install`.

**5. Arranca el backend** (primera terminal, con el entorno virtual activado)

```bash
cd backend
python manage.py runserver
```

**6. Arranca el frontend** (segunda terminal)

```bash
cd frontend
npm run dev
```

**7. Abre la página**

Ve a **http://localhost:3000** en tu navegador.

## Atajo para Linux y macOS

Si prefieres hacerlo todo de una vez:

```bash
./scripts/setup.sh   # instala dependencias y prepara la base de datos
./scripts/dev.sh     # arranca backend y frontend juntos
```

Después abre **http://localhost:3000**.

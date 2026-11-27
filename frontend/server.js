import path from "node:path";
import { fileURLToPath } from "node:url";

import express from "express";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Carga opcional de frontend/.env (si no existe, se usan los valores por defecto).
try {
  process.loadEnvFile(path.join(__dirname, ".env"));
} catch {
  // El archivo .env es opcional.
}

const PORT = Number(process.env.PORT) || 3000;
const DJANGO_URL = process.env.DJANGO_URL || "http://127.0.0.1:8000";

const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

/**
 * Proxy hacia Django.
 *
 * El navegador solo habla con http://localhost:3000 y este servidor reenvía
 * todo lo que empieza por /api al backend de Django. Así se evitan problemas
 * de CORS y se puede desplegar cada parte por separado.
 */
app.use("/api", async (req, res) => {
  const target = `${DJANGO_URL}/api${req.url}`;

  const headers = {};
  for (const name of ["content-type", "authorization", "cookie"]) {
    if (req.headers[name]) {
      headers[name] = req.headers[name];
    }
  }

  const hasBody = !["GET", "HEAD"].includes(req.method);

  try {
    const response = await fetch(target, {
      method: req.method,
      headers,
      body: hasBody && req.body ? JSON.stringify(req.body) : undefined,
    });

    res.status(response.status);
    res.setHeader(
      "content-type",
      response.headers.get("content-type") || "application/json",
    );

    const setCookie = response.headers.get("set-cookie");
    if (setCookie) {
      res.setHeader("set-cookie", setCookie);
    }

    const body = await response.text();
    res.send(body);
  } catch (error) {
    console.error(`[proxy] No se pudo contactar con Django en ${target}:`, error.message);
    res.status(502).json({
      detail: "El backend de Django no responde. ¿Está arrancado en el puerto 8000?",
    });
  }
});

app.use((req, res) => {
  res.status(404).json({ detail: "Ruta no encontrada" });
});

app.listen(PORT, () => {
  console.log(`Aterriza lista en http://localhost:${PORT}`);
  console.log(`Proxy /api -> ${DJANGO_URL}/api`);
});

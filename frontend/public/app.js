const API_URL = "/api/guides/";
const STORAGE_KEY = "aterriza.progress.v1";
const DEFAULT_TITLE = "Aterriza · Tu guía para estudiar en España";

const homeView = document.querySelector("#home-view");
const guideView = document.querySelector("#guide-view");
const guidesGrid = document.querySelector("#guides-grid");
const noResults = document.querySelector("#no-results");
const listTitle = document.querySelector("#list-title");
const resultCount = document.querySelector("#result-count");
const categoriesEl = document.querySelector("#categories");
const searchInput = document.querySelector("#search");
const clearSearchButton = document.querySelector("#clear-search");
const clearFiltersButton = document.querySelector("#clear-filters");
const heroStats = document.querySelector("#hero-stats");
const progressText = document.querySelector("#progress-text");
const progressBar = document.querySelector("#progress-bar");
const progressTrack = document.querySelector("#progress-track");
const resetProgressButton = document.querySelector("#reset-progress");
const guideCardTemplate = document.querySelector("#guide-card-template");
const stepTemplate = document.querySelector("#step-template");

const detailEmoji = document.querySelector("#detail-emoji");
const detailCategory = document.querySelector("#detail-category");
const detailTitle = document.querySelector("#detail-title");
const detailSummary = document.querySelector("#detail-summary");
const stepsEl = document.querySelector("#steps");
const detailProgressText = document.querySelector("#detail-progress-text");
const detailProgressBar = document.querySelector("#detail-progress-bar");
const detailTrack = document.querySelector("#detail-track");
const resetGuideButton = document.querySelector("#reset-guide");
const officialLink = document.querySelector("#official-link");

let guides = [];
let currentGuide = null;
let progress = loadProgress();
let query = "";
let activeCategory = "Todas";

/* ------------------------------------------------------------------ Estado */

function normalize(text) {
  return text
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();
}

function loadProgress() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY));
    return stored && typeof stored === "object" ? stored : {};
  } catch {
    return {};
  }
}

function saveProgress() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch {
    // Si el navegador bloquea localStorage, la app sigue funcionando sin guardar.
  }
}

function doneIds(slug) {
  return new Set(progress[slug] || []);
}

function countDone(guide) {
  const ids = doneIds(guide.slug);
  return guide.steps.filter((step) => ids.has(step.id)).length;
}

function totals() {
  let total = 0;
  let done = 0;

  for (const guide of guides) {
    total += guide.steps.length;
    done += countDone(guide);
  }

  return { total, done };
}

function setStepDone(slug, stepId, done) {
  const ids = new Set(progress[slug] || []);

  if (done) {
    ids.add(stepId);
  } else {
    ids.delete(stepId);
  }

  if (ids.size > 0) {
    progress[slug] = [...ids];
  } else {
    delete progress[slug];
  }

  saveProgress();
}

/* -------------------------------------------------------------------- Home */

function updateHomeProgress() {
  const { total, done } = totals();
  const percent = total > 0 ? Math.round((done / total) * 100) : 0;

  progressBar.style.width = `${percent}%`;
  progressTrack.setAttribute("aria-valuenow", String(percent));
  progressTrack.setAttribute("aria-valuetext", `${done} de ${total} pasos`);
  progressText.textContent =
    done === 0
      ? "Todavía no has marcado ningún paso."
      : `Has completado ${done} de ${total} pasos (${percent} %).`;
  resetProgressButton.hidden = done === 0;
}

function buildCard(guide, index) {
  const node = guideCardTemplate.content.firstElementChild.cloneNode(true);
  const total = guide.steps.length;
  const done = countDone(guide);

  node.href = `#/guia/${guide.slug}`;
  node.classList.toggle("featured", guide.featured);
  node.style.animationDelay = `${Math.min(index, 8) * 25}ms`;

  node.querySelector(".card-emoji").textContent = guide.emoji;
  node.querySelector(".card-category").textContent = guide.category;
  node.querySelector(".card-title").textContent = guide.title;
  node.querySelector(".card-summary").textContent = guide.summary;
  node.querySelector(".card-steps").textContent = `${total} ${
    total === 1 ? "paso" : "pasos"
  }`;

  if (done > 0) {
    const doneEl = node.querySelector(".card-done");
    doneEl.classList.add("visible");
    doneEl.textContent =
      done === total ? "Completada ✓" : `${done}/${total} hechos`;
  }

  return node;
}

function renderGuides() {
  if (guides.length === 0) {
    return;
  }

  const normalizedQuery = normalize(query.trim());

  const filtered = guides.filter((guide) => {
    if (activeCategory !== "Todas" && guide.category !== activeCategory) {
      return false;
    }

    if (!normalizedQuery) {
      return true;
    }

    const haystack = normalize(
      [
        guide.title,
        guide.summary,
        guide.category,
        ...guide.steps.map((step) => `${step.title} ${step.description}`),
      ].join(" "),
    );

    return haystack.includes(normalizedQuery);
  });

  guidesGrid.replaceChildren(...filtered.map(buildCard));

  noResults.hidden = filtered.length > 0;
  resultCount.textContent = `${filtered.length} ${
    filtered.length === 1 ? "guía" : "guías"
  }`;
  listTitle.textContent =
    query.trim() || activeCategory !== "Todas"
      ? "Resultados"
      : "Todas las guías";
}

function updateChips() {
  for (const chip of categoriesEl.querySelectorAll(".chip")) {
    chip.setAttribute(
      "aria-pressed",
      String(chip.dataset.category === activeCategory),
    );
  }
}

function renderCategories() {
  const categories = [
    "Todas",
    ...new Set(guides.map((guide) => guide.category)),
  ];

  categoriesEl.replaceChildren(
    ...categories.map((category) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "chip";
      button.textContent = category;
      button.dataset.category = category;
      button.setAttribute("aria-pressed", String(category === activeCategory));

      button.addEventListener("click", () => {
        activeCategory = category;
        updateChips();
        renderGuides();
      });

      return button;
    }),
  );
}

function syncClearSearchButton() {
  clearSearchButton.hidden = searchInput.value.length === 0;
}

/* ------------------------------------------------------------------- Guía */

function buildStep(guide, step, index) {
  const node = stepTemplate.content.firstElementChild.cloneNode(true);
  const input = node.querySelector(".step-check");
  const isDone = doneIds(guide.slug).has(step.id);

  input.checked = isDone;
  input.setAttribute("aria-label", `Marcar como hecho: ${step.title}`);
  node.classList.toggle("done", isDone);

  node.querySelector(".step-num").textContent = `Paso ${index + 1}`;
  node.querySelector(".step-title").textContent = step.title;
  node.querySelector(".step-text").textContent = step.description;

  const tip = node.querySelector(".step-tip");
  if (step.tip) {
    tip.textContent = step.tip;
    tip.hidden = false;
  } else {
    tip.remove();
  }

  input.addEventListener("change", () => {
    setStepDone(guide.slug, step.id, input.checked);
    node.classList.toggle("done", input.checked);
    updateGuideProgress(guide);
    updateHomeProgress();
  });

  return node;
}

function updateGuideProgress(guide) {
  const total = guide.steps.length;
  const done = countDone(guide);
  const percent = total > 0 ? Math.round((done / total) * 100) : 0;

  detailProgressBar.style.width = `${percent}%`;
  detailTrack.setAttribute("aria-valuenow", String(percent));
  detailTrack.setAttribute("aria-valuetext", `${done} de ${total} pasos`);

  if (done === total && total > 0) {
    detailProgressText.textContent = `¡Guía completada! ${done} de ${total} pasos.`;
  } else {
    detailProgressText.textContent = `${done} de ${total} pasos completados`;
  }

  resetGuideButton.hidden = done === 0;
}

function renderGuide(slug) {
  const guide = guides.find((item) => item.slug === slug);

  if (!guide) {
    history.replaceState(null, "", "#/");
    showHome();
    return;
  }

  currentGuide = guide;
  homeView.hidden = true;
  guideView.hidden = false;
  document.title = `${guide.title} · Aterriza`;

  detailEmoji.textContent = guide.emoji;
  detailCategory.textContent = guide.category;
  detailTitle.textContent = guide.title;
  detailSummary.textContent = guide.summary;

  stepsEl.replaceChildren(
    ...guide.steps.map((step, index) => buildStep(guide, step, index)),
  );

  if (guide.official_url) {
    officialLink.href = guide.official_url;
    officialLink.textContent = `${
      guide.official_label || "Consultar la fuente oficial"
    } ↗`;
    officialLink.hidden = false;
  } else {
    officialLink.hidden = true;
    officialLink.removeAttribute("href");
  }

  updateGuideProgress(guide);
  window.scrollTo({ top: 0, behavior: "auto" });
}

function showHome() {
  currentGuide = null;
  guideView.hidden = true;
  homeView.hidden = false;
  document.title = DEFAULT_TITLE;

  updateHomeProgress();
  renderGuides();
  window.scrollTo({ top: 0, behavior: "auto" });
}

/* ------------------------------------------------------------------ Router */

function route() {
  const match = window.location.hash.match(/^#\/guia\/([\w-]+)\/?$/);

  if (match) {
    renderGuide(match[1]);
  } else {
    showHome();
  }
}

/* ----------------------------------------------------------------- Eventos */

searchInput.addEventListener("input", () => {
  query = searchInput.value;
  syncClearSearchButton();
  renderGuides();
});

clearSearchButton.addEventListener("click", () => {
  query = "";
  searchInput.value = "";
  syncClearSearchButton();
  renderGuides();
  searchInput.focus();
});

clearFiltersButton.addEventListener("click", () => {
  query = "";
  searchInput.value = "";
  activeCategory = "Todas";
  syncClearSearchButton();
  updateChips();
  renderGuides();
});

resetProgressButton.addEventListener("click", () => {
  const confirmed = window.confirm(
    "¿Seguro que quieres borrar todo tu progreso? Esta acción no se puede deshacer.",
  );

  if (!confirmed) {
    return;
  }

  progress = {};
  saveProgress();
  updateHomeProgress();
  renderGuides();
});

resetGuideButton.addEventListener("click", () => {
  if (!currentGuide) {
    return;
  }

  const confirmed = window.confirm(
    "¿Quieres borrar el progreso de esta guía?",
  );

  if (!confirmed) {
    return;
  }

  delete progress[currentGuide.slug];
  saveProgress();

  for (const input of stepsEl.querySelectorAll(".step-check")) {
    input.checked = false;
    input.closest(".step").classList.remove("done");
  }

  updateGuideProgress(currentGuide);
  updateHomeProgress();
});

window.addEventListener("hashchange", route);

/* --------------------------------------------------------------- Arranque */

function showLoading() {
  const loading = document.createElement("p");
  loading.className = "loading";
  loading.textContent = "Cargando guías…";
  guidesGrid.replaceChildren(loading);
}

function showLoadError() {
  const box = document.createElement("div");
  box.className = "error-box";

  const message = document.createElement("p");
  message.textContent =
    "No pudimos cargar las guías. Comprueba que el servidor de Django está arrancado en el puerto 8000.";

  const retry = document.createElement("button");
  retry.type = "button";
  retry.className = "button";
  retry.textContent = "Reintentar";
  retry.addEventListener("click", () => window.location.reload());

  box.append(message, retry);
  guidesGrid.replaceChildren(box);
  resultCount.textContent = "";
}

async function init() {
  showLoading();

  try {
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error(`Error ${response.status}`);
    }

    guides = await response.json();

    if (!Array.isArray(guides) || guides.length === 0) {
      throw new Error("La API no devolvió guías");
    }

    const totalSteps = guides.reduce(
      (sum, guide) => sum + guide.steps.length,
      0,
    );
    heroStats.textContent = `${guides.length} guías · ${totalSteps} pasos · Sin registro`;

    renderCategories();
    route();
  } catch (error) {
    console.error(error);
    showLoadError();
  }
}

init();

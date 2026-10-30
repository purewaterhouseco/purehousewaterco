// Mobile menu
const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
    toggle.textContent = open ? "✕" : "☰";
  });
}

// Lead forms: emailed to the address in data-email via FormSubmit (https://formsubmit.co).
// The first submission triggers a one-time activation email that must be confirmed.
document.querySelectorAll("form[data-lead-form]").forEach((form) => {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const button = form.querySelector("button[type=submit]");
    const ok = form.querySelector(".form-success");
    const err = form.querySelector(".form-error");
    const data = Object.fromEntries(new FormData(form));
    data["Page"] = window.location.href;
    data._template = "table";

    button.disabled = true;
    button.textContent = "Sending…";
    err.style.display = "none";
    try {
      const res = await fetch(`https://formsubmit.co/ajax/${form.dataset.email}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(data),
      });
      const json = await res.json().catch(() => ({}));
      if (!res.ok || String(json.success) === "false") throw new Error(json.message || res.status);
      ok.style.display = "block";
      form.querySelectorAll("input, select, textarea, button").forEach((el) => (el.disabled = true));
      button.textContent = "Sent ✓";
    } catch (error) {
      console.error("Form submission failed:", error);
      err.style.display = "block";
      button.disabled = false;
      button.textContent = "Try Again";
    }
  });
});

document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

// Hero video: play inline when the overlay is clicked.
document.querySelectorAll(".video-card").forEach((card) => {
  const video = card.querySelector("video");
  const overlay = card.querySelector(".video-overlay");
  if (!video || !overlay) return;
  overlay.addEventListener("click", () => {
    card.classList.add("playing");
    video.controls = true;
    video.play();
  });
});

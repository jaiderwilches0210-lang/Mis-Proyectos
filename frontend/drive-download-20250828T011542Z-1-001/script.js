// ===== Generar estrellitas en el loader =====
const fondo = document.getElementById("fondo");

for (let i = 0; i < 80; i++) {
  let star = document.createElement("div");
  star.classList.add("star");
  star.style.top = Math.random() * 100 + "%";
  star.style.left = Math.random() * 100 + "%";
  star.style.animationDuration = 1 + Math.random() * 2 + "s";
  fondo.appendChild(star);
}

// ===== Ocultar loader después de cargar =====
window.addEventListener("load", () => {
  setTimeout(() => {
    const loader = document.getElementById("loader");
    loader.style.transition = "opacity 1s ease";
    loader.style.opacity = "0";

    setTimeout(() => {
      loader.style.display = "none";
    }, 1000);
  }, 3000);
});

// ===== Scroll Reveal =====
const scrollElements = document.querySelectorAll(".scroll-reveal");

const elementInView = (el, offset = 100) => {
  const elementTop = el.getBoundingClientRect().top;
  return elementTop <= (window.innerHeight || document.documentElement.clientHeight) - offset;
};

const displayScrollElement = (element) => {
  element.classList.add("active");
};

const hideScrollElement = (element) => {
  element.classList.remove("active");
};

const handleScrollAnimation = () => {
  scrollElements.forEach((el) => {
    if (elementInView(el, 100)) {
      displayScrollElement(el);
    } else {
      hideScrollElement(el);
    }
  });
};

window.addEventListener("scroll", () => {
  handleScrollAnimation();
});

// ===== Ejecutar al cargar =====
handleScrollAnimation();

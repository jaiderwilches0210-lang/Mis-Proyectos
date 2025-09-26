// === POPUP CIERRE ===
document.getElementById("close-btn")?.addEventListener("click", () => {
  document.getElementById("popup").style.display = "none";
});

// === CARRITO (sigue en localStorage por ahora) ===
let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

function guardarCarrito() {
  localStorage.setItem("carrito", JSON.stringify(carrito));
}

function actualizarContador() {
  const contador = document.getElementById("contador-carrito");
  if (contador) contador.textContent = carrito.length;
}
actualizarContador();

// === FUNCIÓN PARA AGREGAR AL CARRITO ===
function agregarAlCarrito(boton) {
  const nombre = boton.getAttribute("data-producto");
  const precio = parseFloat(boton.getAttribute("data-precio"));
  const imagen = boton.getAttribute("data-imagen");

  carrito.push({ nombre, precio, imagen });
  guardarCarrito();
  actualizarContador();

  // Confirmación flotante
  const confirmacion = document.createElement("div");
  confirmacion.textContent = `${nombre} agregado al carrito ✅`;
  confirmacion.className = "confirmacion-carrito";
  document.body.appendChild(confirmacion);

  setTimeout(() => confirmacion.remove(), 2000);
}

// === ASIGNAR EVENTOS DESPUÉS DE CREAR LOS PRODUCTOS ===
function asignarEventosCarrito() {
  const botonesCarrito = document.querySelectorAll(".btn-carrito");
  botonesCarrito.forEach(boton => {
    boton.addEventListener("click", () => agregarAlCarrito(boton));
  });
}

// === CARGAR PRODUCTOS DESDE EL BACKEND ===
document.addEventListener("DOMContentLoaded", async () => {
  const contenedor = document.querySelector(".grid");

  try {
    const res = await fetch("http://localhost:8080/api/productos");
    if (!res.ok) throw new Error("Error al cargar productos");

    const productos = await res.json();

    productos.forEach(producto => {
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
        <div class="card-inner">
          <div class="card-front">
            <h3>${producto.nombre}</h3>
            <img src="${producto.imagen}" alt="${producto.nombre}">
          </div>
          <div class="card-back">
            <div class="meta">
              <span class="badge-soft">Producto disponible</span>
              <p>${producto.descripcion}</p>
              <p><strong>Precio: $${producto.precio}</strong></p>
            </div>
            <button class="btn-carrito"
              data-id="${producto.id}"
              data-producto="${producto.nombre}"
              data-precio="${producto.precio}"
              data-imagen="${producto.imagen}">
              <span class="icono">🛒</span> Agregar al carrito
            </button>
          </div>
        </div>
      `;
      contenedor.appendChild(card);
    });

    asignarEventosCarrito();

  } catch (error) {
    console.error("Error cargando productos:", error);
    contenedor.innerHTML = "<p>No se pudieron cargar los productos. 😢</p>";
  }
});

// === MOSTRAR CARRITO EN carrito.html ===
if (document.getElementById("lista-carrito")) {
  const listaCarrito = document.getElementById("lista-carrito");
  const totalElemento = document.getElementById("total");
  const btnVaciar = document.getElementById("vaciar-carrito");
  const btnpagar = document.getElementById("btn-pay");


  function renderizarCarrito() {
    listaCarrito.innerHTML = "";
    let total = 0;

    if (carrito.length === 0) {
      listaCarrito.innerHTML = "<p>Tu carrito está vacío 🛍</p>";
    } else {
      carrito.forEach((item, index) => {
        total += item.precio;

        const div = document.createElement("div");
        div.className = "item-carrito";
        div.innerHTML = `
          <img src="${item.imagen}" alt="${item.nombre}">
          <p><strong>${item.nombre}</strong> - $${item.precio}</p>
          <button data-index="${index}" class="eliminar">❌</button>
        `;
        listaCarrito.appendChild(div);
      });
    }

    totalElemento.textContent = `Total: $${total}`;
    guardarCarrito();
  }

  document.addEventListener("click", e => {
    if (e.target.classList.contains("eliminar")) {
      const i = e.target.getAttribute("data-index");
      carrito.splice(i, 1);
      renderizarCarrito();
      actualizarContador();
    }
  });

  btnVaciar.addEventListener("click", () => {
    carrito = [];
    renderizarCarrito();
    actualizarContador();
  });

btnpagar.addEventListener("click", async () => {
    if (carrito.length === 0) {
        alert("Tu carrito está vacío");
        return;
    }

    try {
        const res = await fetch("http://localhost:8080/api/ventas", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(carrito)
        });

        if (res.ok) {
            alert("Proceso de pago iniciado ✅");
            // Aquí puedes limpiar el carrito o redirigir al usuario
            carrito.length = 0; // Limpia el carrito
            localStorage.setItem("carrito", JSON.stringify(carrito));
            // Opcional: recarga la página o redirige
            window.location.reload();
        } else {
            const txt = await res.text();
            console.error('Error al procesar pago:', res.status, txt);
            alert("❌ Ocurrió un error al procesar el pago");
        }
    } catch (err) {
        console.error('Error de conexión:', err);
        alert('No se pudo conectar al servidor de pagos');
    }
});

  renderizarCarrito();
}

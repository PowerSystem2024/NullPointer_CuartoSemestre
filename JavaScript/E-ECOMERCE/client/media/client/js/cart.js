const modalContainer = document.getElementById("modal-container"); //contenedor del modal
const modalOverlay = document.getElementById("modal-overlay"); //overlay del modal

const carBtn = document.getElementById("cart-btn"); //boton del carrito

const displayCart = () => {
    modalContainer.innerHTML = ""; //limpia el contenido del modal
    modalContainer.style.display = "block"; //muestra el modal
    modalOverlay.style.display = "block"; //muestra el overlay

    //Modal Header
    const modalHeader = document.createElement("div"); //crea un div

    const modalClose = document.createElement("div"); //crea un div
    modalClose.innerText ="❌";
    modalClose.className = "modal-close"; //clase del div
    modalHeader.append(modalClose); //agrega el div al modalHeader

    modalClose.addEventListener("click", () =>  {
        modalContainer.style.display = "none"; //oculta el modal
        modalOverlay.style.display = "none"; //oculta el overlay
    });

    const modalTitle = document.createElement("div"); 
    modalTitle.innerText = "Carrito"; //titulo del modal
    modalTitle.className = "modal-title"; //clase del titulo
    modalHeader.append(modalTitle); //agrega el titulo al modalHeader

    modalContainer.append(modalHeader); //agrega el modalHeader al modalContainer


};

carBtn.addEventListener("click", displayCart); //evento al hacer click en el boton del carrito
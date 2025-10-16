const modalContainer = document.getElementById("modal-container"); //contenedor del modal
const modalOverlay = document.getElementById("modal-overlay"); //overlay del modal

const cartBtn = document.getElementById("cart-btn"); //boton del carrito
const cartCounter = document.getElementById("cart-counter"); //contador del carrito

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
    modalTitle.innerText = "Carrito de compras"; //titulo del modal
    modalTitle.className = "modal-title"; //clase del titulo
    modalHeader.append(modalTitle); //agrega el titulo al modalHeader

    modalContainer.append(modalHeader); //agrega el modalHeader al modalContainer

    //modal body
    if (cart.length > 0) {
        cart.forEach((products) => { //recorre el arreglo del carrito
        const modalBody = document.createElement("div"); //crea un div
        modalBody.className = "modal-body";
        modalBody.innerHTML= `
        <div class="products">
                <img class="products-img" src="${products.img}"/>
                <div class="products-info">
                    <h4>${products.productName}</h4>
                </div>
            <div class= "quantity">
                <span class="quantity-btn-decrese">-</span>
                <span class="quantity-input">${products.quanty}</span>
                <span class="quantity-btn-increse">+</span>
            </div>
                <div class="price">${products.price * products.quanty} $</div>
                <div class="delete-products">❌</div>
        </div>
        `;
        modalContainer.append(modalBody); //agrega el div al modalContainer , hace que se muestre en el modal

        //restando productos
        const decrese = modalBody.querySelector(".quantity-btn-decrese"); //selecciona el boton de la clase decrese
        decrese.addEventListener("click", () => { //escuche el evento click
            if(products.quanty !== 1){ //si la cantidad es diferente de 1
                products.quanty --; //disminuya la cantidad en uno
                displayCart(); //vuelva a ejecutar la funcion displayCart para que se actualice el carrito   
            }
            displayCartCounter();
        });

        //sumando productos
        const increse = modalBody.querySelector(".quantity-btn-increse"); //selecciona el boton de la clase increse
        increse.addEventListener("click", () => { //escuche el evento click
            products.quanty ++; //aumente la cantidad en uno
            displayCart(); //vuelva a ejecutar la funcion displayCart para que se actualice el carrito
            displayCartCounter();
        });

        // delete products
        const deleteProducts = modalBody.querySelector('.delete-products'); //selecciona el boton de la clase delete-products

        deleteProducts.addEventListener("click", () => { //escuche el evento click
            deleteCartProducts(products.id); 
        });

    });

    //modal footer
    const total =cart.reduce((acc, el) => acc + el.price * el.quanty, 0); //reduce el arreglo del carrito y suma el precio por la cantidad de cada producto, inicia en 0 

    const modalFooter = document.createElement("div"); //crea un div
    modalFooter.className = "modal-footer"; //clase del div
    modalFooter.innerHTML = `
    <div class= "total-price">Total a pagar 💸 es: ${total} </div>

    `;
    modalContainer.append(modalFooter); //agrega el div al modalContainer, y se muestra al final
    } else {
        const modalText = document.createElement("h2"); //crear un texto en el modal
        modalClose.className = "modal-body";
        modalText.innerText = "Tu carrito 🛒 esta vacio :("; //texto del modal
        modalContainer.append(modalText); //agrega el texto al modalContainer
    }
};

cartBtn.addEventListener("click", displayCart); //evento al hacer click en el boton del carrito y se ejecuta la funcion displayCart

const deleteCartProducts = (id) => {
    const foundId = cart.findIndex((element) => element.id === id); //busca el id del producto
    cart.splice(foundId, 1); //elimina el producto del carrito
    displayCart(); //vuelve a ejecutar la funcion displayCart para que se actualice el carrito
    displayCartCounter(); //vuelve a ejecutar la funcion displayCartCounter para que se actualice el contador del carrito
}

const displayCartCounter = () => {
    const cartLength =cart.reduce((acc, el) => acc + el.quanty, 0); //hace que el contador del carrito sume la cantidad de productos en el carrito
    if (cartLength > 0) {
        cartCounter.style.display = "block"; //muestra el contador
            cartCounter.innerText = cartLength; //muestra la cantidad de productos en el carrito
    }else {
        cartCounter.style.display = "none"; //sino oculta el contador en 0
    }
};
const shopContent = document.getElementById("shopContent"); //donde se van a mostrar los productos
const cart=[]; //Este es nuestro carrito de compras, un array vacio


productos.forEach((products)=> { //recorre el arreglo de productos
    const content = document.createElement("div"); //crea un div
    content.className = "card"; //clase del div
    content.innerHTML = `
    <img src="${products.img}"/>
    <h3>${products.productName}</h3>
    <p class="price">${products.price} $</p> 
    `; //contenido dinamico
    shopContent.append(content);

    const buyButton= document.createElement("button"); //crea un boton
    buyButton.innerText = "Comprar"; //texto del boton
   
    content.append(buyButton); //agrega el boton al div

    buyButton.addEventListener("click", () => { //evento al hacer click en el boton
        const repeat = cart.some((repeatProducts) => repeatProducts.id === products.id); //esto hace que no se repitan los productos en el carrito

        if (repeat) {
            cart.map((prod) => { //recorre el carrito y detecta
                if (prod.id === products.id) {//si el id del producto es igual al id del producto que se esta comprando o agregando 
                prod.quanty++; //aumenta la cantidad en uno mas
                }
            });
        }else {
            cart.push({
            id: products.id, //id del producto
            productName: products.productName, //nombre del producto
            price: products.price, //precio del producto
            quanty: products.quanty, //cantidad del producto
            img: products.img, //imagen del producto
            });
        }
    });

});
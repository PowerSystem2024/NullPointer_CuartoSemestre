const shopContent = document.getElementById("shopContent"); //donde se van a mostrar los productos
const cart=[]; //Este es nuestro carrito de compras, un array vacio


productos.forEach((products)=> { //recorre el arreglo de productos
    const content = document.createElement("div"); //crea un div
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
        cart.push({
            id: products.id, //id del producto
            productName: products.productName, //nombre del producto
            price: products.price, //precio del producto
            quanty: products.quanty, //cantidad del producto
            img: products.img, //imagen del producto
        })
        console.log(cart); //muestra el carrito en la consola
    })

});
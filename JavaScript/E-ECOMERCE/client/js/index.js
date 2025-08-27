const shopContent = document.getElementById("shopContent"); //donde se van a mostrar los productos

productos.forEach((products)=> { //recorre el arreglo de productos
    const content = document.createElement("div"); //crea un div
    content.innerHTML = `
        <img src="${products.img}/>
        <h3>${products.productName}</h3>
        <p>${products.price} $</p>
    `; //contenido dinamico
    shopContent.append(content);
});

console.log("Productos cargados:", productos);
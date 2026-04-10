async function loadProducts() {
    const response = await fetch('api/v1/products');
    const products = await response.json();

    const container = document.getElementById('products');
    container.innerHTML = '';

    products.forEach(product => {
        const div = document.createElement('div');
        div.innerHTML = `
            <h3>${product.name}</h3>
            <p>Category: ${product.category}</p>
            <p>Price: $${product.price}</p>
            <hr>
        `;
        container.appendChild(div);
    });
}

loadProducts();

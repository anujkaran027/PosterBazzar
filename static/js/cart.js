// Global cart functionality
document.addEventListener('DOMContentLoaded', function() {
    // Update cart count on page load
    updateCartCount();
});

function updateCartCount() {
    fetch('/cart/count/')
    .then(response => response.json())
    .then(data => {
        // Update cart count in navbar
        const cartCountElements = document.querySelectorAll('.cart-count');
        cartCountElements.forEach(element => {
            element.textContent = data.count;
        });
    })
    .catch(error => {
        console.error('Error updating cart count:', error);
    });
}

function addToCartAjax(productId, quantity = 1) {
    return fetch(`/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: `quantity=${quantity}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            updateCartCount();
        }
        return data;
    })
    .catch(error => {
        console.error('Error adding to cart:', error);
        return { success: false, message: 'Error adding item to cart' };
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toggleMethod(method) {
    var onlineButton = document.getElementById('Online');
    var offlineButton = document.getElementById('Offline');

    if (method === 'Online') {
        onlineButton.classList.add('active');
        onlineButton.classList.remove('inactive');
        offlineButton.classList.add('inactive');
        offlineButton.classList.remove('active');
    } else if (method === 'Offline') {
        onlineButton.classList.add('inactive');
        onlineButton.classList.remove('active');
        offlineButton.classList.add('active');
        offlineButton.classList.remove('inactive');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    applyFiltersFromURL();
});

function applyFiltersFromURL() {
    var urlParams = new URLSearchParams(window.location.search);
    var method = urlParams.get('method');
    var term = urlParams.get('term');
    var interest = urlParams.get('interest');

    if (method) {
        var methodButtons = document.querySelectorAll('.method-button');
        methodButtons.forEach(function(button) {
            if (button.id === method) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });
    }

    if (term) {
        document.getElementById('term-unit').value = term;
    };
    
    if (interest) {
        document.getElementById('interest-unit').value = interest;
    }
}

function applyFilters() {
    var method = document.querySelector('.method-button.active').id;
    var term = document.getElementById('term-unit').value;
    var interest = document.getElementById('interest-unit')

    var url = '/invest/?method=' + method + '&term=' + term + '&interest=' + interest;

    // Переадресация на новую страницу
    window.location.href = url;
}

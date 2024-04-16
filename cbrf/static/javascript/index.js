function formatDate(date) {
    var dd = String(date.getDate()).padStart(2, '0');
    var mm = String(date.getMonth() + 1).padStart(2, '0');
    var yyyy = date.getFullYear();
    return dd + '.' + mm + '.' + yyyy;
}

window.onload = function currencyDate() {
    var today = new Date();

    var yesterday = new Date(today);
    yesterday.setDate(today.getDate() - 1);

    var formattedToday = formatDate(today);
    var formattedYesterday = formatDate(yesterday);

    document.getElementById('yesterday').textContent = formattedYesterday;
    document.getElementById('today').textContent = formattedToday;
}

document.addEventListener("DOMContentLoaded", function() {
    var newsItems = document.querySelectorAll('.news-item');

    newsItems.forEach(function(newsItem) {
        var shortText = newsItem.querySelector('.short-text');
        var fullText = newsItem.querySelector('.full-text');
        var hideBtn = newsItem.querySelector('.hide-btn');

        shortText.addEventListener('click', function() {
            shortText.style.display = 'none';
            fullText.style.display = 'inline';
            hideBtn.style.display = 'inline';
        });

        hideBtn.addEventListener('click', function() {
            shortText.style.display = 'inline';
            fullText.style.display = 'none';
            hideBtn.style.display = 'none';
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var arrowIcons = document.querySelectorAll(".faq-item .question i");

    arrowIcons.forEach(function(arrowIcon) {
        arrowIcon.addEventListener("click", function() {
            var question = this.parentElement;
            var answer = question.nextElementSibling;
            answer.classList.toggle("show");
        });
    });
});

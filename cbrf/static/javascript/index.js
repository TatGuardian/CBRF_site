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

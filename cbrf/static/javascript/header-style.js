function toggleDropdown(id) {
    var dropdownContent = document.getElementById(id);
    var overlay = document.getElementById("overlay");

    // Toggle the visibility of the dropdown content
    if (dropdownContent.style.display === "grid") {
        dropdownContent.style.display = "none";
        overlay.style.display = "none";
    } else {
        // Hide all other dropdowns before showing this one
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            dropdowns[i].style.display = "none";
        }
        // Show the clicked dropdown
        dropdownContent.style.display = "grid";
        overlay.style.display = "grid";
    }
}

document.addEventListener("click", function(event) {
    // Получаем элемент, на котором произошел клик
    var targetElement = event.target;
    // Проверяем, является ли кликнутый элемент кнопкой выпадающего списка
    var isDropdownButton = targetElement.classList.contains("dropbtn");
    // Если кликнутый элемент не является кнопкой выпадающего списка, скрываем все выпадающие списки
    if (!isDropdownButton) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var overlay = document.getElementById("overlay");
        for (var i = 0; i < dropdowns.length; i++) {
            dropdowns[i].classList.remove("show");
        }
        overlay.style.display = "none";
    }
})

document.addEventListener("DOMContentLoaded", function() {
    var currentDateElement = document.getElementById("currentDate");
    
    // Функция для обновления времени
    function updateCurrentTime() {
        var currentDate = new Date();
        
        // Устанавливаем часовой пояс Москвы (+3 часа относительно UTC)
        currentDate.setUTCHours(currentDate.getUTCHours() + 3);
        
        var daysOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
        var months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
        
        var dayOfWeek = daysOfWeek[currentDate.getUTCDay()];
        var dayOfMonth = currentDate.getUTCDate();
        var month = months[currentDate.getUTCMonth()];
        var year = currentDate.getUTCFullYear();
        
        var hours = currentDate.getUTCHours();
        var minutes = currentDate.getUTCMinutes();
        
        // Добавляем ведущие нули к минутам, если они меньше 10
        minutes = (minutes < 10 ? '0' : '') + minutes;
        
        var currentTimeString = dayOfWeek + ', ' + dayOfMonth + ' ' + month + ' ' + year + ' '  + hours + ':' + minutes + ' (мск)';
        
        currentDateElement.textContent = currentTimeString;
    }
    
    // Вызываем функцию обновления времени сразу после загрузки страницы
    updateCurrentTime();
    
    // Обновляем время каждую минуту
    setInterval(updateCurrentTime, 20000);  // 60000 миллисекунд = 1 минута
});





function getInputValue(){
    // Выбор элемента input и получение его значения
    var inputVal = document.getElementById("search_input").value;
    var arrayOfStrings = window.location.href.split('/');
    if (inputVal == '') {
        window.location.href = arrayOfStrings.slice(0, 5).join('/');
    } else if (arrayOfStrings.length == 4) {
        window.location.href = arrayOfStrings.slice(0, 5).join('/') + 'universities/perm/' + inputVal;
    } else if (arrayOfStrings.length == 5) {
        window.location.href = window.location.href + '/' + inputVal;
    } else {
        window.location.href = arrayOfStrings.slice(0, 5).join('/') + '/' + inputVal;
    }
}
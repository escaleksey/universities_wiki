function change_theme() {
    var checkbox = document.getElementById("color_theme");
    if (checkbox.checked) {
        $('#theme_icon').attr('src', '/static/img/icons/dark_theme.png');
        
    }
    else {
        $('#theme_icon').attr('src', '/static/img/icons/light_theme.png');
    }

}

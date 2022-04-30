 /*function change_theme() {
    var checkbox = document.getElementById("color_theme");
    if (checkbox.checked) {
        $('#theme_icon').attr('src', '/static/img/icons/dark_theme.png');

    }
    else {
        $('#theme_icon').attr('src', '/static/img/icons/light_theme.png');
    }

}
*/
var btn = document.getElementById("theme-button");
var link = document.getElementById("theme-link");

btn.addEventListener("click", function () { ChangeTheme(); });

function ChangeTheme()
    var theme = "";
    let lightTheme = "styles/light.css";
    let darkTheme = "styles/dark.css";
    var checkbox = document.getElementById("color_theme");
    if (checkbox.checked) {
        $('#theme_icon').attr('src', '/static/img/icons/dark_theme.png');
        currTheme = darkTheme;
   	    theme = "dark_theme"
    }
    else {
        $('#theme_icon').attr('src', '/static/img/icons/light_theme.png');
        theme = "color_theme"

    Save(theme);
}
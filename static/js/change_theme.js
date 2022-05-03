function change_theme() {
    
    console.log(localStorage.getItem('theme'));
    if (localStorage.getItem('theme') == 'light') {
        localStorage.setItem('theme', 'dark');
        $('#theme_icon').attr('src', '/static/img/icons/dark_theme.png');
        $('.header').css('background-color', 'var(--dark_header_color)');
        $('.footer').css('background-color', 'var(--dark_header_color)');
        $('.nav-link').css('color', 'var(--dark_link_color)');
        $('.footer_content').css('color', 'var(--dark_text_color)');
        $('.body').css('background-color', 'var(--dark_body_color)');
        $('.index_content').css('color', 'var(--dark_text_color)');
        $('.universities_content').css('color', 'var(--dark_text_color)');
        $('.text_content').css('color', 'var(--dark_text_color)');
        $('.cities_menu').css('background-color', 'var(--dark_body_color)');
        $('.cities_menu').css('color', 'var(--dark_text_color)');
        $('.faculties_item').css('color', 'var(--dark_text_color)');
        $('.profile_content').css('color', 'var(--dark_text_color)');


        
    }
    else {
        localStorage.setItem('theme', 'light');
        $('#theme_icon').attr('src', '/static/img/icons/light_theme.png');
        $('.header').css('background-color', 'var(--light_header_color)');
        $('.footer').css('background-color', 'var(--light_header_color)');
        $('.nav-link').css('color', 'var(--light_link_color)');
        $('.footer_content').css('color', 'var(--light_text_color)');
        $('.body').css('background-color', 'var(--light_body_color)');
        $('.index_content').css('color', 'var(--light_text_color)');
        $('.universities_content').css('color', 'var(--light_text_color)');
        $('.text_content').css('color', 'var(--light_text_color)');
        $('.cities_menu').css('background-color', 'var(--light_body_color)');
        $('.cities_menu').css('color', 'var(--light_text_color)');
        $('.faculties_item').css('color', 'var(--light_text_color)');
        $('.profile_content').css('color', 'var(--light_text_color)');
    }

}

if (localStorage.getItem('theme') == null) {
    localStorage.setItem('theme', 'light');
    console.log('ch')
}


function update_change_theme() {
    
    console.log(localStorage.getItem('theme'));
    if (localStorage.getItem('theme') == 'dark') {
        $('#theme_icon').attr('src', '/static/img/icons/dark_theme.png');
        $('.header').css('background-color', 'var(--dark_header_color)');
        $('.footer').css('background-color', 'var(--dark_header_color)');
        $('.nav-link').css('color', 'var(--dark_link_color)');
        $('.footer_content').css('color', 'var(--dark_text_color)');
        $('.body').css('background-color', 'var(--dark_body_color)');
        $('.index_content').css('color', 'var(--dark_text_color)');
        $('.universities_content').css('color', 'var(--dark_text_color)');
        $('.text_content').css('color', 'var(--dark_text_color)');
        $('.cities_menu').css('background-color', 'var(--dark_body_color)');
        $('.cities_menu').css('color', 'var(--dark_text_color)');
        $('.faculties_item').css('color', 'var(--dark_text_color)');
        $('.profile_content').css('color', 'var(--dark_text_color)');


        
    }
    else {
        $('#theme_icon').attr('src', '/static/img/icons/light_theme.png');
        $('.header').css('background-color', 'var(--light_header_color)');
        $('.footer').css('background-color', 'var(--light_header_color)');
        $('.nav-link').css('color', 'var(--light_link_color)');
        $('.footer_content').css('color', 'var(--light_text_color)');
        $('.body').css('background-color', 'var(--light_body_color)');
        $('.index_content').css('color', 'var(--light_text_color)');
        $('.universities_content').css('color', 'var(--light_text_color)');
        $('.text_content').css('color', 'var(--light_text_color)');
        $('.cities_menu').css('background-color', 'var(--light_body_color)');
        $('.cities_menu').css('color', 'var(--light_text_color)');
        $('.faculties_item').css('color', 'var(--light_text_color)');
        $('.profile_content').css('color', 'var(--light_text_color)');
    }

}
update_change_theme();


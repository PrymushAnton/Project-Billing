function register_html() {
    $('.have_or_not_account').append(
        `<p>Є акаунт?</p>
        <button class="have_account" onclick="have_account()">Ввійти</button>`
    )
    $('.form_div').append(
        `<p>Логін</p>
        <input type="text" name="login" id="login">
        <p>Ім'я</p>
        <input type="text" name="first_name" id="first_name">
        <p>Прізвище</p>
        <input type="text" name="last_name" id="last_name">
        <p>Пароль</p>
        <input type="password" name="password" id="password">
        <p>Пошта</p>
        <input type="text" name="email" id="email">
        <input type="hidden" name='register_id' id="register_id" value="1">
        <button onclick="make_new_account()">Зареєструватись</button>`
    )
}

$(document).ready(function() {
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'GET',
        success: register_html()
    })
})

function html_login() {
    $('.have_or_not_account').empty()
    $('.have_or_not_account').append(
        `<p>Немає акаунту?</p>
        <button class="create_account" onclick='create_account()'>Створити</button>`
    )
    $('.form_div').empty()
    $('.form_div').append(
        `<p>Логін</p>
        <input type="text" name="login_log" id='login_log'>
        <p>Пароль</p>
        <input type="password" name="password_log" id='password_log'>
        <p>Пошта</p>
        <input type="text" name="email_log" id='email_log'>
        <input type="hidden" name='log_id' id="log_id" value="1">
        <button onclick="log_into_account()">Ввійти в акаунт</button>`
    )
}

function have_account(){
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'GET',
        success: html_login()
    })
}



function create_account(){
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'GET',
        success: function(){
            $('.have_or_not_account').empty()
            $('.form_div').empty()
            register_html()
        }
    })
}

function make_new_account() {
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            login: $('#login').val(),
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            password: $('#password').val(),
            email: $("#email").val(),
            register_id: $('#register_id').val(),
        },
        success: html_login()
    })
}

function log_into_account(){
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            login: $('#login').val(),
            password: $('#password').val(),
            email: $("#email_log").val(),
            log_id: $('#log_id').val(),
        },
        success: function(){
            console.log(1)
        }

    })
}
$(document).ready(function() {
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'GET',
        success: function(){
            $('main').append(
                `<p>Є акаунт?</p>
                <button class="have_account" onclick="have_account()">Ввійти</button>
                
                <form action="" method="POST" class="form">
                    <p>Логін</p>
                    <input type="text" name="login">
                    <p>Ім'я</p>
                    <input type="text" name="first_name">
                    <p>Прізвище</p>
                    <input type="text" name="last_name">
                    <p>Пароль</p>
                    <input type="password" name="password">
                    <p>Пошта</p>
                    <input type="text" name="email">
                    <button>Зареєструватись</button>
                </form>`
            )
        }
    })
})


function have_account(){
    console.log(2)
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'GET',
        success: function(){
            $('main').empty()
            $('main').append(
                `<p>Немає акаунту?</p>
                <button class="create_account" onclick='create_account()'>Створити</button>

                <form action="" method="POST" class="form">
                    <p>Логін</p>
                    <input type="text" name="login">
                    <p>Пароль</p>
                    <input type="password" name="password">
                    <p>Пошта</p>
                    <input type="text" name="email">
                    <button>Ввійти в акаунт</button>
                </form>`
                
            )
        }
    })
}


function create_account(){
    console.log(1)
    $.ajax({
        url: '/adding_new_tenant/',
        type: 'GET',
        success: function(){
            $('main').empty()
            $('main').append(
                `<p>Є акаунт?</p>
                <button class="have_account" onclick="have_account()">Ввійти</button>
                
                <form action="" method="POST" class="form">
                    <p>Логін</p>
                    <input type="text" name="login">
                    <p>Ім'я</p>
                    <input type="text" name="first_name">
                    <p>Прізвище</p>
                    <input type="text" name="last_name">
                    <p>Пароль</p>
                    <input type="password" name="password">
                    <p>Пошта</p>
                    <input type="text" name="email">
                    <button>Зареєструватись</button>
                </form>`
            )
        }
    })
}
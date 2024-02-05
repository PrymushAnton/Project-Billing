$(document).ready(function() {
    $('button#theme').click(function(){
        if ($('button#theme').hasClass('login')){
            $('button#theme').removeClass('login').addClass('registr')
            $('button#theme').html('Ввійти в акаунт')
            $("input[name='csrfmiddlewaretoken'").after(
                `<label for='first_name' id='first_name'>Ім'я</label>
                <input type="text" name="first_name" id="first_name">
                <label for='last_name' id="last_name">Прізвище</label>
                <input type="text" name="last_name" id="last_name">`
            )
            $(`input[value='login'`).val('registr')
        }
        else if ($('button#theme').hasClass('registr')){
            $('button#theme').removeClass('registr').addClass('login')
            $('button#theme').html('Створити акаунт')
            $(`input[value='registr'`).val('login')
            $(`*#last_name`).remove()
            $(`*#first_name`).remove()
        }
        $(`.error`).empty()
    })
    $('button.submit').click(function(){
        let form = $("form")
        $.ajax({
            url: "",
            type: "POST",
            data: form.serialize(),
            success: function (response){
                $(`.error`).empty()
                if(response.error == 'succ'){
                    window.location.replace('/main/')
                }
                else{
                    $(`.error`).append(`
                    <h2>${response.error}</h2>
                    `)
                }
            }
        })
    })
})

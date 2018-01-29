
$('document').ready(function () {

});

function loading(ennable) {
    if (ennable) {
        $('#loader').removeClass('hidden');
        $('#input').attr('disabled', "");
        $('#submit').prop('disabled', true);
    } else {
        $('#loader').addClass('hidden');
        $('#input').removeAttr('disabled');
        $('#submit').prop('disabled', false);
    }
}

function sendRequest(request) {
    loading(true);
    $('#input').val('');
    $.ajax({
        method: "GET",
        url: "./api/api-name",
        contentType: "application/text",
        data: { "request": request }
    })
        .done(function (response) {
            doSomething(response);
            loading(false);
        });
}

$('#input').keydown(function (e) {
    var data = $('#input').val();
    if (e.which == 13 && data.length > 0) { //catch Enter key
        sendRequest(data);
    }
});

$('#submit').click(function (e) {
    var data = $('#input').val();
    if (data.length > 0) {
        sendRequest(data);
    }
});
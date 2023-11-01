$(document).ready(function () {
  function sayHello () {
    const input = $('INPUT#language_code').val();
    if (input) {
      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + input,
        success: function (data) { $('DIV#hello').html(data.hello); }
      });
    }
  }
  $('INPUT#btn_translate').click(sayHello);
  $('INPUT#language_code').keypress(function (key) {
    if (key.which === 13) { sayHello(); }
  });
});

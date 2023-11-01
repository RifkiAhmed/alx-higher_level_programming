$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const input = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + input,
      success: function (data) { $('DIV#hello').html(data.hello); }
    });
  });
});

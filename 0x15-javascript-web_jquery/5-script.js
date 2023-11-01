$('DIV#add_item').click(function () {
  const list = $('UL.my_list');
  list.append('<li>Item</li>');
});

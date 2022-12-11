var $lists = $('ul.my_list');
$('DIV#add_item').on('click',(function () {
    $lists.append('<li>Item</li>');
}));

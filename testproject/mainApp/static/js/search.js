$('#search-form').submit(function(e) {
    $.post('/search/', $(this).serialize(), function(data) {
        $('.poscasts').html(data);
    });
    e.preventDefault();
});
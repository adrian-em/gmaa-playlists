
$(document).ready(function() {
    $('#btnaddplaylist').click(function () {
        $('#modalForm').modal('toggle');
    });

    $('#btnplaylistform').click(function () {
        $('#playlistform').submit();
    });

    $('.favorite').click(function () {
        var p_id = $(this).attr('data-id');
        var ele = $(this);
        if (ele.attr('class').search('empty') > 0) {
            $.post('/favorite/add/' + p_id, function (data) {
            }).success(function (data) {

                    ele.removeClass('glyphicon-star-empty');
                    ele.addClass('glyphicon-star')

                });
        } else {
            $.post('/favorite/remove/' + p_id, function (data) {

            }).success(function (data) {
                    ele.removeClass('glyphicon-star');
                    ele.addClass('glyphicon-star-empty')
                });
        }
    });

    $('.remove').click(function () {
        console.log("REMOVE");
        var p_id = $(this).attr('data-id');
        var ele = $(this);
        console.log(ele);
        $.post('/delete/playlist/' + p_id, function (data) {

        }).success(function (data) {
//                ele.parentElement.parentElement.remove();
                  ele.parent().parent().fadeOut('slow');
            });
    });

    $('.helptext').hide();

    $('#btnfilter').click(function (e) {
        e.preventDefault();
        $.post('/filter/', $('#filterform').serialize(), function (data) {
        }).success(function (data) {
                document.getElementById('results').innerHTML = data;
            })
    });



});
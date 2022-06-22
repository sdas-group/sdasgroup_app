/*jshint strict:true, browser:true, jquery:true */
$(function() {
    $('textarea').redactor({
        minHeight: 300,
        lang: 'es',
        deniedTags: ['html', 'head', 'link', 'body', 'meta', 'script', 'applet'],
        convertDivs: false,
        plugins: ['imagemanager', 'alignment']
    });

    $('#id_service_type').on('change', function () {
        var value = $(this).val();

        if (value == 310 || value == 320) {
            $('#serviceitem_set-group').hide();
        } else {
            $('#serviceitem_set-group').show();
        }
    });
});

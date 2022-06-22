$(function() {
    'use strict';

    jQuery.validator.addMethod("valid_password", function(value, element) {
        return this.optional(element) || /^(?=.*\d)(?!.*\s)(?=.*[a-zA-Z]).{8,}$/.test(value);
    }, "La contraseña debe tener al menos una letra y un número. Los caracteres no pueden ser todos iguales");

    $.datetimepicker.setLocale('es');

    var setMainNavigation = function() {
        // Get url path.
        var path = window.location.pathname;
        path = path.replace(/\/$/, "");
        path = decodeURIComponent(path);

        // Add active class to menu item.
        $('.CIMainNAVnav a').each(function () {
            // Remove last slash from href.
            var href = $(this).attr('href');
            href = href.substring(0, href.length - 1);

            if (path.substring(0, href.length) === href) {
                $(this).closest('li').addClass('active');
            }
        });
    };

    setMainNavigation();

    var setUserNavigation = function() {
        // Get url path.
        var path = window.location.pathname;
        path = path.replace(/\/$/, "");
        path = decodeURIComponent(path);

        // Add active class to menu item.
        $('.user_menu a').each(function () {
            // Remove last slash from href.
            var href = $(this).attr('href');
            href = href.substring(0, href.length - 1);

            if (path.substring(0, href.length) === href) {
                $(this).closest('li').addClass('active');
            }
        });
    };

    // Activate current navigation menu item.
    setUserNavigation();
});

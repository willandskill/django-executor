$(document).ready(function () {

    $('.btn-run-command').click(function (e) {
        var button = $(this);

        var commandName = button.attr('data-command-name');
        var appName = button.attr('data-app-name');
        var argvRaw = $(".input-argv-raw[data-app-name='" + appName + "'][data-command-name='" + commandName + "']").val();
        var responseElement = $('#std-response');

        var activeButtons = $('.btn-run-command[data-success-btn="True"]');
        activeButtons.attr('disabled', true);

        button.addClass('btn-run-command-active');

        var data = {
            appName: appName,
            commandName: commandName,
            argvRaw: argvRaw
        };

        var resetStates = function () {
            activeButtons.removeAttr('disabled');
            button.removeClass('btn-run-command-active');
        };

        var displayResponse = function (success, response) {
            var separator = response.stdout && response.stderr ? '\n' : '';
            var value = response.stdout + separator + response.stderr;

            if (!response.stdout && !response.stderr) {
                value = '<span style="color: yellow;">Management command didn\'t output anything.</span>'
            }

            responseElement.html(value);
            responseElement.fadeIn();
            $('body').scrollTop(responseElement.offset().top - 10)
        };

        $.ajax({
            type: "POST",
            url: "run-management-command/",
            data: data,
            success: function (response) {
                resetStates();
                displayResponse(true, response);
            },
            error: function (response) {
                resetStates();
                displayResponse(false, response.responseJSON);
            }
        });

    })
});
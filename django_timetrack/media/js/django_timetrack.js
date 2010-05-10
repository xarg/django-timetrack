$(document).ready(function(){
    var input_obj = $('#submit-input-line input')
    var default_input_value = input_obj.val()
    
    input_obj.focus(function(){
        if ($(this).val() == default_input_value){
            $(this).val('')
            $(this).addClass('active')
        }
    }).blur(function(){
        if ($(this).val() == ''){
            $(this).val(default_input_value)
            $(this).removeClass('active')
        }
    })
    
    input_obj.commandline({
        'url': SUBMIT_URL,
        'commands': [
            [/^add .+(?: with )?(.*)/i, [
                [SUGGEST_URL + 'Tag?q=\1']
            ]],
            [/^show (.*)(?: from )?(?: in )?(.*)/, [
                [SUGGEST_URL + 'Project?q=\1'],
                [SUGGEST_URL + 'Tag?p=\1&q=\2']
            ]],
            [/^.+ on (.+) in (.+)/, [
                [SUGGEST_URL + 'Project?q=\1'],
                [SUGGEST_URL + 'Tag?p=\1&q=\2']
            ]],
            [/^export (\w+)/, [
                'pdf', 'csv'
            ]]
        ],
        'complete': function(data){
            console.log(this);
        }
    })
    
    // Toggle documentation
    $('#documentation-toggle').click(function(){
        $('#documentation').toggle();
        $(this).hide()
    })
    $('#documentation-close').click(function(){
        $('#documentation').hide();
        $('#documentation-toggle').show()
    })
})

/**
 * Reload timesheet
*/
function reload(){
    
}

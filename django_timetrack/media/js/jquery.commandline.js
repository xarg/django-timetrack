(function($){
    $.fn.extend({
 		commandline: function(options) {
    		if (options){
				var obj = this
				url = options['url']
				commands = options['commands']
				this.keyup(function(key){
					if (key.keyCode == 13){ // Go command
						$.get(url + obj.val(), options['complete']);
					}
				})
            }
            /**
            * Fetch results
            */
            function getJSON(url){
                this.addClass('cmd-loading')
                $.getJSON(url, function(data){
                    this.removeClass('cmd-loading')
                    return data;
                })
            }
            /**
             * Create a div and display results
            */
            function display(data){
                console.log(data);
            }
    	}
	});	
})(jQuery);
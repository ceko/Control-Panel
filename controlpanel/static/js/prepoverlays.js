$(function() {
	$(document.body).append(
    		'<div class="simple_overlay" id="overlay">' +  
    			'<div class="contentWrap"></div>' +
    		'</div>');
    // if the function argument is given to overlay,
    // it is assumed to be the onBeforeLoad event listener
    $("a[rel]").overlay({
    	mask: {
    		color: '#FFF',
    		loadSpeed: 100,
    		opacity: 0.5
    	},
    	        
        onBeforeLoad: function() {
 
            // grab wrapper element inside content
            var wrap = this.getOverlay().find(".contentWrap");
            // load the page specified in the trigger
            wrap.load(this.getTrigger().attr("href"));
        }
 
    });
});


$(function() {
	var init_watermarks = function() {
		$this = $(this);
		if($this.attr('watermark')) {
			$this.watermark($this.attr('watermark'));
		}
	}
	
	$('input[type=text]').each(init_watermarks);
	$('textarea').each(init_watermarks);
})

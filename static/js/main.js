jQuery(document).ready(function($) {

	var myTheme = window.myTheme || {},
    $win = $( window );


	myTheme.Isotope = function () {
	
		// 4 column layout
		var isotopeContainer = $('.isotopeContainer');
		if( !isotopeContainer.length || !jQuery().isotope ) return;
		$win.load(function(){
			isotopeContainer.isotope({
				itemSelector: '.isotopeSelector'
			});
		$('.isotopeFilters').on( 'click', 'a', function(e) {
				$('.isotopeFilters').find('.active').removeClass('active');
				$(this).parent().addClass('active');
				var filterValue = $(this).attr('data-filter');
				isotopeContainer.isotope({ filter: filterValue });
				e.preventDefault();
			});
		});
	
	};


	myTheme.Fancybox = function () {
		
		$(".fancybox-pop").fancybox({
			maxWidth	: 900,
			maxHeight	: 700,
			fitToView	: true,
			width		: '80%',
			height		: '80%',
			autoSize	: false,
			closeClick	: false,
			openEffect	: 'elastic',
			closeEffect	: 'none'
		});
	
	};

	myTheme.Isotope();
	myTheme.Fancybox();
	
	

});





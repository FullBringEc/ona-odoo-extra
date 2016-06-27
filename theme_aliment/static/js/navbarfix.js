$(document).ready(function() {
	var $header = $("header");
	if ($('#oe_main_menu_navbar').length) {
		$header.css('top', '36px');
	}
	$(window).bind('scroll', function() {
		var navHeight = $(window).height() / 3 - 70;
		if ($(window).scrollTop() > navHeight) {
			$('.navbar-default').addClass('navbar-fixed-top navbar-back');
			$('.navbar-default').removeClass('nav-trans');
		} else {
			$('.navbar-default').removeClass('navbar-fixed-top navbar-back');
			$('.navbar-default').addClass('nav-trans');
		}
	});
	$("html").niceScroll({
		cursorcolor : "#999",
		cursoropacitymin : 0,
		cursoropacitymax : 1,
		cursorwidth : "3px",
		cursorborder : "1px solid #999",
		zindex : 5000,
		smoothscroll : true,
	});

});

$("#back-top").hide();
// fade in #back-top
$(function() {
	$(window).scroll(function() {
		if ($(this).scrollTop() > 30) {
			$('#back-top').fadeIn();
		} else {
			$('#back-top').fadeOut();
		}
	});
	// scroll body to 0px on click
	$('#back-top a').click(function() {
		$('body,html').animate({
			scrollTop : 0
		}, 800);
		return false;
	});
});

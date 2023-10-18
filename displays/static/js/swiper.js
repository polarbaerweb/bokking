import { HandleArrowAction } from "./arrow_control.js"


const swiper_wrapper = document.querySelectorAll( ".swiper-wrapper" );

swiper_wrapper.forEach( element =>
{
	const amount = element.querySelectorAll( ".swiper-slide" ).length;
	const places_amount = amount >= 5 ? 5 : amount;
	
	const swiper_top_movies = new Swiper( '.main__collection-swiper', {
		direction: 'horizontal',
		loop: true,
		autoplay: true,
		slidesPerView: places_amount,
	
		breakpoints: {
			1440: {
				slidesPerView: places_amount,
				spaceBetween: 12
			},
			992: {
				slidesPerView: 4,
				spaceBetween: 10
			},
			720: {
				slidesPerView: 3,
				spaceBetween: 8
			},
			540: {
				slidesPerView: 2,
				spaceBetween: 6
			},
			320: {
				slidesPerView: 1,
				spaceBetween: 4
			}
		},
	} )
} )


const swiper = new Swiper( '.main__swiper', {
	direction: 'horizontal',
	loop: true,
	autoplay: true,

	pagination: {
		el: '.swiper-pagination',
		clickable: true,
	}
} )

const swiper_tickets = new Swiper( ".main__ticket-swiper", {
	direction: 'horizontal',
	loop: true,
	autoplay: true,
	breakpoints: {
		992: {
			slidesPerView: 5,
			spaceBetween: 10,
		},
		550: {
			slidesPerView: 4,
			spaceBetween: 10,
		},
		320: {
			slidesPerView: 1,
		}
	},
})

const arrow_configuration = {
	swiper_container: ".main__collection-swiper",
	button: ".main__slide-button",
}


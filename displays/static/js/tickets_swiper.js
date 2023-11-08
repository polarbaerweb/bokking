	const swiper_tickets = new Swiper( ".main__ticket-swiper", {
		direction: 'horizontal',
		loop: true,
		autoplay: true,
		breakpoints: {
			992: {
				slidesPerView: 5,
				spaceBetween: 20
			},
			550: {
				slidesPerView: 4,
			},
			320: {
				slidesPerView: 1,
			}
		},
	})
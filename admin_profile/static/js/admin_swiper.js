export function makeSwiper() {
	const swiper_top_movies = new Swiper(".main__session-swiper", {
		direction: "vertical",
		slidesPerView: 1,
		autoHeight: true,
		loop: true,
		effect: "coverflow",

		autoplay: {
			delay: 5000,
		},
	});
}

document.addEventListener("DOMContentLoaded", () => makeSwiper());

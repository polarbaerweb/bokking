export function makeSwiper() {
	const main__collection = document.querySelectorAll(
		".main__collection-movies",
	);

	main__collection.forEach((element) => {
		const amount = element.querySelectorAll(".swiper-slide").length;
		const places_amount = amount >= 5 ? 5 : amount;

		const swiper_top_movies = new Swiper(
			element.querySelector(".main__collection-swiper"),
			{
				direction: "horizontal",
				loop: true,
				autoplay: true,
				slidesPerView: places_amount,
				breakpoints: {
					1440: {
						slidesPerView: places_amount,
						spaceBetween: 12,
					},
					992: {
						slidesPerView: 4,
						spaceBetween: 10,
					},
					720: {
						slidesPerView: 3,
						spaceBetween: 8,
					},
					540: {
						slidesPerView: 2,
						spaceBetween: 6,
					},
					320: {
						slidesPerView: 1,
						spaceBetween: 4,
					},
				},
			},
		);
	});
}

document.addEventListener("DOMContentLoaded", () => makeSwiper());

import { makeSwiper } from "./admin_swiper.js";

async function buildSessionsList() {
	const config = {
		method: "GET",
	};

	const endpoint = "http://127.0.0.1:8000/user_admin/sold_tickets_list/";

	const response = await fetch(endpoint, config);
	const json_to_object = await response.json();

	makeList(json_to_object);
}

function makeList(response) {
	const div = document.querySelector(".main__collection-swiper-wrapper");

	const ul = document.createElement("ul");
	ul.className = "main__collection-list main__session-list swiper-slide ";

	response.sessions.forEach((session) => {
		const li = document.createElement("li");
		li.className = "main__collection-item main__session-item";

		const a = document.createElement("a");
		a.href = `http://127.0.0.1:8000/user_profile/profile/${session.id}`;
		a.className = "main__collection-link main__session-link";

		const figure = document.createElement("figure");
		figure.className = "main__collection-box main__session-box";

		const imgWrapper = document.createElement("div");
		imgWrapper.className = "main__img-wrapper main__session-wrapper";

		const img = document.createElement("img");
		img.src = session.movie_img;
		img.alt = "top movie image";
		img.className = "main__collection-img";

		const figcaption = document.createElement("figcaption");
		figcaption.className = "main__collection-title";

		const movie_link = document.createElement("a");
		movie_link.href = `http://127.0.0.1:8000/detail/${session.movie_id}`;
		movie_link.className = "main__sub-link";

		const h3 = document.createElement("h3");
		h3.className = "main__collection-title";
		h3.textContent = session.movie_name;

		movie_link.appendChild(h3);

		const subList = document.createElement("ul");
		subList.className =
			"main__session-sub-list main__collection-sub-list main__tickets-sub-list";

		const subItems = ["start_time", "price", "hall"];

		subItems.forEach((item) => {
			const liSub = document.createElement("li");
			liSub.className = "main__sub-item";

			const aSub = document.createElement("a");
			aSub.href = "#";
			aSub.className = "main__sub-link main__tickets-sub-link";
			aSub.textContent = session[item];

			liSub.appendChild(aSub);
			subList.appendChild(liSub);
		});

		figcaption.appendChild(movie_link);
		figcaption.appendChild(subList);

		imgWrapper.appendChild(img);

		figure.appendChild(imgWrapper);
		figure.appendChild(figcaption);

		a.appendChild(figure);
		li.appendChild(a);
		ul.appendChild(li);
	});

	div.appendChild(ul);

	cashFormatter();
	makeSwiper();
}

function cashFormatter() {
	const prices = document.querySelectorAll(".price");

	const formatter = new Intl.NumberFormat("en-US", {
		style: "currency",
		currency: "USD",
	});

	prices.forEach((price) => {
		const value = price.textContent;
		price.textContent = formatter.format(value);
	});
}

buildSessionsList();

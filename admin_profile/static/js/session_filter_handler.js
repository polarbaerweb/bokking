import { makeSessionChoices } from "./session_choices.js";

import {
	updateChoices,
	getValues,
	appendToFormData,
} from "./admin_form_handler.js";

import { makeSwiper } from "./admin_swiper.js";

const form = document.querySelector(".main__session-filter");

form.addEventListener("submit", handleFormSubmit);

async function handleFormSubmit(event) {
	event.preventDefault();

	const select = document.querySelector("#cinema");
	const option = select.querySelector("option");
	const id = option.value;
	const label = option.textContent;

	const endpoint = `http://127.0.0.1:8000/user_admin/session_list/get_data_by_name_and_related_obj/${id}/`;

	appendSelect(id, label, endpoint);
}

function moviesMemorization() {
	const movies_cache = new Map();

	const methods = {
		addToMoviesCache: function (label, sessions) {
			if (!movies_cache.has(label)) {
				movies_cache.set(label, sessions);
			}
		},

		isHigher: function (label, sessions) {
			let current_length = movies_cache.get(label);

			console.log(current_length, label, movies_cache);

			if (!current_length && sessions.length > 0) {
				return true;
			}

			current_length = current_length.length;

			if (sessions.length > current_length) {
				movies_cache.set(label, sessions);
				return true;
			}

			return false;
		},
	};

	return methods;
}

const movies_memorization = moviesMemorization();

async function appendSelect(id, label, endpoint) {
	if (document.querySelector(`select[data-select_unique_key="${id}"]`)) {
		await updateChoices(`select[data-select_unique_key]`, endpoint);

		await buildSessionsList(
			document.querySelector(`select[data-select_unique_key="${id}"]`).dataset
				.select_type,

			label,
		);

		return;
	}

	const selects_container = document.querySelector(".column");

	const div = document.createElement("div");

	div.className = "main__admin-select-block main__admin-select-block--full";

	div.innerHTML = `
			<label for='hall${id}'>${label}-halls</label>
			<select
				name='filter_name'
				id='hall${id}'
				class='main__admin-select'
				data-is_not_single='false'
				data-select_unique_key='${id}';
				data-select_type='hall'>
			</select>`;

	selects_container.appendChild(div);

	makeSessionChoices(endpoint, id, label);
}

export async function buildSessionsList(select_type, label) {
	function getCsrfToken() {
		const value = document.querySelector(
			"input[name=csrfmiddlewaretoken]",
		).value;

		return value;
	}

	const headers = {
		"X-CSRFToken": getCsrfToken(),
	};

	const values = await getValues(null, form);
	const form_data = await appendToFormData(values, select_type);

	const config = {
		method: "POST",
		body: form_data,
		headers,
	};

	const endpoint = "http://127.0.0.1:8000/user_admin/session_list/filter/";

	fetch(endpoint, config)
		.then((response) => {
			return response.json();
		})
		.then((response) => {
			makeList(label, response);
		});
}

function makeList(label, response) {
	if (movies_memorization.isHigher(label, response.sessions)) {
		const div = document.querySelector(".main__collection-swiper-wrapper");

		movies_memorization.addToMoviesCache(label, response.sessions);

		const ul = document.createElement("ul");
		ul.className = "main__collection-list main__session-list swiper-slide ";

		response.sessions.forEach((session) => {
			const li = document.createElement("li");
			li.className = "main__collection-item main__session-item";

			const a = document.createElement("a");
			a.href = `http://127.0.0.1:8000/detail/${session.movie_id}`;
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

			const h3 = document.createElement("h3");
			h3.className = "main__collection-title";
			h3.textContent = session.movie_name;

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

			const editLi = document.createElement("li");
			editLi.className = "main__sub-item";

			const editA = document.createElement("a");
			editA.href = "#";
			editA.className = "main__sub-link main__tickets-sub-link";
			editA.textContent = "Edit";

			editLi.appendChild(editA);
			subList.appendChild(editLi);

			const deleteLi = document.createElement("li");
			deleteLi.className = "main__sub-item";

			const deleteA = document.createElement("a");
			deleteA.href = `http://127.0.0.1:8000/user_admin/delete_session/${session.id}`;
			deleteA.className = "main__sub-link main__tickets-sub-link";
			deleteA.textContent = "Delete";

			deleteLi.appendChild(deleteA);
			subList.appendChild(deleteLi);

			figcaption.appendChild(h3);
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

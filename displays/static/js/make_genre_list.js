export async function makeGenreList() {
	const values = await getValues();
	const genre_list = document.querySelector(".genre_list");
	let container = document.querySelector(".genre");

	if (!container) {
		container = document.createElement("ul");
		container.className = "header__sub-menu sub__menu genre";
	}

	genre_list.appendChild(container);

	if (typeof values !== "undefined") {
		values.forEach((genre) => {
			const li = document.createElement("li");
			li.className = "header__sub-item sub__item";

			const a = document.createElement("a");
			a.className = "header__sub-link";
			a.href = `http://127.0.0.1:8000/genre/${genre.pk}`;
			a.textContent = genre.name;

			li.appendChild(a);
			container.appendChild(li);
		});
	}
}

async function getValues() {
	const config = {
		method: "GET",
	};

	const endpoint = "http://127.0.0.1:8000/genre_list/";

	try {
		const response = await fetch(endpoint, config);
		const data = await response.json();

		console.log(data);

		const values = JSON.parse(data["list"]);
		const processedValues = values.map((value) => getGenreNameAndPK(value));

		return processedValues;
	} catch (error) {
		console.error(error);
		throw error;
	}
}

function getGenreNameAndPK(value) {
	const object = {};
	const { fields, pk } = value;

	(object["pk"] = pk), (object["name"] = fields["name"]);
	return object;
}

document.addEventListener("DOMContentLoaded", () => makeGenreList());

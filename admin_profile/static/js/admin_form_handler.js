const admin_forms = document.querySelectorAll("form[data-form_type]");
const items = document.querySelectorAll("li[data-admin_aside]");

const ADMIN_FORMS_OBJECT = {};
const ITEMS_OBJECT = {};

collectBlocksToObject();

function collectBlocksToObject() {
	admin_forms.forEach((element) => {
		const type = element.dataset.form_type;
		ADMIN_FORMS_OBJECT[type] = element;
	});

	items.forEach((element) => {
		const type = element.dataset.form_type;
		ITEMS_OBJECT[type] = element;
	});
}

document.addEventListener("click", (event) => {
	const attrs = {
		event,
	};

	handleAsideList(attrs);
});

document.addEventListener("DOMContentLoaded", (event) => {
	const attrs = {
		event,
		is_loaded: true,
	};

	handleAsideList(attrs);
});

function handleAsideList(attrs) {
	const { event, is_loaded } = attrs;

	const target = event.target.tagName === "LI" ? event.target : null;
	const type = target !== null ? target.dataset.form_type : null;

	if (type || is_loaded) {
		removeActiveClasses();
		ITEMS_OBJECT[type || "actors"].classList.add("active");

		showFormByName(type || "actors");
		handleSubmitFormByName(type || "actors");
	} else {
		console.log("Null was detected");
	}

	function removeActiveClasses() {
		items.forEach((element) => {
			element.classList.remove("active");
		});
	}
}

function showFormByName(form_type) {
	hideRestForms();
	ADMIN_FORMS_OBJECT[form_type].style.display = "flex";

	function hideRestForms() {
		admin_forms.forEach((element) => {
			element.style.display = "none";
		});
	}
}

function handleSubmitFormByName(form_type) {
	const form = ADMIN_FORMS_OBJECT[form_type];

	form.addEventListener("submit", function (event) {
		const attrs = {
			event,
			form_type,
		};

		submit(attrs);
	});
}

function submit(attrs) {
	const { event, form_type } = attrs;

	event.preventDefault();
	appendToFormData(getValues(form_type), form_type);
}

function getValues(form_type) {
	const form = ADMIN_FORMS_OBJECT[form_type];
	const inputs = Array.from(form.querySelectorAll("input:not(.form-control)"));
	const selects = Array.from(form.querySelectorAll("select"));

	console.log(inputs);

	const values = inputs.map((input) => {
		const object = {};
		object[input.name] = input.value;
		input.value = "";
		return object;
	});

	if (selects.length > 0) {
		selects.forEach((select) => {
			const options = select.querySelectorAll("option");

			options.forEach((option) => {
				const object = {};
				object[select.name] = option.value;
				values.push(object);
			});
		});
	}

	return values;
}

function appendToFormData(values, form_type) {
	const form = new FormData();

	values.forEach((object) => {
		let name = Object.keys(object)[0];
		const value = Object.values(object)[0];

		if (name == "name_add") name = "name";

		form.append(name, value);
	});

	const type = ["name_add", "prizes_add"].includes(form_type)
		? removeSuffixAdd()
		: form_type;

	const removeSuffixAdd = () => form_type.split("_")[0];

	form.append("form_type", type);

	makePostRequest(form);
}

function makePostRequest(form_data) {
	function getCsrfToken() {
		const value = document.querySelector(
			"input[name=csrfmiddlewaretoken]",
		).value;

		return value;
	}

	function showMessage(message, bg_color = "#ffb703") {
		const message_block = document.querySelector(".main__massage-block");

		message_block.style.opacity = 1;
		message_block.style.visibility = "visible";
		message_block.style.backgroundColor = bg_color;

		message_block.textContent = message;

		setTimeout(() => {
			message_block.style.opacity = 0;
			message_block.style.visibility = "hidden";
		}, 2000);
	}

	const headers = {
		"X-CSRFToken": getCsrfToken(),
	};

	const config = {
		method: "POST",
		body: form_data,
		headers,
	};

	const endpoint = "http://127.0.0.1:8000/user_admin/save/";

	fetch(endpoint, config)
		.then((response) => {
			return response.json();
		})
		.then((response) => {
			showMessage(response.message);
		})
		.catch((error) => {
			showMessage(error.message, "#780000");
		});
}

import {
	getChoices,
	choice_cache,
	destroyChoicesIfAllowed,
} from "./choices.js";

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

		const logic = type || "sessions_edit";

		if (typeof ITEMS_OBJECT[logic] !== "undefined") {
			ITEMS_OBJECT[logic].classList.add("active");
		}

		showFormByName(logic);
		handleSubmitFormByName(logic);
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

export function handleSubmitFormByName(form_type) {
	const form = ADMIN_FORMS_OBJECT[form_type];
	const is_true = !Boolean(form.dataset.listener);

	if (is_true) {
		form.addEventListener("submit", function (event) {
			const attrs = {
				event,
				form_type,
				form,
			};

			form.dataset.listener = "true";

			submit(attrs);
		});
	}
}

async function submit(attrs) {
	alert("Submit");
	const { event, form_type } = attrs;

	event.preventDefault();

	const form_data = await appendToFormData(
		await getValues(form_type),
		form_type,
	);

	makePostRequest(form_data, form_type);
}

export async function getValues(form_type = null, form_block = null) {
	const form = ADMIN_FORMS_OBJECT[form_type] || form_block;
	const inputs = Array.from(
		form.querySelectorAll("input:not(.form-control), textarea"),
	);
	const selects = Array.from(
		form.querySelectorAll("select:not([data-session-filter])"),
	);
	const values = [];

	if (inputs.length > 0) {
		inputs.forEach(async (input) => {
			const object = {};

			if (input.name === "img") {
				const file = await handleFiles(input.files);
				object[input.name] = file.img;
			} else {
				object[input.name] = input.value;
			}

			values.push(object);
		});
	}

	if (selects.length > 0) {
		selects.forEach((select) => {
			const options = select.querySelectorAll("option");

			options.forEach((option) => {
				const object = {};
				object[select.name] = option.value;
				values.push(object);
				console.log(object, values);
			});
		});
	}

	return values;
}

function handleFiles(files) {
	const selectedFile = files[0];

	if (!selectedFile) {
		return Promise.reject(new Error("No file selected."));
	}

	const files_object = {};
	files_object["img"] = selectedFile;

	return Promise.resolve(files_object);
}

export async function appendToFormData(values, form_type) {
	const form = new FormData();

	values.forEach((object) => {
		let name = Object.keys(object)[0];
		let value = Object.values(object)[0];

		if (name == "name_add") name = "name";

		if (value instanceof File) {
			form.append(name, value, value.name);
		} else {
			form.append(name, value);
		}
	});

	const type = ["name_add", "prizes_add"].includes(form_type)
		? removeSuffixAdd()
		: form_type;

	const removeSuffixAdd = () => form_type.split("_")[0];

	form.append("form_type", type);

	return form;
}

async function makePostRequest(form_data, form_type = null) {
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
		.then(async (response) => {
			await updateChoices();

			const res = await response.json();
			showMessage(res.message);
		})
		.catch((error) => {
			showMessage(error.message, "#780000");
		});
}

export async function updateChoices(
	selector = "select[data-choice]",
	endpoint = null,
	is_single = false,
) {
	const select_elements = is_single
		? document.querySelector(selector)
		: document.querySelectorAll(selector);

	if (is_single) {
		await updateChoicesHelper(select_elements, endpoint);
		return;
	}

	select_elements.forEach(async (select) => {
		await updateChoicesHelper(select, endpoint);
	});
}

async function updateChoicesHelper(block, endpoint) {
	const select_id =
		block.tagName === "SELECT" ? block.id : block.querySelector("select").id;

	const { values, valuesLength } = await getChoices(select_id, endpoint);

	const statement = choice_cache.isValuesLengthHigherToOld(
		select_id,
		valuesLength,
		values,
	);

	if (statement) {
		destroyChoicesIfAllowed(select_id, values);
	}
}

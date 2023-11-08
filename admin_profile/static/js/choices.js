const select_elements = document.querySelectorAll("select[data-choice]");

async function initializeChoices(select) {
	const id = select.id;
	const options = await getChoices(id);
	const is_not_single = Boolean(select.dataset.is_not_single);

	const choice_config = {
		choices: options,
		removeItemButton: is_not_single,
	};

	if (options !== null) {
		const choices = new Choices(select, choice_config);
	}
}

select_elements.forEach((select) => {
	initializeChoices(select);
});

async function getChoices(name) {
	const config = {
		method: "GET",
	};

	const endpoint = `http://127.0.0.1:8000/user_admin/get_data_by_name/${name}/`;

	try {
		const response = await fetch(endpoint, config);
		let data = await response.json();
		data = JSON.parse(data.message);

		return getValues(data);
	} catch (error) {
		console.error("An error occurred:", error);
		return null;
	}
}

function getValues(data) {
	const values = [];

	data.forEach((info) => {
		const value = {};

		const field = info.fields.name;
		const value_id = info.pk;
		const name = field;

		value["value"] = value_id;
		value["label"] = name;
		value["selected"] = false;

		values.push(value);
	});

	return values;
}

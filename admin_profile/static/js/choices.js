function choicesCache() {
	const choicesCache = new Map();

	const methods = {
		addToChoiceCache: function (choice_name, valuesLength, values) {
			if (!choicesCache.has(choice_name)) {
				choicesCache.set(choice_name, {
					valuesLength: valuesLength,
					values: values,
				});
				return false;
			}
		},

		isValuesLengthHigherToOld: function (choice_name, valuesLength, values) {
			const currentLength = choicesCache.get(choice_name);

			if (valuesLength > currentLength.valuesLength) {
				choicesCache.set(choice_name, {
					valuesLength: valuesLength,
					values: values,
				});

				return true;
			}

			return false;
		},

		getValuesFromCache: function (choice_name) {
			const values = choicesCache.get(choice_name);

			if (values) return values || null;
		},
	};

	return methods;
}

function choicesMemorization() {
	const choicesBox = new Map();

	const methods = {
		addToChoicesBox: function (choices, select, choiceName) {
			if (!choicesBox.has(choiceName)) {
				choicesBox.set(choiceName, {
					select: select,
					choices: choices,
				});
			}
		},

		getChoiceFromChoicesBox: function (choiceName) {
			if (choicesBox.has(choiceName)) {
				return choicesBox.get(choiceName);
			}

			return null;
		},
	};

	return methods;
}

export const choice_cache = choicesCache();

const choicesMemorized = choicesMemorization();

document.addEventListener("DOMContentLoaded", function () {
	const selectElements = document.querySelectorAll("select[data-choice]");

	selectElements.forEach((element) => {
		initializeChoices(element);
	});
});

export async function initializeChoices(select, reqLink = null) {
	const id = select.id;

	const { values, valuesLength } =
		(choice_cache.getValuesFromCache(id) && !reqLink) ||
		(await getChoices(id, reqLink));

	const isNotSingle = Boolean(select.dataset.is_not_single);

	const choiceConfig = {
		choices: values,
		removeItemButton: isNotSingle,
	};

	if (valuesLength > 0) {
		const choices = new Choices(select, choiceConfig);

		console.log("DONE");

		choice_cache.addToChoiceCache(id, valuesLength, values);
		choicesMemorized.addToChoicesBox(choices, select, id);
	}
}

export function destroyChoicesIfAllowed(choiceName, values) {
	const box = choicesMemorized.getChoiceFromChoicesBox(choiceName);
	if (box) {
		box.choices.clearChoices();
		box.choices.setChoices(values);
	}
}

export async function getChoices(name, reqLink) {
	const config = {
		method: "GET",
	};

	const endpoint =
		reqLink || `http://127.0.0.1:8000/user_admin/get_data_by_name/${name}/`;

	try {
		const response = await fetch(endpoint, config);
		let data = await response.json();
		data = JSON.parse(data.message);

		return getValues(data);
	} catch (error) {
		console.log(error);
		return null;
	}
}

function getValues(data) {
	const values = data.map((info) => {
		const field = info.fields.name;
		const valueId = info.pk;
		const name = field;

		return {
			value: valueId,
			label: name,
			selected: false,
		};
	});

	return {
		values: values,
		valuesLength: values.length,
	};
}

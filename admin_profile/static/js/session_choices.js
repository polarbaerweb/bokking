import { initializeChoices } from "./choices.js";
import { buildSessionsList } from "./session_filter_handler.js";

function makePrimarySessionChoices() {
	const element = document.querySelector("select[data-session-filter]");
	initializeChoices(element);
}

export async function makeSessionChoices(req_link = null, unique_id, label) {
	const select = document.querySelector(
		`select[data-select_unique_key="${unique_id}"]`,
	);
	const select_type = select.dataset.select_type;

	await initializeChoices(select, req_link);
	await buildSessionsList(select_type, label);
}

document.addEventListener("DOMContentLoaded", () =>
	makePrimarySessionChoices(),
);

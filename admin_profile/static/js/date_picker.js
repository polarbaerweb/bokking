// import { flatpickr } from "flatpickr";

const start_time = document.querySelector("#start_time");

const fp = flatpickr(start_time, {
	altInput: true,
	altFormat: "M j, Y H:i",
	dateFormat: "Y-m-dTH:i:S",
	enableTime: true,
});

const start_time = document.querySelector(".date");

const fp = flatpickr(start_time, {
	altInput: true,
	altFormat: "M j, Y H:i",
	dateFormat: "Y-m-dTH:i:S",
	defaultDate: start_time.value,
	enableTime: true,
});

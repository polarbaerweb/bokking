const start_times = document.querySelectorAll(".date");

start_times.forEach((element) => {
	const fp = flatpickr(element, {
		altInput: true,
		altFormat: "M j, Y H:i",
		dateFormat: "Y-m-dTH:i:S",
		enableTime: true,
	});
});

const browse_button = document.querySelector("#img");
const browse_button_label = document.querySelector(".main__form-browse");

browse_button.addEventListener("change", function () {
	browse_button_label.textContent = this.files[0]["name"];
});

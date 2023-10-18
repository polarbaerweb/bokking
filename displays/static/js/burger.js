const burger = document.querySelector( ".burger" );
const header_navigation_box = document.querySelector( ".header__navigation-box" );

burger.addEventListener( "click", function ()
{
	this.classList.toggle( "active" );
	header_navigation_box.classList.toggle( "active" );
	document.body.classList.toggle("lock") 
} );
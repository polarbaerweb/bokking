window.onload = handleWindowLoad

function handleWindowLoad ()
{
	const CURRENT_PATH = window.location.pathname;
	
	let CURRENT_PATH_SPLITTED = CURRENT_PATH !== '/' ? CURRENT_PATH.split( '/' ) : 'main';
	if ( Array.isArray( CURRENT_PATH_SPLITTED ) )
	{
		CURRENT_PATH_SPLITTED = CURRENT_PATH_SPLITTED.filter( ( word ) => !["/", ""].includes(word));
	}

	const BREADCRUMBS_CONTAINER = document.querySelector( ".main__breadcrumbs-list" );
	
	if ( CURRENT_PATH_SPLITTED !== 'main') {
		for ( let path of CURRENT_PATH_SPLITTED ){
			let li = document.createElement( 'li' );
			li.className = 'main__breadcrumbs-item';
			
			if ( CURRENT_PATH_SPLITTED.indexOf( path ) === CURRENT_PATH_SPLITTED.length )
			{
				var a = document.createElement( 'a' );
				a.className = 'main__breadcrumbs-link';	
				a.setAttribute( 'href', path );
			} else
			{
				var a = document.createElement( 'span' );
				a.className = 'main__breadcrumbs-item main__breadcrumbs-link disabled';
			}
			a.textContent = `${path}/`;
			
			
			if ( CURRENT_PATH_SPLITTED.indexOf( path ) === CURRENT_PATH_SPLITTED.length )
			{
				BREADCRUMBS_CONTAINER.appendChild( a )
				break
			} else
			{
				li.appendChild( a )
				BREADCRUMBS_CONTAINER.appendChild(li)
			}
			
		}
	} else
	{
		var a = document.createElement( 'span' );
		a.className = 'main__breadcrumbs-item main__breadcrumbs-link disabled';
		a.textContent = CURRENT_PATH_SPLITTED
		BREADCRUMBS_CONTAINER.appendChild( a );
	}
}
 $(document).ready(function(e){

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

	var error = "{{error}}";
	console.log('Halo');
	if(error) {
		$('#login-form-link').removeClass('active');
		$('#register-form-link').addClass('active');
		e.preventDefault();
	}
});


function registerError (error){
	if(error){
		$('#login-form-link').removeClass('active');
		$('#register-form-link').addClass('active');
	}
};

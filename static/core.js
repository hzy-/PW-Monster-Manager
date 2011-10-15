// defining functions

	// new monster page

		// form functions

			// reusable
			function bind_delete_x() {
				$('.delete_x').click(function(){
					$(this).parent().remove();
					return false;
				})
			}

			// resistances
			var skill_count = 0;
			function add_skill() {
				html = $('.skill').filter(':first').html();
				div = "<div class='skill'>" + html + "</div>";
				$('.skill').filter(':last').after(div);

				//set the id correctly
				skill_count ++;
				$('.skill_input').filter(':last').attr('name', 'skill[' + skill_count + ']');
			}

			// natural attacks
			var natural_attack_count = 0;
			function add_natural_attack() {
				html = $('.natural_attack').filter(':first').html();
				div = "<div class='natural_attack'>" + html + "</div>";
				$('.natural_attack').filter(':last').after(div);

				//lets get this id set
				natural_attack_count ++;
				$('.natural_attack').filter(':last').children(':input').each(function() {
					console.log('hi');
					chunks = $(this).attr('name').split('.');
					$(this).attr('name', 'natural_attack['+natural_attack_count+'].'+chunks[1]);
				});
			}


// code to be executed when DOM is ready
$(document).ready(function() {

	// new monser page
		// form submit function
		//$('#new_monster_form').submit(function(){
		$('#submit_form').click(function(){
			formData = $('#new_monster_form').toObject();
			json = JSON.stringify(formData);
			console.log(json);
			$.post('/monsters/', {'json': json}, function(url) {
//				document.location.href = url;
				console.log(url);
			});
			return false;
		})

		// bind form functions
			// bind resistance
			$('#skill_add').click(function(){
				add_skill();
				bind_delete_x();
				return false;
			})

			// natural attack
			$('#natural_attack_add').click(function(){
				add_natural_attack();
				bind_delete_x();
				return false;
			})
});
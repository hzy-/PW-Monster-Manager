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
			function add_resistance() {
				html = $('.resistance').filter(':first').html();
				div = "<div class='resistance'>" + html + "</div>";
				$('.resistance').filter(':last').after(div);
			}

			// skills
			function add_skill() {
				html = $('.skill').filter(':first').html();
				div = "<div class='skill'>" + html + "</div>";
				$('.skill').filter(':last').after(div);
			}

			// natural attacks
			function add_natural_attack() {
				html = $('.natural_attack').filter(':first').html();
				div = "<div class='natural_attack'>" + html + "</div>";
				$('.natural_attack').filter(':last').after(div);
			}


// code to be executed when DOM is ready
$(document).ready(function() {

	// new monser page
		// form submit function
		$('#new_monster_form').submit(function(){
			console.log($(this).serializeArray());
			return false;
		})

		// bind form functions
			// bind resistance
			$('#resistance_add').click(function(){
				add_resistance();
				bind_delete_x();
				return false;
			})

			// bind skill
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
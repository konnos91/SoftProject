import Ember from 'ember';

export default Ember.Component.extend({
	actions: {
		addStudent: function(){

			var id = this.get('id');
			var name = this.get('name');
			var birth = this.get('birth');
			var stclass = this.get('stclass');
			var Year = this.get('Year');
			var Quarter = this.get('Quarter');
			var math = this.get('math');
			var computer = this.get('computer');
			var literature = this.get('literature');

			
			//Create New student
			var student = this.store.createRecord('student', {
				id:id,
				name: name,
				birth: new Date(birth),
				stclass:stclass,
				Year:Year,
				Quarter:Quarter,
				math:math,
				computer:computer,
				literature:literature
			});

			//save the model
			student.save();
			 

			// Clear Form
			this.setProperties({
				id:'',
				name: '',
				birth: '',
				stclass:'',
				Year:'',
				Quarter:'',
				math:'',
				computer:'',
				literature:''
			});

			this.transitionToRoute('manage');


		}
	}
});

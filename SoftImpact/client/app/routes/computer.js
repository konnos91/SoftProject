import Ember from 'ember';  

export default Ember.Route.extend({
  	model:function(params) {
       //get the JSON values from the specified url
  	   var url = 'http://localhost:8080/modules/computer';
	  //return this.store.findRecord('statistic',params.student_id).then(function(data) {
	  return Ember.$.getJSON(url).then(function(data) {

		//adds the data to/from an array. splice(0,2) is the number of items to be displayed: is 2

		//array to strorw the results which will produce the graph
		var result = [];

		//get the records to identify the name and q1,q2,q3 and q4
		var temprecs = data.computer; //error undefined 

		//loop to find all the suitable records		
		for(var i=0; i<temprecs.length; i++){
			var item = temprecs[i];
			var element = {
				"name":item.stclass, //get the name
				"data": [item.q1,item.q2,item.q3,item.q4]
			};
			//the elements of name and data are pushing into the array results
			result.push(element);

		};
		//send the results for producing the graph 
		return result;

	   });
	}

});
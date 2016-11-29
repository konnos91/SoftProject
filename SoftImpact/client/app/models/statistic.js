import DS from 'ember-data';

export default DS.Model.extend({ 
	  //define  the suitable model to produce the statistics
  q1: DS.attr('number'),
  studentid: DS.attr('number'),
  name: DS.attr('string'), 
  q2: DS.attr('number'),
  q3: DS.attr('number'),
  q4: DS.attr('number'),
});
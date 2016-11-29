import DS from 'ember-data';

export default DS.Model.extend({ 
  //define  the suitable model to produce the right chart
  Year: DS.attr('string'), 
  Quarter: DS.attr('string'), 
  Maths: DS.attr('number'),
  IT: DS.attr('number'),
  Literature: DS.attr('number'),
});

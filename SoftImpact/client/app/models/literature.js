import DS from 'ember-data';

export default DS.Model.extend({
  //define  the suitable model to produce the right chart 
  q1: DS.attr('number'),
  stclass: DS.attr('string'), 
  q2: DS.attr('number'),
  q3: DS.attr('number'),
  q4: DS.attr('number'),
});

// controller 
import Ember from 'ember';
import defaultTheme from '../themes/default-theme';

 
export default Ember.Controller.extend({
  
  chartOptions: {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Quarter-Q1',

    },
    tooltip: {
            headerFormat: '<b>{point.x}</b><br/>',
            pointFormat: '{item.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    xAxis: { 
      categories: ["Math","IT","Literature"],
      title: {
        text: 'Subjects'
      },
    labels: {
    }
    },
    yAxis: {
      title: {
        text: ''
      }
    }
  },
    
  chartData: function(){
      return this.get('model')}.property('model.@each'),
      theme: defaultTheme,

  
});
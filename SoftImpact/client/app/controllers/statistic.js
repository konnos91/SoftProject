// controller 
import Ember from 'ember';
import defaultTheme from '../themes/default-theme';

 
export default Ember.Controller.extend({
  
  chartOptions: {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Data Analysis'
    },
    xAxis: {
      title: {
        text: ''
      },
	  labels: {
		formatter: function() {
			return 'q'+this.value;
		}
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

      theme: defaultTheme

  
});
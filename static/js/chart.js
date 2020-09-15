var chartCPU;
let chart; // global


///  Calling API and modeling data for each chart ///

  async function requestData() {
    const result = await fetch('http://127.0.0.1:5000/records/getall');
    if (result.ok) {
      const data = await result.json();
      const [date, value] = data[1];
      const point = [new Date(date).getTime(), value * 10];
      const series = chart.series[0],
        shift = series.data.length > 20; // shift if the series is longer than 20
      // add the point
      chart.series[0].addPoint(point, true, shift);
      // call it again after one second
      setTimeout(requestData, 1000);
    }
  }


  /// Error handling ///
function checkStatus(response) {
    if (response.ok) {
      return Promise.resolve(response);
    } else {
      return Promise.reject(new Error(response.statusText));
    }
  }



// Create the chart
Highcharts.stockChart('contenedor', {
    chart: {
        events: {
            load: function () {

                // set up the updating of the chart each second
                var series = this.series[0];
                setInterval(function () {
                    var x = (new Date()).getTime(), // current time
                        y = Math.round(Math.random() * 100);
                    series.addPoint([x, y], true, true);
                }, 1000);
            }
        }
    },

    time: {
        useUTC: false
    },

    rangeSelector: {
        buttons: [{
            count: 1,
            type: 'minute',
            text: '1M'
        }, {
            count: 5,
            type: 'minute',
            text: '5M'
        }, {
            type: 'all',
            text: 'All'
        }],
        inputEnabled: false,
        selected: 0
    },

    title: {
        text: 'Live random data'
    },

    exporting: {
        enabled: false
    },

    series: [{
        name: 'data',
        data: []
    }]
});






















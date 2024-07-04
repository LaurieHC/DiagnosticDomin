
<template>
  <div class="w-full h-screen bg-slate-700">
    <div class="w-full h-16 bg-black p-4"> 
      <div>
        <h1 class="text-white text-4xl"> Domin Diagnostics </h1>
      </div>
    </div>
    <div class="w-full h-20 bg-red p-8"> 
      <dateSelecter @sensorData="recieveSensorData" v-on="$listeners" />

    </div>
    <div class="w-full grid grid-cols-2"> 
      <div> 
        <Line :data="chartData.lineData" :options="chartData.lineOptions" />
        <div class="w-80 h-80">
          <Pie :data="chartData.pieData" />
        </div>
      </div>
      <div class="w-full h-full grid grid-cols-2"> 
        <div>
          <button class="bg-white" @click="beginLiveDataStream()"> Stream Data </button>
          <h3 class="text-2xl text-white"> Direction: {{latestStreamedData.vehicle_direction}}  </h3>
          <h3 class="text-2xl text-white"> Acceleration: {{latestStreamedData.vehicle_acceleration}} </h3>
          <h3 class="text-2xl text-white"> Speed: {{ latestStreamedData.vehicle_speed }}</h3>
          <h3 class="text-2xl text-white"> Event: {{latestStreamedData.events}}</h3>
        </div>
        <div>
          <img src="./assets/car.svg">
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import { Line, Pie } from 'vue-chartjs'
export default {
    components: {
      Line,
      Pie
    },
    data() {
      return {
        collectedData: [],
        timer: null,
        streamedData: [],
        latestStreamedData: {},
        isStreamingData: false
      }
    },
    methods: {
      recieveSensorData(data) {
        this.isStreamingData = false
        this.timer = null
        this.collectedData = data
      },
      randomIntFromInterval(min, max) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min);
      },
      countDown() {

        var generatedData = {
          timestamp: Date.now(),
          vehicle_speed: this.randomIntFromInterval(0, 120),
          vehicle_direction: "Forward",
          events: "Regular",
          vehicle_acceleration: Math.random()
        }

        this.streamedData.push(generatedData)
        this.latestStreamedData = generatedData
      },
      beginLiveDataStream() {
        this.isStreamingData = true
        this.timer = setInterval(() => {
          this.countDown()
        }, 1000)
      }
    },
    computed: {
      chartData() {

        var collectedAccelerationData = []
        var collectedSpeedData = []
        var collectedPieData = []
        var collectedPieLabels = []
        var eventData = {}


        if (!this.isStreamingData) {
          this.collectedData.forEach(data => {
  
            console.log(data)
            collectedAccelerationData.push({x: new Date(data.timestamp), y:data.vehicle_acceleration})
            collectedSpeedData.push({x: new Date(data.timestamp), y:data.vehicle_speed})
            if (eventData[data.events]) {
              eventData[data.events] = eventData[data.events] + 1
            } else {
              eventData[data.events] = 1
            }
  
          });
        } else {
          this.streamedData.forEach(data => {
            collectedAccelerationData.push({x: new Date(data.timestamp), y:data.vehicle_acceleration})
            collectedSpeedData.push({x: new Date(data.timestamp), y:data.vehicle_speed})
            if (eventData[data.events]) {
              eventData[data.events] = eventData[data.events] + 1
            } else {
              eventData[data.events] = 1
            }
          })
        }
        

        // console.log(eventData)
        Object.entries(eventData).forEach(([key, event]) => {
          collectedPieLabels.push(key)
          collectedPieData.push(event)

        })


        return {
          lineData: {
            labels: [],
            datasets: [
              {
                label: 'Acceleration',
                data: collectedAccelerationData,
                borderColor: '#36A2EB',
              },
              {
                label: 'Speed',
                data: collectedSpeedData,
                borderColor: '#FF0000',
              },
            ],
          },
          pieData: {
            labels: collectedPieLabels,
            datasets: [
              {
                backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                data: collectedPieData
              }
            ]
            
          },
          pieOptions: {
            aspectRatio: 1
          },
          lineOptions: {
            responsive: true,
            scales: {
              x: {
                type: 'time',
                time: {
                  unit: 'hour'
                },
                title: {
                  display: true,
                },
              },
              y: {
                display: true,
                title: {
                  display: true,
                  text: 'Value',
                },
              },
            },
          }
        }
      }
    },
    beforeDestroy() {
      clearInterval(this.timer)
    }

}
</script>

<style scoped>
.right-top-wheel {
    margin-top: 21.25rem;
    margin-bottom: 1.25rem;
    margin-right: 66.25rem;
}
.right-bottom-wheel {
    margin-top: 28.25rem;
    margin-bottom: 1.25rem;
    margin-right: 66.25rem;
}
.left-top-wheel {
    margin-top: 21.25rem;
    margin-bottom: 1.25rem;
    margin-left: 66.25rem;
}
.left-bottom-wheel {
    margin-top: 28.25rem;
    margin-bottom: 1.25rem;
    margin-left: 66.25rem;
}
</style>
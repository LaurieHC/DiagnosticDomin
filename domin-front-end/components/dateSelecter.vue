<template>
    <div>
        <!-- <input class="mr-2" type="datetime-local" v-model="date" placeholder="place date here"/> -->
        <div class="flex flex-row">
            <h1 class="text-xl text-white"> Start Time: </h1>
            <input class="mr-2" type="datetime-local" v-model="startTime" placeholder="place time here"/>
            <h1 class="text-xl text-white"> End Time: </h1>
            <input class="mr-2" type="datetime-local" v-model="endTime" placeholder="place time here"/>
            <button class="bg-white border-solid border-2" @click="retrieveData()"> submit </button>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            date: '',
            startTime: '',
            endTime: '',
            sensorData: {}
        }
    },

    methods: {
        updateData(data) {
            this.data = data
        },
        async retrieveData() {
            const startingTime = this.startTime
            const endingTime = this.endTime

            // await useAsyncData('photos', () => $fetch('https://jsonplaceholder.typicode.com/photos'))
            this.sensorData = await useAsyncData('sensorData', () => $fetch(`http://127.0.0.1:8000/sensorData/?timestamp__gte=${startingTime}&timestamp__lte=${endingTime}&timestamp=&timestamp__gt=&timestamp__lt=&events=`))
            // this.sensorData = await useFetch('http://127.0.0.1:8000/sensorData/').data
            this.$emit('sensorData', this.sensorData.data)
        }
    }
}
</script>
import { Chart, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement, TimeScale, ArcElement } from 'chart.js'
import 'chartjs-adapter-moment';
export default defineNuxtPlugin(() => {
    Chart.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, PointElement, LineElement, TimeScale, ArcElement)
})
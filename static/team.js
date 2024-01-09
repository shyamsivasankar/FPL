export function createChart(data,avg_pts,hst_pts) {
    const ctx = document.getElementById('myChart').getContext('2d');
    
    const gradient = ctx.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, 'rgba(13,169,87,0.4)');
    gradient.addColorStop(0.6, 'rgba(13,169,87,0)');
    gradient.addColorStop(1, 'rgba(13,169,87,0)');

    const gradient1 = ctx.createLinearGradient(0, 0, 0, 600);
    gradient1.addColorStop(0, 'rgba(255,10,10,0.4)');
    gradient1.addColorStop(0.6, 'rgba(255,10,10,0');
    gradient1.addColorStop(1, 'rgba(13,169,87,0)');

    const gradient2 = ctx.createLinearGradient(0, 0, 0, 400);
    gradient2.addColorStop(0, 'rgba(0,0,255,0.4)');
    gradient2.addColorStop(0.6, 'rgba(0,0,255,0)');
    gradient2.addColorStop(1, 'rgba(0,0,255,0)');


    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
            datasets: [
                {
                    label: 'Highest Points',
                    data: hst_pts,
                    borderColor: 'blue',
                    fill: true,
                    borderWidth: 2,
                    backgroundColor: gradient2
                },
                {
                    label: 'Points',
                    data: data,
                    borderColor: 'rgba(13,169,87,1)',
                    fill: true,
                    borderWidth: 2,
                    backgroundColor: gradient
                },
                {
                    label: 'Avg_Points',
                    data: avg_pts,
                    borderColor: 'red',
                    fill: true,
                    borderWidth: 2,
                    backgroundColor: gradient1
                },
                ]
        },
        options: {
            scales: {
                y: {
                    grid: {
                        display: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        maxRotation: 0 
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            },
            elements: {
                line: {
                    tension: 0.2
                },
                point: {
                    radius: 4
                }
            },
        }
    });
}
let date = Date.parse('2090-11-12 18:00:10')
let today = Date.now()

function convert(date1, date2) {
    let days = Math.floor(((date - today) / 1000 / 60 / 60 / 24));
    let hours = Math.floor(((date - today) / 1000 / 60 / 60) % 24);
    let minutes = Math.floor(((date - today) / 1000 / 60) % 60);
    let seconds = Math.floor(((date - today) / 1000) % 60);

    return {
        days,
        hours, 
        minutes, 
        seconds
    }
} 

console.log(convert(date, today))

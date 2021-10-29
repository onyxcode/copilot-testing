// fetch the weather for new york city
function getWeather() {
    const API_KEY = 'b6c2a6a9a9a9c8f7b6f9d9a9b6f9d9a';
    const url = `https://api.weatherbit.io/v2.0/current?city=New%20York&key=${API_KEY}`;
    fetch(url)
        .then(response => response.json())
        .then(data => {
        const weather = data.data[0];
        const weatherInfo = document.querySelector('.weather-info');
        weatherInfo.innerHTML = `
            <h2>${weather.city_name}</h2>
            <p>${weather.weather.description}</p>
            <img src="${weather.weather.icon}" alt="weather icon">
            <p>${weather.temp}&deg;F</p>
        `;
        })
        .catch(error => console.log(error));
    }

// where did it get this api key from?
// https://www.weatherbit.io/api/

// run the function
getWeather();
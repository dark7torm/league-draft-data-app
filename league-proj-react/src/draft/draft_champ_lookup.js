const axios = require('axios');

const KEY = process.env.REACT_APP_MOVIE_API_KEY;
// RGAPI-6a3053ff-8f8d-4374-a511-e8aac410f892

const options = {
  method: 'GET',
  url: 'https://league-of-legends-champions.p.rapidapi.com/champions/%7Blang%7D',
  params: {
    page: '0',
    size: '10',
    name: 'aatrox',
    role: 'fighter'
  },
  headers: {
    'X-RapidAPI-Key': 'SIGN-UP-FOR-KEY',
    'X-RapidAPI-Host': 'league-of-legends-champions.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}
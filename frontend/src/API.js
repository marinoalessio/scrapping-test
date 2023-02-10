const APIURL = new URL('http://localhost:8000/api/'); // server address

async function scrapeBoats(city) {
    // call: GET /api/city/<city_name>
    const response = await fetch(new URL(`city/${city}`, APIURL));
    const jsonList = await response.json();
    if (response.ok) {
      return jsonList;
    } else {
      throw jsonList; 
    }
  }

const API = { scrapeBoats };
export default API;
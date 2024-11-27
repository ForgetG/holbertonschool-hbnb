let PRICE_LIST_PLACES = 0;

async function loginUser(email, password) {
  const response = await fetch('http://localhost:5000/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Referer': "http://localhost:5500"
    },
    body: JSON.stringify({ email, password })
  });
  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = 'index.html';
  } else {
      alert('Login failed: ' + response.statusText);
  }
}

async function fetchUserConnected() {
  const response = await fetch('http://localhost:5000/api/v1/users/me', {
    method: 'GET',
    headers: {
      "content-type": "application/json",
      'Accept': 'application/json',
      "Authorization": "Bearer "+getCookie('token')
    }
  });
  if (response.ok) {
    const data = await response.json();
    return data;
  } else {
    console.log('Fetch places failed: ' + response.statusText);
  }
}

async function fetchPlaces() {
  const response = await fetch('http://localhost:5000/api/v1/places/', {
    method: 'GET',
    headers: {
      "content-type": "application/json",
      'Accept': 'application/json',
      "Authorization": "Bearer "+getCookie('token')
    }
  });
  if (response.ok) {
    const data = await response.json();
    console.log("Places: ", data);
    return data;
  } else {
    console.log('Fetch places failed: ' + response.statusText);
  }
}

async function fetchPlace(placeId) {
  const response = await fetch('http://localhost:5000/api/v1/places/'+placeId, {
    method: 'GET',
    headers: {
      "content-type": "application/json",
      'Accept': 'application/json',
      "Authorization": "Bearer "+getCookie('token')
    }
  });
  if (response.ok) {
    const data = await response.json();
    console.log("Place: ", data);
    return data;
  } else {
    console.log('Fetch place failed: ' + response.statusText);
  }
}

async function fetchPlaceReviews(placeId) {
  const response = await fetch('http://localhost:5000/api/v1/reviews/places/'+placeId+'/reviews', {
    method: 'GET',
    headers: {
      "content-type": "application/json",
      'Accept': 'application/json',
      "Authorization": "Bearer "+getCookie('token')
    }
  });
  if (response.ok) {
    const data = await response.json();
    console.log("Place Reviews: ", data);
    return data || [];
  } else {
    console.log('Fetch place failed: ' + response.statusText);
    return [];
  }
}

function checkAuthentication() {
  const token = getCookie('token');
  if (!token) {
    window.location.href = 'index.html';
  }

  const loginLink = document.getElementById('login-link');
  if (loginLink) {
    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
    }
  }

  // Hide review form in Place page
  const placeDetail = document.getElementById('place-details');
  if (placeDetail) {
    if (!token) {
      document.getElementById('add-review').style.display = 'none';
    }
    else {
      document.getElementById('add-review').style.display = 'block';
    }
  }
}
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();

  // Login form event listener
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const target = event.target;
      await loginUser(target.email.value, target.password.value);
    });
  }

  // Index page
  const placesList = document.getElementById('places-list');
  const priceFilter = document.getElementById('price-filter');
  if (placesList && priceFilter) {
    function displayPlaces(places) {
      placesList.innerHTML = '';

      places.forEach(place => {
        if (PRICE_LIST_PLACES != 0 && place['price'] > PRICE_LIST_PLACES) {
          return;
        }

        const article = document.createElement('article');
        article.classList.add('place-card');

        const articleTitle = document.createElement('h2');
        articleTitle.textContent = place['title'];
        const articleP = document.createElement('p');
        articleP.textContent = `Price per night: $${place['price']}`;

        const articleButton = document.createElement('button');
        articleButton.textContent = 'View Details';
        articleButton.addEventListener('click', () => {
          window.location.href = `place.html?id=${place['id']}`;
        });
        articleButton.classList.add('details-button');

        article.appendChild(articleTitle);
        article.appendChild(articleP);
        article.appendChild(articleButton);
        placesList.appendChild(article);
      });
    }

    priceFilter.addEventListener('change', (event) => {
      PRICE_LIST_PLACES = parseInt(event.target.value);
      fetchPlaces().then(places => {
        displayPlaces(places);
      });
    });

    fetchPlaces().then(places => {
      displayPlaces(places);

      priceFilter.innerHTML = '';
      const option = document.createElement('option');
      option.value = 0;
      option.innerHTML = 'All prices';
      option.selected = true;
      priceFilter.appendChild(option);

      places.forEach(place => {
        // <option value="1">1 Star</option>
        const option = document.createElement('option');
        option.value = place['price'];
        option.innerHTML = `$${place['price']}`;
        priceFilter.appendChild(option);
      });
    });
  }

  // Place page
  const placeDetail = document.getElementById('place-details');
  const reviewsList = document.getElementById('reviews');
  if (placeDetail) {
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');

    fetchPlace(placeId).then(place => {
      document.getElementById('place-details__title').innerHTML = place['title'];
      document.getElementById('place-details__host').innerHTML = `<strong>Host:</strong> ${place['owner']['first_name']} ${place['owner']['last_name']}`;
      document.getElementById('place-details__price').innerHTML = `<strong>Price per night:</strong> $${place['price']}`;
      document.getElementById('place-details__description').innerHTML = `<strong>Description:</strong> ${place['description']}`;
      
      const amenities = document.getElementById('place-details__amenities');
      amenities.innerHTML = `<strong>Amenities:</strong> `;
      place['amenities'].forEach(amenity => {
        amenities.innerHTML += amenity['name'] + ', ';
      });
    });

    reviewsList.innerHTML = '';
    const reviews = fetchPlaceReviews(placeId);
    if (reviews.length > 0) {
      reviews.forEach(review => {
        // <article class="review-card">
        //     <p><strong>Robert Brown:</strong></p>
        //     <p>Amazing location and very comfortable.</p>
        //     <p><strong>Rating:</strong> 5</p>
        // </article>
        const article = document.createElement('article');
        article.classList.add('review-card');

        const articleP1 = document.createElement('p');
        articleP1.innerHTML = `<strong>${review['user']['first_name']} ${review['user']['last_name']}:</strong>`;
        const articleP2 = document.createElement('p');
        articleP2.textContent = review['text'];
        const articleP3 = document.createElement('p');
        articleP3.innerHTML = `<strong>Rating:</strong> ${review['rating']}`;

        article.appendChild(articleP1);
        article.appendChild(articleP2);
        article.appendChild(articleP3);
        reviewsList.appendChild(article);
      });
    }

    // Review form page
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
      const urlParams = new URLSearchParams(window.location.search);
      const placeId = urlParams.get('id');

      reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const target = event.target;
        const response = await fetch('http://localhost:5000/api/v1/reviews/', {
          method: 'POST',
          headers: {
            "content-type": "application/json",
            'Accept': 'application/json',
            "Authorization": "Bearer "+getCookie('token')
          },
          body: JSON.stringify({
            place_id: placeId,
            text: target.review.value,
            rating: target.rating.value
          })
        });
        if (response.ok) {
          alert('Review added successfully');
        } else {
          alert('Review failed: ' + response.statusText);
        }
      });
    }
  }
});
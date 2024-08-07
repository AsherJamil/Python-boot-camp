const apiBaseUrl = "https://the-one-api.dev/v2";
const apiKey = "YOUR_API_KEY_HERE"; // Replace with your actual API key sign up and put ur API here

const searchInput = document.getElementById("search-input");
const categorySelect = document.getElementById("category-select");
const searchButton = document.getElementById("search-button");
const resultsSection = document.getElementById("results-section");

searchButton.addEventListener("click", performSearch);

async function performSearch() {
	const searchTerm = searchInput.value.trim();
	const category = categorySelect.value;

	if (!searchTerm) {
		alert("Please enter a search term");
		return;
	}

	try {
		const results = await fetchData(category, searchTerm);
		displayResults(results, category);
	} catch (error) {
		console.error("Error fetching data:", error);
		resultsSection.innerHTML =
			"<p>An error occurred while fetching data. Please try again.</p>";
	}
}

async function fetchData(category, searchTerm) {
	const url = `${apiBaseUrl}/${category}?name=${encodeURIComponent(
		searchTerm
	)}`;
	const response = await fetch(url, {
		headers: {
			Authorization: `Bearer ${apiKey}`,
		},
	});

	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}

	const data = await response.json();
	return data.docs;
}

function displayResults(results, category) {
	resultsSection.innerHTML = "";

	if (results.length === 0) {
		resultsSection.innerHTML = "<p>No results found.</p>";
		return;
	}

	results.forEach((result) => {
		const card = document.createElement("div");
		card.className = "result-card";

		let content = "";
		switch (category) {
			case "character":
				content = `<h2>${result.name}</h2><p>Race: ${
					result.race || "Unknown"
				}</p>`;
				break;
			case "location":
				content = `<h2>${result.name}</h2>`;
				break;
			case "quote":
				content = `<p>${result.dialog}</p><p>- ${
					result.character || "Unknown"
				}</p>`;
				break;
		}

		card.innerHTML = content;
		resultsSection.appendChild(card);
	});
}

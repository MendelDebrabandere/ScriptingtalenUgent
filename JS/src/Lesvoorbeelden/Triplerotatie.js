const mod = (m, d) => (m % d + d) % d;

function categorie(karakter) {

	// eerste categorie: a-i
	if (/^[a-i]$/i.test(karakter)) {
		return 0;
	}
	// tweede categorie: j-r
	if (/^[j-r]$/i.test(karakter)) {
		return 1;
	}
	// derde categorie: r-z
	if (karakter.length === 1) {
		return 2;
	}
	throw new Error("ongeldig karakter");
}

function codeer(klare_tekst, k1, k2, k3) {

	// string opsplitsen in 3 deelstrings
	deelstrings = ["", "", ""];
	for (let karakter of klare_tekst) {
		deelstrings[categorie(karakter)] += karakter;
	}

	// karakters vervangen door karakter uit zelfde categorie maar aantal posities verder
	let cijfertekst = ""
	const posities = [k1, k2, k3];
	for (let karakter of klare_tekst) {
		const cat = categorie(karakter);
		const deelstring = deelstrings[cat];
		cijfertekst += deelstring[mod(posities[cat], deelstring.length)];
		posities[cat] += 1;
	}
	return cijfertekst

}

function decodeer(klare_tekst, k1, k2, k3) {
	return codeer(klare_tekst, -k1, -k2, -k3);
}






console.log(codeer("Nobody expects the Spanish Inquisition!", 2, 3, 1));
// "ppene xctnhes t aiSsqhoI iuinNsitb!dooy"
console.log(decodeer(decodeer("ppene xctnhes t aiSsqhoI iuinNsitb!dooy", 2, 3, 1)));
// "Nobody expects the Spanish Inquisition!"






















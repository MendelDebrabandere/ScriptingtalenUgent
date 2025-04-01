"use strict";

const fs = require("fs");
const assert = require("assert");
// const assert = (voorwaarde, boodschap) => {if (!v) throw new Error("b"); }

function familieleden(bestandsnaam) {
	const stamboom = {};

	const regels = fs
		.readFileSync(bestandsnaam, "utf8")
		.trimEnd()
		.split(/[\r\n]+/);

	for (let regel of regels) {
		const familieleden = regel.split(/\s+/);

		for (let familielid of familieleden) {
			stamboom[familielid] = stamboom[familielid] || {};
		}

		const [moeder, vader, ...kinderen] = familieleden;
		stamboom[moeder].kinderen = kinderen.sort();
		stamboom[vader].kinderen = kinderen;
		for (let kind of kinderen) {
			stamboom[kind].vader = vader;
			stamboom[kind].moeder = moeder;
		}

	}

	return stamboom;

}

function voorouder(persoon, relatie, stamboom) {

	assert (persoon in stamboom, "onbekende persoon");

	const voorouders = relatie.match(/mor|far/g);

	// const voorouders = [];
	// for (let index = 0; index < relatie.length; index += 3){
	// 	let voorouder = relatie.substring(index, index+3);
	// 	voorouders.push(voorouder);
	// }

	const boodschap = "onbekende voorouder";

	for (let voorouder of voorouders) {
		if (voorouder === "mor") {
			assert("moeder" in stamboom[persoon], boodschap);
			persoon = stamboom[persoon].moeder;
		} else if (voorouder === "far") {
			assert("vader" in stamboom[persoon], boodschap);
			persoon = stamboom[persoon].vader;
		} else {
			throw new Error("ongeldige relatie");
		}
	}

	return persoon;

}

function nakomelingen(persoon, generaties, stamboom) {
	assert (persoon in stamboom, "ongeldige persoon");

	let vorigeGeneratie = {};
	vorigeGeneratie[persoon] = "";

	for (let index = 0; index < generaties; index += 1) {
		let volgendeGeneratie = {};
		for (let ouder in vorigeGeneratie) {
			let omschrijving = vorigeGeneratie[ouder];
			if ("kinderen" in stamboom[ouder]) {
				for (let kind of stamboom[ouder].kinderen) {
					if (ouder === stamboom[kind].vader) {
						volgendeGeneratie[kind] = "far" + omschrijving;
					} else {
						volgendeGeneratie[kind] = "mor" + omschrijving;
					}
				}
			}
		}


		vorigeGeneratie = volgendeGeneratie;
	}

	let omschrijvingen = {};
	for (let persoon in vorigeGeneratie) {
		let omschrijving = vorigeGeneratie[persoon];
		if (omschrijving in omschrijvingen) {
			omschrijvingen[omschrijving].push(persoon);
		} else {
			omschrijvingen[omschrijving] = [persoon];
		}
	}

	for (let omschrijving in omschrijvingen) {
		omschrijvingen[omschrijving].sort();
	}

	return omschrijvingen;

}


// console.log(familieleden("data.txt"));
const relaties = familieleden("data.txt");
//console.log(relaties);
//console.log(voorouder("Drake", "mor", relaties));
// "Amira"
//console.log(voorouder("Sincere", "morfarfar", relaties));
// "Ronan"
console.log(nakomelingen("Ronan", 2, relaties));
// {"morfar": ["Ramiro", "Regan"], "farfar": ["Drake", "Eric", "Jadon", "Rosa"]}
































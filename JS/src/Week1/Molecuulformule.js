"use strict";


function groepen(naam) {
	let reeks = [];

	let group = "";
	let depth = 0;

	for (let char of naam) {
		if (char.match(/\(/)) {
			if (depth === 0) {
				// verwerk group
				reeks.push(group);
				group = "";
			}
			depth += 1;
		} else if (char.match(/\)/)) {
			depth -= 1;
		} else if ( char.match(/[A-Z]/) && depth === 0) {
			// verwerk group
			reeks.push(group);
			group = "";
		}

		group += char;
	}
	reeks.push(group);
	reeks = reeks.slice(1);
	return reeks;
}

function splitMolecuul(naam) {
	let letters = naam.match(/^[a-z]+/i);
	let cijfers = naam.match(/[0-9]*$/);
	if (cijfers[0] === "") {
		cijfers = 1;
	} else {
		cijfers = +cijfers[0];
	}
	return [letters[0], cijfers];
}



function molecuulformule(naam, multiplier=1) {
	let groepn = groepen(naam);

	let myObj = {};

	for (let groep of groepn) {
		if (groep.match(/\(/)) {
			let newmultiplier = groep.match(/[0-9]*$/)[0];
			if (newmultiplier === "") newmultiplier = 1;
			else newmultiplier = +newmultiplier;
			groep = groep.match(/^\((.*)\)/)[1];
			//groep = groepen(groep);
			let subObj = molecuulformule(groep, multiplier * newmultiplier);
			for (let item in subObj) {
				if (item in myObj) {
					myObj[item] += subObj[item];
				} else {
					myObj[item] = subObj[item];
				}
			}
		} else { // was alr fine
			let [naam, cijfers] = splitMolecuul(groep);
			if (naam in myObj)
				myObj[naam] += cijfers * multiplier;
			else
				myObj[naam] = cijfers * multiplier;
		}
	}


	return myObj;

}


//console.log(molecuulformule("Th8((Na9Hg4Nd10Rf10)5Lv13Pt14)K4Sn2"));
// {"Sn": 2, "Th": 8, "Hg": 20, "Rf": 50, "Nd": 50, "Pt": 14, "K": 4, "Lv": 13, "Na": 45}

// console.log(groepen("C6H12O6"));
// //	["C6", "H12", "O6"]
// console.log(groepen("C4H8(OH)2"));
// //	["C4", "H8", "(OH)2"]
// console.log(groepen("PbCl(NH3)2(COOH)2"));
// //	["Pb", "Cl", "(NH3)2", "(COOH)2"]
// console.log(groepen("PbCl(NH3(H2O)4)2"));
// //	["Pb", "Cl", "(NH3(H2O)4)2"]


//console.log(molecuulformule("CCl2F2"));


// console.log(molecuulformule("C6H12O6"));
// //{"C": 6, "H": 12, "O": 6}
// console.log(molecuulformule("C4H8(OH)2"));
// //{"C": 4, "H": 10, "O": 2}
// console.log(molecuulformule("PbCl(NH3)2(COOH)2"));
// //{"Pb": 1, "Cl": 1, "N": 2, "H": 8, "C": 2, "O": 4}
// console.log(molecuulformule("PbCl(NH3(H2O)4)2"));
// //{"Pb": 1, "Cl": 1, "N": 2, "H": 22, "O": 8}

















"use strict";

const mod = function(a, b) {
	return (a % b + b) % b;
};

function ontleding(notatie) {
	let obj = {};

	let grondsize = 1;
	if (notatie.length > 1 && notatie[1] === "#") {
		grondsize = 2;
	}

	obj.grondnoot = notatie.substring(0, grondsize);
	obj.symbool = notatie.substring(grondsize);

	return obj;
}

function noten(grondnoot, reeks) {
	const noten = ["A", "A#",
						"B",
						"C", "C#",
						"D", "D#",
						"E",
						"F", "F#",
						"G", "G#",
	];

	const startPos = noten.indexOf(grondnoot);

	let toonladder = [];

	for (const num of reeks) {
		toonladder.push(noten[mod(startPos + num, noten.length)]);
	}

	return toonladder;

}

function akkoord(kort_not, naam_to_reeks, symbool_to_naam) {
	const ontl = ontleding(kort_not);

	return noten(ontl.grondnoot, naam_to_reeks[symbool_to_naam[ontl.symbool]]);
}






// console.log(ontleding("F"));
// //{"grondnoot": "F", "symbool": ""}
// console.log(ontleding("Gm7"));
// //{"grondnoot": "G", "symbool": "m7"}
// console.log(ontleding("D#M7"));
// //{"grondnoot": "D#", "symbool": "M7"}

// console.log(noten("F", [0, 4, 7]));
// //	["F", "A", "C"]
// console.log(noten("G", [0, 3, 7, 10]));
// //	["G", "A#", "D", "F"]
// console.log(noten("D#", [0, 4, 7, 11]));
// //	["D#", "G", "A#", "D"]



const akkoordtypes = {"majeur": [0, 4, 7], "mineur": [0, 3, 7], "dominant septiem": [0, 4, 7, 10], "mineur septiem": [0, 3, 7, 10], "majeur septiem": [0, 4, 7, 11]}
const akkoordsymbolen = {"": "majeur", "m": "mineur", "7": "dominant septiem", "m7": "mineur septiem", "M7": "majeur septiem"};
console.log(akkoord("F", akkoordtypes, akkoordsymbolen));
//	["F", "A", "C"]
console.log(akkoord("Gm7", akkoordtypes, akkoordsymbolen));
//	["G", "A#", "D", "F"]
console.log(akkoord("D#M7", akkoordtypes, akkoordsymbolen));
//	["D#", "G", "A#", "D"]






















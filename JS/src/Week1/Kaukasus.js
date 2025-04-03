"use strict";

function voorkomens(woord) {
	let obj = {};
	for (let letter of woord) {
		letter = letter.toLowerCase();
		if (letter in obj) {
			obj[letter] += 1;
		} else {
			obj[letter] = 1;
		}
	}
	return obj;
}



function evenwichtig(woord) {
	let vk = voorkomens(woord);

	let allnum = undefined;

	for (let num of Object.values(vk)) {
		if (allnum === undefined) {
			allnum = num;
			if (allnum < 2) return false;
		} else if (num !== allnum) {
			return false;
		}
	}

	return true;
}



console.log(voorkomens("Kaukasus"));

console.log(evenwichtig("blablablabla"));
console.log(evenwichtig("stroommeter"));
console.log(evenwichtig("Kaukasus"));























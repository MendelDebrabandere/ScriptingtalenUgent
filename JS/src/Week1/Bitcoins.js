"use strict";

const assert = require("assert");

function winst(waarden, acties) {
	let p = 0;
	let hasCoin = false;
	const message = "ongeldige acties";

	for (let idx = 0; idx < waarden.length; idx++) {
		const waarde = waarden[idx];
		const actie = acties[idx];

		if (actie === "K") {
			assert(!hasCoin, message);
			p = p - waarde;
			hasCoin = true;
		} else if (actie === "V") {
			assert(hasCoin, message);
			p = p + waarde;
			hasCoin = false;
		}
	}
	assert(!hasCoin, message);

	return p;
}

function maximaleWinst(waarden) {

	if (waarden.length === 0) return 0;

	let p = 0;
	let po = -waarden[0];

	for (let idx = 1; idx < waarden.length; ++idx) {
		let p2 = Math.max(p, po + waarden[idx]);
		let po2 = Math.max(po, p - waarden[idx]);

		p = p2;
		po = po2;
	}

	return p;
}





// console.log(winst([5, 11, 4, 2, 8, 10, 7, 4, 3, 6], "KV-K-V--KV"));
// console.log(winst([4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11], "-K-V-KV-KVKV"));
// console.log(winst([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10], "-K-V--K-VK--V"));



//
// console.log(maximaleWinst([5, 11, 4, 2, 8, 10, 7, 4, 3, 6]));











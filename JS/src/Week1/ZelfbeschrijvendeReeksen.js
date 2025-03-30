function cijferfrequentie(input) {
	let myArr = new Array(10).fill(0);
	for (let c of input) {
		if ( '0' <= c && c <= '9') {
			myArr[parseInt(c)] += 1;
		}
	}
	return myArr;
}

function beschrijving(lijst) {
	let myArr = [];
	for (let idx = 0; idx < lijst.length; ++idx) {
		if (lijst[idx] === 0) {
			myArr.push(`${idx}`);
		} else {
			myArr.push(`${lijst[idx]}${idx}`);
		}
	}
	return myArr.join(' ');
}

function isZelfbeschrijvend(input) {
	let myArr = new Array(10).fill(0);

	for (let idx = 0; idx < arguments.length; ++idx) {
		let cijferfreq = cijferfrequentie(arguments[idx]);

		for (let i = 0; i < cijferfreq.length; ++i) {
			myArr[i] += cijferfreq[i];
		}
		if (arguments[idx] !== beschrijving(myArr)) {
			return false;
		}
	}
	return true;
}

console.log(cijferfrequentie("10 71 32 23 14 15 16 27 18 19"));
console.log(beschrijving([1, 7, 3, 2, 1, 1, 1, 2, 1, 1]));
console.log(isZelfbeschrijvend("10 71 32 23 14 15 16 27 18 19"));
console.log(isZelfbeschrijvend("F1gur471v3ly 5p34k1ng?"));
console.log(isZelfbeschrijvend("10 71 32 23 14 15 16 27 18 19", "20 81 72 53 44 35 26 47 38 29"));
console.log(cijferfrequentie("60 241 112 113 114 85 76 137 108 89"));
"use strict";

function isBereikbaar(pos1, pos2) {
	const vertDist = Math.abs(pos1[0] - pos2[0]);
	const horDist = Math.abs(pos1[1] - pos2[1]);

	if (vertDist === 0) return false;

	return horDist / vertDist <= 1;
}


function maxScorePoort(pos, maxScores) {

	let curmax = pos[2];

	for (const poort of maxScores) {
		if (isBereikbaar(pos, poort)) {
			curmax = Math.max(poort[2] + pos[2], curmax);
		}
	}

	return curmax;
}

function maxTotaalscore(poortjes) {

	let maxScore = 0;
	let prevPoortjes = [];

	poortjes.sort(function(a, b)
	{
		if (a[0] !== b[0]) return a[0] - b[0];
		return a[1] - b[1];
	});

	for (let poortje of poortjes) {
		let currScore = maxScorePoort(poortje, prevPoortjes);
		poortje[2] = currScore;
		prevPoortjes.push(poortje);
		maxScore = Math.max(currScore, maxScore);
	}
	return maxScore;

}


// console.log(isBereikbaar([0, 0], [1, 0]));
// console.log(isBereikbaar([0, 5], [2, 1]))
// console.log(isBereikbaar([0, 0], [3, 3]))
// console.log(isBereikbaar([0, 0], [3, 4]))

// console.log(maxScorePoort([5, 2, 0], [[4, 6, 4]]));
// console.log(maxScorePoort([0, 3, 2], []));
// console.log(maxScorePoort([1, 4, 3], [[1, 0, 6], [0, 3, 2]]));
// console.log(maxScorePoort([3, 3, 4], [[1, 4, 5], [0, 3, 2], [1, 0, 6]]));
// console.log(maxScorePoort([4, 1, 2], [[0, 3, 2], [1, 0, 6], [3, 3, 9], [1, 4, 5]]));
// console.log(maxScorePoort([6, 1, 5], [[3, 3, 9], [1, 4, 5], [0, 3, 2], [1, 0, 6], [4, 1, 8]]));
// console.log(maxScorePoort([8, 4, 1], [[6, 1, 14], [4, 1, 8], [1, 0, 6], [1, 4, 5], [3, 3, 9], [0, 3, 2]]));


console.log(maxTotaalscore([[5, 2, 0], [9, 4, 3], [10, 8, 5], [4, 6, 4]]));
//9
console.log(maxTotaalscore([[1, 0, 6], [4, 1, 2], [1, 4, 3], [0, 3, 2], [6, 1, 5], [3, 3, 4], [8, 4, 1]]));
//14
console.log(maxTotaalscore([[0, 1, 1], [2, 0, 2], [3, 2, 4]]))
//5
console.log(maxTotaalscore([[6, 3, 1], [4, 10, 3], [10, 4, 7], [6, 7, 5]]));
//12



















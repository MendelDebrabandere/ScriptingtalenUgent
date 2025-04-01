const assert = (voorwaarde, boodschap) => {if (!voorwaarde) throw Error(boodschap);};

function profiel(sequenties) {
	const profielmatrix = new Map();
	const lengte = sequenties.length === 0 ? 0 : sequenties[0].length;

	for (let base of "ACGT") {
		profielmatrix.set(base, new Array(lengte).fill(0));
	}

	for (let sequentie of sequenties) {
		assert(sequentie.length === lengte, "sequenties moeten even lang zijn");

		for (let [number, base] of [...sequentie].entries()) {
			profielmatrix.get(base)[number] += 1;
		}



	}

	return profielmatrix;
}


function consensus (profielmatrix) {

	let consensus = "";

	for (let [kolom, aantal] of profielmatrix.get("A").entries() ) {
		let cons = "A";
		for (let base of "CGT") {
			if (profielmatrix.get(base)[kolom] > aantal) {
				cons = base;
				aantal = profielmatrix.get(base)[kolom];
			} else if (profielmatrix.get(base)[kolom] === aantal) {
				cons = "N";
			}
		}


		consensus += cons;
	}


	return consensus;

}





let seqs = ["GCAAAACG", "GCGAAACT", "TACCTTCA", "TATGTTCA", "GCCTTAGG", "GACTTATA", "TCGGATCC"]
console.log(profiel(seqs));
// new Map([["A", [0, 3, 1, 2, 3, 4, 0, 3]], ["C", [0, 4, 3, 1, 0, 0, 5, 1]], ["T", [3, 0, 1, 2, 4, 3, 1, 1]], ["G", [4, 0, 2, 2, 0, 0, 1, 2]]])
console.log(consensus(profiel(seqs)));
// "GCCNTACA"











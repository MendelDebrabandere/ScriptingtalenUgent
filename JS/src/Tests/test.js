await Promise.all([1,2,Promise.resolve(3), Promise.resolve(4)]).then((value) => {

	console.log(value)

}, (error) => {

	console.log(error)

})
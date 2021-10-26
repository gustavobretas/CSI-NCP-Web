function validation(arrayCalc) {
	let result = true;

	document.getElementById("error").innerHTML = "";
	document.getElementById("result").innerHTML = "";

	for (let index = 0; index < arrayCalc.length; index++) {
		if (isNaN(arrayCalc[index])) {
			result = false;
		}
	}

	return result;
}

function btnMean() {
	const arrayCalc = document.getElementById("txtCalc").value.split(" ");

	if (!validation(arrayCalc) || document.getElementById("txtCalc").value == "") {
		document.getElementById("error").innerHTML = "Invalid Input";
	} else {
		let totalSum = 0;
		for (let i = 0; i < arrayCalc.length; i++) {
			if (arrayCalc[i] != "") {
				totalSum += parseInt(arrayCalc[i]);
			}
		}
		const result = totalSum / arrayCalc.length;
		document.getElementById("result").innerHTML = `The Mean is: ${result}`;
	}
}

function calcVariance(arr) {
	let sum = 0;
	let result = 0;
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] != "") {
			sum += parseFloat(arr[i]);
		}
	}

	let v = 0;
	if (arr.length > 1) {
		var mean = sum / arr.length;
		for (var j = 0; j < arr.length; j++) {
			if (arr[j] != "") {
				v += (arr[j] - mean) * (arr[j] - mean);
			}
		}
		result = v / arr.length;
	}
	return result;
}

function btnVariance() {
	const arrayCalc = document.getElementById("txtCalc").value.split(" ");

	if (!validation(arrayCalc) || document.getElementById("txtCalc").value == "") {
		document.getElementById("error").innerHTML = "Invalid Input";
	} else {
		document.getElementById("result").innerHTML = `The Variance is: ${calcVariance(arrayCalc)}`;
	}
}

function btnStdDeviation() {
	const arrayCalc = document.getElementById("txtCalc").value.split(" ");

	if (!validation(arrayCalc) || document.getElementById("txtCalc").value == "") {
		document.getElementById("error").innerHTML = "Invalid Input";
	} else {
		document.getElementById("result").innerHTML = `The Standard Deviation is: ${Math.sqrt(calcVariance(arrayCalc))}`;
	}
}

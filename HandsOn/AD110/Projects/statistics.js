class NumberList {
	constructor() {
		this.registerElements();
		this.registerHandlers();
	};

	registerElements() {
		this.numList = document.getElementById("txtCalc");
		this.errorMessage = document.getElementById("error");
		this.outputMessage = document.getElementById("output")
		this.btnMean = document.getElementById("btnMean")
		this.btnVariance = document.getElementById("btnVariance")
		this.btnStandardDeviation = document.getElementById("btnStandardDeviation")
	};

	registerHandlers() {
		this.btnMean.onclick = (event) => this.btnMeanClick(event);
		this.btnVariance.onclick = (event) => this.btnVarianceClick(event);
		this.btnStandardDeviation.onclick = (event) => this.btnStandardDeviationClick(event);
	};

	validation(arrayCalc) {
		let result = true;

		this.errorMessage.innerHTML = "";
		this.outputMessage.innerHTML = "";

		for (let index = 0; index < arrayCalc.length; index++) {
			if (isNaN(arrayCalc[index])) {
				result = false;
			}
		}

		return result;
	};

	calcMean(arr) {
		let totalSum = 0;
		for (let i = 0; i < arr.length; i++) {
			if (arr[i] != "") {
				totalSum += parseFloat(arr[i]);
			}
		}
		const result = totalSum / arr.length;
		return result;
	};

	calcVariance(arr) {
		let result = 0;
		
		let variance = 0;
		if (arr.length > 1) {
			var mean = this.calcMean(arr);
			for (var j = 0; j < arr.length; j++) {
				if (arr[j] != "") {
					variance += (parseFloat(arr[j]) - mean) * (parseFloat(arr[j]) - mean);
				}
			}
			result = variance / arr.length;
		}
		return result;
	};

	btnMeanClick(event) {
		event.preventDefault();
		const arrayCalc = this.numList.value.split(" ");
	
		if (!this.validation(arrayCalc) || this.numList.value == "") {
			this.errorMessage.innerHTML = "Invalid Input";
		} else {
			this.outputMessage.innerHTML = `The Mean is: ${this.calcMean(arrayCalc).toFixed(2)}`;
		}
	};

	btnVarianceClick(event) {
		event.preventDefault();
		const arrayCalc = this.numList.value.split(" ");
	
		if (!this.validation(arrayCalc) || this.numList.value == "") {
			this.errorMessage.innerHTML = "Invalid Input";
		} else {
			this.outputMessage.innerHTML = `The Variance is: ${this.calcVariance(arrayCalc).toFixed(2)}`;
		}
	};

	btnStandardDeviationClick(event) {
		event.preventDefault();
		const arrayCalc = this.numList.value.split(" ");
	
		if (!this.validation(arrayCalc) || this.numList.value == "") {
			this.errorMessage.innerHTML = "Invalid Input";
		} else {
			this.outputMessage.innerHTML = `The Standard Deviation is: ${Math.sqrt(this.calcVariance(arrayCalc)).toFixed(2)}`;
		}
	}
};

new NumberList();
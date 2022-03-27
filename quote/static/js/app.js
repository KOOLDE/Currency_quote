// Save default value of Real
const defaultValueBRL = document.getElementById("brl").value;

document.addEventListener("keyup", function(event) { 

    if (event.code === "Enter") {

        // Get values of Dolar and Real     
        var usd = document.getElementById("usd").value; 
        var brl = defaultValueBRL;

        var result = usd * brl;

        // Show in input the value o Real
        document.getElementById("brl").value = result.toFixed(3);

    }
});

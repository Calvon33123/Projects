function calculateSum(){
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    const number1 = parseFloat(num1); 
    const number2 = parseFloat(num2); 

    //Calculate Sum

    const sum = number1 + number2;

    //Displlay the result

    document.getElementById('result').textContent = 'The sum is: ' + sum;
}
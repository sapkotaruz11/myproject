function formValidation(){

    var ownername =  document.getElementById('title');
    var pgname =  document.getElementById('address');
    var price =  document.getElementById('price');
    var phone =  document.getElementById('phone');
    var area =  document.getElementById('area');
    var street =  document.getElementById('street');
    var description =  document.getElementById('pg_descp');


     if(inputAlphabet(ownername, "* Please enter a valid name *")){

        if(textAlphanumeric(pgname, "* Please enter a valid pg name *")){

            if(textNumeric(price, "* Please enter price in numbers *")){

                if(textNumerical(phone, "* Please enter a valid phone numbers *")){

                            if(textArea(area, "* Please enter a valid area *")){

                                if(textStreet(street, "* Please enter a valid street *")){

                    if(textAlphanumerical(description, "* Please enter some description *")){

                          return true;
                           }
                    }
               }
          }
      }
  }
}

    return false;

}

function inputAlphabet(inputtext, alertMsg){
    var alphaExp = /^([a-zA-Z]+\s*)+$/;
    if(inputtext.value.match(alphaExp)){
        return true;
    }else{
        document.getElementById('p1').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

function textAlphanumeric(inputtext, alertMsg){
    var alphaExp = /^([0-9a-zA-Z]+\s*)+$/;
    if(inputtext.value.match(alphaExp)){
        return true;
    }else{
        document.getElementById('p2').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

function textNumeric(inputtext, alertMsg){
    var numericExpression = /^[0-9]+$/;
    if(inputtext.value.match(numericExpression)){
        return true;
    }else{
        document.getElementById('p3').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

function textNumerical(inputtext, alertMsg){
    var numericExpression = /^[0-9]+$/;
    if(inputtext.value.match(numericExpression)){
        return true;
    }else{
        document.getElementById('p4').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

function textAlphanumerical(inputtext, alertMsg){
    var alphaExp = /^([0-9a-zA-Z]+\s*)+$/;
    if(inputtext.value.match(alphaExp)){
        return true;
    }else{
        document.getElementById('p5').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

function textArea(inputtext, alertMsg){
    var alphaExp = /^([a-zA-Z]+\s*)+$/;
    if(inputtext.value.match(alphaExp)){
        return true;
    }else{
        document.getElementById('p6').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

function textStreet(inputtext, alertMsg){
    var alphaExp = /^([0-9a-zA-Z]+\s*)+$/;
    if(inputtext.value.match(alphaExp)){
        return true;
    }else{
        document.getElementById('p7').innerText = alertMsg;
        inputtext.focus();
        return false;
    }
}

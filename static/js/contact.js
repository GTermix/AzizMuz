document
  .querySelector(".number-form")
  .addEventListener('keydown', (event)=> {
  // Allow numbers, space, plus sign, left bracket, right bracket, and backspace
  if (!(event.key.match(/[0-9\s\+\-\(\)]/) || event.key === "Backspace")) {
    event.preventDefault();
  }
  });

var submitButton = document.querySelector(".site-btn");
submitButton.addEventListener("click", () => {
  var phoneNumberInput = document.querySelector(".number-form");
  var phoneNumber = phoneNumberInput.value;
  var nameI = document.querySelector(".name-form");
  var name = nameI.value;
  var commenti = document.querySelector("#id_comment");
  var comment = commenti.value;
  var o = 1;
  var regex =
    /^\+?(?:998)?\s?-?\(?(20|33|50|71|77|78|88|90|91|93|94|95|97|99)\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})$/;
  var match = regex.exec(phoneNumber);
  if (match && comment && name) {
    r = phoneNumber.substring(1, 4);
    e = phoneNumber.substring(0, 1);
    q = phoneNumber.substring(0, 3);
    var numbers = phoneNumber.replace(/\D/g, "");
    console.log(numbers);
    if (e == "+" && r != "998") {
      alert(s.a);
      o *= 0;
    }
    if (e != "+" && q == "998" && numbers.length > 9) {
      alert("Telefon raqami yaroqli emas");
      o *= 0;
    }
    if (comment.length < 5) {
      alert(
        "Iltimos xabaringizni ma`nosi tushiniladigan darajada ko`proq yozing"
      );
      o *= 0;
    }
    if (name.length < 3) {
      alert("Iltimos ismingizni kiriting");
      o *= 0;
    }
    if (o) {
      var form = document.querySelector(".contact-form");
      var formData = new FormData(form);
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/contact/");
      xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (!(JSON.stringify(response) === "{}")) {
              alert(response.message);
            }
          } else {
            console.error("Error submitting form data:", xhr.status);
          }
        }
      };
      xhr.send(formData);
    }
  } else {
    if (!match) {
      alert("Phone number is invalid");
    }
    if (!name) {
      alert("Please enter your name");
    }
    if (!comment) {
      alert("Please write a message");
    }
  }
});

s = {
  a: "Iltimos to'g'ri formatdagi telefon raqami kiriting. Misollar:\n+998(99)999-99-99\n99-999-99-99",
};

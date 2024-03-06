var submitButton = document.querySelector(".send-btn");
submitButton.addEventListener("click", () => {
  var e_mail = document.querySelector(".email-subscribe");
  var email = e_mail.value;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const isValidEmail = emailRegex.test(email);
  if (isValidEmail){
      var form = document.querySelector(".subscribe-form");
      var formData = new FormData(form);
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/subscribe-email/");
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
  } else {
    alert('Please enter a valid email address');
  }
});



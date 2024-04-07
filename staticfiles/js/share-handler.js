function fallbackCopyTextToClipboard(text) {
  var textArea = document.createElement("textarea");
  textArea.value = text;

  textArea.style.top = "0";
  textArea.style.left = "0";
  textArea.style.position = "fixed";

  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand("copy");
    var msg = successful ? "successful" : "unsuccessful";
    console.log("Fallback: Copying text command was " + msg);
  } catch (err) {
    console.error("Fallback: Oops, unable to copy", err);
  }

  document.body.removeChild(textArea);
}
function copyTextToClipboard(text) {
  if (!navigator.clipboard) {
    fallbackCopyTextToClipboard(text);
    return;
  }
  navigator.clipboard.writeText(text).then(
    function () {
      console.log("Async: Copying to clipboard was successful!");
    },
    function (err) {
      console.error("Async: Could not copy text: ", err);
    }
  );
}

const shareButton = document.querySelector(".lnk-sh");
shareButton.addEventListener("click", (e) => {
  var a = document.querySelector(".title").textContent;
  var b = document
    .querySelector(".content")
    .textContent.substring(0, 140)
    .replace(/\n/g, " ")
    .replace(/\t/g, " ");
  var textToCopy = a + "\n\n" + b + "...\n\n" + window.location.href;
  copyTextToClipboard(textToCopy);
});

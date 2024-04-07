function freezeScroll() {
  var top = window.scrollY || document.documentElement.scrollTop;
  window.onscroll = () => {
    window.scrollTo(0, top);
  };
}

function allowScroll() {
  window.onscroll = null; // Remove the previously set onscroll event handler
}

var gridItems = document.querySelectorAll(".grid-item");
var gridItems_ = document.querySelectorAll(".main-player-button");

gridItems.forEach((item) => {
  item.addEventListener("click", () => {
    freezeScroll();
    document.querySelector(".ad-banner").style.display = "none";
  });
});
gridItems_.forEach((item) => {
  item.addEventListener("click", () => {
    freezeScroll();
    document.querySelector(".ad-banner").style.display = "none";
  });
});

// Add an event listener to the document to handle the click event for the close button
document.addEventListener("click", (event) => {
  if (event.target.classList.contains("mfp-close")) {
    allowScroll();
    document.querySelector(".ad-banner").style.display = "flex";
  }
});

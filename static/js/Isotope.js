var shouldLoadMoreImages = true;
var iso;
var isDisconnected = false;
var dn = false;
var last = false;
var currentPage = 1;
var maxPage = 0;
var wasLast = false;
var nl = true; //not loaded
var ld = false;

function initializeIsotope() {
  var grid = document.querySelector(".grid-container");
  const firstElement = grid.firstElementChild;

  if (firstElement.tagName === "H3") {
    iso = new Isotope(grid, {
      itemSelector: ".grid-item",
      percentPosition: true,
      masonry: {
        columnWidth: ".grid-item",
        gutter: 10,
      },
    });
  }
}

function observeNextToLastElement() {
  const nextToLastElement = document.querySelector(
    ".grid-item:nth-last-child(2)"
  );
  observer.observe(nextToLastElement);
}

window.addEventListener("DOMContentLoaded", () => {
  const gridContainer = document.querySelector(".grid-container");
  const firstElement = gridContainer.firstElementChild;

  if (!(firstElement.tagName === "H3")) {
    loadCnt();
    magPopup();
    initializeIsotope();
  }
});
function isElementInViewport(element) {
  const rect = element.getBoundingClientRect();
  const windowHeight =
    window.innerHeight || document.documentElement.clientHeight;
  const windowWidth = window.innerWidth || document.documentElement.clientWidth;
  const topVisible = rect.top >= 0 && rect.top <= windowHeight;
  const bottomVisible = rect.bottom >= 0 && rect.bottom <= windowHeight;
  const leftVisible = rect.left >= 0 && rect.left <= windowWidth;
  const rightVisible = rect.right >= 0 && rect.right <= windowWidth;
  return (topVisible || bottomVisible) && (leftVisible || rightVisible);
}

function lazyLoadImages() {
  var shimmerElements = document.querySelectorAll(".blurred-shimmer-effect");
  shimmerElements.forEach((element) => {
    const image = element.querySelector("img.images");

    if (isElementInViewport(element) && image.getAttribute("data-src")) {
      // Image is in the viewport and not yet loaded, start loading it
      image.src = image.getAttribute("data-src");
      image.removeAttribute("data-src");

      // Optional: Add a load event listener to hide the shimmer effect once the image is loaded
      image.addEventListener("load", () => {
        element.classList.remove("blurred-shimmer-effect");
      });
    }
    iso.layout();
  });
}

window.addEventListener("load", () => {
  const gridContainer = document.querySelector(".grid-container");
  const firstElement = gridContainer.firstElementChild;

  if (!(firstElement.tagName === "H3")) {
    lazyLoadImages();
    ld = true;
    iso.layout();
  } 
});
window.addEventListener("scroll", () => {
  const gridContainer = document.querySelector(".grid-container");
  const firstElement = gridContainer.firstElementChild;
  if (!(firstElement.tagName === "H3")) {
    lazyLoadImages();
    if (nl && ld) {
      iso.layout();
      const nextToLastElement = document.querySelector(
        ".grid-item:nth-last-child(2)"
      );
      const nextToLastElementa = document.querySelector(
        ".grid-item:last-child"
      );
      if (
        isElementInViewport(nextToLastElement) &&
        isElementInViewport(nextToLastElementa)
      ) {
        observeNextToLastElement();
        nl = false;
      }
    }
  }
});
function loadCnt() {
  const xhr = new XMLHttpRequest();
  xhr.onload = () => {
    if (xhr.status === 200) {
      newImages = [];
      const jsonResponse = JSON.parse(xhr.responseText);
      p = jsonResponse.p;
      maxPage = p;
    } else {
      console.error("Error: " + xhr.status);
    }
  };

  xhr.open("GET", "/imgs-api/cnt/", false);
  xhr.send();
}

function magPopup() {
  $(".grid-item").magnificPopup({
    type: "image",
    delegate: "a",
    gallery: {
      enabled: true,
    },
    image: {
      srcImg: (item) => {
        return item.el.find("img").attr("src");
      },
    },
  });
  $(".grid-item a").click((event) => {
    event.preventDefault();
  });
}

function loadPictures(number) {
  const xhr = new XMLHttpRequest();
  xhr.onload = () => {
    if (xhr.status === 200) {
      newImages = [];
      const jsonResponse = JSON.parse(xhr.responseText);
      jsonResponse.forEach((item) => {
        const imageUrl = item.image;
        const cImageUrl = item.compressed_image;
        const title = item.title;
        const date = item.date;
        const newPicture = document.createElement("div");
        //https://i.ibb.co/YRMS6Sx/1024px-Blank1x1-svg.png
        newPicture.classList.add("grid-item", "blurred-shimmer-effect", "new");
        newPicture.innerHTML = `
          <a href="${imageUrl}" class="ln">
            <img src="${cImageUrl}" data-src="${imageUrl}" alt="${title}" class="lazy-load images">
            <div class="item-details">
              <h3>${title}</h3>
              <p>${date}</p>
            </div>
          </a>
          `;
        newImages.push(newPicture);
        const gridContainer = document.querySelector(".grid-container");
        gridContainer.appendChild(newPicture);
      });
      iso.appended(newImages);
      iso.layout();
      if (number == maxPage) {
        wasLast = true;
      }
    } else {
      const error = "Error: " + xhr.status;
    }
  };

  xhr.open("GET", "/imgs-api/data/" + number, false);
  xhr.send();
}

var scrollEventListener = () => {
  loadPictures(currentPage);
  iso.layout();
  lazyLoadImages();
  observer.disconnect();
  setTimeout(() => {
    const newDivs = document.querySelectorAll(".new");
    newDivs.forEach((element) => {
      element.classList.remove("new");
    });
    iso.layout();
    currentPage++;
    if (!dn) {
      iso.layout();
      setTimeout(() => {
        iso.once("arrangeComplete", function () {
          console.log("arrange done, just this one time");
        });
        iso.layout();
        nextToLastElement = document.querySelector(
          ".grid-item:nth-last-child(2)"
        );
        observer.observe(nextToLastElement);
        return;
      }, 4500);
    }
  }, 1500);
};

var observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      // if (wasLast && dn) {
      //   console.log(maxPage + " ^ " + currentPage + "  " + logCurrentTime());
      //   nextToLastElement = document.querySelector(".grid-item:last-child");
      //   observer.observe(nextToLastElement, { childList: true });
      //   last = true;
      //   return
      // }
      if (maxPage < currentPage) {
        observer.disconnect();
      }

      if (maxPage == currentPage - 1 && wasLast && !dn) {
        setTimeout(() => {
          dn = true;
          const container = document.querySelector(".bottom");
          const endMessage = document.createElement("h2");
          endMessage.textContent = "The end of the page";
          endMessage.classList.add("end-message");
          container.appendChild(endMessage);
          magPopup();
          observer.disconnect();
          return;
        }, 2000);
      }
      if (!wasLast) {
        scrollEventListener();
        magPopup();
      }
    }
  });
});

function freezeScroll() {
  var top = window.scrollY || document.documentElement.scrollTop;
  window.onscroll = function () {
    window.scrollTo(0, top);
  };
}

var gridItems = document.querySelectorAll(".grid-item");

gridItems.forEach(function (item) {
  item.addEventListener("click", function () {
    freezeScroll();
  });
});

function uo() {
  if (dn && last) {
    observer.disconnect();
    console.log("ds" + "  " + logCurrentTime());
    window.removeEventListener("scroll", uo);
  }
}

// window.addEventListener("scroll", uo);


var submitButton = document.getElementById("submitButton");
submitButton.addEventListener("click", function () {
  var form = document.getElementById("myForm");
  var formData = new FormData(form);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "your-server-url");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        console.log("Form data submitted successfully");
      } else {
        console.error("Error submitting form data:", xhr.status);
      }
    }
  };
  xhr.send(formData);
});
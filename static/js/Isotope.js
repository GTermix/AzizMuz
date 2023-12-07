var shouldLoadMoreImages = true;
var iso;

function initializeIsotope() {
  var grid = document.querySelector(".grid-container");
  iso = new Isotope(grid, {
    itemSelector: ".grid-item",
    percentPosition: true,
    masonry: {
      columnWidth: ".grid-item",
      gutter: 10,
    },
  });
}
window.addEventListener("load", () => {
  initializeIsotope();
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
        iso.layout();
      });
    }
  });
}

window.addEventListener("load", lazyLoadImages);
window.addEventListener("scroll", lazyLoadImages);
var currentPage = 1;
var isLastNotAppended = true;
var maxPage = 0;
var last = false;
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

  xhr.open("GET", "/imgs-api/cnt/", true);
  xhr.send();
}

document.addEventListener("DOMContentLoaded", loadCnt);
function loadPictures(number, callback) {
  const xhr = new XMLHttpRequest();
  xhr.onload = () => {
    if (xhr.status === 200) {
      newImages = [];
      const jsonResponse = JSON.parse(xhr.responseText);
      jsonResponse.forEach((item) => {
        const imageUrl = item.image;
        const title = item.title;
        const date = item.date;
        const newPicture = document.createElement("div");
        //https://i.ibb.co/YRMS6Sx/1024px-Blank1x1-svg.png
        newPicture.classList.add("grid-item", "blurred-shimmer-effect");
        newPicture.innerHTML = `
            <img src="${imageUrl}" data-src="${imageUrl}" alt="${title}" class="lazy-load images">
            <div class="item-details">
              <h3>${title}</h3>
              <p>${date}</p>
            </div>
          `;
        newImages.push(newPicture);
        const gridContainer = document.querySelector(".grid-container");
        gridContainer.appendChild(newPicture);
      });
      iso.appended(newImages);
      newImages = [];
      if (number == maxPage) {
        last = true;
      }
      callback(null, true);
    } else {
      const error = "Error: " + xhr.status;
      callback(error, null);
    }
  };

  xhr.open("GET", "/imgs-api/data/" + number, false);
  xhr.send();
}

function startLoadingAnimation() {
  var dots = document.querySelectorAll(".dot");
  dots.forEach((dot, index) => {
    dot.style.animationDelay = index * 0.2 + "s";
  });
  document.querySelector(".loading-animation").style.display = "flex";
}

// Function to stop the loading animation
function stopLoadingAnimation() {
  document.querySelector(".loading-animation").style.display = "none";
}

const scrollEventListener = () => {
  var div = document.querySelector(".grid-container");
  var lastElement = div.lastElementChild;
  if (
    isElementInViewport(lastElement) &&
    maxPage >= currentPage &&
    isLastNotAppended
  ) {
    isLastNotAppended = false;
    startLoadingAnimation();
    setTimeout(() => {
    loadPictures(currentPage, (error, result) => {
      if (error) {
        console.error(error);
      } else {
        if (
          maxPage == currentPage &&
          last &&
          isElementInViewport(lastElement)
        ) {
          console.log(90);
          const container = document.querySelector(".bottom");
          const endMessage = document.createElement("h2");
          endMessage.textContent = "The end of the page";
          container.appendChild(endMessage);
          currentPage++;
        }
      }
      currentPage++;
      isLastNotAppended = true;
    });
  }, 10000);
    stopLoadingAnimation();
    lazyLoadImages();
    // setTimeout(() => {
    //   var newDivs = document.querySelectorAll(".new");
    //   newDivs.forEach((element) => {
    //     element.classList.remove("new");
    //   });
    //   iso.layout();
    // }, 500);
  }
};

window.addEventListener("scroll", scrollEventListener);

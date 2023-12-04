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

function loadPictures() {
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        newImages = [];
        const jsonResponse = JSON.parse(xhr.responseText);
        const picturesPerPage = 20;
        const startIndex = (currentPage - 1) * picturesPerPage;
        const endIndex = currentPage * picturesPerPage;
        const picturesData = jsonResponse.slice(startIndex, endIndex);
        picturesData.forEach((item) => {
          console.log(1)
          const imageUrl = item.image;
          const title = item.title;
          const date = item.date;
          const newPicture = document.createElement("div");
          //https://i.ibb.co/YRMS6Sx/1024px-Blank1x1-svg.png
          newPicture.classList.add(
            "grid-item",
            "blurred-shimmer-effect",
            "new"
          );
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
        currentPage++;
        if (endIndex >= jsonResponse.length) {
          const endMessage = document.createElement("h2");
          endMessage.textContent = "The end of the page";
          const container = document.querySelector(".grid-container");
          const parentElement = container.parentNode;
          parentElement.appendChild(endMessage);
        }
        iso.appended(newImages);
        iso.resetItems();
        shouldLoadMoreImages = true;
        newImages = [];
      } else {
        console.error("Error: " + xhr.status);
      }
    }
  };

  xhr.open("GET", "/img-api/data/all/", true);
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

shouldLoadMoreImages = true;
window.addEventListener("scroll", () => {
  var div = document.querySelector(".grid-container");
  var lastElement = div.lastElementChild;
  if (shouldLoadMoreImages && isElementInViewport(lastElement)) {
    shouldLoadMoreImages = false;
    startLoadingAnimation();
    loadPictures();
    stopLoadingAnimation();
    lazyLoadImages();
    setTimeout(() => {
      var newDivs = document.querySelectorAll(".new");
      newDivs.forEach((element) => {
        element.classList.remove("new");
      });
      iso.layout();
    }, 500);
  }
});



// window.addEventListener("scroll", () => {
//   var div = document.querySelector(".gr");
//   var lastElement = div.lastElementChild;
//   if (shouldLoadMoreImages && isElementInViewport(lastElement)) {
//     shouldLoadMoreImages = false; // Prevent further loading until current images are loaded
//     loadPictures();
//     appendImagesToIsotope();
//   }

//   // Check if the user has scrolled back to the top of the page
//   // if (window.scrollY === 0) {
//   //   shouldLoadMoreImages = true; // Allow loading more images again
//   // }
// });
// function isAtBottom() {
//   var div = document.querySelector(".gr");
//   var lastElement = div.lastElementChild;
//   var lastElementOffset = lastElement.getBoundingClientRect();

//   return (
//     lastElementOffset.top >= 0 && lastElementOffset.bottom <= window.innerHeight
//   );
// }

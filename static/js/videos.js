var grid = document.querySelector(".grid-container");

var iso = new Isotope(grid, {
  itemSelector: ".grid-item",
  percentPosition: true,
  masonry: {
    columnWidth: ".grid-item",
    gutter: 10,
  },
});

var currentPage = 1;
var totalPages = parseInt(
  document.querySelector(".pagination").getAttribute("count")
); // Calculate the total number of pages based on the media count

document
  .querySelector(".pagination .next")
  .addEventListener("click", function () {
    if (currentPage < totalPages) {
      currentPage++;
      updatePageContent();
    }
  });

document
  .querySelector(".pagination .previous")
  .addEventListener("click", function () {
    if (currentPage > 1) {
      currentPage--;
      updatePageContent();
    }
  });

document
  .querySelector(".pagination .first")
  .addEventListener("click", function () {
    currentPage = 1;
    updatePageContent();
  });

document
  .querySelector(".pagination .last")
  .addEventListener("click", function () {
    currentPage = totalPages;
    updatePageContent();
  });
document.querySelectorAll(".num").forEach((element) => {
  element.addEventListener("click", () => {
    currentPage = parseInt(element.textContent);
    updatePageContent();
  });
});

function updatePageContent() {
  fetch("/videos-api/data/?page=" + currentPage)
    .then((response) => response.json())
    .then((data) => {
      var videos = JSON.parse(data.videos);
      var iframes = document.querySelectorAll(
        ".grid-container .grid-item iframe"
      );
      for (var i = 0; i < iframes.length; i++) {
        if (videos[i]) {
          iframes[i].src =
            "https://www.youtube.com/embed/" + videos[i].fields.link;
          iframes[i].style.display = "block"; // Show the iframe
        } else {
          iframes[i].src = "https://www.youtube.com/embed/"; // Clear the src of unused iframes
          iframes[i].style.display = "none"; // Hide the iframe
        }
      }

      var previousPage = currentPage - 1;
      if (previousPage >= 1) {
        a = document.querySelectorAll(".num")[0];
        a.style.display = "inline";
        if (a.classList.contains("current")) {
          a.classList.remove("current");
        }
        a.textContent = previousPage;
      } else {
        document.querySelectorAll(".num")[0].style.display = "none";
      }

      u = document.querySelectorAll(".num")[1];
      u.textContent = currentPage;
      if (!u.classList.contains("current")) {
        u.classList.add("current");
        u.style.display = "inline";
      }

      var nextPage = currentPage + 1;
      if (nextPage <= totalPages) {
        a = document.querySelectorAll(".num")[2];
        a.style.display = "inline";
        if (a.classList.contains("current")) {
          a.classList.remove("current");
        }
        document.querySelectorAll(".num")[2].textContent = nextPage;
      } else {
        document.querySelectorAll(".num")[2].style.display = "none";
      }

      // Enable or disable the pagination buttons based on the current page
      document.querySelector(".pagination .previous").disabled =
        currentPage === 1;
      document.querySelector(".pagination .first").disabled = currentPage === 1;
      document.querySelector(".pagination .next").disabled =
        currentPage === totalPages || currentPage === 1;
      document.querySelector(".pagination .last").disabled =
        currentPage === totalPages || currentPage === 1;
    });
}
var iso_,
  f = false;
document.querySelector("#all").addEventListener("click", () => {
  if (!f) {
    setTimeout(() => {
      var grid_ = document.querySelector(".all-videos");

      iso_ = new Isotope(grid_, {
        itemSelector: ".video-object",
        percentPosition: true,
        masonry: {
          columnWidth: ".video-object",
          gutter: 10,
        },
      });
    }, 1000);
    setTimeout(() => {
      iso_.layout();
    }, 2000);
    f = !f;
    console.log(2324);
  }
});

document.querySelectorAll(".video-object").forEach((el) => {
  el.addEventListener("click", (event) => {
    let videoCode = el.getAttribute("code");
    // send request to /videos-api/data/{$videoCode} to retrieve page data
    fetch("/videos-api/data/" + videoCode)
      .then((response) => response.json())
      .then((data) => {
        title = data.title;
        link = data.link;
        add_time = data.add_time;
        duration = data.duration;
        thumb = data.thumb;
        document
          .querySelector(".videos__large__item")
          .setAttribute("style", "background-image:url('" + thumb + "')");
        document
          .querySelector(".videos__large__item")
          .setAttribute("data-setbg", thumb);
        document.querySelector(
          ".linker-main"
        ).href = `https://www.youtube.com/watch?v=${link}`;
        document.querySelector(".main-title").innerText = title;
        document.querySelector(".main-date").innerText = add_time;
        document.querySelector(".main-duration").innerText = duration;
        let element = document.getElementById("main-video");
        if (element) {
          element.scrollIntoView({ behavior: "smooth", block: "center" });
        }
      });
  });
});

var iso;

function initializeIsotope_() {
  var grid = document.querySelector(".media-container");
  var opt = {
    itemSelector: ".media-item",
    layoutMode: "fitRows",
    percentPosition: true,
    gutter: 10,
  };

  if (window.innerWidth < 768) {
    var sortingOptions = {
      getSortData: {
        priority: (itemElem) => {
          return itemElem.classList.contains("v") ? 0 : 1;
        },
      },
      sortBy: ["priority", "original-order"],
    };
    Object.assign(opt, sortingOptions);
  }

  iso = new Isotope(grid, opt);
}

function initializeIsotope() {
  var grid = document.querySelector(".media-container");

  iso = new Isotope(grid, {
    itemSelector: ".media-item",
    percentPosition: true,
    masonry: {
      columnWidth: ".media-item",
      gutter: 10,
    },
  });
}

window.addEventListener("load", initializeIsotope);

window.addEventListener("resize", initializeIsotope);

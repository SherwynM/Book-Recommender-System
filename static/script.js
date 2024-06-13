document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const searchDropdown = document.getElementById('search-dropdown');
    const dropdownItems = document.querySelectorAll('.dropdown-item');

    searchInput.addEventListener('input', function () {
      const query = searchInput.value.toLowerCase();
      dropdownItems.forEach(item => {
        const bookName = item.textContent.toLowerCase();
        if (bookName.includes(query)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
      if (query === '') {
        searchDropdown.style.display = 'none';
      } else {
        searchDropdown.style.display = 'block';
      }
    });

    dropdownItems.forEach(item => {
      item.addEventListener('click', function (event) {
        event.preventDefault();
        searchInput.value = this.textContent;
        searchDropdown.style.display = 'none';
      });
    });

    document.addEventListener('click', function (event) {
      if (!searchInput.contains(event.target) && !searchDropdown.contains(event.target)) {
        searchDropdown.style.display = 'none';
      }
    });

    const slider = tns({
      container: '.recommendation-carousel',
      items: 3,
      slideBy: 'page',
      autoplay: true,
      autoplayButtonOutput: false,
      controls: false,
      nav: true,
      navPosition: 'bottom',
      mouseDrag: true,
      responsive: {
        768: {
          items: 3
        },
        576: {
          items: 2
        },
        0: {
          items: 1
        }
      }
    });
  });
